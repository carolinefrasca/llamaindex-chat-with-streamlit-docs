---
title: Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn?)
slug: /knowledge-base/deploy/does-streamlit-support-wsgi-protocol
---

# Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn?)

## Problem

You're not sure whether your Streamlit app can be deployed with gunicorn.

## Solution

Streamlit does not support the WSGI protocol at this time, so deploying Streamlit with (for example) gunicorn is not currently possible. Check out this [forum thread regarding deploying Streamlit in a gunicorn-like manner](https://discuss.streamlit.io/t/how-do-i-set-the-server-to-0-0-0-0-for-deployment-using-docker/216) to see how other users have accomplished this.
