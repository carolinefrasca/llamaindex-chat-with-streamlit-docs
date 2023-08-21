---
title: st.sidebar
slug: /library/api-reference/layout/st.sidebar
description: st.sidebar displays items in a sidebar.
---

## st.sidebar

## Add widgets to sidebar

Not only can you add interactivity to your app with widgets, you can organize them into a sidebar. Elements can be passed to `st.sidebar` using object notation and `with` notation.

The following two snippets are equivalent:

```python
# Object notation
st.sidebar.[element_name]
```

```python
# "with" notation
with st.sidebar:
    st.[element_name]
```

Each element that's passed to `st.sidebar` is pinned to the left, allowing users to focus on the content in your app.

<Tip>

The sidebar is resizable! Drag and drop the right border of the sidebar to resize it! ↔️

</Tip>

Here's an example of how you'd add a selectbox and a radio button to your sidebar:

```python
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
```

<Important>

The only elements that aren't supported using object notation are `st.echo`, `st.spinner`, and `st.toast`. To use these elements, you must use `with` notation.

</Important>

Here's an example of how you'd add [`st.echo`](/library/api-reference/utilities/st.echo) and [`st.spinner`](/library/api-reference/status/st.spinner) to your sidebar:

```python
import streamlit as st

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
```
