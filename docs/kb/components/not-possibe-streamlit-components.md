---
title: What types of things aren't possible with Streamlit Components?
slug: /knowledge-base/components/not-possibe-streamlit-components
---

# What types of things aren't possible with Streamlit Components?

Because each Streamlit Component gets mounted into its own sandboxed iframe, this implies a few limitations on what is possible with Components:

- **Can't communicate with other Components**: Components can’t contain (or otherwise communicate with) other components, so Components cannot be used to build something like `grid_layout`
- **Can't modify CSS**: A Component can’t modify the CSS that the rest of the Streamlit app uses, so you can't create something like `dark_mode`
- **Can't add/remove elements**: A Component can’t add or remove other elements of a Streamlit app, so you couldn't make something like `remove_streamlit_app_menu`
