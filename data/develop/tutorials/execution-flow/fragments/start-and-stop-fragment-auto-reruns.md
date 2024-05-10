---
title: Start and stop a streaming fragment
slug: /develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns
---

# Start and stop a streaming fragment

Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. Additionally, you can tell Streamlit to rerun a fragment at a set time interval. This is great for streaming data or monitoring processes. You may want the user to start and stop this live streaming. To do this, programmatically set the `run_every` parameter for your fragment.

## Applied concepts

- Use a fragment to stream live data.
- Start and stop a fragment from automatically rerunning.

## Prerequisites

**`streamlit>=1.33.0`**

- This tutorial uses fragments, which require Streamlit version 1.33.0 or later.
- This tutorial assumes you have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments.

## Summary

In this example, you'll build an app that streams two data series in a line chart. Your app will gather recent data on the first load of a session and statically display the line chart. Two buttons in the sidebar will allow users to start and stop data streaming to update the chart in real time. You'll use a fragment to manage the frequency and scope of the live updates.

Here's a look at what you'll build:

<Collapse title="Complete code" expanded={false}>

```python
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def get_recent_data(last_timestamp):
    """Generate and return data from last timestamp to now, at most 60 seconds."""
    now = datetime.now()
    if now - last_timestamp > timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    sample_time = timedelta(seconds=0.5)  # time between data points
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data


if "data" not in st.session_state:
    st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))

if "stream" not in st.session_state:
    st.session_state.stream = False


def toggle_streaming():
    st.session_state.stream = not st.session_state.stream


st.title("Data feed")
st.sidebar.slider(
    "Check for updates every: (seconds)", 0.5, 5.0, value=1.0, key="run_every"
)
st.sidebar.button(
    "Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
)
st.sidebar.button(
    "Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
)

if st.session_state.stream is True:
    run_every = st.session_state.run_every
else:
    run_every = None


@st.experimental_fragment(run_every=run_every)
def show_latest_data():
    last_timestamp = st.session_state.data.index[-1]
    st.session_state.data = pd.concat(
        [st.session_state.data, get_recent_data(last_timestamp)]
    )
    st.session_state.data = st.session_state.data[-100:]
    st.line_chart(st.session_state.data)


show_latest_data()
```

</Collapse>

<Cloud src="https://doc-tutorial-fragment-streaming.streamlit.app/?embed=true" height="550" />

## Build the example

### Initialize your app

1. In `your_repository`, create a file named `app.py`.
1. In a terminal, change directories to `your_repository` and start your app.

   ```bash
   streamlit run app.py
   ```

   Your app will be blank since you still need to add code.

1. In `app.py`, write the following:

   ```python
    import streamlit as st
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
   ```

   You'll be using these libraries as follows:

   - You'll work with two data series in a `pandas.DataFrame`.
   - You'll generate random data with `numpy`.
   - The data will have `datetime.datetime` index values.

1. Save your `app.py` file and view your running app.
1. Click "**Always rerun**" or hit your "**A**" key in your running app.

   Your running preview will automatically update as you save changes to `app.py`. Your preview will still be blank. Return to your code.

### Build a function to generate random, recent data

To begin with, you'll define a function to randomly generate some data for two time series, which you'll call "A" and "B." It's okay to skip this section if you just want to copy the function.

<Collapse title="Complete function to randomly generate sales data" expanded={false}>

```python
def get_recent_data(last_timestamp):
    """Generate and return data from last timestamp to now, at most 60 seconds."""
    now = datetime.now()
    if now - last_timestamp > timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    sample_time = timedelta(seconds=0.5)  # time between data points
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data
```

</Collapse>

1. Start your function definition.

   ```python
   def get_recent_data(last_timestamp):
       """Generate and return data from last timestamp to now, at most 60 seconds."""
   ```

   You'll pass the timestamp of your most recent datapoint to your data-generating function. Your function will use this to only return new data.

1. Get the current time and adjust the last timestamp if it is over 60 seconds ago.

   ```python
       now = datetime.now()
       if now - last_timestamp > timedelta(seconds=60):
           last_timestamp = now - timedelta(seconds=60)
   ```

   By updating the last timestamp, you'll ensure the function never returns more than 60 seconds of data.

1. Declare a new variable, `sample_time`, to define the time between datapoints. Calculate the timestamp of the first, new datapoint.

   ```python
       sample_time = timedelta(seconds=0.5)  # time between data points
       next_timestamp = last_timestamp + sample_time
   ```

1. Create a `datetime.datetime` index and generate two data series of the same length.

   ```python
       timestamps = np.arange(next_timestamp, now, sample_time)
       sample_values = np.random.randn(len(timestamps), 2)
   ```

1. Combine the data series with the index into a `pandas.DataFrame` and return the data.

   ```python
       data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
       return data
   ```

1. (Optional) Test out your function by calling it and displaying the data.

   ```python
   data = get_recent_data(datetime.now() - timedelta(seconds=60))
   data
   ```

   Save your `app.py` file to see the preview. Delete these two lines when finished.

### Initialize Session State values for your app

Since you will dynamically change the `run_every` parameter of `@st.experimental_fragment()`, you'll need to initialize the associated variables and Session State values before defining your fragment function. Your fragment function will also read and update values in Session State, so you can define those now to make the fragment function easier to understand.

1. Initialize your data for the first app load in a session.

   ```python
   if "data" not in st.session_state:
       st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))
   ```

   Your app will display this initial data in a static line chart before a user starts streaming data.

1. Initialize `"stream"` in Session State to turn streaming on and off. Set the default to off (`False`).

   ```python
   if "stream" not in st.session_state:
       st.session_state.stream = False
   ```

1. Create a callback function to toggle `"stream"` between `True` and `False`.

   ```python
   def toggle_streaming():
       st.session_state.stream = not st.session_state.stream
   ```

1. Add a title to your app.

   ```python
   st.title("Data feed")
   ```

1. Add a slider to the sidebar to set how frequently to check for data while streaming.

   ```python
   st.sidebar.slider(
       "Check for updates every: (seconds)", 0.5, 5.0, value=1.0, key="run_every"
   )
   ```

1. Add buttons to the sidebar to turn streaming on and off.

   ```python
   st.sidebar.button(
       "Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
   )
   st.sidebar.button(
       "Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
   )
   ```

   Both functions use the same callback to toggle `"stream"` in Session State. Use the current value `"stream"` to disable one of the buttons. This ensures the buttons are always consistent with the current state; "**Start streaming**" is only clickable when streaming is off, and "**Stop streaming**" is only clickable when streaming is on. The buttons also provide status to the user by highlighting which action is available to them.

1. Create and set a new variable, `run_every`, that will determine whether or not the fragment function will rerun automatically (and how fast).

   ```python
   if st.session_state.stream is True:
       run_every = st.session_state.run_every
   else:
       run_every = None
   ```

### Build a fragment function to stream data

To allow the user to turn data streaming on and off, you must set the `run_every` parameter in the `@st.experimental_fragment()` decorator.

<Collapse title="Complete function to show and stream data" expanded={false}>

```python
@st.experimental_fragment(run_every=run_every)
def show_latest_data():
    last_timestamp = st.session_state.data.index[-1]
    st.session_state.data = pd.concat(
        [st.session_state.data, get_recent_data(last_timestamp)]
    )
    st.session_state.data = st.session_state.data[-100:]
    st.line_chart(st.session_state.data)
```

</Collapse>

1. Use an [`@st.experimental_fragment`](/develop/api-reference/execution-flow/st.fragment) decorator and start your function definition.

   ```python
    @st.experimental_fragment(run_every=run_every)
    def show_latest_data():
   ```

   Use the `run_every` variable declared above to set the parameter of the same name.

1. Retrieve the timestamp of the last datapoint in Session State.

   ```python
       last_timestamp = st.session_state.data.index[-1]
   ```

1. Update the data in Session State and trim to keep only the last 100 timestamps.

   ```python
       st.session_state.data = pd.concat(
           [st.session_state.data, get_recent_data(last_timestamp)]
       )
       st.session_state.data = st.session_state.data[-100:]
   ```

1. Show the data in a line chart.

   ```python
       st.line_chart(st.session_state.data)
   ```

   Your fragment-function definition is complete.

### Call and test out your fragment function

1. Call your function at the bottom of your code.

   ```python
   show_latest_data()
   ```

1. Test out your app by clicking "**Start streaming**." Try adjusting the frequency of updates.

### Next steps

Try adjusting the frequency of data generation or how much data is kept in Session State. Within `get_recent_data` try setting `sample_time` with a widget.

Try using [st.plotly_chart](/develop/api-reference/charts/st.plotly_chart) or [st.altair_chart](/develop/api-reference/charts/st.altair_chart) to add labels to your chart.
