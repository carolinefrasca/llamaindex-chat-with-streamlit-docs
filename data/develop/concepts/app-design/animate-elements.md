---
title: Animate and update elements
slug: /develop/concepts/design/animate
description: st.add_rows appends a dataframe to the bottom of the current one in certain elements, for optimized data updates.
---

# Animate and update elements

Sometimes you display a chart or dataframe and want to modify it live as the app
runs (for example, in a loop). Some elements have built-in methods to allow you
to update them in-place without rerunning the app.

Updatable elements include the following:

- `st.empty` containers can be written to in sequence and will always show the last thing written. They can also be cleared with an
  additional `.empty()` called like a method.
- `st.dataframe`, `st.table`, and many chart elements can be updated with the `.add_rows()` method which appends data.
- `st.progress` elements can be updated with additional `.progress()` calls. They can also be cleared with a `.empty()` method call.
- `st.status` containers have an `.update()` method to change their labels, expanded state, and status.
- `st.toast` messages can be updated in place with additional `.toast()` calls.

## `st.empty` containers

`st.empty` can hold a single element. When you write any element to an `st.empty` container, Streamlit discards its previous content
displays the new element. You can also `st.empty` containers by calling `.empty()` as a method. If you want to update a set of elements, use
a plain container (`st.container()`) inside `st.empty` and write contents to the plain container. Rewrite the plain container and its
contents as often as desired to update your app's display.

## The `.add_rows()` method

`st.dataframe`, `st.table`, and all chart functions can be mutated using the `.add_rows()` method on their output. In the following example, we use `my_data_element = st.line_chart(df)`. You can try the example with `st.table`, `st.dataframe`, and most of the other simple charts by just swapping out `st.line_chart`. Note that `st.dataframe` only shows the first ten rows by default and enables scrolling for additional rows. This means adding rows is not as visually apparent as it is with `st.table` or the chart elements.

```python
import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")
```
