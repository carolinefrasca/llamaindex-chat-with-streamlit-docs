---
title: Reboot your app
slug: /streamlit-community-cloud/manage-your-app/reboot-your-app
---

# Reboot your app

If you need to clear your app's memory or force a fresh build after modifying a file that Streamlit Community Cloud doesn't monitor, you may need to reboot your app. This will interrupt any user who may currently be using your app and may take a few minutes for your app to re-deploy. Anyone visiting your app will see "Your app is in the oven" during a reboot.

Rebooting your app on Streamlit Community Cloud is easy! You can reboot your app:
* [From your workspace](#reboot-your-app-from-your-workspace).
* [From your Cloud logs](#reboot-your-app-from-your-cloud-logs).

### Reboot your app from your workspace

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) next to your app. Click "**Reboot**".

    ![Reboot your app from your workspace](/images/streamlit-community-cloud/workspace-app-reboot.png)

2. A confirmation will display. Click "**Reboot**".

    <div style={{ maxWidth: '50%', margin: 'auto' }}>
    <Image alt="Confirm rebooting your app in Streamlit Community Cloud" src="/images/streamlit-community-cloud/workspace-app-reboot-confirm.png" clean />
    </div>

### Reboot your app from your Cloud logs

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Manage app**" in the lower-right corner.

    ![Access Streamlit Community Cloud logs from your app](/images/streamlit-community-cloud/cloud-logs-open.png)

2. Click the overflow menu icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>) and click "**Reboot app**".

    ![Reboot your app from your Cloud logs](/images/streamlit-community-cloud/cloud-logs-menu-reboot.png)

3. A confirmation will display. Click "**Reboot**".

    <div style={{ maxWidth: '50%', margin: 'auto' }}>
    <Image alt="Confirm rebooting your app in Streamlit Community Cloud" src="/images/streamlit-community-cloud/workspace-app-reboot-confirm.png" clean />
    </div>
