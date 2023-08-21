---
title: Multipage apps
slug: /library/get-started/multipage-apps
---

# Multipage apps

As apps grow large, it becomes useful to organize them into multiple pages. This makes the app easier to manage as a developer and easier to navigate as a user. Streamlit provides a frictionless way to create multipage apps. Pages are automatically shown in a nice navigation widget inside the app sidebar, and clicking on a page will navigate to the page without reloading the frontend — making app browsing incredibly fast!

We created a "single-page app" to explore a public Uber dataset for pickups and drop-offs in New York City on the [previous page](/library/get-started/create-an-app). In this guide, let’s learn how to create multipage apps. Once we have a solid foundation on what it takes to create multipage apps, let’s build one for ourselves in the [next section](/library/get-started/multipage-apps/create-a-multipage-app)!

## Structuring multipage apps

Let's understand what it takes to create multipage apps — including how to define pages, structure and run multipage apps, and navigate between pages in the user interface. Once you've understood the basics, you can jump right into the [next section](/library/get-started/multipage-apps/create-a-multipage-app) to convert the familiar `streamlit hello` command into a multipage app!

## Run a multipage app

Running a multipage app is identical to running a single-page app. The command to run a multipage app is:

```python
streamlit run [entrypoint file]
```

The "entrypoint file" is the first page the app will show to the user. Once you have added pages to your app, the entrypoint file appears as the top-most page in the sidebar. You can think of the entrypoint file as your app's "main page". For example, say your entrypoint file is `Home.py`. Then, to run your app, you can run `streamlit run Home.py`. This will start your app and execute the code in `Home.py`.

## Adding pages

Once you've created your entrypoint file, you can add pages by creating `.py` files in a `pages/` directory relative to your entrypoint file. For example, if your entrypoint file is `Home.py`, then you can create a `pages/About.py` file to define the "About" page. Here's a valid directory structure for a multipage app:

```
Home.py # This is the file you run with "streamlit run"
└─── pages/
  └─── About.py # This is a page
  └─── 2_Page_two.py # This is another page
  └─── 3_😎_three.py # So is this
```

<Tip>

When adding emojis to filenames, it’s best practice to include a numbered-prefix to make autocompletion in your terminal easier. Terminal-autocomplete can get confused by unicode (which is how emojis are represented).

</Tip>

Pages are defined as `.py` files in a `pages/` directory. The filenames of pages are transformed to page names in the sidebar based on the the rules in the [section below](#how-pages-are-labeled-and-sorted-in-the-ui). For example, the `About.py` file will appear as "About" in the sidebar, `2_Page_two.py` appears as "Page two", and `3_😎_three.py` appears as “😎 three":

![Directory structure](/images/mpa-add-pages.png)

Only `.py` files in the `pages/` directory will be loaded as pages. Streamlit ignores all other files in the `pages/` directory and subdirectories.

## How pages are labeled and sorted in the UI

Page labels in the sidebar UI are generated from filenames. They may differ from the page title set in [`st.set_page_config`](/library/api-reference/utilities/st.set_page_config). Let's learn what constitutes a valid filename for a page, how pages are displayed in the sidebar, and how pages are sorted.

### Valid filenames for pages

Filenames are composed of four different parts:

1. A `number` — if the file is prefixed with a number.
2. A separator — could be `_`, `-`, space, or any combination thereof.
3. A `label` — which is everything up to, but not including, `.py`.
4. The extension — which is always `.py`.

### How pages are displayed in the sidebar

What is displayed in the sidebar is the `label` part of the filename:

- If there's no `label`, Streamlit uses the `number` as the label.
- In the UI, Streamlit beautifies the `label` by replacing `_` with space.

### How pages are sorted in the sidebar

Sorting considers numbers in the filename to be actual numbers (_integers_):

- Files that have a `number` appear before files without a `number`.
- Files are sorted based on the `number` (if any), followed by the `title` (if any).
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

Emojis can be used to make your page names more fun! For example, a file named `🏠_Home.py` will create a page titled "🏠 Home" in the sidebar.

</Tip>

## Navigating between pages

Pages are automatically shown in a nice navigation UI inside the app's sidebar. When you click on a page in the sidebar UI, Streamlit navigates to that page without reloading the entire frontend — making app browsing incredibly fast!

You can also navigate between pages using URLs. Pages have their own URLs, defined by the file's `label`. When multiple files have the same `label`, Streamlit picks the first one (based on the ordering [described above](/library/get-started/multipage-apps#how-pages-are-sorted-in-the-sidebar)). Users can view a specific page by visiting the page's URL.

If a user tries to access a URL for a page that does not exist, they will see a modal like the one below, saying the user has requested a page that was not found in the app’s pages/ directory.

<Image src="/images/mpa-page-not-found.png" />

## Notes

- Pages support [magic commands](https://docs.streamlit.io/library/api-reference/write-magic/magic).
- Pages support run-on-save. Additionally, when you save a page, this causes a rerun for users currently viewing that exact page.
- Adding or deleting a page causes the UI to update immediately.
- Updating pages in the sidebar does not rerun the script.
- `st.set_page_config` works at the page level. When you set a title or favicon using [st.set_page_config](/library/api-reference/utilities/st.set_page_config), this applies to the current page only.
- Pages share the same Python modules globally:

  ```python
  # page1.py
  import foo
  foo.hello = 123

  # page2.py
  import foo
  st.write(foo.hello)  # If page1 already executed, this should write 123
  ```

- Pages share the same [st.session_state](https://docs.streamlit.io/library/advanced-features/session-state):

  ```python
  # page1.py
  import streamlit as st
  if "shared" not in st.session_state:
     st.session_state["shared"] = True

  # page2.py
  import streamlit as st
  st.write(st.session_state["shared"])
  # If page1 already executed, this should write True
  ```

You now have a solid understanding of multipage apps. You've learned how to structure apps, define pages, and navigate between pages in the user interface. It's time to [create your first multipage app](/library/get-started/multipage-apps/create-a-multipage-app)! 🥳
