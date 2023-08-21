---
title: Streamlit Trust and Security
slug: /streamlit-community-cloud/get-started/trust-and-security
---

# Streamlit Trust and Security

Streamlit is a framework that turns Python scripts into interactive apps, giving data scientists the ability to quickly create data and model-based apps for the entire company.

A simple Streamlit app is:

```python
import streamlit as st
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
```

When you `streamlit run my_app.py`, you start a web server that runs the interactive application on your local computer at `http://localhost:8501`. This is great for local development. When you want to share with your colleagues, Streamlit Community Cloud enables you to deploy and run these applications in the cloud. Streamlit Community Cloud handles all the details of containerization and provides you an interface for easily managing your deployed apps.

This document is an overview of how we provide best-in-industry security for you. We'll cover all the important areas in the lifecycle of your data:

- **Product Security**: how we ensure only you can create and view apps that access your data
- **Network and Application Security**: how we ensure your data is protected when it is in our cloud
- **Ongoing Operations**: how we stay good stewards of security best practices

## Product Security

### Authentication

Authentication through GitHub is required to deploy or administer an app. Authentication through Google or single-use emailed links are required to view a private app for which you are not an admin. These links are valid for 15 minutes once requested. We do not store customer passwords.

### Credential Storage

We encrypt sensitive customer data (e.g. secrets, authentication tokens) at-rest with AES256 as described in Google's documentation.

### Permissions

Our permission levels inherit from the permissions you have assigned in GitHub. Users with write access to a GitHub repository for a given app will be able to make changes in the Streamlit administrative console.

Only users with _admin access_ to a repository are able to **deploy and delete apps**.

## Network and Application Security

### Data Hosting

Our physical infrastructure is hosted and managed within Google Cloud Platform (GCP) using their secure data centers. Streamlit leverages many of the platform's built-in security, privacy, and redundancy features. GCP continually monitors its data centers for risk and undergoes assessments to ensure compliance with industry standards. GCP's data centers have numerous accreditations, including ISO-27001, SOC 1 and SOC 2.

### Virtual Private Cloud

All of our servers are within a virtual private cloud (VPC) with firewalls and network access control lists (ACLs) to allow external access to a select few API endpoints; all other internal services are only accessible within the VPC.

### Encryption

All Streamlit apps are served entirely over HTTPS. All data sent to or from Streamlit over the public internet is encrypted in transit using 256-bit encryption. Our API and application endpoints are TLS only (v1.2). We use only strong cipher suites and HTTP Strict Transport Security (HSTS) to ensure browsers interact with Streamlit apps over HTTPS. We also encrypt data at rest using AES-256.

### Permissions and Authentication

Access to customer data is limited to authorized employees who require it for their job. We run a zero-trust corporate network so there are no corporate resources or additional privileges gained from being on Streamlit's internal network. We utilize single sign-on, 2-factor authentication (2FA), and enforce strong password policies to ensure access to all cloud-related services are protected.

### Incident Response

We have an internal protocol for handling security events which includes escalation procedures, rapid mitigation, and documented post-mortems. We notify customers promptly and publicize security advisories at [https://streamlit.io/advisories](https://streamlit.io/advisories).

### Penetration Testing

Streamlit uses third-party security tools to scan for vulnerabilities on a regular basis. Our security partners conduct periodic, intensive penetration tests on the Streamlit platform. Our product development team immediately responds to any identified issues or potential vulnerabilities to ensure the quality and security of Streamlit applications.

## Security and Compliance Programs

### People

#### Background Checks

All Streamlit employees go through a thorough background check before hiring.

### Training

We take a least-privilege approach to the access and handling of data. While we retain a minimal amount of customer data and limit internal access on a need-to-know basis, all employees are required to review related security policies and are trained on proper data handling to ensure they uphold our strict commitment to the privacy and security of your data.

### Confidentiality

All employees sign a confidentiality agreement before they start at Streamlit.

## Vulnerability Control

### Vulnerability Management

We keep our systems up-to-date with the latest security patches and continuously monitor for new vulnerabilities through compliance and security mailing lists. This includes automatic scanning of our code repositories for vulnerable dependencies.
