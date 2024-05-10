---
title: Creating multipage apps using the `pages/` directory
slug: /develop/concepts/multipage-apps/pages-directory
description: Streamlit provides a simple way to create multipage apps.
---

# Creating multipage apps using the `pages/` directory

As your app grows large, it becomes useful to organize your script into multiple pages. This makes your app easier to manage as a developer and easier to navigate as a user. Streamlit provides a frictionless way to create multipage apps. Pages are automatically shown in a navigation widget inside your app's sidebar. If a user clicks on a page in the sidebar, Streamlit navigates to that page without reloading the frontend — making app browsing incredibly fast! In this guide, let’s learn how to create multipage apps.

## Structuring your multipage app

Streamlit identifies pages in a multipage app by directory structure and filenames. The file you pass to `streamlit run` is called your entrypoint file. This is your app's homepage. When you have a `pages/` directory next to your entrypoint file, Streamlit will identify each Python file within it as a page. The following example has three pages. `your_homepage.py` is the entrypoint file and homepage.

```
your_working_directory/
├── pages/
│   ├── a_page.py
│   └── another_page.py
└── your_homepage.py
```

Run your multipage app just like you would for a single-page app. Pass your entrypoint file to `streamlit run`.

```
streamlit run your_homepage.py
```

Only `.py` files in the `pages/` directory will be identified as pages. Streamlit ignores all other files in the `pages/` directory and its subdirectories. Streamlit also ignores Python files in subdirectories of `pages/`.

Keep reading to learn how filenames are displayed and ordered in your app's navigation.

## Naming and ordering your pages

The entrypoint file is your app's homepage and the first page users will see when visiting your app. Once you've added pages to your app, the entrypoint file appears as the topmost page in the sidebar. Streamlit determines the page label and ordering of each page from your filenames. Labels may differ from the page title set in [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config).

### Filenames for pages

Filenames are composed of four different parts as follows:

1. `number`. A non-negative integer.
2. `separator`. Any combination of underscore (`"_"`), dash (`"-"`), and space (`" "`).
3. `label`. Everything up to, but not including, `".py"`.
4. `".py"`

### How Streamlit converts filenames into page labels

Streamlit displays page labels as follows:

1. If your filename contains a `label`, Streamlit displays the `label` in the left navigation. Any underscores within the page's `label` are treated as spaces.
2. If your filename contains a `number` but does not contain a `label`, Streamlit displays the `number` instead.
3. If your filename contains only a `separator` with no `number` and no `label`, Streamlit will not display the page in the sidebar navigation.

The following filenames would all display as "Awesome homepage" in the sidebar navigation.

- `"Awesome homepage.py"`
- `"Awesome_homepage.py"`
- `"02Awesome_homepage.py"`
- `"--Awesome_homepage.py"`
- `"1_Awesome_homepage.py"`
- `"33 - Awesome homepage.py"`

### How pages are sorted in the sidebar

The entrypoint file is always displayed first. The remaining pages are sorted as follows:

- Files that have a `number` appear before files without a `number`.
- Files are sorted based on the `number` (if any), followed by the `label` (if any).
- When files are sorted, Streamlit treats the `number` as an actual number rather than a string. So `03` is the same as `3`.

This table shows examples of filenames and their corresponding labels, sorted by the order in which they appear in the sidebar.

**Examples**:

| **Filename**              | **Rendered label** |
| :------------------------ | :----------------- |
| `1 - first page.py`       | first page         |
| `12 monkeys.py`           | monkeys            |
| `123.py`                  | 123                |
| `123_hello_dear_world.py` | hello dear world   |
| `_12 monkeys.py`          | 12 monkeys         |

<Tip>

Emojis can be used to make your page names more fun! For example, a file named `🏠_Home.py` will create a page titled "🏠 Home" in the sidebar. When adding emojis to filenames, it’s best practice to include a numbered prefix to make autocompletion in your terminal easier. Terminal-autocomplete can get confused by unicode (which is how emojis are represented).

</Tip>

## Navigating between pages

Pages are automatically shown in a sidebar navigation UI. When a user clicks on a page in the sidebar UI, Streamlit navigates to that page without reloading the entire frontend — making app browsing incredibly fast! Optionally, you can hide the default navigation UI and build your own with [`st.page_link`](/develop/api-reference/widgets/st.page_link). For more information, see [Build a custom navigation menu with `st.page_link`](/develop/tutorials/multipage/st.page_link-nav).

If you need to programmatically switch pages, use [`st.switch_page`](/develop/api-reference/navigation/st.switch_page).

Users can also navigate between pages using URLs. Pages have their own URLs, defined by the file's `label`. When multiple files have the same `label`, Streamlit picks the first one (based on the ordering [described above](#how-pages-are-sorted-in-the-sidebar)). Users can view a specific page by visiting the page's URL.

<Important>

Navigating between pages by URL creates a new browser session and clears `st.session_state`. In particular, clicking markdown links to other
pages resets `st.session_state`. In order to retain values in `st.session_state`, a user must use the sidebar navigation or other Streamlit
widgets to switch pages.

</Important>

If a user tries to access a URL for a page that does not exist, they will see a modal like the one below, saying the user has requested a page that was not found in the app’s `pages/` directory.

<Image src="/images/mpa-page-not-found.png" />

## Notes and limitations

- Pages support run-on-save.
  - When you update a page while your app is running, this causes a rerun for users currently viewing that exact page.
  - When you update a page while your app is running, the app will not automatically rerun for users currently viewing a different page.
- While your app is running, adding or deleting a page updates the sidebar navigation immediately.
- [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) works at the page level.
  - When you set `title` or `favicon` using `st.set_page_config`, this applies to the current page only.
  - When you set `layout` using `st.set_page_config`, the setting will remain for the session until changed by another call to `st.set_page_config`. If you use `st.set_page_config` to set `layout`, it's recommended to call it on _all_ pages.
- Pages share the same Python modules globally:

  ```python
  # page1.py
  import foo
  foo.hello = 123

  # page2.py
  import foo
  st.write(foo.hello)  # If page1 already executed, this writes 123
  ```

- Pages share the same [st.session_state](/develop/concepts/architecture/session-state):

  ```python
  # page1.py
  import streamlit as st
  if "shared" not in st.session_state:
     st.session_state["shared"] = True

  # page2.py
  import streamlit as st
  st.write(st.session_state["shared"]) # If page1 already executed, this writes True
  ```

You now have a solid understanding of multipage apps. You've learned how to structure apps, define pages, and navigate between pages in the user interface. It's time to [create your first multipage app](/get-started/tutorials/create-a-multipage-app)! 🥳
