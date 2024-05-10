---
title: Managing dependencies when deploying your app
slug: /deploy/concepts/dependencies
---

# Managing dependencies when deploying your app

Before you began developing your app, you set up and configured your development environment by installing Python and Streamlit. When you deploy your app, you need to set up and configure your deployment environment in the same way. When you deploy your app to a cloud service, your app's [Python server](/develop/concepts/architecture/architecture#python-backend-server) will be running on a remote machine. This remote machine will not have access all the files and programs on your personal computer.

All Streamlit apps have at least two dependencies: Python and Streamlit. Your app may have additional dependencies in the form of Python packages or software that must be installed to properly execute your script. If you are using a service like Streamlit Community Cloud which is designed for Streamlit apps, we'll take care of Python and Streamlit for you!

## Install Python and other software

If you are using Streamlit Community Cloud, Python is already installed. You can just pick the version in the deployment dialog. If you need to install Python yourself or you have other non-Python software to install, follow your platform's instructions to install additional software. You will commonly use a package management tool to do this.
For example, Streamlit Community Cloud uses Advanced Package Tool (`apt`) for Debian-based Linux systems. For more information about installing non-Python depencies on Streamlit Community Cloud, see [`apt-get` dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies).

## Install Python packages

Once you have Python installed in your deployment environment, you'll need to install all the necessary Python packages, including Streamlit! With each `import` of an installed package, you add a Python dependency to your script. You need to install those dependencies in your deployment environment through a Python package manager.

If you are using Streamlit Community Cloud, you'll have the latest version of Streamlit and all of its dependencies installed by default. So, if you're making a simple app and don't need additional dependencies, you won't have to do anything at all!

### `pip` and `requirements.txt`

Since `pip` comes by default with Python, the most common way to configure your Python environment is with a `requirements.txt` file. Each line of a `requirements.txt` file is a package to `pip install`. You should _not_ include <a href="https://docs.python.org/3/py-modindex.html" target="_blank">built-in Python libraries</a> like `math` or `random` in your `requirements.txt` file. These are a part of Python and aren't installed separately.

If you have a script like the following, you would only need to install Streamlit. No extra dependencies would be needed since `pandas` and `numpy` are installed as direct dependencies of `streamlit`. Similarly, `math` and `random` are built into Python.

```python
import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')
```

However, it's a best practice accurately record packages you use, so the recommended `requirements.txt` file would be:

```none
streamlit
pandas
numpy
```

If you needed to specify certain versions, another valid example would be:

```none
streamlit==1.24.1
pandas>2.0
numpy<=1.25.1
```

A `requirements.txt` file is commonly saved in the root of your repository or file directory. If you are using Streamlit Community Cloud, see [Add Python dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) for more information. Otherwise, check your platform's documentation.
