---
title: Deploy Streamlit using Kubernetes
slug: /knowledge-base/tutorials/deploy/kubernetes
---

# Deploy Streamlit using Kubernetes

## Introduction

So you have an amazing app and you want to start sharing it with other people, what do you do? You have a few options. First, where do you want to run your Streamlit app, and how do you want to access it?

- **On your corporate network** - Most corporate networks are closed to the outside world. You typically use a VPN to log onto your corporate network and access resources there. You could run your Streamlit app on a server in your corporate network for security reasons, to ensure that only folks internal to your company can access it.
- **On the cloud** - If you'd like to access your Streamlit app from outside of a corporate network, or share your app with folks outside of your home network or laptop, you might choose this option. In this case, it'll depend on your hosting provider. We have [community-submitted guides](/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud) from Heroku, AWS, and other providers.

Wherever you decide to deploy your app, you will first need to containerize it. This guide walks you through using Kubernetes to deploy your app. If you prefer Docker see [Deploy Streamlit using Docker](/knowledge-base/tutorials/deploy/docker).

## Prerequisites

1. [Install Docker Engine](#install-docker-engine)
2. [Install the gcloud CLI](#install-the-gcloud-cli)

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

### Install the gcloud CLI

In this guide, we will orchestrate Docker containers with Kubernetes and host docker images on the Google Container Registry (GCR). As GCR is a Google-supported Docker registry, we need to register [`gcloud`](https://cloud.google.com/sdk/gcloud/reference) as the Docker credential helper.

Follow the official documentation to [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install) and initialize it.

## Create a Docker container

We need to create a docker container which contains all the dependencies and the application code. Below you can see the entrypoint, i.e. the command run when the container starts, and the Dockerfile definition.

### Create an entrypoint script

Create a `run.sh` script containing the following:

```bash
#!/bin/bash

APP_PID=
stopRunningProcess() {
    # Based on https://linuxconfig.org/how-to-propagate-a-signal-to-child-processes-from-a-bash-script
    if test ! "${APP_PID}" = '' && ps -p ${APP_PID} > /dev/null ; then
       > /proc/1/fd/1 echo "Stopping ${COMMAND_PATH} which is running with process ID ${APP_PID}"

       kill -TERM ${APP_PID}
       > /proc/1/fd/1 echo "Waiting for ${COMMAND_PATH} to process SIGTERM signal"

        wait ${APP_PID}
        > /proc/1/fd/1 echo "All processes have stopped running"
    else
        > /proc/1/fd/1 echo "${COMMAND_PATH} was not started when the signal was sent or it has already been stopped"
    fi
}

trap stopRunningProcess EXIT TERM

source ${VIRTUAL_ENV}/bin/activate

streamlit run ${HOME}/app/streamlit_app.py &
APP_ID=${!}

wait ${APP_ID}
```

### Create a Dockerfile

Docker builds images by reading the instructions from a `Dockerfile`. A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image. Learn more in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/). The [docker build](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile`. The [docker run](https://docs.docker.com/engine/reference/commandline/run/) command first creates a container over the specified image, and then starts it using the specified command.

Here's an example `Dockerfile` that you can add to the root of your directory.

```docker
FROM python:3.8-slim

RUN groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid 1000 -ms /bin/bash appuser

RUN pip3 install --no-cache-dir --upgrade \
    pip \
    virtualenv

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git

USER appuser
WORKDIR /home/appuser

RUN git clone https://github.com/streamlit/streamlit-example.git app

ENV VIRTUAL_ENV=/home/appuser/venv
RUN virtualenv ${VIRTUAL_ENV}
RUN . ${VIRTUAL_ENV}/bin/activate && pip install -r app/requirements.txt

EXPOSE 8501

COPY run.sh /home/appuser
ENTRYPOINT ["./run.sh"]
```

<Important>

As mentioned in [Development flow](/library/get-started/main-concepts#development-flow), for Streamlit version 1.10.0 and higher, Streamlit apps cannot be run from the root directory of Linux distributions. Your main script should live in a directory other than the root directory. If you try to run a Streamlit app from the root directory, Streamlit will throw a `FileNotFoundError: [Errno 2] No such file or directory` error. For more information, see GitHub issue [#5239](https://github.com/streamlit/streamlit/issues/5239).

If you are using Streamlit version 1.10.0 or higher, you must set the `WORKDIR` to a directory other than the root directory. For example, you can set the `WORKDIR` to `/home/appuser` as shown in the example `Dockerfile` above.
</Important>

### Build a Docker image

Put the above files (`run.sh` and `Dockerfile`) in the same folder and build the docker image:

```docker
docker build --platform linux/amd64 -t gcr.io/$GCP_PROJECT_ID/k8s-streamlit:test .
```

<Important>

Replace `$GCP_PROJECT_ID` in the above command with the name of your Google Cloud project.

</Important>

### Upload the Docker image to a container registry

The next step is to upload the Docker image to a container registry. In this example, we will use the [Google Container Registry (GCR)](https://cloud.google.com/container-registry). Start by enabling the Container Registry API. Sign in to Google Cloud and navigate to your project’s **Container Registry** and click **Enable**.

We can now build the Docker image from the previous step and push it to our project’s GCR. Be sure to replace `$GCP_PROJECT_ID` in the docker push command with the name of your project:

```bash
gcloud auth configure-docker
docker push gcr.io/$GCP_PROJECT_ID/k8s-streamlit:test
```

## Create a Kubernetes deployment

For this step you will need a:

- Running Kubernetes service
- Custom domain for which you can generate a TLS certificate
- DNS service where you can configure your custom domain to point to the application IP

As the image was uploaded to the container registry in the previous step, we can run it in Kubernetes using the below configurations.

### Install and run Kubernetes

Make sure your [Kubernetes client](https://kubernetes.io/docs/tasks/tools/#kubectl), `kubectl`, is installed and running on your machine.

### Configure a Google OAuth Client and oauth2-proxy

For configuring the Google OAuth Client, please see [Google Auth Provider](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider#google-auth-provider). Configure oauth2-proxy to use the desired [OAuth Provider Configuration](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider) and update the oath2-proxy config in the config map.

The below configuration contains a ouath2-proxy sidecar container which handles the authentication with Google. You can learn more from the [oauth2-proxy repository](https://github.com/oauth2-proxy/oauth2-proxy).

### Create a Kubernetes configuration file

Create a [YAML](https://yaml.org/) [configuration file](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#organizing-resource-configurations) named `k8s-streamlit.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: streamlit-configmap
data:
  oauth2-proxy.cfg: |-
    http_address = "0.0.0.0:4180"
    upstreams = ["http://127.0.0.1:8501/"]
    email_domains = ["*"]
    client_id = "<GOOGLE_CLIENT_ID>"
    client_secret = "<GOOGLE_CLIENT_SECRET>"
    cookie_secret = "<16, 24, or 32 bytes>"
    redirect_url = <REDIRECT_URL>

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: streamlit-deployment
  labels:
    app: streamlit
spec:
  replicas: 1
  selector:
    matchLabels:
      app: streamlit
  template:
    metadata:
      labels:
        app: streamlit
    spec:
      containers:
        - name: oauth2-proxy
          image: quay.io/oauth2-proxy/oauth2-proxy:v7.2.0
          args: ["--config", "/etc/oauth2-proxy/oauth2-proxy.cfg"]
          ports:
            - containerPort: 4180
          livenessProbe:
            httpGet:
              path: /ping
              port: 4180
              scheme: HTTP
          readinessProbe:
            httpGet:
              path: /ping
              port: 4180
              scheme: HTTP
          volumeMounts:
            - mountPath: "/etc/oauth2-proxy"
              name: oauth2-config
        - name: streamlit
          image: gcr.io/GCP_PROJECT_ID/k8s-streamlit:test
          imagePullPolicy: Always
          ports:
            - containerPort: 8501
          livenessProbe:
            httpGet:
              path: /_stcore/health
              port: 8501
              scheme: HTTP
            timeoutSeconds: 1
          readinessProbe:
            httpGet:
              path: /_stcore/health
              port: 8501
              scheme: HTTP
            timeoutSeconds: 1
          resources:
            limits:
              cpu: 1
              memory: 2Gi
            requests:
              cpu: 100m
              memory: 745Mi
      volumes:
        - name: oauth2-config
          configMap:
            name: streamlit-configmap

---
apiVersion: v1
kind: Service
metadata:
  name: streamlit-service
spec:
  type: LoadBalancer
  selector:
    app: streamlit
  ports:
    - name: streamlit-port
      protocol: TCP
      port: 80
      targetPort: 4180
```

<Important>

While the above configurations can be copied verbatim, you will have to configure the `oauth2-proxy` yourself and use the correct `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_ID`, `GCP_PROJECT_ID`, and `REDIRECT_URL`.

</Important>

Now create the configuration from the file in Kubernetes with the [`kubectl create`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create) command:

```bash
kubctl create -f k8s-streamlit.yaml
```

### Set up TLS support

Since you are using the Google authentication, you will need to set up TLS support. Find out how in [TLS Configuration](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/tls).

### Verify the deployment

Once the deployment and the service are created, we need to wait a couple of minutes for the public IP address to become available. We can check when that is ready by running:

```bash
kubectl get service streamlit-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

After the public IP is assigned, you will need to configure in your DNS service an `A record` pointing to the above IP address.
