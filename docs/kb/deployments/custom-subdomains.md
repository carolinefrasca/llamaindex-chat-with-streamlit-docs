---
title: Custom subdomains
slug: /knowledge-base/deploy/custom-subdomains
---

# Custom subdomains

Once you've [deployed your app](/streamlit-community-cloud/deploy-your-app) on Community Cloud, it's given an automatically generated subdomain that follows a structure based on your GitHub repo. This subdomain is unique to your app and can be used to share your app with others. However, the default subdomain is not always the most memorable or easy to share. E.g. the following is a bit of a mouthful!

`https://streamlit-demo-self-driving-streamlit-app-8jya0g.streamlit.app`

You can instead set up a custom subdomain to make your app easier to share. You can customize your subdomain to reflect your app content, personal branding, or whatever you’d like. The URL will appear as:

```
<your-custom-subdomain>.streamlit.app
```

To customize your app subdomain from your [workspace](/streamlit-community-cloud/manage-your-app#manage-your-app-from-your-workspace):

1. Click the "︙" overflow menu to the app's right and select "**Settings**".

   ![App settings](/images/streamlit-community-cloud/workspace-app-settings.png)

2. View the "**General**" tab in the App settings modal. Your app's unique subdomain will appear here.
   ![General app settings](/images/streamlit-community-cloud/workspace-app-settings-general.png)

3. Pick a custom subdomain between 6 and 63 characters in length for your app's URL and hit "**Save**".
   ![New custom subdomain](/images/streamlit-community-cloud/workspace-app-settings-general-valid-domain.png)

It's that simple! You can then access your app by visiting your custom subdomain URL 🎉.

If a custom subdomain is not available (e.g. because it's already taken), you'll see an error message like this:

![Invalid custom subdomain](/images/streamlit-community-cloud/workspace-app-settings-general-invalid-domain.png)
