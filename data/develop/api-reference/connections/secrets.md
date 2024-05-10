---
title: st.secrets
slug: /develop/api-reference/connections/st.secrets
---

## st.secrets

`st.secrets` provides a dictionary-like interface to access secrets stored in a `secrets.toml` file. It behaves similarly to `st.session_state`. `st.secrets` can be used with both key and attribute notation. For example, `st.secrets.your_key` and `st.secrets["your_key"]` refer to the same value. For more information about using `st.secrets`, see [Secrets management](/develop/concepts/connections/secrets-management).

### secrets.toml

Secrets can be saved globally or per-project. When both types of secrets are saved, Streamlit will combine the saved values but give precedence to per-project secrets if there are duplicate keys. For information on how to format and locate your `secrets.toml` file for your development environment, see [`secrets.toml`](/develop/api-reference/connections/secrets.toml).

#### Example

```toml
OpenAI_key = "your OpenAI key"
whitelist = ["sally", "bob", "joe"]

[database]
user = "your username"
password = "your password"
```

In your Streamlit app, the following values would be true:

```python
st.secrets["OpenAI_key"] == "your OpenAI key"
"sally" in st.secrets.whitelist
st.secrets["database"]["user"] == "your username"
st.secrets.database.password == "your password"
```
