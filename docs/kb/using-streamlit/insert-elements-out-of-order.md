---
title: How to insert elements out of order?
slug: /knowledge-base/using-streamlit/insert-elements-out-of-order
---

# How to insert elements out of order?

You can use the [`st.empty`](/library/api-reference/layout/st.empty) method as a placeholder,
to "save" a slot in your app that you can use later.

```python
st.text('This will appear first')
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text('This will appear last')
# Appends some more text to the app.

my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.
```
