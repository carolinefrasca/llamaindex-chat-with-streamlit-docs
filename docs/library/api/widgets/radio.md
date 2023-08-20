---
title: st.radio
slug: /library/api-reference/widgets/st.radio
description: st.radio displays a radio button widget.
---

<Autofunction function="streamlit.radio" />

<br />

Widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Radio buttons can also be disabled with the `disabled` parameter, and oriented horizontally with the `horizontal` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
```

<Cloud src="https://doc-radio1.streamlit.app/?embed=true" height="300" />

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the radio button! 🔘

<YouTube videoId="CVHIMGVAzwA" />

In the video below, we'll take it a step further and learn how to combine a [button](/library/api-reference/widgets/st.button), [checkbox](/library/api-reference/widgets/st.checkbox) and radio button!

<YouTube videoId="EnXJBsCIl_A" />
