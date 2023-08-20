---
title: API Reference
slug: /library/api-reference
next: caching
previous: index.md
---

# API reference

Streamlit makes it easy for you to visualize, mutate, and share data. The API
reference is organized by activity type, like displaying data or optimizing
performance. Each section includes methods associated with the activity type,
including examples.

Browse our API below and click to learn more about any of our available commands! 🎈

## Display almost anything

<TileContainer>
<RefCard href="/library/api-reference/write-magic/st.write">

#### st.write

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/library/api-reference/write-magic/magic">

#### Magic

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>

## Text elements

<TileContainer>
<RefCard href="/library/api-reference/text/st.markdown">

<Image pure alt="screenshot" src="/images/api/markdown.jpg" />

#### Markdown

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.title">

<Image pure alt="screenshot" src="/images/api/title.jpg" />

#### Title

Display text in title formatting.

```python
st.title("The app title")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.header">

<Image pure alt="screenshot" src="/images/api/header.jpg" />

#### Header

Display text in header formatting.

```python
st.header("This is a header")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.subheader">

<Image pure alt="screenshot" src="/images/api/subheader.jpg" />

#### Subheader

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.caption">

<Image pure alt="screenshot" src="/images/api/caption.jpg" />

#### Caption

Display text in small font.

```python
st.caption("This is written small caption text")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.code">

<Image pure alt="screenshot" src="/images/api/code.jpg" />

#### Code block

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.text">

<Image pure alt="screenshot" src="/images/api/text.jpg" />

#### Preformatted text

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.latex">

<Image pure alt="screenshot" src="/images/api/latex.jpg" />

#### LaTeX

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

</RefCard>
<RefCard href="/library/api-reference/text/st.divider">

<Image pure alt="screenshot" src="/images/api/divider.jpg" />

#### Divider

Display a horizontal rule.

```python
st.divider()
```

</RefCard>
</TileContainer>

<ComponentSlider>
<ComponentCard href="https://github.com/tvst/st-annotated-text">

<Image pure alt="screenshot" src="/images/api/components/annotated-text.jpg" />

#### Annotated text

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

#### Drawable Canvas

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/JohnSnowLabs/nlu">

<Image pure alt="screenshot" src="/images/api/components/nlu.jpg" />

#### NLU

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load('sentiment').predict('I love NLU! <3')
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-mentions.jpg" />

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
mention(label="An awesome Streamlit App", icon="streamlit",  url="https://extras.streamlit.app",)
```

</ComponentCard>
</ComponentSlider>

## Data elements

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

## Chart elements

<TileContainer>
<RefCard href="/library/api-reference/charts/st.line_chart">
<Image pure alt="screenshot" src="/images/api/line_chart.jpg" />

#### Simple line charts

Display a line chart.

```python
st.line_chart(my_data_frame)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.area_chart">
<Image pure alt="screenshot" src="/images/api/area_chart.jpg" />

#### Simple area charts

Display an area chart.

```python
st.area_chart(my_data_frame)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.bar_chart">
<Image pure alt="screenshot" src="/images/api/bar_chart.jpg" />

#### Simple bar charts

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.map">
<Image pure alt="screenshot" src="/images/api/map.jpg" />

#### Scatterplots on maps

Display a map with points on it.

```python
st.map(my_data_frame)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.pyplot">
<Image pure alt="screenshot" src="/images/api/pyplot.jpg" />

#### Matplotlib

Display a matplotlib.pyplot figure.

```python
st.pyplot(my_mpl_figure)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.altair_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

#### Altair

Display a chart using the Altair library.

```python
st.altair_chart(my_altair_chart)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.vega_lite_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

#### Vega-Lite

Display a chart using the Vega-Lite library.

```python
st.vega_lite_chart(my_vega_lite_chart)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.plotly_chart">
<Image pure alt="screenshot" src="/images/api/plotly_chart.jpg" />

#### Plotly

Display an interactive Plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.bokeh_chart">
<Image pure alt="screenshot" src="/images/api/bokeh_chart.jpg" />

#### Bokeh

Display an interactive Bokeh chart.

```python
st.bokeh_chart(my_bokeh_chart)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.pydeck_chart">
<Image pure alt="screenshot" src="/images/api/pydeck_chart.jpg" />

#### PyDeck

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

</RefCard>
<RefCard href="/library/api-reference/charts/st.graphviz_chart">
<Image pure alt="screenshot" src="/images/api/graphviz_chart.jpg" />

#### GraphViz

Display a graph using the dagre-d3 library.

```python
st.graphviz_chart(my_graphviz_spec)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/tvst/plost">

<Image pure alt="screenshot" src="/images/api/components/plost.jpg" />

#### Plost

A deceptively simple plotting library for Streamlit. Created by [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

</ComponentCard>

<ComponentCard href="https://github.com/facebookresearch/hiplot">

<Image pure alt="screenshot" src="/images/api/components/hiplot.jpg" />

#### HiPlot

High dimensional Interactive Plotting. Created by [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-echarts">

<Image pure alt="screenshot" src="/images/api/components/echarts.jpg" />

#### ECharts

High dimensional Interactive Plotting. Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

#### Streamlit Folium

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/explosion/spacy-streamlit">

<Image pure alt="screenshot" src="/images/api/components/spacy.jpg" />

#### Spacy-Streamlit

spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

</ComponentCard>

<ComponentCard href="https://github.com/ChrisDelClea/streamlit-agraph">

<Image pure alt="screenshot" src="/images/api/components/agraph.jpg" />

#### Streamlit Agraph

A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

#### Streamlit Lottie

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

#### Plotly Events

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-chart-annotations.jpg" />

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

</ComponentCard>

</ComponentSlider>

## Input widgets

<TileContainer>
<RefCard href="/library/api-reference/widgets/st.button">

<Image pure alt="screenshot" src="/images/api/button.jpg" />

#### Button

Display a button widget.

```python
clicked = st.button("Click me")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.experimental_data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

#### Data editor

Display a data editor widget.

```python
edited = st.experimental_data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.download_button">

<Image pure alt="screenshot" src="/images/api/download_button.jpg" />

#### Download button

Display a download button widget.

```python
st.download_button("Download file", file)
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.checkbox">

<Image pure alt="screenshot" src="/images/api/checkbox.jpg" />

#### Checkbox

Display a checkbox widget.

```python
selected = st.checkbox("I agree")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.radio">

<Image pure alt="screenshot" src="/images/api/radio.jpg" />

#### Radio

Display a radio button widget.

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.selectbox">

<Image pure alt="screenshot" src="/images/api/selectbox.jpg" />

#### Selectbox

Display a select widget.

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.multiselect">

<Image pure alt="screenshot" src="/images/api/multiselect.jpg" />

#### Multiselect

Display a multiselect widget. The multiselect widget starts as empty.

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.slider">

<Image pure alt="screenshot" src="/images/api/slider.jpg" />

#### Slider

Display a slider widget.

```python
number = st.slider("Pick a number", 0, 100)
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.select_slider">

<Image pure alt="screenshot" src="/images/api/select_slider.jpg" />

#### Select-slider

Display a slider widget to select items from a list.

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.text_input">

<Image pure alt="screenshot" src="/images/api/text_input.jpg" />

#### Text input

Display a single-line text input widget.

```python
name = st.text_input("First name")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.number_input">

<Image pure alt="screenshot" src="/images/api/number_input.jpg" />

#### Number input

Display a numeric input widget.

```python
choice = st.number_input("Pick a number", 0, 10)
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.text_area">

<Image pure alt="screenshot" src="/images/api/text_area.jpg" />

#### Text-area

Display a multi-line text input widget.

```python
text = st.text_area("Text to translate")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.date_input">

<Image pure alt="screenshot" src="/images/api/date_input.jpg" />

#### Date input

Display a date input widget.

```python
date = st.date_input("Your birthday")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.time_input">

<Image pure alt="screenshot" src="/images/api/time_input.jpg" />

#### Time input

Display a time input widget.

```python
time = st.time_input("Meeting time")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.file_uploader">

<Image pure alt="screenshot" src="/images/api/file_uploader.jpg" />

#### File Uploader

Display a file uploader widget.

```python
data = st.file_uploader("Upload a CSV")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.camera_input">

<Image pure alt="screenshot" src="/images/api/camera_input.jpg" />

#### Camera input

Display a widget that allows users to upload images directly from a camera.

```python
image = st.camera_input("Take a picture")
```

</RefCard>
<RefCard href="/library/api-reference/widgets/st.color_picker">

<Image pure alt="screenshot" src="/images/api/color_picker.jpg" />

#### Color picker

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

#### Streamlit Elements

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

#### Tags

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

#### Stqdm

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/innerdoc/streamlit-timeline">

<Image pure alt="screenshot" src="/images/api/components/timeline.jpg" />

#### Timeline

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
  timeline(f.read(), height=800)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-camera-input-live">

<Image pure alt="screenshot" src="/images/api/components/camera-live.jpg" />

#### Camera input live

Alternative for st.camera_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

#### Streamlit Ace

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/AI-Yash/st-chat">

<Image pure alt="screenshot" src="/images/api/components/chat.jpg" />

#### Streamlit Chat

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```

</ComponentCard>

<ComponentCard href="https://github.com/victoryhb/streamlit-option-menu">

<Image pure alt="screenshot" src="/images/api/components/option-menu.jpg" />

#### Streamlit Option Menu

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'],
  icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-toggle.jpg" />

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!", """🥷 Surprise! Here's some additional content""",)
```

</ComponentCard>

</ComponentSlider>

## Media elements

<TileContainer>
<RefCard href="/library/api-reference/media/st.image">

<Image pure alt="screenshot" src="/images/api/image.jpg" />

#### Image

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

</RefCard>
<RefCard href="/library/api-reference/media/st.audio">

<Image pure alt="screenshot" src="/images/api/audio.jpg" />

#### Audio

Display an audio player.

```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```

</RefCard>
<RefCard href="/library/api-reference/media/st.video">

<Image pure alt="screenshot" src="/images/api/video.jpg" />

#### Video

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

#### Streamlit Webrtc

Handling and transmitting real-time video/audio streams with Streamlit. Created by [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

#### Drawable Canvas

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas

st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/fcakyon/streamlit-image-comparison">

<Image pure alt="screenshot" src="/images/api/components/image-comparison.jpg" />

#### Image Comparison

Compare images with a slider using [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison

image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

</ComponentCard>

<ComponentCard href="https://github.com/turner-anderson/streamlit-cropper">

<Image pure alt="screenshot" src="/images/api/components/cropper.jpg" />

#### Streamlit Cropper

A simple image cropper for Streamlit. Created by [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper

st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

#### Image Coordinates

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates

streamlit_image_coordinates("https://placekitten.com/200/300")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

#### Streamlit Lottie

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

</ComponentSlider>

## Layouts and containers

<TileContainer>
<RefCard href="/library/api-reference/layout/st.sidebar">

<Image pure alt="screenshot" src="/images/api/sidebar.jpg" />

#### Sidebar

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

</RefCard>
<RefCard href="/library/api-reference/layout/st.columns">

<Image pure alt="screenshot" src="/images/api/columns.jpg" />

#### Columns

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

</RefCard>
<RefCard href="/library/api-reference/layout/st.tabs">

<Image pure alt="screenshot" src="/images/api/tabs.jpg" />

#### Tabs

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

</RefCard>
<RefCard href="/library/api-reference/layout/st.expander">

<Image pure alt="screenshot" src="/images/api/expander.jpg" />

#### Expander

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
  st.write("This is more content")
```

</RefCard>
<RefCard href="/library/api-reference/layout/st.container">

<Image pure alt="screenshot" src="/images/api/container.jpg" />

#### Container

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

</RefCard>
<RefCard href="/library/api-reference/layout/st.empty">

<Image pure alt="screenshot" src="/images/api/empty.jpg" />

#### Empty

Insert a single-element container.

```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

#### Streamlit Elements

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

#### Pydantic

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

#### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>

## Chat elements

Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. `st.chat_input` lets you display a chat input widget so the user can type in a message.

<TileContainer>
<RefCard href="/library/api-reference/chat/st.chat_message">

<Image pure alt="screenshot" src="/images/api/chat_message.jpg" />

#### Chat message

Insert a chat message container.

```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

</RefCard>
<RefCard href="/library/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

#### Chat input

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>
</TileContainer>

## Display progress and status

<TileContainer>
<RefCard href="/library/api-reference/status/st.progress">

<Image pure alt="screenshot" src="/images/api/progress.jpg" />

#### Progress bar

Display a progress bar.

```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.spinner">

<Image pure alt="screenshot" src="/images/api/spinner.jpg" />

#### Spinner

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.toast">

<Image pure alt="screenshot" src="/images/api/toast.jpg" />

#### Toast

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```

</RefCard>
<RefCard href="/library/api-reference/status/st.balloons">

<Image pure alt="screenshot" src="/images/api/balloons.jpg" />

#### Balloons

Display celebratory balloons!

```python
do_something()

# Celebrate when all done!
st.balloons()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.snow">

<Image pure alt="screenshot" src="/images/api/snow.jpg" />

#### Snowflakes

Display celebratory snowflakes!

```python
do_something()

# Celebrate when all done!
st.snow()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.error">

<Image pure alt="screenshot" src="/images/api/error.jpg" />

#### Error box

Display error message.

```python
st.error("We encountered an error")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.warning">

<Image pure alt="screenshot" src="/images/api/warning.jpg" />

#### Warning box

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.info">

<Image pure alt="screenshot" src="/images/api/info.jpg" />

#### Info box

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.success">

<Image pure alt="screenshot" src="/images/api/success.jpg" />

#### Success box

Display a success message.

```python
st.success("Match found!")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.exception">

<Image pure alt="screenshot" src="/images/api/exception.jpg" />

#### Exception output

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

#### Stqdm

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/Socvest/streamlit-custom-notification-box">

<Image pure alt="screenshot" src="/images/api/components/custom-notification-box.jpg" />

#### Custom notification box

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-emojis.jpg" />

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(emoji="🎈", font_size=54,
  falling_speed=5, animation_length="infinite",)
```

</ComponentCard>

</ComponentSlider>

## Control flow

<TileContainer>
<RefCard href="/library/api-reference/control-flow/st.form">

<!--<Image pure alt="screenshot" src="/images/api/form.jpg" />-->

#### Forms

Create a form that batches elements together with a “Submit" button.

```python
with st.form(key='my_form'):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")
```

</RefCard>
<RefCard href="/library/api-reference/control-flow/st.stop">

#### Stop execution

Stops execution immediately.

```python
st.stop()
```

</RefCard>
<RefCard href="/library/api-reference/control-flow/st.experimental_rerun">

#### Rerun script

Rerun the script immediately.

```python
st.experimental_rerun()
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/kmcgrady/streamlit-autorefresh">

<Image pure alt="screenshot" src="/images/api/components/autorefresh.jpg" />

#### Autorefresh

Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

#### Pydantic

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

#### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>

## Developer tools

<ComponentSlider>

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

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

#### Streamlit Ace

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/jrieke/streamlit-analytics">

<Image pure alt="screenshot" src="/images/api/components/analytics.jpg" />

#### Streamlit Anaylitics

Track & visualize user interactions with your streamlit app. Created by [@jrieke](https://github.com/jrieke).

```python
import streamlit_analytics

with streamlit_analytics.track():
    st.text_input("Write something")
```

</ComponentCard>

</ComponentSlider>

## Utilities

<TileContainer>
<RefCard href="/library/api-reference/utilities/st.set_page_config">

#### Set page title, favicon, and more

Configures the default settings of the page.

```python
st.set_page_config(
  page_title="My app",
  page_icon=":shark:",
)
```

</RefCard>
<RefCard href="/library/api-reference/utilities/st.echo">

<!--<Image pure alt="screenshot" src="/images/api/echo.jpg" />-->

#### Echo

Display some code on the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```

</RefCard>
<RefCard href="/library/api-reference/utilities/st.help">

#### Get help

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

</RefCard>
<RefCard href="/library/api-reference/utilities/st.experimental_get_query_params">

#### Get query parameters

Return the query parameters that are currently showing in the browser's URL bar.

```python
st.experimental_get_query_params()
```

</RefCard>
<RefCard href="/library/api-reference/utilities/st.experimental_set_query_params">

#### Set query parameters

Set the query parameters that are shown in the browser's URL bar.

```python
st.experimental_set_query_params(
  show_map=True,
  selected=["asia"]
)
```

</RefCard>
</TileContainer>

## Mutate charts

<TileContainer>
<RefCard href="/library/api-reference/mutate">

#### Add rows

Append a dataframe to the bottom of the current one in certain elements, for optimized data updates.

```python
element = st.line_chart(df)
element.add_rows(df_with_extra_rows)
```

</RefCard>
</TileContainer>

## State management

<TileContainer>
<RefCard href="/library/api-reference/session-state">

#### Session state

Session state is a way to share variables between reruns, for each user session.

```python
st.session_state['key'] = value
```

</RefCard>
</TileContainer>

## Connections and databases

<ComponentSlider>

<ComponentCard href="https://github.com/mkhorasani/Streamlit-Authenticator">

<Image pure alt="screenshot" src="/images/api/components/authenticator.jpg" />

#### Authenticator

A secure authentication module to validate user credentials. Created by [@mkhorasani](https://github.com/mkhorasani).

```python
import streamlit_authenticator as stauth

authenticator = stauth.Authenticate( config['credentials'], config['cookie']['name'],
config['cookie']['key'], config['cookie']['expiry_days'], config['preauthorized'])
```

</ComponentCard>

<ComponentCard href="https://github.com/gagangoku/streamlit-ws-localstorage">

<Image pure alt="screenshot" src="/images/api/components/localstorage.jpg" />

#### WS localStorage

A simple synchronous way of accessing localStorage from your app. Created by [@gagangoku](https://github.com/gagangoku).

```python
from streamlit_ws_localstorage import injectWebsocketCode

ret = conn.setLocalStorageVal(key='k1', val='v1')
st.write('ret: ' + ret)
```

</ComponentCard>

<ComponentCard href="https://github.com/conradbez/streamlit-auth0">

<Image pure alt="screenshot" src="/images/api/components/auth0.jpg" />

#### Streamlit Auth0

The fastest way to provide comprehensive login inside Streamlit. Created by [@conradbez](https://github.com/conradbez).

```python
from auth0_component import login_button

user_info = login_button(clientId, domain = domain)
st.write(user_info)
```

</ComponentCard>

</ComponentSlider>

## Performance

<TileContainer>
<RefCard href="/library/api-reference/performance/st.cache_data" size="half">

#### Cache data

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data
```

</RefCard>

<RefCard href="/library/api-reference/performance/st.cache_resource" size="half">

#### Cache resource

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

<RefCard href="/library/api-reference/performance/st.cache_data.clear" size="half">

#### Clear cached data

Clear all in-memory and on-disk data caches.

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data

if st.checkbox("Clear All"):
  # Clear values from *all* cache_data functions
  st.cache_data.clear()
```

</RefCard>

<RefCard href="/library/api-reference/performance/st.cache_resource.clear" size="half">

#### Clear cached resources

Clear all `st.cache_resource` caches.

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )

if st.checkbox("Clear All"):
  # Clear values from *all* cache_resource functions
  st.cache_data.clear()
```

</RefCard>

</TileContainer>

## Connections and databases

### Setup your connection

<TileContainer>
<RefCard href="/library/api-reference/connections/st.experimental_connection" size="half">

<Image pure alt="screenshot" src="/images/api/connection.jpg" />

#### Create a connection

Connect to a data source or API

```python
conn = st.experimental_connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

</RefCard>
</TileContainer>

### Built-in connections

<TileContainer>

<RefCard href="/library/api-reference/connections/st.connections.sqlconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SQLConnection.jpg" />

#### SQLConnection

A connection to a SQL database using SQLAlchemy.

```python
conn = st.experimental_connection('sql')
```

</RefCard>

<RefCard href="/library/api-reference/connections/st.connections.snowparkconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SnowparkConnection.jpg" />

#### SnowparkConnection

A connection to Snowflake Snowpark.

```python
conn = st.experimental_connection('snowpark')
```

</RefCard>
</TileContainer>

### Third-party connections

<TileContainer>
<RefCard href="/library/api-reference/connections/st.connections.experimentalbaseconnection" size="half">

#### Connection base class

Build your own connection with `ExperimentalBaseConnection`.

```python
class MyConnection(ExperimentalBaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

</RefCard>

</TileContainer>

## Personalization

<TileContainer>
<RefCard href="/library/api-reference/personalization/st.experimental_user" size="half">

#### User info

`st.experimental_user` returns information about the logged-in user of private apps on Streamlit Community Cloud.

```python
if st.experimental_user.email == "foo@corp.com":
  st.write("Welcome back, ", st.experimental_user.email)
else:
  st.write("You are not authorized to view this page.")
```

</RefCard>
</TileContainer>
