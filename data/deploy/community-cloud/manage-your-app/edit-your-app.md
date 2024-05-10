---
title: Edit your app
slug: /deploy/streamlit-community-cloud/manage-your-app/edit-your-app
---

# Edit your app

You can edit your app from any development environment of your choice. Community Cloud will monitor your repository and automatically copy any file changes you commit. You will immediately see commits reflected in your deployed app for most changes (such as edits to your app's Python files).

Community Cloud also makes it easy to skip the work of setting up a development environment. With a few simple clicks, you can configure a development environment using GitHub Codespaces.

## Edit your app with GitHub Codespaces

Spin up a cloud-based development environment for your deployed app in minutes. You can run your app within your codespace to enjoy experimenting in a safe, sandboxed environment. When you are done editing your code, you can commit your changes to your repo or just leave them in your codespace to return to later.

### Create a codespace for your deployed app

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) next to your app. Click "**Edit**."

   ![Edit your app with GitHub Codespaces](/images/streamlit-community-cloud/workspace-app-edit.png)

2. A `.devcontainer/devcontainer.json` file will be added to your repository. If you already have a file of the same name in your repository, it will not be changed. You may delete or rename your existing devcontainer configuration if you would like your repository to receive the instance created by Streamlit Community Cloud.

   ![Adding a devcontainer file to your repository](/images/streamlit-community-cloud/workspace-app-edit-preparing.png)

3. Click "**Create codespace**" to confirm the creation of a codespace on your account. Read more about <a href="https://github.com/features/codespaces" target="_blank">GitHub Codespaces</a> to learn about monthly limits for free use and paid plans.

   ![Create your GitHub Codespace](/images/streamlit-community-cloud/deploy-codespaces-2.png)

4. Wait for GitHub to set up your codespace.

   ![GitHub preparing your codespace](/images/streamlit-community-cloud/deploy-codespaces-3.png)

5. GitHub will automatically execute the commands to launch your Streamlit app within your codespace. Your app will be visible in a "Simple Browser" on the right. This may take a minute to complete from when your codespace first appears on screen.

   ![Your new GitHub Codespace](/images/streamlit-community-cloud/deploy-sample-codespace.png)

6. When you make changes to your app, the file is automatically saved within your codespace. Your edits do not affect your repository unless you choose to commit those changes. We will describe committing your changes in a later step.

   In order to see updates automatically reflected on the right, click "**Always rerun**" when prompted after an edit.

   ![Edit the title of your sample Streamlit app](/images/streamlit-community-cloud/deploy-sample-edit-title.png)
   ![Select "Always rerun" to automatically see edits in your running app](/images/streamlit-community-cloud/deploy-sample-edit-rerun.png)

7. See your edits appear within the "Simple Browser" tab and keep going with more!

   ![See the results of your edit to your Streamlit app](/images/streamlit-community-cloud/deploy-sample-edit-result.png)

### Commit your changes to your repository (optional)

After making edits to your app, you can choose to commit your edits to your repository to update your deployed app instantly. If you just want to keep your edits in your codespace to return to later, skip to [Stop or delete your codespace](#stop-or-delete-your-codespace).

8. In the left navigation bar, click the source control icon.

   ![Click on the source control icon](/images/streamlit-community-cloud/deploy-sample-edit-commit-1.png)

9. Fill out your desired commit message and click "**Commit**."

   ![Commit your changes](/images/streamlit-community-cloud/deploy-sample-edit-commit-2.png)

10. Click "**Yes**" to stage and commit all your changes. To learn more about source control in GitHub Codespaces, check out <a href="https://docs.github.com/en/codespaces/developing-in-codespaces/using-source-control-in-your-codespace" target="_blank">Source control</a> in GitHub Docs.

<div style={{ maxWidth: '70%', margin: 'auto' }}>
<Image alt="Confirm to stage all changes and commit" src="/images/streamlit-community-cloud/deploy-sample-edit-commit-3.png" />
</div>

### Stop or delete your codespace

When you are done, remember to stop your codespace on GitHub to avoid any undesired use of your capacity.

11. Go to <a href="https://github.com/codespaces" target="_blank">github.com/codespaces</a>. At the bottom of the page, all your codespaces are listed. Click the overflow menu icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_horiz</i>) for your codespace.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Stop or delete your GitHub Codespace" src="/images/streamlit-community-cloud/deploy-sample-codespace-manage.png" />
</div>

12. Click "**Stop codespace**" if you'd like to return to your work later. Otherwise, click "**Delete**."

    <Flex>
    <div style={{ maxWidth: '40%', margin: 'auto' }}>
    <Image alt="Stop your GitHub codespace" src="/images/streamlit-community-cloud/codespace-menu-stop.png" />
    </div>
    <div style={{ maxWidth: '40%', margin: 'auto' }}>
    <Image alt="Delete your GitHub codespace" src="/images/streamlit-community-cloud/codespace-menu-delete.png" />
    </div>
    </Flex>
