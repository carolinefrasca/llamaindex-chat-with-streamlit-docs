---
title: Installation
slug: /library/get-started/installation
---

# Install Streamlit

## Table of contents

1. [Prerequisites](#prerequisites)
2. [Install Streamlit on Windows](#install-streamlit-on-windows)
3. [Install Streamlit on macOS/Linux](#install-streamlit-on-macoslinux)

## Prerequisites

Before you get started, you're going to need a few things:

- Your favorite IDE or text editor
- [Python 3.8 - Python 3.11](https://www.python.org/downloads/)
- [PIP](https://pip.pypa.io/en/stable/installation/)

## Set up your virtual environment

Regardless of which package management tool you're using, we recommend running
the commands on this page in a virtual environment. This ensures that the dependencies
pulled in for Streamlit don't impact any other Python projects
you're working on.

Below are a few tools you can use for environment management:

- [venv](https://docs.python.org/3/library/venv.html)
- [pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
- [poetry](https://python-poetry.org/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [conda](https://www.anaconda.com/distribution/)

## Install Streamlit on Windows

Streamlit's officially-supported environment manager on Windows is [Anaconda Navigator](https://docs.anaconda.com/free/navigator/).

### Install Anaconda

If you don't have Anaconda install yet, follow the steps provided on the [Anaconda installation page](https://docs.anaconda.com/free/anaconda/install/windows/).

### Create a new environment with Streamlit

Next you'll need to set up your environment.

1. Follow the steps provided by Anaconda to [set up and manage your environment](https://docs.anaconda.com/free/navigator/getting-started/#navigator-managing-environments) using the Anaconda Navigator.

2. Select the "▶" icon next to your new environment. Then select "Open terminal":

   !["Open terminal" in Anaconda Navigator](https://i.stack.imgur.com/EiiFc.png)

3. In the terminal that appears, type:

   ```bash
   pip install streamlit
   ```

4. Test that the installation worked:

   ```bash
   streamlit hello
   ```

   Streamlit's Hello app should appear in a new tab in your web browser!

### Use your new environment

1. In Anaconda Navigator, open a terminal in your environment (see step 2 above).
2. In the terminal that appears, use Streamlit as usual:

   ```bash
   streamlit run myfile.py
   ```

## Install Streamlit on macOS/Linux

Streamlit's officially-supported package manager and environment manager for macOS and Linux are [pip](https://pypi.org/project/pip/) and [venv](https://docs.python.org/3/library/venv.html), respectively. `venv` is a part of [The Python Standard Library](https://docs.python.org/3/library/index.html) and comes bundled with your installation of Python. See instructions on how to install and use `pip` below.

### Install `pip`

Install `pip`. More details about installing `pip` can be found in [pip's documentation](https://pip.pypa.io/en/stable/installation/#supported-methods).

On a macOS:

```bash
python -m ensurepip --upgrade
```

On Ubuntu with Python 3:

```bash
sudo apt-get install python3-pip
```

For other Linux distributions, see [How to install PIP for Python](https://www.makeuseof.com/tag/install-pip-for-python/).

### Install Xcode command line tools on macOS

On macOS, you'll need to install Xcode command line tools. They are required to compile some of Streamlit's Python dependencies during installation. To install Xcode command line tools, run:

```bash
xcode-select --install
```

### Create a new environment with Streamlit

1. Navigate to your project folder:

   ```bash
   cd myproject
   ```

2. Create a new virtual environment in that folder and activate that environment:

   ```bash
   python -m venv .venv
   ```

   When you run the command above, a directory called `.venv` will appear in `myproject/`. This directory is where your virtual environment and its dependencies are installed.

3. Install Streamlit in your environment:

   ```bash
   pip install streamlit
   ```

4. Test that the installation worked:

   ```bash
   streamlit hello
   ```

   Streamlit's Hello app should appear in a new tab in your web browser!

   <Cloud src="https://doc-mpa-hello.streamlit.app/?embed=true" height="700" />

### Use your new environment

1. Any time you want to use the new environment, you first need to go to your project folder (where the `.venv` directory lives) and run:

   ```bash
   source .venv/bin/activate
   ```

2. Now you can use Python and Streamlit as usual:

   ```bash
   streamlit run myfile.py
   ```

   To stop the Streamlit server, press `ctrl-C`.

3. When you're done using this environment, type `deactivate` to return to your normal shell.

Now that you've installed Streamlit, take a few minutes to read through [Main concepts](/library/get-started/main-concepts) to understand Streamlit's data flow model.
