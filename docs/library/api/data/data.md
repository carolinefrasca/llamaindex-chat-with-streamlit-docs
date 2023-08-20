---
title: Data elements
slug: /library/api-reference/data
---

# Data elements

When you're working with data, it is extremely valuable to visualize that
data quickly, interactively, and from multiple different angles. That's what
Streamlit is actually built and optimized for.

You can display data via [charts](#display-charts), and you can display it in
raw form. These are the Streamlit commands you can use to display and interact with raw data.

<TileContainer>
<RefCard href="/library/api-reference/data/st.dataframe">
<Image pure alt="screenshot" src="/images/api/dataframe.jpg" />

#### Dataframes

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

</RefCard>
<RefCard href="/library/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

#### Data editor

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/library/api-reference/data/st.column_config">

<Image pure alt="screenshot" src="/images/api/column_config.jpg" />

#### Column configuration

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

</RefCard>

<RefCard href="/library/api-reference/data/st.table">
<Image pure alt="screenshot" src="/images/api/table.jpg" />

#### Static tables

Display a static table.

```python
st.table(my_data_frame)
```

</RefCard>
<RefCard href="/library/api-reference/data/st.metric">
<Image pure alt="screenshot" src="/images/api/metric.jpg" />

#### Metrics

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

</RefCard>
<RefCard href="/library/api-reference/data/st.json">
<Image pure alt="screenshot" src="/images/api/json.jpg" />

#### Dicts and JSON

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/PablocFonseca/streamlit-aggrid">

<Image pure alt="screenshot" src="/images/api/components/aggrid.jpg" />

#### Streamlit Aggrid

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)

new_df = grid_return['data']
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

#### Streamlit Folium

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">

<Image pure alt="screenshot" src="/images/api/components/pandas-profiling.jpg" />

#### Pandas Profiling

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

#### Image Coordinates

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])

selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-metric-cards.jpg" />

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)

style_metric_cards()
```

</ComponentCard>

</ComponentSlider>
