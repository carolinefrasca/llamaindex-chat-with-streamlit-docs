---
title: Pre-release features
slug: /library/advanced-features/prerelease
---

# Pre-release features

At Streamlit, we like to move quick while keeping things stable. In our latest effort to move even faster without sacrificing stability, we're offering our bold and fearless users two ways to try out Streamlit's bleeding-edge features:

1. [Experimental features](#experimental-features)
2. [Nightly releases](#nightly-releases)

## Experimental Features

Less stable Streamlit features have one naming convention: `st.experimental_`. This distinction is a prefix we attach to our command names to make sure their status is clear to everyone.

Here's a quick rundown of what you get from each naming convention:

- **st**: this is where our core features like `st.write` and `st.dataframe` live. If we ever make backward-incompatible changes to these, they will take place gradually and with months of announcements and warnings.
- **experimental**: this is where we'll put all new features that may or may not ever make it into Streamlit core. This gives you a chance to try the next big thing we're cooking up weeks or months before we're ready to stabilize its API. We don't know whether these features have a future, but we want you to have access to everything we're trying, and work with us to figure them out.

Features with the `experimental_` naming convention are things that we're still working on or trying
to understand. If these features are successful, at some point they'll become part of Streamlit
core. If unsuccessful, these features are removed without much notice. While in experimental, a feature's API and behaviors may not be stable, and it's possible they could change in ways that aren't backward-compatible.

<Warning>

Experimental features and their APIs may change or be removed at any time.

</Warning>

### The lifecycle of an experimental feature

1. A feature is added with the `experimental_` prefix.
2. The feature is potentially tweaked over time, with possible API/behavior breakages.
3. If successful, we promote the feature to Streamlit core and remove it from `experimental_`:
   - a\. The feature's API stabilizes and the feature is _cloned_ without the `experimental_` prefix, so it exists as both `st` and `experimental_`. At this point, users will see a warning when using the version of the feature with the `experimental_` prefix -- but the feature will still work.
   - b\. At some point, the code of the `experimental_`-prefixed feature is _removed_, but there will still be a stub of the function prefixed with `experimental_` that shows an error with appropriate instructions.
   - c\. Finally, at a later date the `experimental_` version is removed.
4. If unsuccessful, the feature is removed without much notice and we leave a stub in `experimental_` that shows an error with instructions.

## Nightly releases

In addition to experimental features, we offer another way to try out Streamlit's newest features: nightly releases.

At the end of each day (at night 🌛), our bots run automated tests against the latest Streamlit code and, if everything looks good, it publishes them as the `streamlit-nightly` package. This means the nightly build includes all our latest features, bug fixes, and other enhancements on the same day they land on our codebase.

**How does this differ from official releases?**

Official Streamlit releases go not only through both automated tests but also rigorous manual testing, while nightly releases only have automated tests. It's important to keep in mind that new features introduced in nightly releases often lack polish. In our official releases, we always make double-sure all new features are ready for prime time.

**How do I use the nightly release?**

All you need to do is install the `streamlit-nightly` package:

```bash
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```

<Warning>

You should never have both `streamlit` and `streamlit-nightly` installed in the same environment!

</Warning>

**Why should I use the nightly release?**

Because you can't wait for official releases, and you want to help us find bugs early!

**Why shouldn't I use the nightly release?**

While our automated tests have high coverage, there's still a significant likelihood that there will be some bugs in the nightly code.

**Can I choose which nightly release I want to install?**

If you'd like to use a specific version, you can find the version number in our [Release history](https://pypi.org/project/streamlit-nightly/#history). Specify the desired version using `pip` as usual: `pip install streamlit-nightly==x.yy.zz-123456`.

**Can I compare changes between releases?**

If you'd like to review the changes for a nightly release, you can use the [comparison tool on GitHub](https://github.com/streamlit/streamlit/compare/0.57.3...0.57.4.dev20200412).
