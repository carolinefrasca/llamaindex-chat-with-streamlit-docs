---
title: st.altair_chart
slug: /library/api-reference/charts/st.altair_chart
description: st.altair_chart displays a chart using the Altair library.
---

<Autofunction function="streamlit.altair_chart" />

### Theming

Altair charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Altair's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Altair theme:

```python
import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud src="https://doc-altair-chart.streamlit.app/?embed=true" height="500" />

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Altair chart where manual color passing is done and reflected:

<Collapse title="See the code">

```python
import altair as alt
import streamlit as st
from vega_datasets import data

source = data.seattle_weather()

scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(date):T", title="Date"),
        alt.Y(
            "temp_max:Q",
            title="Maximum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)

# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(
        width=550,
    )
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
```

</Collapse>

Notice how the custom colors are still reflected in the chart, even when the Streamlit theme is enabled 👇

<Cloud src="https://doc-altair-custom-colors.streamlit.app/?embed=true" height="675" />

For many more examples of Altair charts with and without the Streamlit theme, check out the [altair.streamlit.app](https://altair.streamlit.app).

### Annotating charts

Altair also allows you to annotate your charts with text, images, and emojis. You can do this by creating [layered charts](https://altair-viz.github.io/user_guide/compound_charts.html#layered-charts), which let you overlay two different charts on top of each other. The idea is to use the first chart to show the data, and the second chart to show the annotations. The second chart can then be overlaid on top of the first chart using the `+` operator to create a layered chart.

Let's walk through an example of annotating a time-series chart with text and an emoji.

#### Step 1: Create the base chart

In this example, we create a time-series chart to track the evolution of stock prices. The chart is interactive and contains a multi-line tooltip. Click [here](https://altair-viz.github.io/gallery/multiline_tooltip.html) to learn more about multi-line tooltips in Altair.

First, we import the required libraries and load the example stocks dataset using the [`vega_datasets`](https://pypi.org/project/vega-datasets/) package:

```python
import altair as alt
import pandas as pd
import streamlit as st
from vega_datasets import data

# We use @st.cache_data to keep the dataset in cache
@st.cache_data
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source

source = get_data()
```

Next, we define a function `get_chart()` to create the interactive time-series chart of the stock prices with a multi-line tooltip. The x-axis represents the date, and the y-axis represents the stock price.

We then invoke `get_chart()` that takes the stock prices dataframe as an input and returns a chart object. This is going to be our base chart on which we will overlay the annotations in [Step 2](/library/api-reference/charts/st.altair_chart#step-2-annotate-the-chart).

```python
# Define the base time-series chart.
def get_chart(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Evolution of stock prices")
        .mark_line()
        .encode(
            x="date",
            y="price",
            color="symbol",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="yearmonthdate(date)",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("price", title="Price (USD)"),
            ],
        )
        .add_selection(hover)
    )
    return (lines + points + tooltips).interactive()

chart = get_chart(source)
```

#### Step 2: Annotate the chart

Now that we have our first chart that shows the data, we can annotate it with text and an emoji. Let's overlay the ⬇ emoji on top of the time-series chart at specifc points of interest. We want users to hover over the ⬇ emoji to see the associated annotation text.

For simplicity, let's annotate four specific dates and set the height of the annotations at constant value of `10`.

<Tip>

You can vary the horizontal and vertical postions of the annotations by replacing the hard-coded values with the output of Streamlit widgets! Click [here](/library/api-reference/charts/st.altair_chart#interactive-example) to jump to a live example below, and develop an intuition for the ideal horizontal and vertical positions of the annotations by playing with Streamlit widgets.

</Tip>

To do so, we create a dataframe `annotations_df` containing the dates, annotation text, and the height of the annotations:

```python
# Add annotations
ANNOTATIONS = [
    ("Mar 01, 2008", "Pretty good day for GOOG"),
    ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
    ("Nov 01, 2008", "Market starts again thanks to..."),
    ("Dec 01, 2009", "Small crash for GOOG after..."),
]
annotations_df = pd.DataFrame(ANNOTATIONS, columns=["date", "event"])
annotations_df.date = pd.to_datetime(annotations_df.date)
annotations_df["y"] = 10
```

Using this dataframe, we create a scatter plot with the x-axis representing the date, and the y-axis representing the height of the annotation. The data point at the specific date and height is represented by the ⬇ emoji, using Altair's `mark_text()` [mark](https://altair-viz.github.io/user_guide/marks.html).

The annotation text is displayed as a tooltip when users hover over the ⬇ emoji. This is achieved using Altair's `encode()` method to map the `event` column containing the annotation text to the visual attribute ⬇ of the plot.

```python
annotation_layer = (
    alt.Chart(annotations_df)
    .mark_text(size=20, text="⬇", dx=-8, dy=-10, align="left")
    .encode(
        x="date:T",
        y=alt.Y("y:Q"),
        tooltip=["event"],
    )
    .interactive()
)
```

Finally, we overlay the annotations on top of the base chart using the `+` operator to create the final layered chart! 🎈

```python
st.altair_chart(
    (chart + annotation_layer).interactive(),
    use_container_width=True
)
```

<Image src="/images/api/altair-annotation.png" />

To use images instead of emojis, replace the line containing `.mark_text()` with `.mark_image()`, and replace `image_url` below with the URL of the image:

```python
.mark_image(
    width=12,
    height=12,
    url="image_url",
)
```

#### Interactive example

Now that you've learned how to annotate charts, the sky's the limit! We've extended the above example to let you interactively paste your favorite emoji and set its position on the chart with Streamlit widgets. 👇

<Cloud src="https://example-time-series-annotation.streamlit.app/?embed=true" height="700" />
