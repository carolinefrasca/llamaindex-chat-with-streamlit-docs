---
title: Streamlit Trust and Security
slug: /deploy/streamlit-community-cloud/get-started/trust-and-security
---

# Streamlit trust and security

Streamlit is a framework that turns Python scripts into interactive apps, giving data scientists the ability to quickly create data and model-based apps for the entire company.

A simple Streamlit app is:

```python
import streamlit as st
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
```

When you `streamlit run my_app.py`, you start a web server that runs the interactive application on your local computer at `http://localhost:8501`. This is great for local development. When you want to share with your colleagues, Streamlit Community Cloud enables you to deploy and run these applications in the cloud. Streamlit Community Cloud handles the details of containerization and provides you an interface for easily managing your deployed apps.

This document provides an overview of the security safeguards we've implemented to protect you and your data. Security, however, is a shared responsibility and you are ultimately responsible for making appropriate use of Streamlit and the Streamlit Community Cloud, including implementation of appropriate user-configurable security safeguards and best practices.

## Product security

### Authentication

You must authenticate through GitHub to deploy or administer an app. Authentication through Google or single-use emailed links are required to view a private app when you don't have push or admin permissions on the associated GitHub repository. The single-use emailed links are valid for 15 minutes once requested.

### Permissions

Streamlit Community Cloud inherits the permissions you have assigned in GitHub. Users with write access to a GitHub repository for a given app will be able to make changes in the Streamlit administrative console. However, only users with _admin access_ to a repository are able to **deploy and delete apps**.

## Network and application security

### Data hosting

Our physical infrastructure is hosted and managed within secure data centers maintained by infrastructure-as-a-service cloud providers. Streamlit leverages many of these platforms' built-in security, privacy, and redundancy features. Our cloud providers continually monitor their data centers for risk and undergo assessments to ensure compliance with industry standards.

### Data deletion

Community Cloud users have the option to delete any apps they’ve deployed as well as their entire account.

When a user deletes their application from the admin console, we delete their source code, including any files copied from their GitHub repository or created within our system from the running app. However, we keep a record representing the application in our database. This record contains the coordinates of the application: the GitHub organization or user, the GitHub repository, the branch, and the path of the main module file.

When a user deletes their account, we perform a hard deletion of their data and a hard deletion of all the apps that belong to the GitHub identity associated with their account. In this case, we do not maintain the records of application coordinates described above. When an account is deleted, we also delete any HubSpot contact associated with the Community Cloud account.

### Virtual private cloud

All of our servers are within a virtual private cloud (VPC) with firewalls and network access control lists (ACLs) to allow external access to a select few API endpoints; all other internal services are only accessible within the VPC.

### Encryption

Streamlit apps are served entirely over HTTPS. We use only strong cipher suites and HTTP Strict Transport Security (HSTS) to ensure browsers interact with Streamlit apps over HTTPS.

All data sent to or from Streamlit over the public internet is encrypted in transit using 256-bit encryption. Our API and application endpoints use Transport Layer Security (TLS) 1.2 (or better). We also encrypt data at rest on disk using AES-256.

### Permissions and authentication

Access to Community Cloud user account data is limited to authorized personnel. We run a zero-trust corporate network, utilize single sign-on and multi-factor authentication (MFA), and enforce strong password policies to ensure access to cloud-related services is protected.

### Incident response

Our internal protocol for handling security events includes detection, analysis, response, escalation, and mitigation. Security advisories are made available at [https://streamlit.io/advisories](https://streamlit.io/advisories).

### Penetration testing

Streamlit uses third-party security tools to scan for vulnerabilities on a regular basis. Our security teams conduct periodic, intensive penetration tests on the Streamlit platform. Our product development team responds to any identified issues or potential vulnerabilities to ensure the quality, security, and availability of Streamlit applications.

### Vulnerability management

We keep our systems up-to-date with the latest security patches and continuously monitor for new vulnerabilities. This includes automated scanning of our code repositories for vulnerable dependencies.

If you discover a vulnerability in one of our products or websites, please report the issue to [HackerOne](https://hackerone.com/snowflake?type=team).
