---
title: How can I deploy multiple Streamlit apps on different subdomains?
slug: /knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains
---

# How can I deploy multiple Streamlit apps on different subdomains?

## Problem

You want to deploy multiple Streamlit apps on different subdomains.

## Solution

Like running your Streamlit app on more common ports such as 80, subdomains are handled by a web server like Apache or Nginx:

- Set up a web server on a machine with a public IP address, then use a DNS server to point all desired subdomains to your webserver's IP address

- Configure your web server to route requests for each subdomain to the different ports that your Streamlit apps are running on

For example, let’s say you had two Streamlit apps called `Calvin` and `Hobbes`. App `Calvin` is running on port **8501**. You set up app `Hobbes` to run on port **8502**. Your webserver would then be set up to "listen" for requests on subdomains `calvin.somedomain.com` and `hobbes.subdomain.com`, and route requests to port **8501** and **8502**, respectively.

Check out these two tutorials for Apache2 and Nginx that deal with setting up a webserver to redirect subdomains to different ports:

- [Apache2 subdomains](https://stackoverflow.com/questions/8541182/apache-redirect-to-another-port)
- [NGinx subdomains](https://gist.github.com/soheilhy/8b94347ff8336d971ad0)
