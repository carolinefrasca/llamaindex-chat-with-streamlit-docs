---
title: Utilities and user info
slug: /develop/api-reference/utilities
---

# Utilities and user info

There are a handful of methods that allow you to create placeholders in your
app, provide help using doc strings, get and modify configuration options and query parameters.

<TileContainer>
<RefCard href="/develop/api-reference/utilities/st.experimental_user" size="half">

<h4>User info</h4>

`st.experimental_user` returns information about the logged-in user of private apps on Streamlit Community Cloud.

```python
if st.experimental_user.email == "foo@corp.com":
  st.write("Welcome back, ", st.experimental_user.email)
else:
  st.write("You are not authorized to view this page.")
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.help" size="half">

<h4>Get help</h4>

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.html" size="half">

<h4>Render HTML</h4>

Renders HTML strings to your app.

```python
css = """
<style>
    p { color: red; }
</style>
"""
st.html(css)
```

</RefCard>
</TileContainer>
