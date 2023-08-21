---
title: st.divider
slug: /library/api-reference/text/st.divider
description: st.divider displays a horizontal rule in your app.
---

<Autofunction function="streamlit.divider" />

Here's what it looks like in action when you have multiple elements in the app:

```python
import streamlit as st

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule
```

<Image src="/images/api/st.divider.png" clean />
