---
title: API Reference
slug: /develop/api-reference
---

# API reference

Streamlit makes it easy for you to visualize, mutate, and share data. The API
reference is organized by activity type, like displaying data or optimizing
performance. Each section includes methods associated with the activity type,
including examples.

Browse our API below and click to learn more about any of our available commands! 🎈

## Display almost anything

### Write and magic

<br />

<TileContainer>

<RefCard href="/develop/api-reference/write-magic/st.write">

<h4>st.write</h4>

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">

<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/magic">

<h4>Magic</h4>

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>

### Text elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/text/st.markdown">

<Image pure alt="screenshot" src="/images/api/markdown.jpg" />

<h4>Markdown</h4>

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.title">

<Image pure alt="screenshot" src="/images/api/title.jpg" />

<h4>Title</h4>

Display text in title formatting.

```python
st.title("The app title")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.header">

<Image pure alt="screenshot" src="/images/api/header.jpg" />

<h4>Header</h4>

Display text in header formatting.

```python
st.header("This is a header")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.subheader">

<Image pure alt="screenshot" src="/images/api/subheader.jpg" />

<h4>Subheader</h4>

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.caption">

<Image pure alt="screenshot" src="/images/api/caption.jpg" />

<h4>Caption</h4>

Display text in small font.

```python
st.caption("This is written small caption text")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.code">

<Image pure alt="screenshot" src="/images/api/code.jpg" />

<h4>Code block</h4>

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.echo">

<Image pure alt="screenshot" src="/images/api/code.jpg" />

<h4>Echo</h4>

Display some code in the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.latex">

<Image pure alt="screenshot" src="/images/api/latex.jpg" />

<h4>LaTeX</h4>

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.text">

<Image pure alt="screenshot" src="/images/api/text.jpg" />

<h4>Preformatted text</h4>

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.divider">

<Image pure alt="screenshot" src="/images/api/divider.jpg" />

<h4>Divider</h4>

Display a horizontal rule.

```python
st.divider()
```

</RefCard>
</TileContainer>

<ComponentSlider>
<ComponentCard href="https://github.com/tvst/st-annotated-text">

<Image pure alt="screenshot" src="/images/api/components/annotated-text.jpg" />

<h4>Annotated text</h4>

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/JohnSnowLabs/nlu">

<Image pure alt="screenshot" src="/images/api/components/nlu.jpg" />

<h4>NLU</h4>

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load('sentiment').predict('I love NLU! <3')
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-mentions.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
mention(label="An awesome Streamlit App", icon="streamlit",  url="https://extras.streamlit.app",)
```

</ComponentCard>
</ComponentSlider>

### Data elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/data/st.dataframe">
<Image pure alt="screenshot" src="/images/api/dataframe.jpg" />

<h4>Dataframes</h4>

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.column_config">

<Image pure alt="screenshot" src="/images/api/column_config.jpg" />

<h4>Column configuration</h4>

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.table">
<Image pure alt="screenshot" src="/images/api/table.jpg" />

<h4>Static tables</h4>

Display a static table.

```python
st.table(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.metric">
<Image pure alt="screenshot" src="/images/api/metric.jpg" />

<h4>Metrics</h4>

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.json">
<Image pure alt="screenshot" src="/images/api/json.jpg" />

<h4>Dicts and JSON</h4>

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/PablocFonseca/streamlit-aggrid">

<Image pure alt="screenshot" src="/images/api/components/aggrid.jpg" />

<h4>Streamlit Aggrid</h4>

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)

new_df = grid_return['data']
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">

<Image pure alt="screenshot" src="/images/api/components/pandas-profiling.jpg" />

<h4>Pandas Profiling</h4>

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])

selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-metric-cards.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)

style_metric_cards()
```

</ComponentCard>

</ComponentSlider>

### Chart elements

<br />

<TileContainer>

<RefCard href="/develop/api-reference/charts/st.area_chart">
<Image pure alt="screenshot" src="/images/api/area_chart.jpg" />

<h4>Simple area charts</h4>

Display an area chart.

```python
st.area_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bar_chart">
<Image pure alt="screenshot" src="/images/api/bar_chart.jpg" />

<h4>Simple bar charts</h4>

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.line_chart">
<Image pure alt="screenshot" src="/images/api/line_chart.jpg" />

<h4>Simple line charts</h4>

Display a line chart.

```python
st.line_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.scatter_chart">
<Image pure alt="screenshot" src="/images/api/scatter_chart.svg" />

<h4>Simple scatter charts</h4>

Display a line chart.

```python
st.scatter_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.map">
<Image pure alt="screenshot" src="/images/api/map.jpg" />

<h4>Scatterplots on maps</h4>

Display a map with points on it.

```python
st.map(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.pyplot">
<Image pure alt="screenshot" src="/images/api/pyplot.jpg" />

<h4>Matplotlib</h4>

Display a matplotlib.pyplot figure.

```python
st.pyplot(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.altair_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Altair</h4>

Display a chart using the Altair library.

```python
st.altair_chart(my_altair_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.vega_lite_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Vega-Lite</h4>

Display a chart using the Vega-Lite library.

```python
st.vega_lite_chart(my_vega_lite_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.plotly_chart">
<Image pure alt="screenshot" src="/images/api/plotly_chart.jpg" />

<h4>Plotly</h4>

Display an interactive Plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bokeh_chart">
<Image pure alt="screenshot" src="/images/api/bokeh_chart.jpg" />

<h4>Bokeh</h4>

Display an interactive Bokeh chart.

```python
st.bokeh_chart(my_bokeh_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.pydeck_chart">
<Image pure alt="screenshot" src="/images/api/pydeck_chart.jpg" />

<h4>PyDeck</h4>

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.graphviz_chart">
<Image pure alt="screenshot" src="/images/api/graphviz_chart.jpg" />

<h4>GraphViz</h4>

Display a graph using the dagre-d3 library.

```python
st.graphviz_chart(my_graphviz_spec)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/tvst/plost">

<Image pure alt="screenshot" src="/images/api/components/plost.jpg" />

<h4>Plost</h4>

A deceptively simple plotting library for Streamlit. Created by [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

</ComponentCard>

<ComponentCard href="https://github.com/facebookresearch/hiplot">

<Image pure alt="screenshot" src="/images/api/components/hiplot.jpg" />

<h4>HiPlot</h4>

High dimensional Interactive Plotting. Created by [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-echarts">

<Image pure alt="screenshot" src="/images/api/components/echarts.jpg" />

<h4>ECharts</h4>

High dimensional Interactive Plotting. Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/explosion/spacy-streamlit">

<Image pure alt="screenshot" src="/images/api/components/spacy.jpg" />

<h4>Spacy-Streamlit</h4>

spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

</ComponentCard>

<ComponentCard href="https://github.com/ChrisDelClea/streamlit-agraph">

<Image pure alt="screenshot" src="/images/api/components/agraph.jpg" />

<h4>Streamlit Agraph</h4>

A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-chart-annotations.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

</ComponentCard>

</ComponentSlider>

### Input widgets

<br />

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.button">

<Image pure alt="screenshot" src="/images/api/button.svg" />

<h4>Button</h4>

Display a button widget.

```python
clicked = st.button("Click me")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.download_button">

<Image pure alt="screenshot" src="/images/api/download_button.svg" />

<h4>Download button</h4>

Display a download button widget.

```python
st.download_button("Download file", file)
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button">

<Image pure alt="screenshot" src="/images/api/form_submit_button.svg" />

<h4>Form button</h4>

Display a form submit button. For use with `st.form`.

```python
st.form_submit_button("Sign up")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.link_button">

<Image pure alt="screenshot" src="/images/api/link_button.svg" />

<h4>Link button</h4>

Display a link button.

```python
st.link_button("Go to gallery", url)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.page_link">

<Image pure alt="screenshot" src="/images/api/page_link.jpg" />

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.checkbox">

<Image pure alt="screenshot" src="/images/api/checkbox.jpg" />

<h4>Checkbox</h4>

Display a checkbox widget.

```python
selected = st.checkbox("I agree")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.color_picker">

<Image pure alt="screenshot" src="/images/api/color_picker.jpg" />

<h4>Color picker</h4>

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.multiselect">

<Image pure alt="screenshot" src="/images/api/multiselect.jpg" />

<h4>Multiselect</h4>

Display a multiselect widget. The multiselect widget starts as empty.

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.radio">

<Image pure alt="screenshot" src="/images/api/radio.jpg" />

<h4>Radio</h4>

Display a radio button widget.

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.selectbox">

<Image pure alt="screenshot" src="/images/api/selectbox.jpg" />

<h4>Selectbox</h4>

Display a select widget.

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.select_slider">

<Image pure alt="screenshot" src="/images/api/select_slider.jpg" />

<h4>Select-slider</h4>

Display a slider widget to select items from a list.

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.toggle">

<Image pure alt="screenshot" src="/images/api/toggle.jpg" />

<h4>Toggle</h4>

Display a toggle widget.

```python
activated = st.toggle("Activate")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.number_input">

<Image pure alt="screenshot" src="/images/api/number_input.jpg" />

<h4>Number input</h4>

Display a numeric input widget.

```python
choice = st.number_input("Pick a number", 0, 10)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.slider">

<Image pure alt="screenshot" src="/images/api/slider.jpg" />

<h4>Slider</h4>

Display a slider widget.

```python
number = st.slider("Pick a number", 0, 100)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.date_input">

<Image pure alt="screenshot" src="/images/api/date_input.jpg" />

<h4>Date input</h4>

Display a date input widget.

```python
date = st.date_input("Your birthday")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.time_input">

<Image pure alt="screenshot" src="/images/api/time_input.jpg" />

<h4>Time input</h4>

Display a time input widget.

```python
time = st.time_input("Meeting time")
```

</RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

<h4>Chat input</h4>

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_area">

<Image pure alt="screenshot" src="/images/api/text_area.jpg" />

<h4>Text-area</h4>

Display a multi-line text input widget.

```python
text = st.text_area("Text to translate")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_input">

<Image pure alt="screenshot" src="/images/api/text_input.jpg" />

<h4>Text input</h4>

Display a single-line text input widget.

```python
name = st.text_input("First name")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.experimental_data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.file_uploader">

<Image pure alt="screenshot" src="/images/api/file_uploader.jpg" />

<h4>File Uploader</h4>

Display a file uploader widget.

```python
data = st.file_uploader("Upload a CSV")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.camera_input">

<Image pure alt="screenshot" src="/images/api/camera_input.jpg" />

<h4>Camera input</h4>

Display a widget that allows users to upload images directly from a camera.

```python
image = st.camera_input("Take a picture")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

<h4>Streamlit Elements</h4>

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

<h4>Stqdm</h4>

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/innerdoc/streamlit-timeline">

<Image pure alt="screenshot" src="/images/api/components/timeline.jpg" />

<h4>Timeline</h4>

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
  timeline(f.read(), height=800)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-camera-input-live">

<Image pure alt="screenshot" src="/images/api/components/camera-live.jpg" />

<h4>Camera input live</h4>

Alternative for st.camera_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

<h4>Streamlit Ace</h4>

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/AI-Yash/st-chat">

<Image pure alt="screenshot" src="/images/api/components/chat.jpg" />

<h4>Streamlit Chat</h4>

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```

</ComponentCard>

<ComponentCard href="https://github.com/victoryhb/streamlit-option-menu">

<Image pure alt="screenshot" src="/images/api/components/option-menu.jpg" />

<h4>Streamlit Option Menu</h4>

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'],
  icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-toggle.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!", """🥷 Surprise! Here's some additional content""",)
```

</ComponentCard>

</ComponentSlider>

### Media elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/media/st.image">

<Image pure alt="screenshot" src="/images/api/image.jpg" />

<h4>Image</h4>

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

</RefCard>
<RefCard href="/develop/api-reference/media/st.audio">

<Image pure alt="screenshot" src="/images/api/audio.jpg" />

<h4>Audio</h4>

Display an audio player.

```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```

</RefCard>
<RefCard href="/develop/api-reference/media/st.video">

<Image pure alt="screenshot" src="/images/api/video.jpg" />

<h4>Video</h4>

Display a video player.

```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/whitphx/streamlit-webrtc">

<Image pure alt="screenshot" src="/images/api/components/webrtc.jpg" />

<h4>Streamlit Webrtc</h4>

Handling and transmitting real-time video/audio streams with Streamlit. Created by [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas

st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/fcakyon/streamlit-image-comparison">

<Image pure alt="screenshot" src="/images/api/components/image-comparison.jpg" />

<h4>Image Comparison</h4>

Compare images with a slider using [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison

image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

</ComponentCard>

<ComponentCard href="https://github.com/turner-anderson/streamlit-cropper">

<Image pure alt="screenshot" src="/images/api/components/cropper.jpg" />

<h4>Streamlit Cropper</h4>

A simple image cropper for Streamlit. Created by [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper

st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates

streamlit_image_coordinates("https://placekitten.com/200/300")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

</ComponentSlider>

### Layouts and containers

<br />

<TileContainer>
<RefCard href="/develop/api-reference/layout/st.columns">

<Image pure alt="screenshot" src="/images/api/columns.jpg" />

<h4>Columns</h4>

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.container">

<Image pure alt="screenshot" src="/images/api/container.jpg" />

<h4>Container</h4>

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.dialog">

<Image pure alt="screenshot" src="/images/api/dialog.jpg" />

<h4>Modal dialogs</h4>

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.experimental_dialog()
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.empty">

<Image pure alt="screenshot" src="/images/api/empty.jpg" />

<h4>Empty</h4>

Insert a single-element container.

```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.expander">

<Image pure alt="screenshot" src="/images/api/expander.jpg" />

<h4>Expander</h4>

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
  st.write("This is more content")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.popover">

<Image pure alt="screenshot" src="/images/api/popover.svg" />

<h4>Popover</h4>

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
  st.checkbox("Show completed")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.sidebar">

<Image pure alt="screenshot" src="/images/api/sidebar.jpg" />

<h4>Sidebar</h4>

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.tabs">

<Image pure alt="screenshot" src="/images/api/tabs.jpg" />

<h4>Tabs</h4>

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

<h4>Streamlit Elements</h4>

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>

### Chat elements

<br />

Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. `st.chat_input` lets you display a chat input widget so the user can type in a message.

<TileContainer>
<RefCard href="/develop/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

<h4>Chat input</h4>

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_message">

<Image pure alt="screenshot" src="/images/api/chat_message.jpg" />

<h4>Chat message</h4>

Insert a chat message container.

```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.status">

<Image pure alt="screenshot" src="/images/api/status.jpg" />

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">

<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
</TileContainer>

### Status elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/status/st.progress">

<Image pure alt="screenshot" src="/images/api/progress.jpg" />

<h4>Progress bar</h4>

Display a progress bar.

```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.spinner">

<Image pure alt="screenshot" src="/images/api/spinner.jpg" />

<h4>Spinner</h4>

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.status">

<Image pure alt="screenshot" src="/images/api/status.jpg" />

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.toast">

<Image pure alt="screenshot" src="/images/api/toast.jpg" />

<h4>Toast</h4>

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.balloons">

<Image pure alt="screenshot" src="/images/api/balloons.jpg" />

<h4>Balloons</h4>

Display celebratory balloons!

```python
do_something()

# Celebrate when all done!
st.balloons()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.snow">

<Image pure alt="screenshot" src="/images/api/snow.jpg" />

<h4>Snowflakes</h4>

Display celebratory snowflakes!

```python
do_something()

# Celebrate when all done!
st.snow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.success">

<Image pure alt="screenshot" src="/images/api/success.jpg" />

<h4>Success box</h4>

Display a success message.

```python
st.success("Match found!")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.info">

<Image pure alt="screenshot" src="/images/api/info.jpg" />

<h4>Info box</h4>

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.warning">

<Image pure alt="screenshot" src="/images/api/warning.jpg" />

<h4>Warning box</h4>

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.error">

<Image pure alt="screenshot" src="/images/api/error.jpg" />

<h4>Error box</h4>

Display error message.

```python
st.error("We encountered an error")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.exception">

<Image pure alt="screenshot" src="/images/api/exception.jpg" />

<h4>Exception output</h4>

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

<h4>Stqdm</h4>

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/Socvest/streamlit-custom-notification-box">

<Image pure alt="screenshot" src="/images/api/components/custom-notification-box.jpg" />

<h4>Custom notification box</h4>

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-emojis.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(emoji="🎈", font_size=54,
  falling_speed=5, animation_length="infinite",)
```

</ComponentCard>

</ComponentSlider>

## App logic and configuration

### Navigation and pages

<br />

<TileContainer>

<RefCard href="/develop/api-reference/navigation/st.switch_page">

<h4>Switch page</h4>

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.page_link">

<Image pure alt="screenshot" src="/images/api/page_link.jpg" />

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

</RefCard>

</TileContainer>

### Execution flow

<br />

<TileContainer>
<RefCard href="/develop/api-reference/execution-flow/st.dialog" size="full">

<Image pure alt="screenshot" src="/images/api/dialog.jpg" />

<h4>Modal dialogs</h4>

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.experimental_dialog()
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.form" size="half">

<h4>Forms</h4>

Create a form that batches elements together with a “Submit" button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.fragment" size="half">

<h4>Partial reruns</h4>

Define a fragment to rerun independently from the rest of the script.

```python
@st.experimental_fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.rerun">

<h4>Rerun script</h4>

Rerun the script immediately.

```python
st.rerun()
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.stop">

<h4>Stop execution</h4>

Stops execution immediately.

```python
st.stop()
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/kmcgrady/streamlit-autorefresh">

<Image pure alt="screenshot" src="/images/api/components/autorefresh.jpg" />

<h4>Autorefresh</h4>

Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>

### Caching and state

<br />

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.cache_data" size="half">

<h4>Cache data</h4>

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_resource" size="half">

<h4>Cache resource</h4>

Function decorator to cache functions that return global resources (e.g. database connections, ML models).

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.session_state">

<h4>Session state</h4>

Session state is a way to share variables between reruns, for each user session.

```python
st.session_state['key'] = value
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.query_params">

<h4>Query parameters</h4>

Get, set, or clear the query parameters that are shown in the browser's URL bar.

```python
st.query_params[key] = value
st.query_params.clear()
```

</RefCard>

</TileContainer>

### Connections and databases

#### Setup your connection

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connection" size="half">

<Image pure alt="screenshot" src="/images/api/connection.svg" />

<h4>Create a connection</h4>

Connect to a data source or API

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

</RefCard>
</TileContainer>

#### Built-in connections

<TileContainer>

<RefCard href="/develop/api-reference/connections/st.connections.snowflakeconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SnowflakeConnection.svg" />

<h4>SnowflakeConnection</h4>

A connection to Snowflake.

```python
conn = st.connection('snowflake')
```

</RefCard>

<RefCard href="/develop/api-reference/connections/st.connections.sqlconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SQLConnection.svg" />

<h4>SQLConnection</h4>

A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```

</RefCard>
</TileContainer>

#### Build your own connections

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.baseconnection" size="half">

<h4>Connection base class</h4>

Build your own connection with `BaseConnection`.

```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

</RefCard>

</TileContainer>

#### Secrets management

<TileContainer>

<RefCard href="/develop/api-reference/connections/st.secrets" size="half">

<h4>Secrets singleton</h4>

Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```

</RefCard>
<RefCard href="/develop/api-reference/connections/secrets.toml" size="half">

<h4>Secrets file</h4>

Save your secrets in a per-project or per-profile TOML file.

```python
OpenAI_key = "<YOUR_SECRET_KEY>"
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/mkhorasani/Streamlit-Authenticator">

<Image pure alt="screenshot" src="/images/api/components/authenticator.jpg" />

<h4>Authenticator</h4>

A secure authentication module to validate user credentials. Created by [@mkhorasani](https://github.com/mkhorasani).

```python
import streamlit_authenticator as stauth

authenticator = stauth.Authenticate( config['credentials'], config['cookie']['name'],
config['cookie']['key'], config['cookie']['expiry_days'], config['preauthorized'])
```

</ComponentCard>

<ComponentCard href="https://github.com/gagangoku/streamlit-ws-localstorage">

<Image pure alt="screenshot" src="/images/api/components/localstorage.jpg" />

<h4>WS localStorage</h4>

A simple synchronous way of accessing localStorage from your app. Created by [@gagangoku](https://github.com/gagangoku).

```python
from streamlit_ws_localstorage import injectWebsocketCode

ret = conn.setLocalStorageVal(key='k1', val='v1')
st.write('ret: ' + ret)
```

</ComponentCard>

<ComponentCard href="https://github.com/conradbez/streamlit-auth0">

<Image pure alt="screenshot" src="/images/api/components/auth0.jpg" />

<h4>Streamlit Auth0</h4>

The fastest way to provide comprehensive login inside Streamlit. Created by [@conradbez](https://github.com/conradbez).

```python
from auth0_component import login_button

user_info = login_button(clientId, domain = domain)
st.write(user_info)
```

</ComponentCard>

</ComponentSlider>

### Custom Components

<br />

<TileContainer>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.declare_component">

<h4>Declare a component</h4>

Create and register a custom component.

```python
st.components.v1.declare_component(
    "custom_slider",
    "/frontend",
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.html">

<h4>HTML</h4>

Display an HTML string in an iframe.

```python
st.components.v1.html(
    "<p>Foo bar.</p>"
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.iframe">

<h4>iframe</h4>

Load a remote URL in an iframe.

```python
st.components.v1.iframe(
    "docs.streamlit.io"
)
```

</RefCard>

</TileContainer>

### Utilities and user info

<br />

<TileContainer>
<RefCard href="/develop/api-reference/utilities/st.experimental_user">

<h4>User info</h4>

`st.experimental_user` returns information about the logged-in user of private apps on Streamlit Community Cloud.

```python
if st.experimental_user.email == "foo@corp.com":
  st.write("Welcome back, ", st.experimental_user.email)
else:
  st.write("You are not authorized to view this page.")
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.help">

<h4>Get help</h4>

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.html">

<h4>Render HTML</h4>

Renders HTML strings to your app.

```python
css = """
<style>
    p { color: red; }
</style>
"""
st.html(css)
```

</RefCard>
</TileContainer>

### Configuration

<br />

<TileContainer>
<RefCard href="/develop/api-reference/configuration/config.toml">

<h4>Configuration file</h4>

Configures the default settings for your app.

```
your-project/
├── .streamlit/
│   └── config.toml
└── your_app.py
```

</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_page_config">

<h4>Set page title, favicon, and more</h4>

Configures the default settings of the page.

```python
st.set_page_config(
  page_title="My app",
  page_icon=":shark:",
)
```

</RefCard>
</TileContainer>

## Developer tools

### App testing

<br />

<TileContainer>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest" size="full">

<h4>st.testing.v1.AppTest</h4>

`st.testing.v1.AppTest` simulates a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception

at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file" size="full">

<h4>AppTest.from_file</h4>

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_string" size="full">

<h4>AppTest.from_string</h4>

`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_string(app_script_as_string)
at.run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_function" size="full">

<h4>AppTest.from_function</h4>

`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_function(app_script_as_callable)
at.run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeblock" size="half">

<h4>Block</h4>

A representation of container elements, including:

- `st.chat_message`
- `st.columns`
- `st.sidebar`
- `st.tabs`
- The main body of the app.

```python
# at.sidebar returns a Block
at.sidebar.button[0].click().run()
assert not at.exception
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeelement" size="half">

<h4>Element</h4>

The base class for representation of all elements, including:

- `st.title`
- `st.header`
- `st.markdown`
- `st.dataframe`

```python
# at.title returns a sequence of Title
# Title inherits from Element
assert at.title[0].value == "My awesome app"
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton" size="third">

<h4>Button</h4>

A representation of `st.button` and `st.form_submit_button`.

```python
at.button[0].click().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treechatinput" size="third">

<h4>ChatInput</h4>

A representation of `st.chat_input`.

```python
at.chat_input[0].set_value("What is Streamlit?").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecheckbox" size="third">

<h4>Checkbox</h4>

A representation of `st.checkbox`.

```python
at.checkbox[0].check().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecolorpicker" size="third">

<h4>ColorPicker</h4>

A representation of `st.color_picker`.

```python
at.color_picker[0].pick("#FF4B4B").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treedateinput" size="third">

<h4>DateInput</h4>

A representation of `st.date_input`.

```python
release_date = datetime.date(2023, 10, 26)
at.date_input[0].set_value(release_date).run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treemultiselect" size="third">

<h4>Multiselect</h4>

A representation of `st.multiselect`.

```python
at.multiselect[0].select("New York").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treenumberinput" size="third">

<h4>NumberInput</h4>

A representation of `st.number_input`.

```python
at.number_input[0].increment().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeradio" size="third">

<h4>Radio</h4>

A representation of `st.radio`.

```python
at.radio[0].set_value("New York").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectslider" size="third">

<h4>SelectSlider</h4>

A representation of `st.select_slider`.

```python
at.select_slider[0].set_range("A","C").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectbox" size="third">

<h4>Selectbox</h4>

A representation of `st.selectbox`.

```python
at.selectbox[0].select("New York").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeslider" size="third">

<h4>Slider</h4>

A representation of `st.slider`.

```python
at.slider[0].set_range(2,5).run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextarea" size="third">

<h4>TextArea</h4>

A representation of `st.text_area`.

```python
at.text_area[0].input("Streamlit is awesome!").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextinput" size="third">

<h4>TextInput</h4>

A representation of `st.text_input`.

```python
at.text_input[0].input("Streamlit").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetimeinput" size="third">

<h4>TimeInput</h4>

A representation of `st.time_input`.

```python
at.time_input[0].increment().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetoggle" size="third">

<h4>Toggle</h4>

A representation of `st.toggle`.

```python
at.toggle[0].set_value("True").run()
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">

<Image pure alt="screenshot" src="/images/api/components/pandas-profiling.jpg" />

<h4>Pandas Profiling</h4>

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

<h4>Streamlit Ace</h4>

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/jrieke/streamlit-analytics">

<Image pure alt="screenshot" src="/images/api/components/analytics.jpg" />

<h4>Streamlit Analytics</h4>

Track & visualize user interactions with your streamlit app. Created by [@jrieke](https://github.com/jrieke).

```python
import streamlit_analytics

with streamlit_analytics.track():
    st.text_input("Write something")
```

</ComponentCard>

</ComponentSlider>
