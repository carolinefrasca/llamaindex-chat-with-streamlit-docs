---
title: st.rerun
slug: /develop/api-reference/execution-flow/st.rerun
description: st.rerun will rerun the script immediately.
---

<Autofunction function="streamlit.rerun" oldName="streamlit.experimental_rerun" />

### Caveats for `st.rerun`

`st.rerun` is one of the tools to control the logic of your app. While it is great for prototyping, there can be adverse side effects:

- Additional script runs may be inefficient and slower.
- Excessive reruns may complicate your app's logic and be harder to follow.
- If misused, infinite looping may crash your app.

In many cases where `st.rerun` works, [callbacks](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state) may be a cleaner alternative. [Containers](/develop/api-reference/layout) may also be helpful.

### A simple example in three variations

###### Using `st.rerun` to update an earlier header

```python
import streamlit as st

if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()
```

###### Using a callback to update an earlier header

```python
##### Option using a callback #####
st.header(st.session_state.value)

def update_value():
    st.session_state.value = "Bar"

st.button("Bar", on_click=update_value)
```

###### Using containers to update an earlier header

```python
##### Option using a container #####
container = st.container()

if st.button("Baz"):
    st.session_state.value = "Baz"

container.header(st.session_state.value)
```
