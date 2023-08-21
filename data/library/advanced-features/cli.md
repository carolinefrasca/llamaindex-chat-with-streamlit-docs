---
title: Command-line options
slug: /library/advanced-features/cli
---

# Command-line interface

When you install Streamlit, a command-line (CLI) tool gets installed
as well. The purpose of this tool is to run Streamlit apps, change Streamlit configuration options,
and help you diagnose and fix issues.

To see all of the supported commands:

```bash
streamlit --help
```

### Run Streamlit apps

```bash
streamlit run your_script.py [-- script args]
```

Runs your app. At any time you can stop the server with **Ctrl+c**.

<Note>

When passing your script some custom arguments, **they must be passed after
two dashes**. Otherwise the arguments get interpreted as arguments to Streamlit
itself.

</Note>

To see the Streamlit 'Hello, World!' example app, run `streamlit hello`.

### View Streamlit version

To see what version of Streamlit is installed, just type:

```bash
streamlit version
```

### View documentation

```bash
streamlit docs
```

Opens the Streamlit documentation (i.e. this website) in a web browser.

### Clear cache

```bash
streamlit cache clear
```

Clears persisted files from the on-disk [Streamlit cache](/library/api-reference/performance), if
present.

### View all configuration options

As described in [Configuration](/library/advanced-features/configuration), Streamlit has several
configuration options. To view them all, including their current values, just type:

```bash
streamlit config show
```
