---
title: App testing cheat sheet
slug: /develop/concepts/app-testing/cheat-sheet
---

# App testing cheat sheet

## Text elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# Headers
assert "My app" in at.title[0].value
assert "New topic" in at.header[0].value
assert "Interesting sub-topic" in at.subheader[0].value
assert len(at.divider) == 2

# Body / code
assert "Hello, world!" in at.markdown[0].value
assert "import streamlit as st" in at.code[0].value
assert "A cool diagram" in at.caption[0].value
assert "Hello again, world!" in at.text[0].value
assert "\int a x^2 \,dx" in at.latex[0].value
```

## Input widgets

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# button
assert at.button[0].value == False
at.button[0].click().run()
assert at.button[0].value == True

# checkbox
assert at.checkbox[0].value == False
at.checkbox[0].check().run() # uncheck() is also supported
assert at.checkbox[0].value == True

# color_picker
assert at.color_picker[0].value == "#FFFFFF"
at.color_picker[0].pick("#000000").run()

# date_input
assert at.date_input[0].value == datetime.date(2019, 7, 6)
at.date_input[0].set_value(datetime.date(2022, 12, 21)).run()

# form_submit_button - shows up just like a button
assert at.button[0].value == False
at.button[0].click().run()
assert at.button[0].value == True

# multiselect
assert at.multiselect[0].value == ["foo", "bar"]
at.multiselect[0].select("baz").unselect("foo").run()

# number_input
assert at.number_input[0].value == 5
at.number_input[0].increment().run()

# radio
assert at.radio[0].value == "Bar"
assert at.radio[0].index == 3
at.radio[0].set_value("Foo").run()

# selectbox
assert at.selectbox[0].value == "Bar"
assert at.selectbox[0].index == 3
at.selectbox[0].set_value("Foo").run()

# select_slider
assert at.select_slider[0].value == "Feb"
at.select_slider[0].set_value("Mar").run()
at.select_slider[0].set_range("Apr", "Jun").run()

# slider
assert at.slider[0].value == 2
at.slider[0].set_value(3).run()
at.slider[0].set_range(4, 6).run()

# text_area
assert at.text_area[0].value == "Hello, world!"
at.text_area[0].set_value("Hello, yourself!").run()

# text_input
assert at.text_input[0].value == "Hello, world!")
at.text_input[0].set_value("Hello, yourself!").run()

# time_input
assert at.time_input[0].value == datetime.time(8, 45)
at.time_input[0].set_value(datetime.time(12, 30))

# toggle
assert at.toggle[0].value == False
assert at.toggle[0].label == "Debug mode"
at.toggle[0].set_value(True).run()
assert at.toggle[0].value == True
```

## Data elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# dataframe
expected_df = pd.DataFrame([1, 2, 3])
assert at.dataframe[0].value.equals(expected_df)

# metric
assert at.metric[0].value == "9500"
assert at.metric[0].delta == "1000"

# json
assert at.json[0].value == '["hi", {"foo": "bar"}]'

# table
table_df = pd.DataFrame([1, 2, 3])
assert at.table[0].value.equals(table_df)
```

## Layouts and containers

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# sidebar
at.sidebar.text_input[0].set_value("Jane Doe")

# columns
at.columns[1].markdown[0].value == "Hello, world!"

# tabs
at.tabs[2].markdown[0].value == "Hello, yourself!"
```

## Chat elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# chat_input
at.chat_input[0].set_value("Do you know any jokes?").run()
# Note: chat_input value clears after every re-run (like in a real app)

# chat_message
assert at.chat_message[0].markdown[0].value == "Do you know any jokes?"
assert at.chat_message[0].avatar == "user"
```

## Status elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# exception
assert len(at.exception) == 1
assert "TypeError" in at.exception[0].value

# Other in-line alerts: success, info, warning, error
assert at.success[0].value == "Great job!"
assert at.info[0].value == "Please enter an API key to continue"
assert at.warning[0].value == "Sorry, the passwords didn't match"
assert at.error[0].value == "Something went wrong :("

# toast
assert at.toast[0].value == "That was lit!" and at.toast[0].icon == "🔥"
```

## Limitations

As of Streamlit 1.28, the following Streamlit features are not natively supported by `AppTest`. However, workarounds are possible for many of them by inspecting the underlying proto directly using `AppTest.get()`. We plan to regularly add support for missing elements until all features are supported.

- Chart elements (`st.bar_chart`, `st.line_chart`, etc)
- Media elements (`st.image`, `st.video`, `st.audio`)
- `st.file_uploader`
- `st.data_editor`
- `st.expander`
- `st.status`
- `st.camera_input`
- `st.download_button`
- `st.link_button`
