---
title: secrets.toml
slug: /develop/api-reference/connections/secrets.toml
---

## secrets.toml

`secrets.toml` is an optional file you can define for your working directory or global development environment. When `secrets.toml` is defined both globally and in your working directory, Streamlit combines the secrets and gives precendence to the working-directory secrets. For more information, see [Secrets management](/develop/concepts/connections/secrets-management).

### File location

To define your secrets locally or per-project, add `.streamlit/secrets.toml` to your working directory. Your working directory is wherever you call `streamlit run`. If you haven't previously created the `.streamlit` directory, you will need to add it.

To define your configuration globally, you must first locate your global `.streamlit` directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linx, this will be `~/.streamlit/secrets.toml`. For Windows, this will be `%userprofile%/.streamlit/secrets.toml`.

### File format

`secrets.toml` is a [TOML](https://toml.io/en/) file.

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
