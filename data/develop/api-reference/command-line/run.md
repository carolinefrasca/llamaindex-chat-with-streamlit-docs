---
title: streamlit run
slug: /develop/api-reference/cli/run
---

## `$ streamlit run`

### Syntax

```
streamlit run <entrypoint file> [-- config options] [script args]
```

### Arguments

`<entrypoint file>`: The path to your entrypoint file for your Streamlit app. Your entrypoint file is your app's homepage.

### Options

Configuration options are passed in the form of `--<section>.<option>=<value>`. For example, if you want to set the primary color of your app to blue, you could use one of the three equivalent options:

- `--theme.primaryColor=blue`
- `--theme.primaryColor="blue"`
- `--theme.primaryColor=#0000FF`

For a complete list of configuration options, see [`config.toml`](/develop/api-reference/configuration/config.toml) in the API reference. For examples, see below.

### Script arguments

If you need to pass arguments directly to your script, you can pass them as positional arguments. If you use `sys.argv` to read your arguments, `sys.arfgv` returns a list of all arugments and does _not_ include any configuration options. Python interprets all arguments as strings.

- `sys.argv[0]` returns the provided path to your entrypoint file (`<entrypoint file>`).
- `sys.argv[1:]` returns a list of arguments in order and does not include any configuration options.

### Examples

- If your app is in your working directory, run it as follows:

  ```
  streamlit run your_app.py
  ```

- If your app is in a subdirectory, run it as follows:

  ```
  streamlit run your_subdirectory/your_app.py
  ```

- If your app is saved in a public GitHub repo or gist, run it as follows:

  ```
  streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
  ```

- If you need to set one or more configuration options, run it as follows:

  ```
  streamlit run your_app.py --client.showErrorDetails=False --theme.primaryColor=blue
  ```

- If you need to pass an argument to your script, run it as follows:

  ```
  streamlit run your_app.py "my list" of arguments
  ```

  Within your script, the following statement will be true:

  ```
  sys.argv[0] == "your_app.py"
  sys.argv[1] == "my list"
  sys.argv[2] == "of"
  sys.argv[3] == "arguments"
  ```
