---
title: App testing
slug: /develop/api-reference/app-testing
---

# App testing

Streamlit app testing framework enables developers to build and run headless tests that execute their app code directly, simulate user input, and inspect rendered outputs for correctness.

The provided class, AppTest, simulates a running app and provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. It can be used to write automated tests of an app in various scenarios. These can then be run using a tool like pytest. A typical pattern is to build a suite of tests for an app that ensure consistent functionality as the app evolves, and run the tests locally and/or in a CI environment like Github Actions.

## The AppTest class

<TileContainer>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest" size="full">

<h3>st.testing.v1.AppTest</h3>

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

<RefCard href="">

{/** TODO: Bug fix. The second RefCard does not render. Empty card is a workaround. **/}

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file" size="full">

<h3>AppTest.from_file</h3>

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_string" size="full">

<h3>AppTest.from_string</h3>

`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

```python
from streamlit.testing.v1 import AppTest

app_script = """
import streamlit as st

word_of_the_day = st.text_input("What's the word of the day?", key="word")
if word_of_the_day == st.secrets["WORD"]:
    st.success("That's right!")
elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
    st.warn("Try again.")
"""

at = AppTest.from_string(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_function" size="full">

<h3>AppTest.from_function</h3>

`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

```python
from streamlit.testing.v1 import AppTest

def app_script ():
    import streamlit as st

    word_of_the_day = st.text_input("What's the word of the day?", key="word")
    if word_of_the_day == st.secrets["WORD"]:
        st.success("That's right!")
    elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
        st.warn("Try again.")

at = AppTest.from_function(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

</RefCard>

</TileContainer>

## Testing-element classes

<TileContainer>

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
