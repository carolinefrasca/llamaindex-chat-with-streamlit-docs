---
title: Deploy your app
slug: /streamlit-community-cloud/deploy-your-app
---

# Deploy your app

Streamlit Community Cloud lets you deploy your apps in just one click, and most apps will deploy in only a few minutes. If you don't have an app ready to deploy, fork or clone one from our <a href="https://streamlit.io/gallery" target="_blank">App gallery</a> — you can find apps for machine learning, data visualization, data exploration, A/B testing and more.

<Note>

If you want to deploy your app on a different cloud service, check out the [Deploy Streamlit apps](/knowledge-base/tutorials/deploy) article in our Knowledge Base.

</Note>

## Add your app to GitHub

Streamlit Community Cloud launches apps directly from your GitHub repo, so your app code and dependencies need to be on GitHub before you try to deploy your app. For more information on how to specify dependencies, see [App dependencies](/streamlit-community-cloud/deploy-your-app/app-dependencies).

Your directory structure should look similar to this:

```
your-repository/
├── your_app.py
└── requirements.txt
```

If you are including any custom [Configuration](/library/advanced-features/configuration) or [Theming](/library/advanced-features/theming), make sure your config file is saved relative to the root of your repo. Within your repo, your config file should be named `.streamlit/config.toml`.

```
your-repository/
├── .streamlit/
│   └── config.toml
├── your_app.py
└── requirements.txt
```

<Important>

   Although you can deploy multiple apps from the same repository, there can be only one configuration file.

</Important>

## Deploy your app

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click "**New app**" from the upper-right corner of your workspace.

    ![Deploy a new app from your workspace](/images/streamlit-community-cloud/deploy-empty-new-app.png)

2. Fill in your repo, branch, and file path. As a shortcut, you can also click "**Paste GitHub URL**" to paste a link directly to `your_app.py` on GitHub.

    An app URL with a random hash is prefilled but you can change this to a custom subdomain instead. In the example below, the app would be deployed to `https://red-balloon.streamlit.app/`. You can always change your subdomain later. See more about [Custom subdomains](#custom-subdomains) at the end of this page.

    ![Fill in your app's information to deploy your app](/images/streamlit-community-cloud/deploy-an-app.png)

## Advanced settings for deployment

3. (Optional) If you are connecting to a data source or want to specify the Python version for your app, you can do that by clicking "**Advanced settings**" before you deploy the app. Learn more about [Secrets management](/streamlit-community-cloud/deploy-your-app/secrets-management).

    ![Advanced settings for deploying your app](/images/streamlit-community-cloud/deploy-an-app-advanced.png)

<Tip>

Streamlit Community Cloud supports Python 3.8 - Python 3.11, and defaults to version 3.9. You can select a version of your choice from the "Python version" dropdown in the "Advanced settings" modal.

</Tip>

## Watch your app launch

Your app is now deploying and you can watch while it launches. Most apps take only a couple of minutes to deploy, but if your app has a lot of dependencies it may take longer to deploy the first time. After the initial deployment, any change that does not touch your dependencies should show up immediately.

![Watch your app launch](/images/streamlit-community-cloud/deploy-an-app-provisioning.png)

<Note>

The Streamlit Community Cloud logs on the right hand side of your app are only viewable to users with developer access to your repository. These logs help you debug any issues with the app. Learn more about [Streamlit Community Cloud logs](/streamlit-community-cloud/manage-your-app#streamlit-community-cloud-logs).

</Note>

## Your app URL

That's it — you're done! Your app now has a unique subdomain URL that you can share with others. Read more about how to [Share your app](/streamlit-community-cloud/share-your-app) with viewers.

### Unique subdomains

If the "**Custom subdomain (optional)**" field is blank when you deploy your app, a URL is assigned following a structure based on your GitHub repo. The URL begins with your GitHub username or organization owning your repo, followed by your repo name, app path, and a short hash. If you deploy from a branch other than `main` or `master`, the URL also includes the branch name.

```bash
https://[GitHub username or organization]-[repo name]-[app path]-[branch name]-[short hash].streamlit.app
```

For example, this is an app deployed from the `streamlit` organization. The repo is `demo-self-driving` and the app name is `streamlit_app.py` in the root directory. The branch name is `master` and therefore not included.

```bash
https://streamlit-demo-self-driving-streamlit-app-8jya0g.streamlit.app
```

### Custom subdomains

Setting a custom subdomain makes it much easier to share your app since you can choose something memorable. Whether you set a custom subdomain during deployment or later, your app's URL will appear as:

```bash
https://<your-custom-subdomain>.streamlit.app
```

To view or customize your app subdomain from the dashboard:

1. Click the overflow icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) to the app's right and select "**Settings**".

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/streamlit-community-cloud/workspace-app-settings.png" alt="Streamlit Community Cloud app settings" />
</div>

2. View the "**General**" tab in the App settings modal. Your app's unique subdomain will appear here.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/streamlit-community-cloud/workspace-app-settings-general.png" alt="Streamlit Community Cloud general app settings" />
</div>

3. Pick a custom subdomain between 6 and 63 characters in length for your app's URL and hit "**Save**".

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/streamlit-community-cloud/workspace-app-settings-general-valid-domain.png" alt="New custom subdomain for your app" />
</div>

It's that simple! You can then access your app by visiting your customized URL 🎉.

If a custom subdomain is not available (e.g. because it's already taken), you'll see an error message like this:

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/streamlit-community-cloud/workspace-app-settings-general-invalid-domain.png" alt="Invalid custom subdomain for your app" />
</div>
