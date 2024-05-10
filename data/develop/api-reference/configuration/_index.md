---
title: Configuration
slug: /develop/api-reference/configuration
---

# Configuration

<TileContainer>
<RefCard href="/develop/api-reference/configuration/config.toml">

<h4>Configuration file</h4>

Configures the default settings for your app.

```
your-project/
├── .streamlit/
│   └── config.toml
└── your_app.py
```

</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_page_config">

<h4>Set page title, favicon, and more</h4>

Configures the default settings of the page.

```python
st.set_page_config(
  page_title="My app",
  page_icon=":shark:",
)
```

</RefCard>
</TileContainer>
