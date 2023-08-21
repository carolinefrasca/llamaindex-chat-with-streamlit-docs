---
title: Create an app
slug: /library/get-started/create-an-app
---

# Create an app

If you've made it this far, chances are you've
[installed Streamlit](/library/get-started/installation) and
run through the basics in our [Main concepts](/library/get-started/main-concepts) guide. If
not, now is a good time to take a look.

The easiest way to learn how to use Streamlit is to try things out yourself. As you read through this guide, test each method. As long as your app is running, every time you add a new element to your script and save, Streamlit's UI will ask if you'd like to rerun the app and view the changes. This allows you to work in a fast interactive loop: you write some code, save it, review the output, write some more, and so on, until you're happy with the results. The goal is to use Streamlit to create an interactive app for your data or model and along the way to use Streamlit to review, debug, perfect, and share your code.

In this guide, you're going to use Streamlit's core features to
create an interactive app; exploring a public Uber dataset for pickups and
drop-offs in New York City. When you're finished, you'll know how to fetch
and cache data, draw charts, plot information on a map, and use interactive
widgets, like a slider, to filter results.

<Tip>

If you'd like to skip ahead and see everything at once, the [complete script
is available below](#lets-put-it-all-together).

</Tip>

## Create your first app

Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better. Please come join us on the community forum. We love to hear your questions, ideas, and help you work through your bugs — stop by today!

1. The first step is to create a new Python script. Let's call it
   `uber_pickups.py`.

2. Open `uber_pickups.py` in your favorite IDE or text editor, then add these
   lines:

   ```python
   import streamlit as st
   import pandas as pd
   import numpy as np
   ```

3. Every good app has a title, so let's add one:

   ```python
   st.title('Uber pickups in NYC')
   ```

4. Now it's time to run Streamlit from the command line:

   ```bash
   streamlit run uber_pickups.py
   ```

   Running a Streamlit app is no different than any other Python script. Whenever you need to view the app, you can use this command.

    <Tip>

   Did you know you can also pass a URL to `streamlit run`? This is great when combined with GitHub Gists. For example:

   ```bash
   streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
   ```

   </Tip>

5. As usual, the app should automatically open in a new tab in your
   browser.

## Fetch some data

Now that you have an app, the next thing you'll need to do is fetch the Uber
dataset for pickups and drop-offs in New York City.

1. Let's start by writing a function to load the data. Add this code to your
   script:

   ```python
   DATE_COLUMN = 'date/time'
   DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

   def load_data(nrows):
       data = pd.read_csv(DATA_URL, nrows=nrows)
       lowercase = lambda x: str(x).lower()
       data.rename(lowercase, axis='columns', inplace=True)
       data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
       return data
   ```

   You'll notice that `load_data` is a plain old function that downloads some
   data, puts it in a Pandas dataframe, and converts the date column from text
   to datetime. The function accepts a single parameter (`nrows`), which
   specifies the number of rows that you want to load into the dataframe.

2. Now let's test the function and review the output. Below your function, add
   these lines:

   ```python
   # Create a text element and let the reader know the data is loading.
   data_load_state = st.text('Loading data...')
   # Load 10,000 rows of data into the dataframe.
   data = load_data(10000)
   # Notify the reader that the data was successfully loaded.
   data_load_state.text('Loading data...done!')
   ```

   You'll see a few buttons in the upper-right corner of your app asking if
   you'd like to rerun the app. Choose **Always rerun**, and you'll see your
   changes automatically each time you save.

Ok, that's underwhelming...

It turns out that it takes a long time to download data, and load 10,000 lines
into a dataframe. Converting the date column into datetime isn’t a quick job
either. You don’t want to reload the data each time the app is updated –
luckily Streamlit allows you to cache the data.

## Effortless caching

1. Try adding `@st.cache_data` before the `load_data` declaration:

   ```python
   @st.cache_data
   def load_data(nrows):
   ```

2. Then save the script, and Streamlit will automatically rerun your app. Since
   this is the first time you’re running the script with `@st.cache_data`, you won't
   see anything change. Let’s tweak your file a little bit more so that you can
   see the power of caching.

3. Replace the line `data_load_state.text('Loading data...done!')` with this:

   ```python
   data_load_state.text("Done! (using st.cache_data)")
   ```

4. Now save. See how the line you added appeared immediately? If you take a
   step back for a second, this is actually quite amazing. Something magical is
   happening behind the scenes, and it only takes one line of code to activate
   it.

### How's it work?

Let's take a few minutes to discuss how `@st.cache_data` actually works.

When you mark a function with Streamlit’s cache annotation, it tells Streamlit
that whenever the function is called that it should check two things:

1. The input parameters you used for the function call.
2. The code inside the function.

If this is the first time Streamlit has seen both these items, with these exact
values, and in this exact combination, it runs the function and stores the
result in a local cache. The next time the function is called, if the two
values haven't changed, then Streamlit knows it can skip executing the function
altogether. Instead, it reads the output from the local cache and passes it on
to the caller -- like magic.

"But, wait a second," you’re saying to yourself, "this sounds too good to be
true. What are the limitations of all this awesomesauce?"

Well, there are a few:

1. Streamlit will only check for changes within the current working directory.
   If you upgrade a Python library, Streamlit's cache will only notice this if
   that library is installed inside your working directory.
2. If your function is not deterministic (that is, its output depends on random
   numbers), or if it pulls data from an external time-varying source (for
   example, a live stock market ticker service) the cached value will be
   none-the-wiser.
3. Lastly, you should avoid mutating the output of a function cached with `st.cache_data` since cached
   values are stored by reference.

While these limitations are important to keep in mind, they tend not to be an
issue a surprising amount of the time. Those times, this cache is really
transformational.

<Tip>

Whenever you have a long-running computation in your code, consider
refactoring it so you can use `@st.cache_data`, if possible. Please read [Caching](/library/advanced-features/caching) for more details.
</Tip>

Now that you know how caching with Streamlit works, let’s get back to the Uber
pickup data.

## Inspect the raw data

It's always a good idea to take a look at the raw data you're working with
before you start working with it. Let's add a subheader and a printout of the
raw data to the app:

```python
st.subheader('Raw data')
st.write(data)
```

In the [Main concepts](/library/get-started/main-concepts) guide you learned that
[`st.write`](/library/api-reference/write-magic/st.write) will render almost anything you pass
to it. In this case, you're passing in a dataframe and it's rendering as an
interactive table.

[`st.write`](/library/api-reference/write-magic/st.write) tries to do the right thing based on
the data type of the input. If it isn't doing what you expect you can use a
specialized command like [`st.dataframe`](/library/api-reference/data/st.dataframe)
instead. For a full list, see [API reference](/library/api-reference).

## Draw a histogram

Now that you've had a chance to take a look at the dataset and observe what's
available, let's take things a step further and draw a histogram to see what
Uber's busiest hours are in New York City.

1. To start, let's add a subheader just below the raw data section:

   ```python
   st.subheader('Number of pickups by hour')
   ```

2. Use NumPy to generate a histogram that breaks down pickup times binned by
   hour:

   ```python
   hist_values = np.histogram(
       data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
   ```

3. Now, let's use Streamlit's
   [`st.bar_chart()`](/library/api-reference/charts/st.bar_chart) method to draw this
   histogram.

   ```python
   st.bar_chart(hist_values)
   ```

4. Save your script. This histogram should show up in your app right away.
   After a quick review, it looks like the busiest time is 17:00 (5 P.M.).

To draw this diagram we used Streamlit's native `bar_chart()` method, but it's
important to know that Streamlit supports more complex charting libraries like
Altair, Bokeh, Plotly, Matplotlib and more. For a full list, see
[supported charting libraries](/library/api-reference/charts).

## Plot data on a map

Using a histogram with Uber's dataset helped us determine what the busiest
times are for pickups, but what if we wanted to figure out where pickups were
concentrated throughout the city. While you could use a bar chart to show this
data, it wouldn't be easy to interpret unless you were intimately familiar with
latitudinal and longitudinal coordinates in the city. To show pickup
concentration, let's use Streamlit [`st.map()`](/library/api-reference/charts/st.map)
function to overlay the data on a map of New York City.

1. Add a subheader for the section:

   ```python
   st.subheader('Map of all pickups')
   ```

2. Use the `st.map()` function to plot the data:

   ```python
   st.map(data)
   ```

3. Save your script. The map is fully interactive. Give it a try by panning or
   zooming in a bit.

After drawing your histogram, you determined that the busiest hour for Uber
pickups was 17:00. Let's redraw the map to show the concentration of pickups
at 17:00.

1. Locate the following code snippet:

   ```python
   st.subheader('Map of all pickups')
   st.map(data)
   ```

2. Replace it with:

   ```python
   hour_to_filter = 17
   filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
   st.subheader(f'Map of all pickups at {hour_to_filter}:00')
   st.map(filtered_data)
   ```

3. You should see the data update instantly.

To draw this map we used the [`st.map`](/library/api-reference/charts/st.map) function that's built into Streamlit, but
if you'd like to visualize complex map data, we encourage you to take a look at
the [`st.pydeck_chart`](/library/api-reference/charts/st.pydeck_chart).

## Filter results with a slider

In the last section, when you drew the map, the time used to filter results was
hardcoded into the script, but what if we wanted to let a reader dynamically
filter the data in real time? Using Streamlit's widgets you can. Let's add a
slider to the app with the `st.slider()` method.

1. Locate `hour_to_filter` and replace it with this code snippet:

   ```python
   hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
   ```

2. Use the slider and watch the map update in real time.

## Use a button to toggle data

Sliders are just one way to dynamically change the composition of your app.
Let's use the [`st.checkbox`](/library/api-reference/widgets/st.checkbox) function to add a
checkbox to your app. We'll use this checkbox to show/hide the raw data
table at the top of your app.

1. Locate these lines:

   ```python
   st.subheader('Raw data')
   st.write(data)
   ```

2. Replace these lines with the following code:

   ```python
   if st.checkbox('Show raw data'):
       st.subheader('Raw data')
       st.write(data)
   ```

We're sure you've got your own ideas. When you're done with this tutorial, check out all the widgets that Streamlit exposes in our [API Reference](/library/api-reference).

## Let's put it all together

That's it, you've made it to the end. Here's the complete script for our interactive app.

<Tip>

If you've skipped ahead, after you've created your script, the command to run
Streamlit is `streamlit run [app name]`.

</Tip>

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
```

## Share your app

After you’ve built a Streamlit app, it's time to share it! To show it off to the world you can use **Streamlit Community Cloud** to deploy, manage, and share your app for free.

It works in 3 simple steps:

1. Put your app in a public GitHub repo (and make sure it has a requirements.txt!)
2. Sign into [share.streamlit.io](https://share.streamlit.io)
3. Click 'Deploy an app' and then paste in your GitHub URL

That's it! 🎈 You now have a publicly deployed app that you can share with the world. Click to learn more about [how to use Streamlit Community Cloud](/streamlit-community-cloud).

## Get help

That's it for getting started, now you can go and build your own apps! If you
run into difficulties here are a few things you can do.

- Check out our [community forum](https://discuss.streamlit.io/) and post a question
- Quick help from command line with `streamlit help`
- Go through our [Knowledge Base](/knowledge-base) for tips, step-by-step tutorials, and articles that answer your questions about creating and deploying Streamlit apps.
- Read more documentation! Check out:
  - [Advanced features](/library/advanced-features) for things like caching, theming, and adding statefulness to apps.
  - [API reference](/library/api-reference/) for examples of every Streamlit command.
