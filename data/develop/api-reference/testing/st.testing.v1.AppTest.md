---
title: st.testing.v1.AppTest
slug: /develop/api-reference/app-testing/st.testing.v1.apptest
---

<h1 style={{display: "none"}}></h1>

# The AppTest class

<Autofunction function="streamlit.testing.v1.AppTest" />

# Initialize a simulated app using AppTest

<Autofunction function="AppTest.from_file" />

<Autofunction function="AppTest.from_string" />

<Autofunction function="AppTest.from_function" />

# Run an AppTest script

<Autofunction function="AppTest.run" />

<Autofunction function="AppTest.switch_page" />

# Get AppTest script elements

The main value of `AppTest` is providing an API to programmatically inspect and interact with the elements and widgets produced by a running Streamlit app. Using the `AppTest.<element type>` properties or `AppTest.get()` method returns a collection of all the elements or widgets of the specified type that would have been displayed by running the app.

Note that you can also retrieve elements within a specific container in the same way - first retrieve the container, then retrieve the elements just in that container.

<Autofunction function="AppTest.get" />

<Autofunction function="AppTest.button" is_property />

<Autofunction function="AppTest.caption" />

<Autofunction function="AppTest.chat_input" />

<Autofunction function="AppTest.chat_message" />

<Autofunction function="AppTest.checkbox" />

<Autofunction function="AppTest.code" />

<Autofunction function="AppTest.color_picker" />

<Autofunction function="AppTest.columns" />

<Autofunction function="AppTest.dataframe" />

<Autofunction function="AppTest.date_input" />

<Autofunction function="AppTest.divider" />

<Autofunction function="AppTest.error" />

<Autofunction function="AppTest.exception" />

<Autofunction function="AppTest.expander" />

<Autofunction function="AppTest.header" />

<Autofunction function="AppTest.info" />

<Autofunction function="AppTest.json" />

<Autofunction function="AppTest.latex" />

<Autofunction function="AppTest.main" />

<Autofunction function="AppTest.markdown" />

<Autofunction function="AppTest.metric" />

<Autofunction function="AppTest.multiselect" />

<Autofunction function="AppTest.number_input" />

<Autofunction function="AppTest.radio" />

<Autofunction function="AppTest.select_slider" />

<Autofunction function="AppTest.selectbox" />

<Autofunction function="AppTest.sidebar" />

<Autofunction function="AppTest.slider" />

<Autofunction function="AppTest.subheader" />

<Autofunction function="AppTest.success" />

<Autofunction function="AppTest.status" />

<Autofunction function="AppTest.table" />

<Autofunction function="AppTest.tabs" />

<Autofunction function="AppTest.text" />

<Autofunction function="AppTest.text_area" />

<Autofunction function="AppTest.text_input" />

<Autofunction function="AppTest.time_input" />

<Autofunction function="AppTest.title" />

<Autofunction function="AppTest.toast" />

<Autofunction function="AppTest.toggle" />

<Autofunction function="AppTest.warning" />
