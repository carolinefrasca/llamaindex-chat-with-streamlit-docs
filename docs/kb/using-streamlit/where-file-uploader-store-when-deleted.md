---
title: Where does st.file_uploader store uploaded files and when do they get deleted?
slug: /knowledge-base/using-streamlit/where-file-uploader-store-when-deleted
---

# Where does st.file_uploader store uploaded files and when do they get deleted?

When you upload a file using [`st.file_uploader`](/library/api-reference/widgets/st.file_uploader), the data are copied to the Streamlit backend via the browser, and contained in a BytesIO buffer in Python memory (i.e. RAM, not disk). The data will persist in RAM until the Streamlit app re-runs from top-to-bottom, which is on each widget interaction. If you need to save the data that was uploaded between runs, then you can [cache](/library/advanced-features/caching) it so that Streamlit persists it across re-runs.

As files are stored in memory, they get deleted immediately as soon as they’re not needed anymore.

This means Streamlit removes a file from memory when:

- The user uploads another file, replacing the original one
- The user clears the file uploader
- The user closes the browser tab where they uploaded the file

Related forum posts:

- https://discuss.streamlit.io/t/streamlit-sharing-fileupload-where-does-it-go/9267
- https://discuss.streamlit.io/t/how-to-update-the-uploaded-file-using-file-uploader/13512/
