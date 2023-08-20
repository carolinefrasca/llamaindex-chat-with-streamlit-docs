---
title: Deploy Streamlit using Docker
slug: /knowledge-base/tutorials/deploy/docker
---

# Deploy Streamlit using Docker

## Introduction

So you have an amazing app and you want to start sharing it with other people, what do you do? You have a few options. First, where do you want to run your Streamlit app, and how do you want to access it?

- **On your corporate network** - Most corporate networks are closed to the outside world. You typically use a VPN to log onto your corporate network and access resources there. You could run your Streamlit app on a server in your corporate network for security reasons, to ensure that only folks internal to your company can access it.
- **On the cloud** - If you'd like to access your Streamlit app from outside of a corporate network, or share your app with folks outside of your home network or laptop, you might choose this option. In this case, it'll depend on your hosting provider. We have [community-submitted guides](/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud) from Heroku, AWS, and other providers.

Wherever you decide to deploy your app, you will first need to containerize it. This guide walks you through using Docker to deploy your app. If you prefer Kubernetes see [Deploy Streamlit using Kubernetes](/knowledge-base/tutorials/deploy/kubernetes).

## Prerequisites

1. [Install Docker Engine](#install-docker-engine)
2. [Check network port accessibility](#check-network-port-accessibility)

### Install Docker Engine

If you haven't already done so, install [Docker](https://docs.docker.com/engine/install/#server) on your server. Docker provides `.deb` and `.rpm` packages from many Linux distributions, including:

- [Debian](https://docs.docker.com/engine/install/debian/)
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Verify that Docker Engine is installed correctly by running the `hello-world` Docker image:

```bash
sudo docker run hello-world
```

<Tip>

Follow Docker's official [post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/) to run Docker as a non-root user, so that you don't have to preface the `docker` command with `sudo`.

</Tip>

### Check network port accessibility

As you and your users are behind your corporate VPN, you need to make sure all of you can access a certain network port. Let's say port `8501`, as it is the default port used by Streamlit. Contact your IT team and request access to port `8501` for you and your users.

## Create a Dockerfile

Docker builds images by reading the instructions from a `Dockerfile`. A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image. Learn more in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/). The [docker build](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile`. The [docker run](https://docs.docker.com/engine/reference/commandline/run/) command first creates a container over the specified image, and then starts it using the specified command.

Here's an example `Dockerfile` that you can add to the root of your directory. i.e. in `/app/`

```docker
# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Dockerfile walkthrough

Let’s walk through each line of the Dockerfile :

1. A `Dockerfile` must start with a [`FROM`](https://docs.docker.com/engine/reference/builder/#from) instruction. It sets the [Base Image](https://docs.docker.com/glossary/#base-image) (think OS) for the container:

   ```docker
   FROM python:3.9-slim
   ```

   Docker has a number of official Docker base images based on various Linux distributions. They also have base images that come with language-specific modules such as [Python](https://hub.docker.com/_/python). The `python` images come in many flavors, each designed for a specific use case. Here, we use the `python:3.9-slim` image which is a lightweight image that comes with the latest version of Python 3.9.

   <Tip>

   You can also use your own base image, provided the image you use contains a [supported version of Python](/knowledge-base/using-streamlit/sanity-checks#check-0-are-you-using-a-streamlit-supported-version-of-python) for Streamlit. There is no one-size-fits-all approach to using any specific base image, nor is there an official Streamlit-specific base image.

   </Tip>

2. The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it in the `Dockerfile` . Let’s set it to `app/` :

   ```docker
   WORKDIR /app
   ```

   <Important>

   As mentioned in [Development flow](/library/get-started/main-concepts#development-flow), for Streamlit version 1.10.0 and higher, Streamlit apps cannot be run from the root directory of Linux distributions. Your main script should live in a directory other than the root directory. If you try to run a Streamlit app from the root directory, Streamlit will throw a `FileNotFoundError: [Errno 2] No such file or directory` error. For more information, see GitHub issue [#5239](https://github.com/streamlit/streamlit/issues/5239).

   If you are using Streamlit version 1.10.0 or higher, you must set the `WORKDIR` to a directory other than the root directory. For example, you can set the `WORKDIR` to `/app` as shown in the example `Dockerfile` above.
   </Important>

3. Install `git` so that we can clone the app code from a remote repo:

   ```docker
   RUN apt-get update && apt-get install -y \
       build-essential \
       curl \
       software-properties-common \
       git \
       && rm -rf /var/lib/apt/lists/*
   ```

4. Clone your code that lives in a remote repo to `WORKDIR`:

   a. If your code is in a public repo:

   ```docker
   RUN git clone https://github.com/streamlit/streamlit-example.git .
   ```

   Once cloned, the directory of `WORKDIR` will look like the following:

   ```bash
   app/
   - requirements.txt
   - streamlit_app.py
   ```

   where `requirements.txt` file contains all your [Python dependencies](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies). E.g

   ```
   altair
   pandas
   streamlit
   ```

   and `streamlit_app.py` is your main script. E.g.

   ```python
   from collections import namedtuple
   import altair as alt
   import math
   import pandas as pd
   import streamlit as st

   """
   # Welcome to Streamlit!

   Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

   If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
   forums](https://discuss.streamlit.io).

   In the meantime, below is an example of what you can do with just a few lines of code:
   """

   with st.echo(code_location='below'):
      total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
      num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

      Point = namedtuple('Point', 'x y')
      data = []

      points_per_turn = total_points / num_turns

      for curr_point_num in range(total_points):
         curr_turn, i = divmod(curr_point_num, points_per_turn)
         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
         radius = curr_point_num / total_points
         x = radius * math.cos(angle)
         y = radius * math.sin(angle)
         data.append(Point(x, y))

      st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
         .mark_circle(color='#0068c9', opacity=0.5)
         .encode(x='x:Q', y='y:Q'))
   ```

   b. If your code is in a private repo, please read [Using SSH to access private data in builds](https://docs.docker.com/develop/develop-images/build_enhancements/#using-ssh-to-access-private-data-in-builds) and modify the Dockerfile accordingly -- to install an SSH client, download the public key for [github.com](https://github.com), and clone your private repo. If you use an alternative VCS such as GitLab or Bitbucket, please consult the documentation for that VCS on how to copy your code to the `WORKDIR` of the Dockerfile.

   c. If your code lives in the same directory as the Dockerfile, copy all your app files from your server into the container, including `streamlit_app.py`, `requirements.txt`, etc, by replacing the `git clone` line with:

   ```docker
   COPY . .
   ```

   More generally, the idea is copy your app code from wherever it may live on your server into the container. If the code is not in the same directory as the Dockerfile, modify the above command to include the path to the code.

5. Install your app’s [Python dependencies](/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) from the cloned `requirements.txt` in the container:

   ```docker
   RUN pip3 install -r requirements.txt
   ```

6. The [`EXPOSE`](https://docs.docker.com/engine/reference/builder/#expose) instruction informs Docker that the container listens on the specified network ports at runtime. Your container needs to listen to Streamlit’s (default) port 8501:

   ```docker
   EXPOSE 8501
   ```

7. The [`HEALTHCHECK`](https://docs.docker.com/engine/reference/builder/#expose) instruction tells Docker how to test a container to check that it is still working. Your container needs to listen to Streamlit’s (default) port 8501:

   ```docker
   HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
   ```

8. An [`ENTRYPOINT`](https://docs.docker.com/engine/reference/builder/#entrypoint) allows you to configure a container that will run as an executable. Here, it also contains the entire `streamlit run` command for your app, so you don’t have to call it from the command line:

   ```docker
   ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

## Build a Docker image

The [`docker build`](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile` . Run the following command from the `app/` directory on your server to build the image:

```docker
docker build -t streamlit .
```

The `-t` flag is used to tag the image. Here, we have tagged the image `streamlit`. If you run:

```docker
docker images
```

You should see a `streamlit` image under the REPOSITORY column. For example:

```
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
streamlit    latest    70b0759a094d   About a minute ago   1.02GB
```

## Run the Docker container

Now that you have built the image, you can run the container by executing:

```docker
docker run -p 8501:8501 streamlit
```

The `-p` flag publishes the container’s port 8501 to your server’s 8501 port.

If all went well, you should see an output similar to the following:

```
docker run -p 8501:8501 streamlit

  You can now view your Streamlit app in your browser.

  URL: http://0.0.0.0:8501
```

To view your app, users can browse to `http://0.0.0.0:8501` or `http://localhost:8501`

<Note>

Based on your server's network configuration, you could map to port 80/443 so that users can view your app using the server IP or hostname. For example: `http://your-server-ip:80` or `http://your-hostname:443`.

</Note>
