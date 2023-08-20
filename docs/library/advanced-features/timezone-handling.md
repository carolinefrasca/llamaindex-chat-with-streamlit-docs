---
title: Working with timezones
slug: /library/advanced-features/timezone-handling
---

# Working with timezones

In general, working with timezones can be tricky. Your Streamlit app users are not necessarily in the same timezone as the server running your app. It is especially true of public apps, where anyone in the world (in any timezone) can access your app. As such, it is crucial to understand how Streamlit handles timezones, so you can avoid unexpected behavior when displaying `datetime` information.

## How Streamlit handles timezones

Streamlit always shows `datetime` information on the frontend with the same information as its corresponding `datetime` instance in the backend. I.e., date or time information does not automatically adjust to the users' timezone. We distinguish between the following two cases:

### **`datetime` instance without a timezone (naive)**

When you provide a `datetime` instance _without specifying a timezone_, the frontend shows the `datetime` instance without timezone information. For example (this also applies to other widgets like [`st.dataframe`](/library/api-reference/data/st.dataframe)):

```python
import streamlit as st
from datetime import datetime

st.write(datetime(2020, 1, 10, 10, 30))
# Outputs: 2020-01-10 10:30:00
```

Users of the above app always see the output as `2020-01-10 10:30:00`.

### **`datetime` instance with a timezone**

When you provide a `datetime` instance _and specify a timezone_, the frontend shows the `datetime` instance in that same timezone. For example (this also applies to other widgets like [`st.dataframe`](/library/api-reference/data/st.dataframe)):

```python
import streamlit as st
from datetime import datetime
import pytz

st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
# Outputs: 2020-01-10 10:30:00-05:00
```

Users of the above app always see the output as `2020-01-10 10:30:00-05:00`.

In both cases, neither the date nor time information automatically adjusts to the users' timezone on the frontend. What users see is identical to the corresponding `datetime` instance in the backend. It is currently not possible to automatically adjust the date or time information to the timezone of the users viewing the app.

<Note>

The legacy version of the `st.dataframe` has issues with timezones. We do not plan to roll out additional fixes or enhancements for the legacy dataframe. If you need stable timezone support, please consider switching to the arrow serialization by changing the [config setting](/library/advanced-features/configuration#set-configuration-options), _config.dataFrameSerialization = "arrow"_.

</Note>
