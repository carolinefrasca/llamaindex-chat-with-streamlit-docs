---
title: st.markdown
slug: /develop/api-reference/text/st.markdown
description: st.markdown displays string formatted as Markdown.
---

<Autofunction function="streamlit.markdown" />

```python
import streamlit as st

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)
```

<Cloud src="https://doc-markdown1.streamlit.app/?embed=true" height="500" />
