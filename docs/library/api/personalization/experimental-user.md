---
title: st.experimental_user
slug: /library/api-reference/personalization/st.experimental_user
description: st.experimental_user returns information about the logged-in user of private apps on Streamlit Community Cloud.
---

# st.experimental_user

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/library/advanced-features/prerelease#experimental-features).

</Important>

`st.experimental_user` is a Streamlit command that returns information about the logged-in user on Streamlit Community Cloud. It allows developers to personalize apps for the user viewing the app. In a private Streamlit Community Cloud app, it returns a dictionary with the viewer's email. This value of this field is empty in a public Streamlit Community Cloud app to prevent leaking user emails to developers.

The API closely resembles that of [`st.session_state`](/library/api-reference/session-state) and [`st.secrets`](/streamlit-community-cloud/deploy-your-app/secrets-management). It follows a field-based API, which is very similar to Python dictionaries.

### Allowed fields

The `st.experimental_user` command returns a dictionary with only one field: `email`.

Display the allowed field by passing the command to `st.write`:

```python
# Display the contents of the dictionary
st.write(st.experimental_user)
```

The above displays a dict with one field and value. The field is always `email`:

```json
{
  "email": "value"
}
```

You can check if a field exists in `st.experimental_user`:

```python
# Returns True if the field exists
"email" in st.experimental_user

# Returns False if the field does not exist
"name" in st.experimental_user
```

### Read values

Read the value of the `email` field and display it by passing to `st.write`:

```python
# Dictionary like API
st.write(st.experimental_user['email'])

# Attribute API
st.write(st.experimental_user.email)
```

The above outputs either `None` or the logged-in user's email or test@localhost.com, depending on where the app is running. Read further to learn about `st.experimental_user`'s context-dependent behavior.

### Updates and modifications

Keys and values for `st.experimental_user` **cannot** be updated or modified. Streamlit throws a handy `StreamlitAPIException` exception if you try to update them:

```python
st.experimental_user.name = None
# Throws an exception!

st.experimental_user.email = "hello"
# Throws an exception!
```

<Image src="/images/st-user-value-exception.png" />

### Context-dependent behavior

The value of `st.experimental_user.email` is context-dependent. It returns a value depending on where the app is running. The [private](#private-app-on-streamlit-cloud) or [public](#public-app-on-streamlit-cloud) app can be running on Streamlit Community Cloud, [locally](#local-development), or on a [3rd party cloud provider](#app-deployed-on-a-3rd-party-cloud-provider). Let's look at the different scenarios.

#### **Private app on Streamlit Community Cloud**

Users need to be logged in to Streamlit Community Cloud to view private apps. If a user is not logged, they see:

<div style={{ maxWidth: '65%', marginBottom: '-1em', marginLeft: '8em' }}>
    <Image src="/images/private-app-access.png" />
</div>

If a user is logged in, `st.experimental_user.email` returns the user's email. Suppose a user logged in to Streamlit Community Cloud using jane@email.com:

```python
st.experimental_user.email
# Returns: jane@email.com
```

#### **Public app on Streamlit Community Cloud**

Currently, `st.experimental_user.email` returns information about the logged-in user of _private apps_ on Streamlit Community Cloud. If used in a public app, it returns `None`. For example:

```python
st.experimental_user.email
# Returns: None
```

This value of this field is empty in a public Streamlit Community Cloud app to prevent leaking user emails to developers.

#### **Local development**

When developing locally, `st.experimental_user.email` returns test@localhost.com. We don't return `None` to make it easier to locally test this functionality. For example:

```python
st.experimental_user.email
# Returns: test@localhost.com
```

#### **App deployed on a 3rd party cloud provider**

When deploying an app on a 3rd party cloud provider (e.g. Amazon EC2, Heroku, etc), `st.experimental_user.email` behaves the same as during local development. For example:

```python
st.experimental_user.email # On a 3rd party cloud provider
# Returns: test@localhost.com
```

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

### Caveats and limitations

- `st.experimental_user` is **read-only**. You cannot update or modify its value. Doing so will throw a `StreamlitAPIException`.
- A valid email is returned only if the user is logged in to Streamlit Community Cloud and the app is private. Else, `None` or test@localhost.com is returned.
- This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/library/advanced-features/prerelease#experimental-features).
