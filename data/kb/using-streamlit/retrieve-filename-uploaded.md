---
title: How do you retrieve the filename of a file uploaded with st.file_uploader?
slug: /knowledge-base/using-streamlit/retrieve-filename-uploaded
---

# How do you retrieve the filename of a file uploaded with st.file_uploader?

If you upload a single file (i.e. `accept_multiple_files=False`), the filename can be retrieved by using the `.name` attribute on the returned UploadedFile object:

```python
import streamlit as st

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
   st.write("Filename: ", uploaded_file.name)
```

If you upload multiple files (i.e. `accept_multiple_files=True`), the individual filenames can be retrieved by using the `.name` attribute on each UploadedFile object in the returned list:

```python
import streamlit as st

uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)

if uploaded_files:
   for uploaded_file in uploaded_files:
       st.write("Filename: ", uploaded_file.name)
```

Related forum posts:

- https://discuss.streamlit.io/t/is-it-possible-to-get-uploaded-file-file-name/7586
