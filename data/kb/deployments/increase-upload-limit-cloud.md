---
title: How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?
slug: /knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud
---

# How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?

## Overview

By default, files uploaded using [`st.file_uploader()`](/library/api-reference/widgets/st.file_uploader) are limited to 200MB. You can configure this using the `server.maxUploadSize` config option.

Streamlit provides [four different ways to set configuration options](/library/advanced-features/configuration#set-configuration-options):

1. In a **global config file** at `~/.streamlit/config.toml` for macOS/Linux or `%userprofile%/.streamlit/config.toml` for Windows:
   ```toml
   [server]
   maxUploadSize = 200
   ```
2. In a **per-project config file** at `$CWD/.streamlit/config.toml`, where `$CWD` is the folder you're running Streamlit from.
3. Through `STREAMLIT_*` **environment variables**, such as:
   ```bash
   export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
   ```
4. As **flags on the command line** when running `streamlit run`:
   ```bash
   streamlit run your_script.py --server.maxUploadSize 200
   ```

Which of the four options should you choose for an app deployed to [Streamlit Community Cloud](/streamlit-community-cloud)? 🤔

## Solution

When deploying your app to Streamlit Community Cloud, you should **use option 1**. Namely, set the `maxUploadSize` config option in a global config file (`.streamlit/config.toml`) uploaded to your app's GitHub repo. 🎈

For example, to increase the upload limit to 400MB, upload a `.streamlit/config.toml` file containing the following lines to your app's GitHub repo:

```toml
[server]
maxUploadSize = 400
```

## Relevant resources

- [Streamlit drag and drop capping at 200MB, need workaround](https://discuss.streamlit.io/t/streamlit-drag-and-drop-capping-at-200mb-need-workaround/19803/2)
- [File uploader widget API](/library/api-reference/widgets/st.file_uploader)
- [How to set Streamlit configuration options](/library/advanced-features/configuration#set-configuration-options)
