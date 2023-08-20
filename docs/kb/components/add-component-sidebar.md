---
title: How do I add a Component to the sidebar?
slug: /knowledge-base/components/add-component-sidebar
---

# How do I add a Component to the sidebar?

You can add a component to [st.sidebar](/library/api-reference/layout/st.sidebar) using the `with` syntax. For example:

```python
with st.sidebar:
    my_component(greeting="hello")
```

In fact, you can add your component to _any_ [layout container](/library/api-reference/layout) (eg st.columns, st.expander), using the `with` syntax!

```python
col1, col2 = st.columns(2)
with col2:
    my_component(greeting="hello")
```
