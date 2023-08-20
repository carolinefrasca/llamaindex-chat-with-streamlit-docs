---
title: Advanced features
slug: /library/advanced-features
---

## Advanced features

This section gives you background on how different parts of Streamlit work.

<TileContainer>

<RefCard href="/library/advanced-features/app-menu" size="half">

##### ⋮ App menu

Streamlit provides a configurable menu within your app to access convenient tools for developers and viewers. These options can modify the appearance of your app while running.

- [Modify your app's theme while running](/library/advanced-features/app-menu#settings)
- [Record a screencast of your app](/library/advanced-features/app-menu#record-a-screencast)
- [Deploy a local app to Streamlit Community Cloud](/library/advanced-features/app-menu#deploy-this-app)
- [Customize or hide the app menu](/library/advanced-features/app-menu#customize-the-menu)

</RefCard>

<RefCard href="/library/advanced-features/cli" size="half">

##### Command-line options

When you install Streamlit, a command-line (CLI) tool gets installed as well. The purpose of this tool is to run Streamlit apps, change Streamlit configuration options, and help you diagnose and fix issues.

- [What is the command-line interface (CLI)?](/library/advanced-features/cli#command-line-interface)
- [How to run Streamlit apps from the CLI?](/library/advanced-features/cli#run-streamlit-apps)
- [View Streamlit version from the CLI?](/library/advanced-features/cli#view-streamlit-version)
- [View documentation from the CLI](/library/advanced-features/cli#view-documentation)
- [Clear cache from the CLI](/library/advanced-features/cli#clear-cache)

</RefCard>

<RefCard href="/library/advanced-features/configuration" size="half">

##### Streamlit configuration

Streamlit provides four different ways to set configuration options. Learn how to use each of them to change the behavior of Streamlit.

- [How to set configuration options?](/library/advanced-features/configuration)
- [Opt out of telemetry collection](/library/advanced-features/configuration#telemetry)
- [View all configuration options](/library/advanced-features/configuration#view-all-configuration-options)

</RefCard>

<RefCard href="/library/advanced-features/theming" size="half">

##### Theming

This section provides examples of how Streamlit page elements are affected by the various theme config options.

- [primaryColor](/library/advanced-features/theming#primarycolor)
- [backgroundcolor](/library/advanced-features/theming#backgroundcolor)
- [secondarybackgroundcolor](/library/advanced-features/theming#secondarybackgroundcolor)
- [textcolor](/library/advanced-features/theming#textcolor)
- [font](/library/advanced-features/theming#font)
- [base](/library/advanced-features/theming#base)

</RefCard>

<RefCard href="/library/advanced-features/caching" size="half">

##### Caching

The Streamlit cache allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations. To cache a function in Streamlit, you need to decorate it with one of two decorators: `st.cache_data` and `st.cache_resource`.

- [Minimal example](/library/advanced-features/caching#minimal-example)
- [Basic usage](/library/advanced-features/caching#basic-usage)
  - [st.cache_data](/library/advanced-features/caching#stcache_data)
  - [st.cache_resource](/library/advanced-features/caching#stcache_resource)
  - [Deciding which caching decorator to use](/library/advanced-features/caching#deciding-which-caching-decorator-to-use)
- [Advanced usage](/library/advanced-features/caching#advanced-usage)
  - [Excluding input parameters](/library/advanced-features/caching#excluding-input-parameters)
  - [Controlling cache size and duration](/library/advanced-features/caching#controlling-cache-size-and-duration)
  - [Customizing the spinner](/library/advanced-features/caching#customizing-the-spinner)
  - [Using Streamlit commands in cached functions](/library/advanced-features/caching#using-streamlit-commands-in-cached-functions)
  - [Mutation and concurrency issues](/library/advanced-features/caching#mutation-and-concurrency-issues)
- [Migrating from st.cache](/library/advanced-features/caching#migrating-from-stcache)

</RefCard>

<RefCard href="/library/advanced-features/session-state" size="half">

##### Add statefulness to apps

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks.

- [What is Session State?](/library/advanced-features/session-state#what-is-state)
- [How to initialize Session State items?](/library/advanced-features/session-state#initialization)
- [How to read and update Session State items?](/library/advanced-features/session-state#reads-and-updates)
- [How to use callbacks in Session State?](/library/advanced-features/session-state#example-2-session-state-and-callbacks)
- [How to use `args` and `kwargs` in callbacks?](/library/advanced-features/session-state#example-3-use-args-and-kwargs-in-callbacks)
- [How to use callbacks in forms?](/library/advanced-features/session-state#example-4-forms-and-callbacks)
- [How is Session State related to Widget State?](/library/advanced-features/session-state#session-state-and-widget-state-association)
- [Caveats and limitations](/library/advanced-features/session-state#caveats-and-limitations)

</RefCard>

<RefCard href="/library/advanced-features/prerelease" size="half">

##### Pre-release features

At Streamlit, we like to move quick while keeping things stable. In our latest effort to move even faster without sacrificing stability, we're offering our bold and fearless users two ways to try out Streamlit's bleeding-edge features.

- [Experimental features](/library/advanced-features/prerelease#experimental-features)
- [Nightly releases](/library/advanced-features/prerelease#nightly-releases)

</RefCard>

<RefCard href="/library/advanced-features/secrets-management" size="half">

##### Secrets management

This section provides examples of how to use secrets management to store and retrieve sensitive information in your Streamlit app.

- [Develop locally and set up secrets](/library/advanced-features/secrets-management#develop-locally-and-set-up-secrets)
- [Use secrets in your app](/library/advanced-features/secrets-management#use-secrets-in-your-app)
- [Error handling](/library/advanced-features/secrets-management#error-handling)
- [Use secrets on Streamlit Community Cloud](/library/advanced-features/secrets-management#use-secrets-on-streamlit-community-cloud)

</RefCard>

<RefCard href="/library/advanced-features/timezone-handling" size="half">

##### Working with timezones

Working with timezones can be tricky. This section provides a high-level description of how to handle timezones in Streamlit to avoid unexpected behavior.

- [Overview](/library/advanced-features/timezone-handling#working-with-timezones)
- [How Streamlit handles timezones](/library/advanced-features/timezone-handling#how-streamlit-handles-timezones)
- [`datetime` instance without a timezone (naive)](/library/advanced-features/timezone-handling#datetime-instance-without-a-timezone-naive)
- [`datetime` instance with a timezone](/library/advanced-features/timezone-handling#datetime-instance-with-a-timezone)

</RefCard>

<RefCard href="/library/advanced-features/widget-semantics" size="full">

##### Advanced notes on widget behavior

Widgets are magical and often work how you want. But they can have surprising behavior in some situations. This section provides is a high-level, abstract description of widget behavior, including some common edge-cases.

</RefCard>
</TileContainer>
