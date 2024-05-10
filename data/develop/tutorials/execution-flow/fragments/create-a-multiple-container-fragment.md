---
title: Create a fragment across multiple containers
slug: /develop/tutorials/execution-flow/create-a-multiple-container-fragment
---

# Create a fragment across multiple containers

Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. If your fragment doesn't write to outside containers, Streamlit will clear and redraw all the fragment elements with each fragment rerun. However, if your fragment _does_ write elements to outside containers, Streamlit will not clear those elements during a fragment rerun. Instead, those elements accumulate with each fragment rerun until the next full-script rerun. If you want a fragment to update multiple containers in your app, use [`st.empty()`](/develop/api-reference/layout/st.empty) containers to prevent accumulating elements.

## Applied concepts

- Use fragments to run two independent processes separately.
- Distribute a fragment across multiple containers.

## Prerequisites

**`streamlit>=1.33.0`**

- This tutorial uses fragments, which require Streamlit version 1.33.0 or later.
- This tutorial assumes you have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.empty()`.

## Summary

In this toy example, you'll build an app with six containers. Three containers will have orange cats. The other three containers will have black cats. You'll have three buttons in the sidebar: "**Herd the black cats**," "**Herd the orange cats**," and "**Herd all the cats**." Since herding cats is slow, you'll use fragments to help Streamlit run the associated processes efficiently. You'll create two fragments, one for the black cats and one for the orange cats. Since the buttons will be in the sidebar and the fragments will update containers in the main body, you'll use a trick with `st.empty()` to ensure you don't end up with too many cats in your app (if it's even possible to have too many cats). 😻

Here's a look at what you'll build:

<Collapse title="Complete code" expanded={false}>

```python
import streamlit as st
import time

st.title("Cats!")

row1 = st.columns(3)
row2 = st.columns(3)

grid = [col.container(height=200) for col in row1 + row2]
safe_grid = [card.empty() for card in grid]


def black_cats():
    time.sleep(1)
    st.title("🐈‍⬛ 🐈‍⬛")
    st.markdown("🐾 🐾 🐾 🐾")


def orange_cats():
    time.sleep(1)
    st.title("🐈 🐈")
    st.markdown("🐾 🐾 🐾 🐾")


@st.experimental_fragment
def herd_black_cats(card_a, card_b, card_c):
    st.button("Herd the black cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()


@st.experimental_fragment
def herd_orange_cats(card_a, card_b, card_c):
    st.button("Herd the orange cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()


with st.sidebar:
    herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
    herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
    st.button("Herd all the cats")
```

</Collapse>

<Cloud src="https://doc-tutorial-fragment-multiple-container.streamlit.app/?embed=true" height="650" />

## Build the example

### Initialize your app

1. In `your_repository`, create a file named `app.py`.
1. In a terminal, change directories to `your_repository` and start your app.

   ```bash
   streamlit run app.py
   ```

   Your app will be blank since you still need to add code.

1. In `app.py`, write the following:

   ```python
   import streamlit as st
   import time
   ```

   You'll use `time.sleep()` to slow things down and see the fragments working.

1. Save your `app.py` file and view your running app.
1. Click "**Always rerun**" or hit your "**A**" key in your running app.

   Your running preview will automatically update as you save changes to `app.py`. Your preview will still be blank. Return to your code.

### Frame out your app's containers

1. Add a title to your app and two rows of three containers.

   ```python
   st.title("Cats!")

   row1 = st.columns(3)
   row2 = st.columns(3)

   grid = [col.container(height=200) for col in row1 + row2]
   ```

   Save your file to see your updated preview.

1. Define a helper function to draw two black cats.

   ```python
   def black_cats():
       time.sleep(1)
       st.title("🐈‍⬛ 🐈‍⬛")
   st.markdown("🐾 🐾 🐾 🐾")
   ```

   This function represents "herding two cats" and uses `time.sleep()` to simulate a slower process. You will use this to draw two cats in one of your grid cards later on.

1. Define another helper function to draw two orange cats.

   ```python
   def orange_cats():
       time.sleep(1)
       st.title("🐈 🐈")
   st.markdown("🐾 🐾 🐾 🐾")
   ```

1. (Optional) Test out your functions by calling each one within a grid card.

   ```python
   with grid[0]:
       black_cats()
   with grid[1]:
       orange_cats()
   ```

   Save your `app.py` file to see the preview. Delete these four lines when finished.

### Define your fragments

Since each fragment will span across the sidebar and three additional containers, you'll use the sidebar to hold the main body of the fragment and pass the three containers as function arguments.

1. Use an [`@st.experimental_fragment`](/develop/api-reference/execution-flow/st.fragment) decorator and start your black-cat fragment definition.

   ```python
   @st.experimental_fragment
   def herd_black_cats(card_a, card_b, card_c):
   ```

1. Add a button for rerunning this fragment.

   ```python
       st.button("Herd the black cats")
   ```

1. Write to each container using your helper function.

   ```python
       with card_a:
           black_cats()
       with card_b:
           black_cats()
       with card_c:
           black_cats()
   ```

   **This code above will not behave as desired, but you'll explore and correct this in the following steps.**

1. Test out your code. Call your fragment function in the sidebar.

   ```python
   with st.sidebar:
       herd_black_cats(grid[0], grid[2], grid[4])
   ```

   Save your file and try using the button in the sidebar. More and more cats are appear in the cards with each fragment rerun! This is the expected behavior when fragments write to outside containers. To fix this, you will pass `st.empty()` containers to your fragment function.

   ![Example Streamlit app showing accumulating elements when a fragment writes to outside containers](/images/tutorials/fragment-multiple-containers-tutorial-app-duplicates.jpg)

1. Delete the lines of code from the previous two steps.

1. To prepare for using `st.empty()` containers, correct your cat-herding function as follows. After the button, define containers to place in the `st.empty()` cards you'll pass to your fragment.

   ```python
       container_a = card_a.container()
       container_b = card_b.container()
       container_c = card_c.container()
       with container_a:
           black_cats()
       with container_b:
           black_cats()
       with container_c:
           black_cats()
   ```

   In this new version, `card_a`, `card_b`, and `card_c` will be `st.empty()` containers. You create `container_a`, `container_b`, and `container_c` to allow Streamlit to draw multiple elements on each grid card.

1. Similarly define your orange-cat fragment function.

   ```python
   @st.experimental_fragment
   def herd_orange_cats(card_a, card_b, card_c):
       st.button("Herd the orange cats")
       container_a = card_a.container()
       container_b = card_b.container()
       container_c = card_c.container()
       with container_a:
           orange_cats()
       with container_b:
           orange_cats()
       with container_c:
           orange_cats()
   ```

### Put the functions together together to create an app

1. Call both of your fragments in the sidebar.

   ```python
   with st.sidebar:
       herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
       herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
   ```

   By creating `st.empty()` containers in each card and passing them to your fragments, you prevent elements from accumulating in the cards with each fragment rerun. If you create the `st.empty()` containers earlier in your app, full-script reruns will clear the orange-cat cards while (first) rendering the black-cat cards.

1. Include a button outside of your fragments. When clicked, the button will trigger a full-script rerun since you're calling its widget function outside of any fragment.

   ```python
       st.button("Herd all the cats")
   ```

1. Save your file and try out the app! When you click "**Herd the black cats**" or "**Herd the orange cats**," Streamlit will only redraw the three related cards. When you click "**Herd all the cats**," Streamlit redraws all six cards.
