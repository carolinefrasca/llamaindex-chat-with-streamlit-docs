---
title: Why does Streamlit restrict nested st.columns?
slug: /knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns
---

# Why does Streamlit restrict nested `st.columns`?

Starting in version 1.18.0, Streamlit allows nesting [`st.columns`](/library/api-reference/layout/st.columns) inside other
`st.columns` with the following restrictions:

- In the main area of the app, columns can be nested up to one level of nesting.
- In the sidebar, columns cannot be nested.

These restrictions are in place to make Streamlit apps look good on all device sizes. Nesting columns multiple times often leads to a bad UI.
You might be able to make it look good on one screen size but as soon as a user on a different screen views the app,
they will have a bad experience. Some columns will be tiny, others will be way too long, and complex layouts will look out of place.
Streamlit tries its best to automatically resize elements to look good across devices, without any help from the developer.
But for complex layouts with multiple levels of nesting, this is not possible.

We are always working on improving layout options though! So if you have a use case that requires a more complex layout,
please [open a GitHub issue](https://github.com/streamlit/streamlit/issues), ideally with a sketch of what you want to do.
