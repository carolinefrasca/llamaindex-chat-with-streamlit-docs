---
title: How do I create an anchor link?
slug: /knowledge-base/using-streamlit/create-anchor-link
---

# How do I create an anchor link?

## Overview

Have you wanted to create anchors so that users of your app can directly navigate to specific sections by specifying `#anchor` in the URL? If so, let's find out how.

## Solution

Anchors are automatically added to header text.

For example, if you define a header text via the [st.header()](/library/api-reference/text/st.header) command as follows:

```python
st.header("Section 1")
```

Then you can create a link to this header using:

```python
st.markdown("[Section 1](#section-1)")
```

## Examples

- Demo app: [https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/](https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/)
- GitHub repo: [https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py](https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py)
