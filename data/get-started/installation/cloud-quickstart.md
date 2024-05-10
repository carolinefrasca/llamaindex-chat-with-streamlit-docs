---
title: Use Community Cloud to develop with GitHub Codespaces
slug: /get-started/installation/community-cloud
---

# Use Community Cloud to develop with GitHub Codespaces

To use GitHub codespaces for Streamlit development, a properly configured `devcontainer.json` file is needed to set up the environment. Fortunately, Community Cloud is here to help! Although Streamlit Community Cloud is primarily used to deploy and share apps with the rest of the world, we've build in some handy features to make it easy to use GitHub Codespaces. This guide explains how to create a Community Cloud account and use an automated workflow to get you into a GitHub codespace and live-editing a Streamlit app. The automated workflow will fork our Streamlit Hello app to your GitHub account, deploy it, then open up a codespace for you to start editing. All this happens right in your browser, no installation required.

You will be signing in to your Google and GitHub accounts during this process. If you do not already have these accounts, you can create them before you begin. If you do not want to use a Google account, you can [create your account with any email](/deploy/streamlit-community-cloud/get-started/create-your-account#primary-identity-option-2-email).

## Sign up for Streamlit Community Cloud

1. Go to <a href="https://share.streamlit.io/signup" target="_blank">share.streamlit.io/signup</a>.
2. Click "**Continue with Google**".

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="Sign up for Streamlit Community Cloud with Google" src="/images/streamlit-community-cloud/sign-up-Google-XL.png" />
</div>

3. Enter your Google credentials and follow Google's authentication prompts.
4. After authenticating with Google, click "**Connect GitHub account**".

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="Connect your GitHub account to Streamlit Community Cloud" src="/images/streamlit-community-cloud/sign-up-2.png" />
</div>

5. Enter your GitHub credentials and follow GitHub's authentication prompts.
6. Click "**Authorize streamlit**".

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="Authorize streamlit to connect to your GitHub account" src="/images/streamlit-community-cloud/GitHub-auth1-none.png" />
</div>

7. To finish, fill in your information and click "**Continue**" at the bottom of the screen.

<div style={{ maxWidth: '70%', margin: 'auto' }}>
<Image alt="Set up your Streamlit Community Cloud account" src="/images/streamlit-community-cloud/sign-up-3.png" />
</div>

8. You will be taken to your Streamlit workspace. If you see a warning icon (<i style={{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}>warning</i>) next to "**Settings**" in the upper-right corner, this will be addressed in the next steps.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Your new workspace in Streamlit Community Cloud" src="/images/streamlit-community-cloud/workspace-empty-warning.png" />
</div>

## Create a new app with GitHub Codespaces

9. Click the down arrow (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>expand_more</i>) to expand the options under "**New App**".

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Options to deploy a new app from your workspace in Streamlit Community Cloud" src="/images/streamlit-community-cloud/deploy-menu.png" />
</div>

10. Click "**Create new app with GitHub Codespaces**".

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Deploy a new app from a sample app template" src="/images/streamlit-community-cloud/deploy-codespaces.png" />
</div>

11. You will be prompted that "Streamlit is requesting additional permissions". Click "**Authorize streamlit**".

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="Authorize streamlit to access private repositories" src="/images/streamlit-community-cloud/GitHub-auth2-none.png" />
</div>

12. The <a href="https://github.com/streamlit/streamlit-hello" target="_blank">Streamlit Hello</a> repository will be forked to your GitHub account. Fill in a repository name and click "**Create!**"

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Fork the sample Streamlit app" src="/images/streamlit-community-cloud/deploy-codespaces-1.png" />
</div>

13. Click "**Create new codespace**" to confirm the creation of a codespace on your GitHub account. Read more about <a href="https://github.com/features/codespaces" target="_blank">GitHub Codespaces</a> the learn about monthly limits for free use and paid plans.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Create your GitHub Codespace" src="/images/streamlit-community-cloud/deploy-codespaces-2.png" />
</div>

14. Wait for GitHub to set up your codespace.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="GitHub preparing your Codespace" src="/images/streamlit-community-cloud/deploy-codespaces-3.png" />
</div>

15. GitHub will automatically execute the commands to launch your Streamlit app within your codespace. Your app will be visible in a "Simple Browser" on the right. This may take a minute to complete from when your codespace first appears on screen.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Your new GitHub Codespace" src="/images/streamlit-community-cloud/deploy-hello-codespace.png" />
</div>

## Edit your app in GitHub Codespaces

16. Go to the app's main file (`Hello.py`) and add some text to the title in `st.write()`. Try typing ":balloon:" at the beginning.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Edit the title of your sample Streamlit app" src="/images/streamlit-community-cloud/deploy-hello-edit-title.png" />
</div>

17. Files are automatically saved in your codespace with each edit. Click "**Always rerun**" in the upper-right corner of your app to automatically rerun with each edit.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt='Select "Always rerun" to automatically see edits in your running app' src="/images/streamlit-community-cloud/deploy-hello-edit-rerun.png" />
</div>

18. See your edits and keep going!

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="See the results of your edit to your Streamlit app" src="/images/streamlit-community-cloud/deploy-hello-edit-result.png" />
</div>

## Stop or delete your codespace

When you are done, remember to stop your codespace on GitHub to avoid any undesired use of your capacity.

19. Go to <a href="https://github.com/codespaces" target="_blank">github.com/codespaces</a>. At the bottom of the page, all your codespaces are listed. Click the overflow menu icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_horiz</i>) for your codespace.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Stop or delete your GitHub Codespace" src="/images/streamlit-community-cloud/deploy-hello-codespace-manage.png" />
</div>

20. Click "**Stop codespace**" if you'd like to return to your work later. Otherwise, click "**Delete**."

    <Flex>
    <div style={{ maxWidth: '40%', margin: 'auto' }}>
    <Image alt="Stop your GitHub codespace" src="/images/streamlit-community-cloud/codespace-menu-stop.png" />
    </div>
    <div style={{ maxWidth: '40%', margin: 'auto' }}>
    <Image alt="Delete your GitHub codespace" src="/images/streamlit-community-cloud/codespace-menu-delete.png" />
    </div>
    </Flex>

21. Congratulations! You just deployed an app to Streamlit Community Cloud. 🎉 Head back to your workspace at <a href="https://share.streamlit.io/" target="_blank">share.streamlit.io/</a> and [deploy another Streamlit app](/deploy/streamlit-community-cloud/deploy-your-app).

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="See your deployed Streamlit app" src="/images/streamlit-community-cloud/deploy-hello-workspace.png" />
</div>
