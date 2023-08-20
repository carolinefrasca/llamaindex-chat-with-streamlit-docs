---
title: Static file serving
slug: /library/advanced-features/static-file-serving
---

# Static file serving

Streamlit apps can host and serve small, static media files to support media embedding use cases that
won't work with the normal [media elements](https://docs.streamlit.io/library/api-reference/media).

To enable this feature, set `enableStaticServing = true` under `[server]` in your config file,
or environment variable `STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true`.

Media stored in the folder `./static/` relative to the running app file is served at path
`app/static/[filename]`, such as `http://localhost:8501/app/static/cat.png`.

## Details on usage

- Files with the following extensions will be served normally: `".jpg", ".jpeg", ".png", ".gif"`. Any other
  file will be sent with header `Content-Type:text/plain` which will cause browsers to render in plain text.
  This is included for security - other file types that need to render should be hosted outside the app.
- Streamlit also sets `X-Content-Type-Options:nosniff` for all files rendered from the static directory.
- For apps running on Streamlit Community Cloud:
  - Files available in the Github repo will always be served. Any files generated while the app is running,
    such as based on user interaction (file upload, etc), are not guaranteed to persist across user sessions.
  - Apps which store and serve many files, or large files, may run into resource limits and be shut down.

## Example usage

- Put an image `cat.png` in the folder `./static/`
- Add `enableStaticServing = true` under `[server]` in your `.streamlit/config.toml`
- Any media in the `./static/` folder is served at the relative URL like `app/static/cat.png`

```toml
# .streamlit/config.toml

[server]
enableStaticServing = true
```

```python
# app.py
import streamlit as st

with st.echo():
    st.title("CAT")

    st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")

```

Additional resources:

- <https://docs.streamlit.io/library/advanced-features/configuration>
- <https://static-file-serving.streamlit.app/>

<Cloud src="https://static-file-serving.streamlit.app/?embedded=true" height="1000" />
