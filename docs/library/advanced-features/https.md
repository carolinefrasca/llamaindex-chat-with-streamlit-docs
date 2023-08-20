---
title: HTTPS support
slug: /library/advanced-features/https-support
---

# HTTPS support

Many apps need to be accessed with SSL / [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol or `https://`.

We recommend performing SSL termination in a reverse proxy or load balancer for self-hosted and production use cases, not directly in the app. [Streamlit Community Cloud](/streamlit-community-cloud) uses this approach, and every major cloud and app hosting platform should allow you to configure it and provide extensive documentation. You can find some of these platforms in our [Deployment tutorials](/knowledge-base/tutorials/deploy).

To terminate SSL in your Streamlit app, you must configure `server.sslCertFile` and `server.sslKeyFile`. Learn how to set config options in [Configuration](/library/advanced-features/configuration).

## Details on usage

- The configuration value should be a local file path to a cert file and key file. These must be available at the time the app starts.
- Both `server.sslCertFile` and `server.sslKeyFile` must be specified. If only one is specified, your app will exit with an error.
- This feature will not work in Community Cloud. Community Cloud already serves your app with TLS.

<Warning>

In a production environment, we recommend performing SSL termination by the load balancer or the reverse proxy, not using this option. The use of this option in Streamlit has not gone through extensive security audits or performance tests.

</Warning>

## Example usage

```toml
# .streamlit/config.toml

[server]
sslCertFile = '/path/to/certchain.pem'
sslKeyFile = '/path/to/private.key'
```
