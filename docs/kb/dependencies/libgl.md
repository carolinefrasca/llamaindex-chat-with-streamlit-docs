---
title: ImportError libGL.so.1 cannot open shared object file No such file or directory
slug: /knowledge-base/dependencies/libgl
---

# ImportError libGL.so.1 cannot open shared object file No such file or directory

## Problem

You receive the error `ImportError libGL.so.1 cannot open shared object file No such file or directory` when using OpenCV in your app deployed on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Solution

If you use OpenCV in your app, include `opencv-python-headless` in your requirements file on Streamlit Community Cloud in place of `opencv_contrib_python` and `opencv-python`.

If `opencv-python` is a _required_ (non-optional) dependency of your app or a dependency of a library used in your app, the above solution is not applicable. Instead, you can use the following solution:

Create a `packages.txt` file in your repo with the following line to install the [apt-get dependency](/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies) `libgl`:

```
libgl1
```
