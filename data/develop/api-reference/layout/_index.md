---
title: Layouts and Containers
slug: /develop/api-reference/layout
---

# Layouts and Containers

## Complex layouts

Streamlit provides several options for controlling how different elements are laid out on the screen.

<TileContainer>
<RefCard href="/develop/api-reference/layout/st.columns">

<Image pure alt="screenshot" src="/images/api/columns.jpg" />

<h4>Columns</h4>

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.container">

<Image pure alt="screenshot" src="/images/api/container.jpg" />

<h4>Container</h4>

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.dialog">

<Image pure alt="screenshot" src="/images/api/dialog.jpg" />

<h4>Modal dialogs</h4>

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.experimental_dialog()
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.empty">

<Image pure alt="screenshot" src="/images/api/empty.jpg" />

<h4>Empty</h4>

Insert a single-element container.

```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.expander">

<Image pure alt="screenshot" src="/images/api/expander.jpg" />

<h4>Expander</h4>

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
  st.write("This is more content")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.popover">

<Image pure alt="screenshot" src="/images/api/popover.svg" />

<h4>Popover</h4>

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
  st.checkbox("Show completed")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.sidebar">

<Image pure alt="screenshot" src="/images/api/sidebar.jpg" />

<h4>Sidebar</h4>

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.tabs">

<Image pure alt="screenshot" src="/images/api/tabs.jpg" />

<h4>Tabs</h4>

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

<h4>Streamlit Elements</h4>

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>
