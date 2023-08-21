---
title: Manage your app
slug: /streamlit-community-cloud/manage-your-app
---

# Manage your app

You can manage your deployed app from your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> or directly from `<your-custom-subdomain>.streamlit.app`. You can view, deploy, delete, reboot, or favorite an app.

## Manage your app from your workspace

Streamlit Community Cloud is organized into workspaces, which automatically group your apps according to the corresponding GitHub repository's owner. Your workspace is indicated in the upper-right corner. You will have one workspace that matches your GitHub username and additional workspaces for any GitHub organization or user who has granted you access.

Additionally, if you have view-only access to an app, you will be able to see that app's workspace. When you do not have developer access to an app, your management options for that app will be restricted as shown in the following sections.

To deploy or manage any app, always switch to the workspace matching the repository's owner first.

![Switching between app workspaces in Streamlit Community Cloud](/images/streamlit-community-cloud/workspace-switch.png)

At the top of your workspace, "**Analytics**" is a shortcut to [App analytics](/streamlit-community-cloud/manage-your-app/app-analytics) and "**Settings**" links to your [Workspace settings](/streamlit-community-cloud/manage-your-account/workspace-settings) (not to be confused with [App settings](/streamlit-community-cloud/manage-your-app/app-settings) for each of your apps).

### App overflow menus

Each app has a menu accessible from the overflow icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) to the right.

* **Copy URL** &mdash; See [Copy your app's URL](/streamlit-community-cloud/share-your-app#copy-your-apps-url)
* **Favorite** &mdash; See [Favorite your app](/streamlit-community-cloud/manage-your-app/favorite-your-app)
* **Analytics** &mdash; See [App analytics](/streamlit-community-cloud/manage-your-app/app-analytics)
* **Reboot** &mdash; See [Reboot your app](/streamlit-community-cloud/manage-your-app/reboot-your-app)
* **Delete** &mdash; See [Delete your app](/streamlit-community-cloud/manage-your-app/delete-your-app)
* **Settings** &mdash; See [App settings](/streamlit-community-cloud/manage-your-app/app-settings)

![App overflow menu in your workspace](/images/streamlit-community-cloud/workspace-app-overflow.png)

If you have view-only access to an app, options will be restricted in that app's menu.

![View-only app overflow menu in your workspace](/images/streamlit-community-cloud/workspace-view-only.png)

## Manage your app directly from your app

You can manage your deployed app directly from the app itself! Just make sure you are signed in to Streamlit Community Cloud then visit your app.

### Streamlit Community Cloud logs

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Manage app**" in the lower-right corner.

    ![Access Cloud logs from Manage app in the lower-right corner of your app](/images/streamlit-community-cloud/cloud-logs-open.png)

2. Once you've clicked on "**Manage app**", you will be able to view your app's logs. This is your primary place to troubleshoot any issues with your app.

    ![Streamlit Community Cloud logs](/images/streamlit-community-cloud/cloud-logs.png)

3. You can access more developer options by clicking the overflow icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) at the bottom of your Cloud logs. To conveniently download your logs, click "**Download log**".

    ![Download your Streamlit Community Cloud logs](/images/streamlit-community-cloud/cloud-logs-menu-download.png)

<Flex>

<Div>

Other options accessible from Cloud logs are:

* **Analytics** &mdash; See [App analytics](/streamlit-community-cloud/manage-your-app/app-analytics).
* **Reboot app** &mdash; See [Reboot your app](/streamlit-community-cloud/manage-your-app/reboot-your-app).
* **Delete app** &mdash; See [Delete your app](/streamlit-community-cloud/manage-your-app/delete-your-app).
* **Settings** &mdash; See [App settings](/streamlit-community-cloud/manage-your-app/app-settings).
* **Your apps** &mdash; Takes you to your [app workspace](#manage-your-app-from-your-workspace).
* **Documentation** &mdash; Takes you to our documentation.
* **Support** &mdash; Takes you to <a href="https://discuss.streamlit.io/" target="_blank">our forums</a>!

</Div>

<div style={{ maxWidth: '30%', margin: "auto" }}>
    <Image src="/images/streamlit-community-cloud/cloud-logs-menu-XL.png" clean />
</div>

</Flex>

### App menus

From your app at `<your-custom-subdomain>.streamlit.app`, you can always access your [app's menu](/library/advanced-features/app-menu) just like you can when developing locally. The option to deploy your app is removed, but you can still clear your cache from here.

![App menus in Streamlit Community Cloud](/images/streamlit-community-cloud/app-menu.png)

## Manage your app in GitHub

### Update your app

Your GitHub repository is the source for the app, so that means that any time you push an update to your repo you'll see it reflected in the app in almost real time. Try it out!

Streamlit also smartly detects whether you touched your dependencies, in which case it will automatically do a full redeploy for you—which will take a little more time. But since most updates don't involve dependency changes, you should usually see your app update in real time.

### Add or remove dependencies

You can add/remove dependencies at any point by updating `requirements.txt` (Python dependenciess) or `packages.txt` (Linux dependencies) and committing the changes to your repository on GitHub. This will cause Streamlit Community Cloud to detect there was a change in your dependencies and automatically trigger (re)installation.

It is best practice to pin your Streamlit version in `requirements.txt`. Otherwise, the version may be auto-upgraded at any point without your knowledge, which could lead to undesired results (e.g. when we deprecate a feature in Streamlit).

## App resources and limits

### Resource limits

All Streamlit Community Cloud users have access to the same resources and are subject to the same limits (1 GB of RAM).
If your app is running slowly or you're hitting the '😦 Oh no.' page, we first highly recommend going through and implementing the suggestions in the following blog posts to prevent your app from hitting the resource limits and to detect if your Streamlit app leaks memory:

- <a href="https://blog.streamlit.io/common-app-problems-resource-limits/" target="_blank">Common app problems: Resource limits</a>
- <a href="https://blog.streamlit.io/3-steps-to-fix-app-memory-leaks/" target="_blank">3 steps to fix app memory leaks</a>

If your app exceeds its resourse limits, developers and viewers alike will see '😦 Oh no.'

<div style={{ maxWidth: '70%', margin: 'auto' }}>
<Image alt="App state: Oh no. Error running your app." src="/images/streamlit-community-cloud/app-state-oh-no.png" />
</div>

If see '😦 Oh no.' when viewing your app, first check your Cloud logs for any specific errors. If there are no errors in your Cloud logs you are likely dealing with a resource issue.

#### Developer view

If you are logged into a developer account for an app over its limits, you can access "**Manage app**" from the lower-right corner of the app to reboot it and clear its memory. "**Manage app**" will be red and have a warning icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>error</i>).

![Developer view: Oh no. Error running your app.](/images/streamlit-community-cloud/app-state-oh-no-developer.png)

### App hibernation

All apps without traffic for 7 consecutive days will automatically go to sleep. This is done to alleviate resources and allow the best communal use of the platform! If you would like to keep your app awake, simply visit the app to create traffic or commit your app's repository, even if it's an empty commit!

If left alone your app will go to sleep at the 7 day mark. When someone visits the app after this, they will see the sleeping page:
<div style={{ maxWidth: '80%', margin: 'auto' }}>
<Image alt="App state: Zzzz. This app has gone to sleep due to inactivity." src="/images/streamlit-community-cloud/app-state-zzzz.png" />
</div>

To wake the app up, click "**Yes, get this app back up!**" This can be done by *anyone* who has access to view the app, not just the app developer!

You can see which of your apps are asleep from your workspace. Sleeping apps have a moon icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>bedtime</i>) to the right.

![App state: Zzzz. This app has gone to sleep due to inactivity](/images/streamlit-community-cloud/app-state-zzzz-workspace.png)
