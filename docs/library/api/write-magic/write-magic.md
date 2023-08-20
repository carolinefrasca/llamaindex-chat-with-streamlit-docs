---
title: st.write and magic commands
slug: /library/api-reference/write-magic
---

# st.write and magic commands

Streamlit has two easy ways to display information into your app, which should typically be the
first thing you try: `st.write` and magic.

<TileContainer>
<RefCard href="/library/api-reference/write-magic/st.write">

#### st.write

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/library/api-reference/write-magic/magic">

#### Magic

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>
