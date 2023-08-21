---
title: Batch elements and input widgets with st.form
slug: /knowledge-base/using-streamlit/batch-elements-input-widgets-form
---

# Batch elements and input widgets with st.form

Let's take a look at how to use [`st.form`](/library/api-reference/control-flow/st.form) to batch elements and input widgets.

In Streamlit, every widget interaction causes a rerun of the app. However,
there are times when you might want to interact with a couple of widgets and
submit those interactions while triggering a single re-run of the app.

Using `st.form` you can batch input widgets together and along with
`st.form_submit_button` submit the state inside these widgets with the click
of a single button.

```python
# Forms can be declared using the 'with' syntax
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')
```

```python
# Alternative syntax, declare a form and use the returned object
form = st.form(key='my_form')
form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')
```

```python
# st.form_submit_button returns True upon form submit
if submit_button:
    st.write(f'hello {name}')
```

Forms can appear anywhere in your app (sidebar, columns etc), but there are
some **constraints**:

- A form cannot have interdependent widgets, i.e. the _output_ of `widget1` cannot
  be the _input_ to `widget2` inside a form.
- By design, interacting with widgets inside `st.form` does not trigger
  a re-run. Because of this reason, `st.button` cannot be declared inside `st.form`.
- `st.form` cannot be embedded inside another `st.form`.
- Forms must have an associated `st.form_submit_button`. Clicking this button
  triggers a re-run. Streamlit throws an error if a form does not have an
  associated `st.form_submit_button`.
