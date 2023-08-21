---
title: Embed your app
slug: /streamlit-community-cloud/share-your-app/embed-your-app
---

# Embed your app

Embedding Streamlit Community Cloud apps enriches your content by integrating interactive, data-driven applications directly within your pages. Whether you're writing a blog post, a technical document, or sharing resources on platforms like Medium, Notion, or even StackOverflow, embedding Streamlit apps adds a dynamic component to your content. This allows your audience to interact with your ideas, rather than merely reading about them or looking at screenshots.

Streamlit Community Cloud supports both [iframe](#embedding-with-iframes) and [oEmbed](#embedding-with-oembed) methods for embedding **public** apps. This flexibility enables you to share your apps across a wide array of platforms, broadening your app's visibility and impact. In this guide, we'll cover how to use both methods effectively to share your Streamlit apps with the world.

## Embedding with iframes

Streamlit Community Cloud supports embedding **public** apps using the subdomain scheme. To embed a public app, add the query parameter `/?embed=true` to the end of the `*.streamlit.app` URL.

For example, say you want to embed the <a href="https://30days.streamlit.app/" target="_blank">30DaysOfStreamlit app</a>. The URL to include in your iframe is: `https://30days.streamlit.app/?embed=true`:

```javascript
<iframe
  src="https://30days.streamlit.app/?embed=true"
  height="450"
  style="width:100%;border:none;"
></iframe>
```

<Cloud src="https://30days.streamlit.app/?embed=true" />

<Important>

There will be no official support for embedding private apps.

</Important>

In addition to allowing you to embed apps via iframes, the `?embed=true` query parameter also does the following:

- Removes the toolbar with the app menu icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>).
- Removes the padding at the top and bottom of the app.
- Removes the footer.
- Removes the colored line from the top of the app.

For granular control over the embedding behavior, Streamlit allows you to specify one or more instances of the `?embed_options` query parameter (e.g. to show the toolbar, open the app in dark theme, etc). [Click here for a full list of Embed options.](#embed-options)

## Embedding with oEmbed

Streamlit's oEmbed support allows for a simpler embedding experience. You can directly drop a Streamlit app's URL into a Medium, Ghost, or Notion page (or any of more than 700 content providers that supports oEmbed or <a href="https://embed.ly/" target="_blank">embed.ly</a>). The embedded app will automatically appear! This helps Streamlit Community Cloud apps seamlessly integrate into these platforms, improving the visibility and accessibility of your apps.

### Example

When creating content in a Notion page, Medium article, or Ghost blog, you only need to paste the app's URL and hit "**Enter**". The app will then render automatically at that spot in your content. You can use your undecorated app URL without the `?embed=true` query parameter.

```
https://30days.streamlit.app/
```

Here's an example of <a href="https://github.com/chrieke" target="_blank">@chrieke</a>'s <a href="https://chrieke-prettymapp-streamlit-prettymappapp-1k0qxh.streamlit.app/" target="_blank">Prettymapp app</a> embedded in a Medium article:

<Image src="/images/streamlit-community-cloud/oembed.gif" alt="Example: Embed an app in a Medium article with oEmbed" clean />

<Tip>

Ensure the platform hosting the embedded Streamlit app supports oEmbed or <a href="https://embed.ly/" target="_blank">embed.ly</a>.

</Tip>

### Key Sites for oEmbed

oEmbed should work out of the box for several platforms including but not limited to:

- <a target="_blank" href="https://medium.com/">Medium</a>
- <a target="_blank" href="https://notion.so/">Notion</a>
- <a target="_blank" href="https://www.looker.com/">Looker</a>
- <a target="_blank" href="https://www.tableau.com/">Tableau</a>
- <a target="_blank" href="https://ghost.org/">Ghost</a>
- <a target="_blank" href="https://www.discourse.org/">Discourse</a>
- <a target="_blank" href="https://stackoverflow.com/">StackOverflow</a>
- <a target="_blank" href="https://www.w3schools.com/">W3</a>
- <a target="_blank" href="https://www.reddit.com/">Reddit</a>

Please check the specific platform's documentation to verify support for oEmbed.

### iframe versus oEmbed

The only noteworthy differences between the methods is that iframing allows you to customize the app's embedding behavior (e.g. showing the toolbar, opening the app in dark theme, etc) using the various `?embed_options` described in the next section.

## Embed options

When [Embedding with iframes](#embedding-with-iframes), Streamlit allows you to specify one or more instances of the `?embed_options` query parameter for granular control over the embedding behavior. 

Both `?embed` and `?embed_options` are invisible to [`st.experimental_get_query_params`](/library/api-reference/utilities/st.experimental_get_query_params) and [`st.experimental_set_query_params`](/library/api-reference/utilities/st.experimental_set_query_params). The former ignores the embed query parameters and does not return them, while the latter disallows setting embed query parameters.

The supported values for `?embed_options` are listed below:

1. Show the toolbar at the top right of the app which includes the app menu (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>), running man, and link to GitHub.

   ```javascript
   /?embed=true&embed_options=show_toolbar
   ```

2. Show padding at the top and bottom of the app.

   ```javascript
   /?embed=true&embed_options=show_padding
   ```

3. Show the footer reading "Made with Streamlit."

   ```javascript
   /?embed=true&embed_options=show_footer
   ```

4. Show the colored line at the top of the app.

   ```javascript
   /?embed=true&embed_options=show_colored_line
   ```

5. Disable scrolling for the main body of the app. (The sidebar will still be scrollable.)

   ```javascript
   /?embed=true&embed_options=disable_scrolling
   ```

6. Open the app with light theme.

   ```javascript
   /?embed=true&embed_options=light_theme
   ```

7. Open the app with dark theme.

   ```javascript
   /?embed=true&embed_options=dark_theme
   ```

You can also combine the params:

```javascript
/?embed=true&embed_options=show_toolbar&embed_options=show_padding&embed_options=show_footer&embed_options=show_colored_line&embed_options=disable_scrolling
```

### Build an embed link

You can conveniently build an embed link for your app &mdash; right from your app!

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.
2. Click "**Embed**" to access a list of selectable embed options.

   ![Access embed options from the share button](/images/streamlit-community-cloud/share-menu-embed.png)

3. Select your embed options and click "**Get embed link**" to copy the embed link to your clipboard.

   ![Build a customized embed link for your app from the share button](/images/streamlit-community-cloud/share-menu-embed-url.png)
