---
title: Delete your app
slug: /streamlit-community-cloud/manage-your-app/delete-your-app
---

# Delete your app

If you need to delete your app, it's simple and easy. There are several cases where you may need to delete your app:

* You have finished playing around with an example app.
* You want to deploy from a private repository but already have a private app.
* You want to change the Python version for your app or otherwise redeploy your app.

If you delete your app and intend to immediately redploy it, your custom subdomain should be immediately available for reuse.

You can delete your app:
* [From your workspace](#delete-your-app-from-your-workspace).
* [From your Cloud logs](#delete-your-app-from-your-cloud-logs).

### Delete your app from your workspace

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) next to your app. Click "**Delete**".

    ![Delete your app from your workspace](/images/streamlit-community-cloud/workspace-app-delete.png)

2. A confirmation will display. Enter the required confirmation string and click "**Delete**".

    <div style={{ maxWidth: '50%', margin: 'auto' }}>
    <Image alt="Confirm deleting your app from Streamlit Community Cloud" src="/images/streamlit-community-cloud/workspace-app-delete-confirm.png" clean />
    </div>

### Delete your app from your Cloud logs

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Manage app**" in the lower-right corner.

    ![Access Streamlit Community Cloud logs from your app](/images/streamlit-community-cloud/cloud-logs-open.png)

2. Click the overflow menu icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) and click "**Delete app**".

    ![Delete your app from your Cloud logs](/images/streamlit-community-cloud/cloud-logs-menu-delete.png)

3. A confirmation will display. Enter the required confirmation string and click "**Delete**".

    <div style={{ maxWidth: '50%', margin: 'auto' }}>
    <Image alt="Confirm deleting your app from Streamlit Community Cloud" src="/images/streamlit-community-cloud/workspace-app-delete-confirm.png" clean />
    </div>
