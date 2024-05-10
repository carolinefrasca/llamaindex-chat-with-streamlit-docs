---
title: st.experimental_user
slug: /develop/api-reference/utilities/st.experimental_user
description: st.experimental_user returns information about the logged-in user of private apps on Streamlit Community Cloud.
---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>

<Autofunction function="streamlit.experimental_user" />

### Examples

The ability to personalize apps for the user viewing the app is a great way to make your app more engaging.

It unlocks a plethora of use-cases for developers, some of which could include: showing additional controls for admins, visualizing a user's Streamlit history, a personalized stock ticker, a chatbot app, and much more. We're excited to see what you build with this feature!

Here's a code snippet that shows extra buttons for admins:

```python
# Show extra buttons for admin users.
ADMIN_USERS = {
    'person1@email.com',
    'person2@email.com',
    'person3@email.com'
}
if st.experimental_user.email in ADMIN_USERS:
    display_the_extra_admin_buttons()
display_the_interface_everyone_sees()
```

Show different content to users based on their email address:

```python
# Show different content based on the user's email address.
if st.experimental_user.email == 'jane@email.com':
    display_jane_content()
elif st.experimental_user.email == 'adam@foocorp.io':
    display_adam_content()
else:
    st.write("Please contact us to get access!")
```

Greet users with their name that's stored in a database:

```python
# Greet the user by their name.
if st.experimental_user.email:
    # Get the user's name from the database.
    name = get_name_from_db(st.experimental_user.email)
    st.write('Hello, %s!' % name)
```

<Autofunction function="streamlit.experimental_user.to_dict" />
