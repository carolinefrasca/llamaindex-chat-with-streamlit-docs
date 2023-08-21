---
title: Quickstart
slug: /streamlit-community-cloud/get-started/quickstart
---

# Quickstart

This is a concise set of steps to create your Streamlit Community Cloud account and deploy a sample app. For other options and complete explanations, start with [Create your account](/streamlit-community-cloud/get-started/create-your-account).

You will be signing in to your Google and GitHub accounts during this process. If you do not already have these accounts, you can create them before you begin. If you do not want to use a Google account, you can [create your account with any email](/streamlit-community-cloud/get-started/create-your-account#primary-identity-option-2-email).

## Sign up

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

## Fork a sample app

9. Click the down arrow (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>expand_more</i>) to expand the options under "**New App**".

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Options to deploy a new app from your workspace in Streamlit Community Cloud" src="/images/streamlit-community-cloud/deploy-example-1.png" />
</div>

10. Click "**Create from sample app template**".

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Deploy a new app from a sample app template" src="/images/streamlit-community-cloud/deploy-example-2.png" />
</div>

11. You will be prompted that "Streamlit is requesting additional permissions". Click "**Authorize streamlit**".

<div style={{ maxWidth: '50%', margin: 'auto' }}>
<Image alt="Authorize streamlit to access private repositories" src="/images/streamlit-community-cloud/GitHub-auth2-none.png" />
</div>

12. Click "**Fork sample app**".

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Fork the sample Streamlit app" src="/images/streamlit-community-cloud/deploy-example-fork.png" />
</div>

## Deploy a sample app

13. After the repository is copied to your GitHub account, the forked repository's information is prefilled into a deployment screen. Click "**Deploy!**"

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Deploy your sample Streamlit app" src="/images/streamlit-community-cloud/deploy-example-deploy.png" />
</div>

14. Wait for the app to build. This may take a few minutes.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="Watch your app build and deploy" src="/images/streamlit-community-cloud/deploy-demo-provisioning.png" />
</div>

## You're done!

Congratulations! You just deployed an app to Streamlit Community Cloud. 🎉 Your app may take a few minutes to fully build, but once it's done it will load automatically.

<div style={{ maxWidth: '90%', margin: 'auto' }}>
<Image alt="See your deployed Streamlit app" src="/images/streamlit-community-cloud/deploy-example-done.png" />
</div>

## What's next?

Start modifying the code in your forked repository and have fun exploring. Alternatively, you can [deploy another Streamlit app](/streamlit-community-cloud/deploy-your-app). Happy Streamlit-ing!🎈
