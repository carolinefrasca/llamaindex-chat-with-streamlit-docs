---
title: How do Streamlit Components differ from functionality provided in the base Streamlit package?
slug: /knowledge-base/components/how-streamlit-components-differ-base-package
---

# How do Streamlit Components differ from functionality provided in the base Streamlit package?

- Streamlit Components are wrapped up in an iframe, which gives you the ability to do whatever you want (within the iframe) using any web technology you like.

- There is a strict message protocol between Components and Streamlit, which makes possible for Components to act as widgets. As Streamlit Components are wrapped in iframe, they cannot modify their parent’s DOM (a.k.a the Streamlit report), which ensures that Streamlit is always secure even with user-written components.
