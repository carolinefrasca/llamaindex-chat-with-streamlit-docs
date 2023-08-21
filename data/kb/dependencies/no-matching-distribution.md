---
title: ERROR No matching distribution found for
slug: /knowledge-base/dependencies/no-matching-distribution
---

# ERROR: No matching distribution found for

## Problem

You receive the error `ERROR: No matching distribution found for` when you deploy an app on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Solution

This error occurs when you deploy an app on Streamlit Community Cloud and have one or more of the following issues with your [Python dependencies](/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) in your requirements file:

1. The package is part of the [Python Standard Library](https://docs.python.org/3/py-modindex.html). E.g. You will see **`ERROR: No matching distribution found for base64`** if you include [`base64`](https://docs.python.org/3/library/base64.html) in your requirements file, as it is part of the Python Standard Library. The solution is to not include the package in your requirements file. Only include packages in your requirements file that are not distributed with a standard Python installation.
2. The package name in your requirements file is misspelled. Double-check the package name before including it in your requirements file.
3. The package does not support the operating system on which your Streamlit app is running. E.g. You see **`ERROR: No matching distribution found for pywin32`** while deploying to Streamlit Community Cloud. The `pywin32` module provides access to many of the Windows APIs from Python. Apps deployed to Streamlit Community Cloud are executed in a Linux environment. As such, `pywin32` fails to install on non-Windows systems, including on Streamlit Community Cloud. The solution is to either exclude `pywin32` from your requirements file, or deploy your app on a cloud service offering Windows machines.

Related forum posts:

- https://discuss.streamlit.io/t/error-no-matching-distribution-found-for-base64/15758
- https://discuss.streamlit.io/t/error-could-not-find-a-version-that-satisfies-the-requirement-pywin32-301-from-versions-none/15343/2
