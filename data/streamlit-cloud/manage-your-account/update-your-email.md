---
title: Update your email
slug: /streamlit-community-cloud/manage-your-account/update-your-email
---

# Update your email

If you wish to update your email on Streamlit Community Cloud, you can do so via your [Workspace settings](/streamlit-community-cloud/manage-your-account/workspace-settings). Updating your email changes the primary identity of your account. Once updated, if your account's email is associated with a Google account, you can sign in with Google OAuth. Otherwise, you through emailed links. The latter involves typing in your email, after which we'll send you a unique, single-use link (valid for 15 minutes).

If you are signed in to GitHub and don't already have a primary identity on your account, see [Connect Google to your account](#connect-google-to-your-account).

## How to update your email

1. Sign in to Streamlit Community Cloud at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
2. Click "**Settings**" in the page's top-right corner.
   ![Access your workspace settings from your workspace](/images/streamlit-community-cloud/account-settings-header.png)

3. Click "**Update email**" within the "**Linked accounts**" section.
   ![Update your email from your workspace settings](/images/streamlit-community-cloud/account-change-email-1.png)

4. Enter your new email and click "**Update email**."
   ![Enter your new email address for your Streamlit Community Cloud account](/images/streamlit-community-cloud/account-change-email-2.png)

5. You'll see a confirmation dialog asking you to check your email for a confirmation link. Click "**Done**."
   ![Confirmation message after choosing a new email for your Streamlit Community Cloud account](/images/streamlit-community-cloud/account-change-email-3.png)

6. Your account settings will show "**Update pending**" until you complete the next step.
   ![Email update pending displayed in your workspace settings](/images/streamlit-community-cloud/account-change-email-4.png)

7. Check your inbox for an email from Streamlit containing a "**Change email**" button and a confirmation link. This one-time link expires in 15 minutes. Click either one to confirm your new email address for Streamlit Community Cloud. Before doing so, ensure you access the link from the same browser session where you are logged in to Streamlit Community Cloud.

   <Important>

   If you access the confirmation link from a browser session where you are not logged in to Streamlit Community Cloud, the confirmation link will not complete the process. You will be prompted to sign in. If you try to sign in with your new email, you will create a second account instead. See [Troubleshooting](#troubleshooting).

   </Important>

   ![Click 'Change email' from the message sent to your email account](/images/streamlit-community-cloud/account-change-email-5.png)

8. A confirmation will display to confirm your email update is complete! 🎈
   ![Confirmation that your email has been changed on your Streamlit Community Cloud account](/images/streamlit-community-cloud/account-change-email-6.png)

## Resend your confirmation link

If your confirmation link expires, don't worry! You can resend it by following these steps:

1. Sign in to Streamlit Community Cloud at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> and click "**Settings**" in the page's top-right corner.
2. Click "**Update pending**"
   ![Click 'Update pending' from your workspace settings](/images/streamlit-community-cloud/account-change-email-7.png)

3. Click "**Resend email**"
   ![Click 'Resend email' to resend the confirmation link to your email](/images/streamlit-community-cloud/account-change-email-8.png)

4. Continue from step 4 of [How to update your email](#how-to-update-your-email).

## Troubleshooting

If you click the confirmation link in a browser session where you are not signed in, you will be informed that "Sign in is required." If you try to sign in with your new email, you will create a second account instead. You cannot resend your confirmation link while you have this second account. If you accidentally created a second account, you can follow the steps to [Delete your account](/streamlit-community-cloud/manage-your-account/delete-your-account) to get rid of the duplicate. Afterwards, [Resend your confirmation link](#resend-your-confirmation-link) from your first account.

## Connect Google to your account

1. If you signed up with GitHub and did not create a primary identity, your workspace will show a warning icon in the upper right corner. Click "**Settings**" to access your workspace settings.

   ![Your workspace without a primary identity](/images/streamlit-community-cloud/account-settings-header-warning.png)

2. When you access your workspace settings, a warning is displayed: "You are not signed in with a primary identity account." Click "**Sign in with Google**" and follow Google's authentication prompts.

   <div style={{ maxWidth: '75%', margin: 'auto' }}>
   <Image alt="Sign in with Google to connect your email to your Streamlit Community Cloud account" src="/images/streamlit-community-cloud/account-no-primary.png" />
   </div>

3. Your account now has both a primary identity and source control account.

   <div style={{ maxWidth: '75%', margin: 'auto' }}>
   <Image alt="A fully signed-in Streamlit Community Cloud account" src="/images/streamlit-community-cloud/account-primary-identity-and-source-control.png" />
   </div>
