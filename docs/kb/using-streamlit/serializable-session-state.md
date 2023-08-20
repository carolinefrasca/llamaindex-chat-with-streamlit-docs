---
title: What is serializable session state?
slug: /knowledge-base/using-streamlit/serializable-session-state
---

# What is serializable session state?

## Serializable Session State

Serialization refers to the process of converting an object or data structure into a format that can be persisted and shared, and allowing you to recover the data’s original structure. Python’s built-in [pickle](https://docs.python.org/3/library/pickle.html) module serializes Python objects to a byte stream ("pickling") and deserializes the stream into an object ("unpickling").

By default, Streamlit’s [Session State](/library/advanced-features/session-state) allows you to persist any Python object for the duration of the session, irrespective of the object’s pickle-serializability. This property lets you store Python primitives such as integers, floating-point numbers, complex numbers and booleans, dataframes, and even [lambdas](https://docs.python.org/3/reference/expressions.html#lambda) returned by functions. However, some execution environments may require serializing all data in Session State, so it may be useful to detect incompatibility during development, or when the execution environment will stop supporting it in the future.

To that end, Streamlit provides a `runner.enforceSerializableSessionState` [configuration option](https://docs.streamlit.io/library/advanced-features/configuration) that, when set to `true`, only allows pickle-serializable objects in Session State. To enable the option, either create a global or project config file with the following or use it as a command-line flag:

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

By "_pickle-serializable_", we mean calling `pickle.dumps(obj)` should not raise a [`PicklingError`](https://docs.python.org/3/library/pickle.html#pickle.PicklingError) exception. When the config option is enabled, adding unserializable data to session state should result in an exception. E.g.,

```python
import streamlit as st

def unserializable_data():
		return lambda x: x

#👇 results in an exception when enforceSerializableSessionState is on
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png" clean />
