---
title: ⋮ App menu
slug: /library/advanced-features/app-menu
---

# ⋮ App menu

Streamlit provides a configurable menu within your app to access convenient tools for developers and viewers. By default, you can access developer options from the app menu when viewing an app locally or on Streamlit Community Cloud while logged into an account with administrative access. While viewing an app, click the icon in the upper-right corner to access the menu.

![App menu](/images/app-menu/app-menu-developer.png)

## Menu options

The menu is split into two sections. The upper section contains options available to all viewers and the lower section contains options for developers. Read more about [customizing this menu](#customize-the-menu) at the end of this page.

### Rerun

You can manually trigger a rerun of your app by clicking "**Rerun**" from the app menu. This rerun will not reset your session. Your widget states and values stored in [`st.session_state`](/library/advanced-features/session-state) will be preserved. As a shortcut, without opening the app menu, you can rerun your app by pressing "**R**" on your keyboard (if you aren't currently focused on an input element).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-rerun-XL.png" alt="Rerun" clean />
</div>

### Settings

With the "**Settings**" option, you can control the appearance of your app while it is running. If viewing the app locally, you can set how your app responds to changes in your source code. See more about development flow in [Main concepts](/library/get-started/main-concepts#development-flow). You can also force your app to appear in wide mode, even if not set within the script using [`st.set_page_config`](/library/api-reference/utilities/st.set_page_config).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-settings-XL.png" alt="Settings" clean />
</div>

#### Theme settings

After clicking "**Settings**" from the app menu, you can choose between "**Light**", "**Dark**", or "**Use system setting**" for the app's base theme. Click on "**Edit active theme**" to modify the theme, color-by-color.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-settings-modal.png" alt="Settings" clean />
</div>

<br />

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-settings-theme.png" alt="Theme" clean />
</div>

### Print

Click "**Print**" to open a print dialog. This option uses your browser's built-in print-to-pdf function.

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-print-XL.png" alt="Print" clean />
</div>

### Record a screencast

You can easily make screen recordings right from your app! Screen recording is supported in the latest versions of Chrome, Edge, and Firefox. Ensure your browser is up-to-date for compatibility. Depending on your current settings, you may need to grant permission to your browser to record your screen or to use your microphone if recording a voiceover.

1. While viewing your app, open the app menu from the upper-right corner.
2. Click "**Record a screencast**."

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-record-XL.png" alt="Record" clean />
</div>

3. If you want to record audio through your microphone, check "**Also record audio**."
4. Click "**Start recording**." (You may be prompted by your OS to permit your browser to record your screen or use your microphone.)

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-2.png" alt="Record" />
</div>

5. Select which tab, window, or monitor you want to record from the listed options. The interface will vary depending on your browser.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-3.png" alt="Record" />
</div>

6. Click "**Share**."

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-4.png" alt="Record" />
</div>

7. While recording, you will see a red circle on your app's tab and on the app menu icon. If you want to cancel the recording, click "**Stop sharing**" at the bottom of your app.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-5.png" alt="Record" />
</div>

8. When you are done recording, press "**Esc**" on your keyboard or click "**Stop recording**" from your app's menu.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-6.png" alt="Record" />
</div>

9. Follow your browser's instructions to save your recording. Your saved recording will be available where your browser saves downloads.

The whole process looks like this:

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record.gif" alt="Record" />
</div>

### About

You can conveniently check what version of Streamlit is running from the "**About**" option. Developers also have the option to customize the message shown here using [`st.set_page_config`](/library/api-reference/utilities/st.set_page_config).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-about-XL.png" alt="Rerun" clean />
</div>

## Developer options

By default, developer options only show when viewing an app locally or when viewing a Community Cloud app while logged in with administrative permission. You can [customize the menu](#customize-the-menu) if you want to make these options available for all users.

### Clear cache

Reset your app's cache by clicking "**Clear cache**" from the app's menu or by pressing "**C**" on your keyboard while not focused on an input element. This will remove all cached entries for [`@st.cache_data`](/library/api-reference/performance/st.cache_data) and [`@st.cache_resource`](/library/api-reference/performance/st.cache_resource).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-clear-XL.png" alt="Rerun" clean />
</div>

### Deploy this app

If you are running an app locally from within a git repo, you can deploy your app to Streamlit Community Cloud in a few easy clicks! Make sure your work has been pushed to your online GitHub repository before beginning. For the greatest convenience, make sure you have already created your [Community Cloud account](/streamlit-community-cloud/get-started/create-your-account) and are signed in. Click "**Deploy this app**" to be taken directly to Community Cloud's "Deploy an app" page. Your app's repository, branch, and file name will be prefilled to match your current app! Learn more about [deploying an app](/streamlit-community-cloud/deploy-your-app) on Streamlit Community Cloud.

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-deploy-XL.png" alt="Rerun" clean />
</div>

## Customize the menu

Using `client.toolbarMode` in your app's [configuration](/library/advanced-features/configuration), you can make the app menu appear in the following ways:

- `"developer"` &mdash; Show the developer options to all viewers.
- `"viewer"` &mdash; Hide the developer options from all viewers.
- `"minimal"` &mdash; Show only those options set externally. These can be options declared through [`st.set_page_config`](/library/api-reference/utilities/st.set_page_config) or options populated through Streamlit Community Cloud.
- `"auto"` &mdash; This is the default and will show the developer options when accessed through localhost or through Streamlit Community Cloud when logged into an administrative account for the app. Otherwise, the developer options will not show.
