---
title: st.cache_data.clear
slug: /library/api-reference/performance/st.cache_data.clear
description: st.cache_data.clear clears all in-memory and on-disk data caches.
---

<Autofunction function="streamlit.cache_data.clear" />

#### Example

In the example below, pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.cache_data`.

```python
import streamlit as st

@st.cache_data
def square(x):
    return x**2

@st.cache_data
def cube(x):
    return x**3

if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()
```
