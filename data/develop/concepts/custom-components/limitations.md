---
title: Limitations of custom components
slug: /develop/concepts/custom-components/limitations
---

# Limitations of custom components

## How do Streamlit Components differ from functionality provided in the base Streamlit package?

- Streamlit Components are wrapped up in an iframe, which gives you the ability to do whatever you want (within the iframe) using any web technology you like.

## What types of things aren't possible with Streamlit Components?

Because each Streamlit Component gets mounted into its own sandboxed iframe, this implies a few limitations on what is possible with Components:

- **Can't communicate with other Components**: Components can’t contain (or otherwise communicate with) other components, so Components cannot be used to build something like a grid layout.
- **Can't modify CSS**: A Component can’t modify the CSS that the rest of the Streamlit app uses, so you can't create something to put the app in dark mode, for example.
- **Can't add/remove elements**: A Component can’t add or remove other elements of a Streamlit app, so you couldn't make something to remove the app menu, for example.

## My Component seems to be blinking/stuttering...how do I fix that?

Currently, no automatic debouncing of Component updates is performed within Streamlit. The Component creator themselves can decide to rate-limit the updates they send back to Streamlit.
