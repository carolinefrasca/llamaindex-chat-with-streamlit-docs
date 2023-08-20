---
title: Components
slug: /library/components
---

# Custom Components

Components are third-party Python modules that extend what's possible with Streamlit.

## How to use a Component

Components are super easy to use:

1. Start by finding the Component you'd like to use. Two great resources for this are:

   - The [Component gallery](https://streamlit.io/components)
   - [This thread](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634),
     by Fanilo A. from our forums.

2. Install the Component using your favorite Python package manager. This step and all following
   steps are described in your component's instructions.

   For example, to use the fantastic [AgGrid
   Component](https://github.com/PablocFonseca/streamlit-aggrid), you first install it with:

   ```python
   pip install streamlit-aggrid
   ```

3. In your Python code, import the Component as described in its instructions. For AgGrid, this step
   is:

   ```python
   from st_aggrid import AgGrid
   ```

4. ...now you're ready to use it! For AgGrid, that's:

   ```python
   AgGrid(my_dataframe)
   ```

## Making your own Component

If you're interested in making your own component, check out the following resources:

- [Create a Component](/library/components/create)
- [Publish a Component](/library/components/publish)
- [Components API](/library/components/components-api)
- [Blog post for when we launched Components!](https://blog.streamlit.io/introducing-streamlit-components/)

Alternatively, if you prefer to learn using videos, our engineer Tim Conkling has put together some
amazing tutorials:

##### Video tutorial, part 1

<YouTube videoId="BuD3gILJW-Q" />

##### Video tutorial, part 2

<YouTube videoId="QjccJl_7Jco" />
