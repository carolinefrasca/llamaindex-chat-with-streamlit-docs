---
title: Control flow
slug: /library/api-reference/control-flow
---

# Control flow

## Change execution

By default, Streamlit apps execute the script entirely, but we allow some functionality to handle control flow in your applications.

<TileContainer>
<RefCard href="/library/api-reference/control-flow/st.stop">

#### Stop execution

Stops execution immediately.

```python
st.stop()
```

</RefCard>

<RefCard href="/library/api-reference/control-flow/st.experimental_rerun">

#### Rerun script

Rerun the script immediately.

```python
st.experimental_rerun()
```

</RefCard>
</TileContainer>

## Group multiple widgets

By default, Streamlit reruns your script everytime a user interacts with your app.
However, sometimes it's a better user experience to wait until a group of related
widgets is filled before actually rerunning the script. That's what `st.form` is for!

<TileContainer>
<RefCard href="/library/api-reference/control-flow/st.form">

#### Forms

Create a form that batches elements together with a “Submit" button.

```python
with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")
```

</RefCard>

<RefCard href="/library/api-reference/control-flow/st.form_submit_button">

#### Form submit button

Display a form submit button.

```python
with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/kmcgrady/streamlit-autorefresh">

<Image pure alt="screenshot" src="/images/api/components/autorefresh.jpg" />

#### Autorefresh

Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

#### Pydantic

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

#### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>
