---
title: Share previews
slug: /streamlit-community-cloud/share-your-app/share-previews
---

# Share previews

Social media sites generate a card with a title, preview image, and description when you share a link. This feature is called a "share preview." In the same way, when you share a link to a public Streamlit app on social media, a share preview is also generated. Here's an example of a share preview for a public Streamlit app posted on Twitter:

<div style={{ marginLeft: '3em' }}>
    <Flex>
    <Image caption="Share preview for a public Streamlit app" src="/images/streamlit-community-cloud/share-preview-twitter-annotated.png" />
    </Flex>
</div>

<Note>

Share previews are generated only for public apps deployed on Streamlit Community Cloud.

</Note>

## Titles

The title is the text that appears at the top of the share preview. The text also appears in the browser tab when you visit the app. You should set the title to something that will make sense to your app's audience and describe what the app does. It is best practice to keep the title concise, ideally under 60 characters.

There are two ways to set the title of a share preview:

1. Set the `page_title` parameter in [`st.set_page_config()`](/library/api-reference/utilities/st.set_page_config) to your desired title. E.g.:

   ```python
   import streamlit as st

   st.set_page_config(page_title="My App")

   # ... rest of your app
   ```

2. If you don't set the `page_title` parameter, the title of the share preview will be the name of your app's GitHub repository. For example, the default title for an app hosted on GitHub at <a href="https://github.com/jrieke/traingenerator" target="_blank">github.com/jrieke/traingenerator</a> will be "traingenerator".

## Descriptions

The description is the text that appears below the title in the share preview. The description should summarize what the app does and ideally should be under 100 characters.

Streamlit pulls the description from the README in the app's GitHub repository. If there is no README, the description will default to:

_This app was built in Streamlit! Check it out and visit https://streamlit.io for more awesome community apps. 🎈_

<div style={{ marginLeft: '6em' }}>
    <Flex>
    <Image caption="Default share preview when a description is missing" src="/images/streamlit-community-cloud/share-preview-private-app.png" />
    </Flex>
</div>

<!-- ![Default share preview when a description is missing](/images/streamlit-community-cloud/share-preview-private-app.png) -->

If you want your share previews to look great and want users to share your app and click on your links, you should write a good description in the README of your app’s GitHub repository.

## Preview images

Streamlit Community Cloud takes a screenshot of your app once a day and uses it as the preview image, unlike titles and descriptions which are pulled directly from your app's code or GitHub repository. This screenshot may take up to 24 hours to update.

### Switching your app from public to private

If you initially made your app public and later decided to make it private, we will stop generating share previews for the app. However, it may take up to 24 hours for the share previews to stop appearing.
