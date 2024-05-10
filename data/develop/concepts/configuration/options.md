---
title: Working with configuration options
slug: /develop/concepts/configuration/options
---

# Working with configuration options

Streamlit provides four different ways to set configuration options. This list is in reverse order of precedence, i.e. command line flags take precedence over environment variables when the same configuration option is provided multiple times.

<Note>

If you change theme settings in `.streamlit/config.toml` _while_ the app is running, these changes will reflect immediately. If you change non-theme settings in `.streamlit/config.toml` _while_ the app is running, the server needs to be restarted for changes to be reflected in the app.

</Note>

1. In a **global config file** at `~/.streamlit/config.toml` for macOS/Linux or `%userprofile%/.streamlit/config.toml` for Windows:

   ```toml
   [server]
   port = 80
   ```

2. In a **per-project config file** at `$CWD/.streamlit/config.toml`, where
   `$CWD` is the folder you're running Streamlit from.

3. Through `STREAMLIT_*` **environment variables**, such as:

   ```bash
   export STREAMLIT_SERVER_PORT=80
   export STREAMLIT_SERVER_COOKIE_SECRET=dontforgottochangeme
   ```

4. As **flags on the command line** when running `streamlit run`:

   ```bash
   streamlit run your_script.py --server.port 80
   ```

## Telemetry

As mentioned during the installation process, Streamlit collects usage statistics. You can find out
more by reading our [Privacy Notice](https://streamlit.io/privacy-policy), but the high-level
summary is that although we collect telemetry data we cannot see and do not store information
contained in Streamlit apps.

If you'd like to opt out of usage statistics, add the following to your config file:

```toml
[browser]
gatherUsageStats = false
```

## Theming

You can change the base colors of your app using the `[theme]` section of the configuration system.
To learn more, see [Theming.](/develop/concepts/configuration/theming)

## View all configuration options

As described in [Command-line options](/develop/api-reference/cli), you can
view all available configuration options using:

```bash
streamlit config show
```
