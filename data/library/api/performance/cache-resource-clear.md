---
title: st.cache_resource.clear
slug: /library/api-reference/performance/st.cache_resource.clear
description: st.cache_resource.clear clears all cache_resource caches.
---

<Autofunction function="streamlit.cache_resource.clear" />

#### Example

In the example below, pressing the "Clear All" button will clear _all_ cache_resource caches. i.e. Clears cached global resources from all functions decorated with `@st.cache_resource`.

```python
import streamlit as st
from transformers import BertModel

@st.cache_resource
 def get_database_session(url):
     # Create a database session object that points to the URL.
     return session

@st.cache_resource
def get_model(model_type):
    # Create a model of the specified type.
    return BertModel.from_pretrained(model_type)

if st.button("Clear All"):
    # Clears all st.cache_resource caches:
    st.cache_resource.clear()
```
