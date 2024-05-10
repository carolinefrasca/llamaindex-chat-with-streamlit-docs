---
title: st.write and magic commands
slug: /develop/api-reference/write-magic
---

# st.write and magic commands

Streamlit has two easy ways to display information into your app, which should typically be the
first thing you try: `st.write` and magic.

<TileContainer>
<RefCard href="/develop/api-reference/write-magic/st.write">

<h4>st.write</h4>

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">

<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/magic">

<h4>Magic</h4>

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>
