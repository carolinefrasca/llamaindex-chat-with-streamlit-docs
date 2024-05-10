---
title: Testing element classes
slug: /develop/api-reference/app-testing/testing-element-classes
---

# Testing element classes

## st.testing.v1.element_tree.Block

The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app. For example, `Block.button` will produce a `WidgetList` of `Button` in the same manner as [`AppTest.button`](/develop/api-reference/testing/st.testing.v1.apptest#apptestbutton).

`ChatMessage`, `Column`, and `Tab` all inherit from `Block`. For all container classes, parameters of the original element can be obtained as properties. For example, `ChatMessage.avatar` and `Tab.label`.

<Autofunction function="streamlit.testing.v1.element_tree.Element" />

<Autofunction function="streamlit.testing.v1.element_tree.Button" />

<Autofunction function="streamlit.testing.v1.element_tree.ChatInput" />

<Autofunction function="streamlit.testing.v1.element_tree.Checkbox" />

<Autofunction function="streamlit.testing.v1.element_tree.ColorPicker" />

<Autofunction function="streamlit.testing.v1.element_tree.DateInput" />

<Autofunction function="streamlit.testing.v1.element_tree.Multiselect" />

<Autofunction function="streamlit.testing.v1.element_tree.NumberInput" />

<Autofunction function="streamlit.testing.v1.element_tree.Radio" />

<Autofunction function="streamlit.testing.v1.element_tree.SelectSlider" />

<Autofunction function="streamlit.testing.v1.element_tree.Selectbox" />

<Autofunction function="streamlit.testing.v1.element_tree.Slider" />

<Autofunction function="streamlit.testing.v1.element_tree.TextArea" />

<Autofunction function="streamlit.testing.v1.element_tree.TextInput" />

<Autofunction function="streamlit.testing.v1.element_tree.TimeInput" />

<Autofunction function="streamlit.testing.v1.element_tree.Toggle" />
