---
title: Huh. This is isn't supposed to happen message after trying to log in
slug: /knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in
---

# Huh. This is isn't supposed to happen message after trying to log in

This article helps to resolve the login issue caused by email mismatching between the GitHub and the Streamlit Community Cloud.

## Problem

You see the following message after signing in to your Streamlit Community Cloud account:

![Huh. This is isn't supposed to happen message](/images/knowledge-base/huh-this-isnt-supposed-to-happen.png)

This message usually indicates that our system has linked your GitHub username with an email address other than the email address you're currently logged in with.

## Solution

No worries – all you have to do is:

1. Log out of Streamlit Community Cloud completely (via both your email and GitHub accounts).
2. Log in first with your email account (you can do so via either ["Continue with Google"](/streamlit-community-cloud/manage-your-account/sign-in-sign-out#sign-in-with-google) or ["Continue with email"](/knowledge-base/deploy/sign-in-without-sso)).
3. Log in with your [GitHub account](/streamlit-community-cloud/manage-your-account/sign-in-sign-out#sign-in-with-email).
