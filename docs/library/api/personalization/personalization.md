---
title: Personalize apps for the user
slug: /library/api-reference/personalization
---

# Personalize apps for the user

<TileContainer>
<RefCard href="/library/api-reference/personalization/st.experimental_user" size="two-third">

#### User info

`st.experimental_user` returns information about the logged-in user of private apps on Streamlit Community Cloud.

```python
if st.experimental_user.email == "foo@corp.com":
  st.write("Welcome back, ", st.experimental_user.email)
else:
  st.write("You are not authorized to view this page.")
```

</RefCard>
</TileContainer>
