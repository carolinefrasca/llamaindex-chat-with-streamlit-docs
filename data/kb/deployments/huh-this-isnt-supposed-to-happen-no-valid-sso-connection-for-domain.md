---
title: Huh. This isn't supposed to happen. No valid SSO connection for domain
slug: /knowledge-base/deploy/huh-this-isnt-supposed-to-happen-no-valid-sso-connection-for-domain
---

# Huh. This isn't supposed to happen. No valid SSO connection for domain

This KB helps you resolve the No valid SSO connection error while login to Streamlit Community Cloud with SSO.

## Problem

You have got the following screen when trying to login to your Streamlit Community Cloud account with SSO(SAML authentication):

![No valid SSO connection for domain](/images/knowledge-base/no-valid-sso-connection-for-this-domain.png)

This message means that you’ve logged in with both GitHub and Google in the past, but now you’re trying to log in with only GitHub.

## Solution

You can resolve the error by just logging in with both GitHub and Google and then, if you’d like to unlink your Google account from Streamlit Community Cloud, you can then log out via only Google.
