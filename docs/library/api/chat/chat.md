---
title: Chat elements
slug: /library/api-reference/chat
---

# Chat elements

Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. `st.chat_input` lets you display a chat input widget so the user can type in a message.

<TileContainer>
<RefCard href="/library/api-reference/chat/st.chat_message">

<Image pure alt="screenshot" src="/images/api/chat_message.jpg" />

#### Chat message

Insert a chat message container.

```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

</RefCard>
<RefCard href="/library/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

#### Chat input

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>
</TileContainer>
