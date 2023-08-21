---
title: ModuleNotFoundError No module named
slug: /knowledge-base/dependencies/module-not-found-error
---

# ModuleNotFoundError: No module named

## Problem

You receive the error `ModuleNotFoundError: No module named` when you deploy an app on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Solution

This error occurs when you import a module on Streamlit Community Cloud that isn’t included in your requirements file. Any external [Python dependencies](/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) that are not distributed with a [standard Python installation](https://docs.python.org/3/py-modindex.html) should be included in your requirements file.

E.g. You will see `ModuleNotFoundError: No module named 'sklearn'` if you don’t include `scikit-learn` in your requirements file and `import sklearn` in your app.

Related forum posts:

- https://discuss.streamlit.io/t/getting-error-modulenotfounderror-no-module-named-beautifulsoup/9126
- https://discuss.streamlit.io/t/modulenotfounderror-no-module-named-vega-datasets/16354
