---
title: Custom components
slug: /develop/api-reference/custom-components
---

# Custom components

<TileContainer>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.declare_component">

<h4>Declare a component</h4>

Create and register a custom component.

```python
st.components.v1.declare_component(
    "custom_slider",
    "/frontend",
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.html">

<h4>HTML</h4>

Display an HTML string in an iframe.

```python
st.components.v1.html(
    "<p>Foo bar.</p>"
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.iframe">

<h4>iframe</h4>

Load a remote URL in an iframe.

```python
st.components.v1.iframe(
    "docs.streamlit.io"
)
```

</RefCard>

</TileContainer>
