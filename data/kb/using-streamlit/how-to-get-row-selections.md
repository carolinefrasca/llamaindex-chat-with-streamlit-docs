---
title: How do I get dataframe row-selections from a user?
slug: /knowledge-base/using-streamlit/how-to-get-row-selections
---

# How do I get dataframe row-selections from a user?

At the moment, [`st.dataframe`](/api-reference/data/st.dataframe) and [`st.data_editor`](/library/api-reference/data/st.data_editor) do not natively support passing user-selected rows to the Python backend. We are working to support this in the future. For now, if you need to get row-selections from a user, you can accomplish this by adding an extra [Checkbox column](/library/api-reference/data/st.column_config/st.column_config.checkboxcolumn)) to your dataframe and using `st.data_editor`. You can use this extra column to collect a user's selection(s).

## Example

In the following example, we define a function which accepts a dataframe and returns the rows selected by a user. Within the function, the dataframe is copied to prevent mutating it. We insert a temporary "Select" column into the copied dataframe before passing the copied data into `st.data_editor`. We have disabled editing for all other columns, but you can make them editable if desired. After filtering the dataframe and dropping the temporary column, our function returns the selected rows.

```python
import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "Animal": ["Lion", "Elephant", "Giraffe", "Monkey", "Zebra"],
        "Habitat": ["Savanna", "Forest", "Savanna", "Forest", "Savanna"],
        "Lifespan (years)": [15, 60, 25, 20, 25],
        "Average weight (kg)": [190, 5000, 800, 10, 350],
    }
)

def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)


selection = dataframe_with_selections(df)
st.write("Your selection:")
st.write(selection)
```
