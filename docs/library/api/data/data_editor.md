---
title: st.data_editor
slug: /library/api-reference/data/st.data_editor
description: st.data_editor display a data editor widget that allows you to edit dataframes and many other data structures in a table-like UI.
---

<Tip>

This page only contains information on the `st.data_editor` API. For an overview of working with dataframes and to learn more about the data editor's capabilities and limitations, read [Dataframes](/library/advanced-features/dataframes).

</Tip>

<Autofunction function="streamlit.data_editor" />

### Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/library/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

<Cloud src="https://doc-column-config-overview.streamlit.app/?embed=true&embed_options=disable_scrolling" height="480"/>
