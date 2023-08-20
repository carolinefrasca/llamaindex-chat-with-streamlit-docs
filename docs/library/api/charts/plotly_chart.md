---
title: st.plotly_chart
slug: /library/api-reference/charts/st.plotly_chart
description: st.plotly_chart displays an interactive Plotly chart.
---

<Autofunction function="streamlit.plotly_chart" />

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud src="https://doc-plotly-chart-theme.streamlit.app/?embed=true" height="525" />

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Plotly chart where a custom color scale is defined and reflected:

```python
import plotly.express as px
import streamlit as st

st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Notice how the custom color scale is still reflected in the chart, even when the Streamlit theme is enabled 👇

<Cloud src="https://doc-plotly-custom-colors.streamlit.app/?embed=true" height="650" />

For many more examples of Plotly charts with and without the Streamlit theme, check out the [plotly.streamlit.app](https://plotly.streamlit.app).
