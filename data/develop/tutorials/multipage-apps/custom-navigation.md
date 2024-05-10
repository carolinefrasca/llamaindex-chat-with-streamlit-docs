---
title: Build a custom navigation menu with `st.page_link`
slug: /develop/tutorials/multipage/st.page_link-nav
description: Streamlit makes it easy to build a custom navigation menu in your multipage app.
---

# Build a custom navigation menu with `st.page_link`

Streamlit lets you build custom navigation menus and elements with `st.page_link`. Introduced in Streamlit version 1.31.0, `st.page_link` can link to other pages in your multipage app or to external sites. When linked to another page in your app, `st.page_link` will show a highlight effect to indicate the current page. When combined with the [`client.showSidebarNavigation`](/develop/concepts/configuration#client) configuration option, you can build sleek, dynamic navigation in your app.

## Prerequisites

Create a new working directory in your development environment. We'll call this directory `your-repository`.

## Summary

In this example, we'll build a dynamic navigation menu for a multipage app that depends on the current user's role. We've abstracted away the use of username and creditials to simplify the example. Instead, we'll use a selectbox on the main page of the app to switch between roles. Session State will carry this selection between pages. The app will have a main page (`app.py`) which serves as the abstracted log-in page. There will be three additional pages which will be hidden or accessible, depending on the current role. The file structure will be as follows:

```
your-repository/
├── .streamlit/
│   └── config.toml
├── pages/
│   ├── admin.py
│   ├── super-admin.py
│   └── user.py
├── menu.py
└── app.py
```

Here's a look at what we'll build:

<Cloud src="https://doc-custom-navigation.streamlit.app/?embed=true" height="400" />

## Build the example

### Hide the default sidebar navigation

When creating a custom navigation menu, you need to hide the default sidebar navigation using `client.showSidebarNavigation`. Add the following `.streamlit/config.toml` file to your working directory:

```toml
[client]
showSidebarNavigation = false
```

### Create a menu function

You can write different menu logic for different pages or you can create a single menu function to call on multiple pages. In this example, we'll use the same menu logic on all pages, including a redirect to the main page when a user isn't logged in. We'll build a few helper functions to do this.

- `menu_with_redirect()` checks if a user is logged in, then either redirects them to the main page or renders the menu.
- `menu()` will call the correct helper function to render the menu based on whether the user is logged in or not.
- `authenticated_menu()` will display a menu based on an authenticated user's role.
- `unauthenticated_menu()` will display a menu for unauthenticated users.

We'll call `menu()` on the main page and call `menu_with_redirect()` on the other pages. `st.session_state.role` will store the current selected role. If this value does not exist or is set to `None`, then the user is not logged in. Otherwise, it will hold the user's role as a string: `"user"`, `"admin"`, or `"super-admin"`.

Add the following `menu.py` file to your working directory. (We'll describe the functions in more detail below.)

```python
import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
```

Let's take a closer look at `authenticated_menu()`. When this function is called, `st.session_state.role` exists and has a value other than `None`.

```python
def authenticated_menu():
    # Show a navigation menu for authenticated users
```

The first two pages in the navigation menu are available to all users. Since we know a user is logged in when this function is called, we'll use the label "Switch accounts" for the main page. (If you don't use the `label` parameter, the page name will be derived from the file name like it is with the default sidebar navigation.)

```python
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
```

We only want to show the next two pages to admins. Furthermore, we've chosen to disable&mdash;but not hide&mdash;the super-admin page when the admin user is not a super-admin. We do this using the `disabled` parameter. (`disabled=True` when the role is not `"super-admin"`.)

```
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )
```

It's that simple! `unauthenticated_menu()` will only show a link to the main page of the app with the label "Log in." `menu()` does a simple inspection of `st.session_state.role` to switch between the two menu-rendering functions. Finally, `menu_with_redirect()` extends `menu()` to redirect users to `app.py` if they aren't logged in.

<Tip>

If you want to include emojis in your page labels, you can use the `icon` parameter. There's no need to include emojis in your file name or the `label` parameter.

</Tip>

### Create the main file of your app

The main `app.py` file will serve as a pseudo-login page. The user can choose a role from the `st.selectbox` widget. A few bits of logic will save that role into Session State to preserve it while navigating between pages&mdash;even when returning to `app.py`.

Add the following `app.py` file to your working directory:

```python
import streamlit as st
from menu import menu

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)
menu() # Render the dynamic menu!
```

### Add other pages to your app

Add the following `pages/user.py` file:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("This page is available to all users")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

Session State resets if a user manually navigates to a page by URL. Therefore, if a user tries to access an admin page in this example, Session State will be cleared, and they will be redirected to the main page as an unauthenicated user. However, it's still good practice to include a check of the role at the top of each restricted page. You can use `st.stop` to halt an app if a role is not whitelisted.

`pages/admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to all admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

`pages/super-admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to super-admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

As noted above, the redirect in `menu_with_redirect()` will prevent a user from ever seeing the warning messages on the admin pages. If you want to see the warning, just add another `st.page_link("pages/admin.py")` button at the bottom of `app.py` so you can navigate to the admin page after selecting the "user" role. 😉
