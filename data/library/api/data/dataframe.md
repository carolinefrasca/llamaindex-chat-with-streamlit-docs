---
title: st.dataframe
slug: /library/api-reference/data/st.dataframe
description: st.dataframe displays a dataframe as an interactive table.
---

<Tip>

This page only contains information on the `st.dataframe` API. For an overview of working with dataframes read [Dataframes](/library/advanced-features/dataframes). If you want to let users interactively edit dataframes, check out [`st.data_editor`](/library/api-reference/data/st.data_editor).

</Tip>

<Autofunction function="streamlit.dataframe" />

<br />

`st.dataframe` supports the `use_container_width` parameter to stretch across the full container width:

```python
import pandas as pd
import streamlit as st

# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)
```

<Cloud src="https://doc-dataframe2.streamlit.app/?embed=true" height="350" />

### Interactivity

Dataframes displayed with `st.dataframe` are interactive. End users can sort, resize, search, and copy data to their clipboard. For on overview of features, read our [Dataframes](/library/advanced-features/dataframes#additional-ui-features) guide.

### Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/library/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

<Cloud src="https://doc-column-config-overview.streamlit.app/?embed=true&embed_options=disable_scrolling" height="480"/>
