---
title: Argh. This app has gone over its resource limits
slug: /knowledge-base/deploy/resource-limits
---

# Argh. This app has gone over its resource limits

Sorry! It means you've hit the [resource limits](/streamlit-community-cloud/manage-your-app#app-resources-and-limits) of your [Streamlit Community Cloud](https://streamlit.io/cloud) account.

<!-- One way to avoid this is to [upgrade your plan](https://streamlit.io/cloud) to one with higher resource limits.  -->

There are a few things you can change in your app to make it less resource-hungry:

- Reboot your app (temporary fix)
- Use `st.cache_data` or `st.cache_resource` to load models or data only once
- Restrict the cache size with `ttl` or `max_entries`
- Move big datasets to a database
- Profile your app's memory usage

Check out our [blog post](https://blog.streamlit.io/common-app-problems-resource-limits/) on [“Common app problems: Resource limits"](https://blog.streamlit.io/common-app-problems-resource-limits/) for more in-depth tips prevent your app from hitting the [resource limits](/streamlit-community-cloud/manage-your-app#app-resources-and-limits) of the Streamlit Community Cloud.

Related forum posts:

- <https://discuss.streamlit.io/t/common-app-problems-resource-limits/16969>
- <https://blog.streamlit.io/common-app-problems-resource-limits/>

We offer free resource increases only to support nonprofits or educational organizations on a case-by-case basis. If you are a nonprofit or educational organization, please complete [this form](https://docs.google.com/forms/d/e/1FAIpQLSfzPNqrvH0HeaJnl0dtBgVV-ILqavzSmAEk84vDnMFIbvkGVA/viewform) and we will review your submission as soon as possible.

Once the increase is completed, you will receive an email from the Streamlit marketing team with a confirmation that the increase has been applied.
