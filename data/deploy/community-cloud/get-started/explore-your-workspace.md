---
title: Explore your workspace
slug: /deploy/streamlit-community-cloud/get-started/explore-your-workspace
---

# Explore your workspace

If you just [created your account](/deploy/streamlit-community-cloud/get-started/create-your-account), congrats! You are now logged in and ready to go. If you are joining someone else's workspace you may already see apps populated in your workspace. If not, then you need to deploy an app! Check out our next section on how to [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app). If you need an app to deploy, check out our <a href="https://streamlit.io/gallery" target="_blank">App gallery</a> which includes apps for machine learning, data science, and business use cases.

![Your Streamlit Community Cloud workspace](/images/streamlit-community-cloud/workspace-empty.png)

## Switching workspaces

You may also find that you already have access to multiple Streamlit Community Cloud workspaces. Streamlit Community Cloud automatically groups your apps according to the corresponding GitHub repository's owner or organzation. In the upper-right corner you can see the workspaces you have access to. If apps have already been deployed from any of your repositories, then you will see those apps when you select the associated workspace in the upper-right corner. Learn more about how to [Manage your app from your workspace](/deploy/streamlit-community-cloud/manage-your-app#manage-your-app-from-your-workspace).

![Switch between your Streamlit Community Cloud workspaces](/images/streamlit-community-cloud/workspace-empty-switch.png)

## New app button

Your workspace is your base of operations to deploy apps and manage them. You can click on "**New app**" to [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app) from a repository where you have administrative privileges. If you want additional options, click the down arrow (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>expand_more</i>) to begin with a template.

- "**Use existing repo**" is the default to [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app) from a repository where you have administrative privileges.
- "**Create from sample app template**" will fork and deploy a <a href="https://github.com/streamlit/streamlit-example" target="_blank">simple, one-page Streamlit app</a>.
- "**Create new app with GitHub Codespaces**" will fork and deploy our multipage <a href="https://github.com/streamlit/streamlit-hello" target="_blank">Streamlit Hello</a> app and create a codespace. To jump quickly into GitHub Codespaces for any of your deployed apps, see [Edit your app with GitHub Codespaces](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app#edit-your-app-with-github-codespaces) instead.

![Options to deploy a new app from your workspace in Streamlit Community Cloud](/images/streamlit-community-cloud/deploy-menu.png)

## Invite other developers to your workspace

Inviting other developers is simple, just invite them to your GitHub repository so that you can code on apps together, and then have them log in to <a href="https://share.streamlit.io/signup" target="_blank">share.streamlit.io/signup</a>. Read more about connecting to a GitHub organization in [Organization access](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

Streamlit Community Cloud inherits developer permissions from GitHub so when others sign in, they will automatically see the workspaces they share with you. From there you can all deploy, manage, and share apps together.

<Note>

Once a user is added to a repository on GitHub, it will take at most 15 minutes before they can deploy the app on Cloud. If a user is removed from a repository on GitHub, it will take at most 15 minutes before their permissions to manage the app from that repository are revoked.

</Note>

And remember, whenever anyone on the team updates the code on GitHub, the app will also automatically update for you!
