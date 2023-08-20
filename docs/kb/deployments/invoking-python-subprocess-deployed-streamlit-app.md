---
title: Invoking a Python subprocess in a deployed Streamlit app
slug: /knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app
---

# Invoking a Python subprocess in a deployed Streamlit app

## Problem

Let's suppose you want to invoke a subprocess to run a Python script `script.py` in your deployed Streamlit app `streamlit_app.py`. For example, the machine learning library [Ludwig](https://ludwig-ai.github.io/ludwig-docs/) is run using a command-line interface, or maybe you want to run a bash script or similar type of process from Python.

You have tried the following, but run into dependency issues for `script.py`, even though you have specified your Python dependencies in a requirements file:

```python
# streamlit_app.py
import streamlit as st
import subprocess

subprocess.run(["python", "script.py"])
```

## Solution

When you run the above code block, you will get the version of Python that is on the system path—not necessarily the Python executable installed in the virtual environment that the Streamlit code is running under.

The solution is to detect the Python executable directy with [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable):

```python
# streamlit_app.py
import streamlit as st
import subprocess
import sys

subprocess.run([f"{sys.executable}", "script.py"])
```

This ensures that `script.py` is running under the same Python executable as your Streamlit code—where your [Python dependencies](/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) are installed.

### Relevant links

- https://stackoverflow.com/questions/69947867/run-portion-of-python-code-in-parallel-from-a-streamlit-app/69948545#69948545
- https://discuss.streamlit.io/t/modulenotfounderror-no-module-named-cv2-streamlit/18319/3?u=snehankekre
- https://docs.python.org/3/library/sys.html#sys.executable
