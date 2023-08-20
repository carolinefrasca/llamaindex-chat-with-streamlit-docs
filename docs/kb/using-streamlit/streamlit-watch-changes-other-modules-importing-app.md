---
title: How can I make Streamlit watch for changes in other modules I'm importing in my app?
slug: /knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app
---

# How can I make Streamlit watch for changes in other modules I'm importing in my app?

By default, Streamlit only watches modules contained in the current directory of the main app module. You can track other modules by adding the parent directory of each module to the `PYTHONPATH`.

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/module
streamlit run your_script.py
```
