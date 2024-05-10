---
title: st.write_stream
slug: /develop/api-reference/write-magic/st.write_stream
description: st.write_stream writes arguments to the app using a typewriter effect.
---

<Autofunction function="streamlit.write_stream" />

<Tip>

If your stream object is not compatible with `st.write_stream`, define a wrapper around your stream object to create a compatible generator function.

```python
for chunk in unsupported_stream:
    yield preprocess(chunk)
```

For an example, see how we use [Replicate](https://replicate.com/docs/get-started/python) with [Snowflake Arctic](https://www.snowflake.com/en/data-cloud/arctic/) in [this code](https://github.com/streamlit/snowflake-arctic-st-demo/blob/0f0d8b49f328f72ae58ced2e9000790fb5e56e6f/simple_app.py#L58).

</Tip>
