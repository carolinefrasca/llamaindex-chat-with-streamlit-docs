---
title: Button behavior and examples
slug: /library/advanced-features/button-behavior-and-examples
---

# Button behavior and examples

## Summary

Buttons created with [`st.button`](/library/api-reference/widgets/st.button) do not retain state. They return `True` on the script rerun resulting from their click and immediately return to `False` on the next script rerun. If a displayed element is nested inside `if st.button('Click me'):`, the element will be visible when the button is clicked and disappear as soon as the user takes their next action. This is because the script reruns and the button return value becomes `False`.

In this guide, we will illustrate the use of buttons and explain common misconceptions. Read on to see a variety of examples that expand on `st.button` using [`st.session_state`](/library/api-reference/session-state). [Anti-patterns](#anti-patterns) are included at the end. Go ahead and pull up your favorite code editor so you can `streamlit run` the examples as you read. Check out Streamlit's [Main concepts](/library/get-started/main-concepts) if you haven't run your own Streamlit scripts yet.

## When to use `if st.button()`

When code is conditioned on a button's value, it will execute once in response to the button being clicked and not again (until the button is clicked again).

Good to nest inside buttons:

- Transient messages that immediately disappear.
- Once-per-click processes that saves data to session state, a file, or
  a database.

Bad to nest inside buttons:

- Displayed items that should persist as the user continues.
- Other widgets which cause the script to rerun when used.
- Processes that neither modify session state nor write to a file/database.\*

\* This can be appropriate when disposable results are desired. If you
have a "Validate" button, that could be a process conditioned directly on a
button. It could be used to create an alert to say 'Valid' or 'Invalid' with no
need to keep that info.

## Common logic with buttons

### Show a temporary message with a button

If you want to give the user a quick button to check if an entry is valid, but not keep that check displayed as the user continues.

In this example, a user can click a button to check if their `animal` string is in the `animal_shelter` list. When the user clicks "**Check availability**" they will see "We have that animal!" or "We don't have that animal." If they change the animal in [`st.text_input`](/library/api-reference/widgets/st.text_input), the script reruns and the message disappears until they click "**Check availability**" again.

```python
import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'
```

Note: The above example uses [magic](/library/api-reference/write-magic/magic) to render the message on the frontend.

### Stateful button

If you want a clicked button to continue to be `True`, create a value in `st.session_state` and use the button to set that value to `True` in a callback.

```python
import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')
```

### Toggle button

If you want a button to work like a toggle switch, consider using [`st.checkbox`](/library/api-reference/widgets/st.checkbox). Otherwise, you can use a button with a callback function to reverse a boolean value saved in `st.session_state`.

In this example, we use `st.button` to toggle another widget on and off. By displaying [`st.slider`](/library/api-reference/widgets/st.slider) conditionally on a value in `st.session_state`, the user can interact with the slider without it disappearing.

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')
```

Alternatively, you can use the value in `st.session_state` on the slider's `disabled` parameter.

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

st.slider('Select a value', disabled=st.session_state.button)
```

### Buttons to continue or control stages of a process

Another alternative to nesting content inside a button is to use a value in `st.session_state` that designates the "step" or "stage" of a process. In this example, we have four stages in our script:

0. Before the user begins.
1. User enters their name.
2. User chooses a color.
3. User gets a thank-you message.

A button at the beginning advances the stage from 0 to 1. A button at the end resets the stage from 3 to 0. The other widgets used in stage 1 and 2 have callbacks to set the stage. If you have a process with dependant steps and want to keep previous stages visible, such a callback forces a user to retrace subsequent stages if they change an earlier widget.

```python
import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    name = st.text_input('Name', on_change=set_state, args=[2])

if st.session_state.stage >= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write(f':{color}[Thank you!]')
    st.button('Start Over', on_click=set_state, args=[0])
```

### Buttons to modify `st.session_state`

If you modify `st.session_state` inside of a button, you must consider where that button is within the script.

#### A slight problem

In this example, we access `st.session_state.name` both before and after the buttons which modify it. When a button ("**Jane**" or "**John**") is clicked, the script reruns. The info displayed before the buttons lags behind the info written after the button. The data in `st.session_state` before the button is not updated. When the script executes the button function, that is when the conditional code to update `st.session_state` creates the change. Thus, this change is reflected after the button.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'

if st.button('John'):
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])
```

#### Logic used in a callback

Callbacks are a clean way to modify `st.session_state`. Callbacks are executed as a prefix to the script rerunning, so the position of the button relative to accessing data is not important.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

def change_name(name):
    st.session_state['name'] = name

st.header(st.session_state['name'])

st.button('Jane', on_click=change_name, args=['Jane Doe'])
st.button('John', on_click=change_name, args=['John Doe'])

st.header(st.session_state['name'])
```

#### Logic nested in a button with a rerun

Although callbacks are often preferred to avoid extra reruns, our first 'John Doe'/'Jane Doe' example can be modified by adding [`st.experimental_rerun`](/library/api-reference/control-flow/st.experimental_rerun) instead. If you need to acces data in `st.session_state` before the button that modifies it, you can include `st.experimental_rerun` to rerun the script after the change has been committed. This means the script will rerun twice when a button is clicked.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'
    st.experimental_rerun()

if st.button('John'):
    st.session_state['name'] = 'John Doe'
    st.experimental_rerun()

st.header(st.session_state['name'])
```

### Buttons to modify or reset other widgets

When a button is used to modify or reset another widget, it is the same as the above examples to modify `st.session_state`. However, an extra consideration exists: you cannot modify a key-value pair in `st.session_state` if the widget with that key has already been rendered on the page for the current script run.

<Important>

Don't do this!

```python
import streamlit as st

st.text_input('Name', key='name')

# These buttons will error because their nested code changes
# a widget's state after that widget within the script.
if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    set_name('Streamlit')
```

</Important>

#### Option 1: Use a key for the button and put the logic before the widget

If you assign a key to a button, you can condition code on a button's state by using its value in `st.session_state`. This means that logic depending on your button can be in your script before that button. In the following example, we use the `.get()` method on `st.session_state` because the keys for the buttons will not exist when the script runs for the first time. The `.get()` method will return `False` if it can't find the key. Otherwise, it will return the value of the key.

```python
import streamlit as st

# Use the get method since the keys won't be in session_state
# on the first script run
if st.session_state.get('clear'):
    st.session_state['name'] = ''
if st.session_state.get('streamlit'):
    st.session_state['name'] = 'Streamlit'

st.text_input('Name', key='name')

st.button('Clear name', key='clear')
st.button('Streamlit!', key='streamlit')
```

#### Option 2: Use a callback

```python
import streamlit as st

st.text_input('Name', key='name')

def set_name(name):
    st.session_state.name = name

st.button('Clear name', on_click=set_name, args=[''])
st.button('Streamlit!', on_click=set_name, args=['Streamlit'])
```

#### Option 3: Use containers

By using [`st.container`](/library/api-reference/layout/st.container) you can have widgets appear in different orders in your script and frontend view (webpage).

```python
import streamlit as st

begin = st.container()

if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    st.session_state.name = ('Streamlit')

# The widget is second in logic, but first in display
begin.text_input('Name', key='name')
```

### Buttons to add other widgets dynamically

When dynamically adding widgets to the page, make sure to use an index to keep the keys unique and avoid a `DuplicateWidgetID` error. In this example, we define a function `display_input_row` which renders a row of widgets. That function accepts an `index` as a parameter. The widgets rendered by `display_input_row` use `index` within their keys so that `dispaly_input_row` can be executed multiple times on a single script rerun without repeating any widget keys.

```python
import streamlit as st

def display_input_row(index):
    left, middle, right = st.columns(3)
    left.text_input('First', key=f'first_{index}')
    middle.text_input('Middle', key=f'middle_{index}')
    right.text_input('Last', key=f'last_{index}')

if 'rows' not in st.session_state:
    st.session_state['rows'] = 0

def increase_rows():
    st.session_state['rows'] += 1

st.button('Add person', on_click=increase_rows)

for i in range(st.session_state['rows']):
    display_input_row(i)

# Show the results
st.subheader('People')
for i in range(st.session_state['rows']):
    st.write(
        f'Person {i+1}:',
        st.session_state[f'first_{i}'],
        st.session_state[f'middle_{i}'],
        st.session_state[f'last_{i}']
    )
```

### Buttons to handle expensive or file-writing processes

When you have expensive processes, set them to run upon clicking a button and save the results into `st.session_state`. This allows you to keep accessing the results of the process without re-executing it unnecessarily. This is especially helpful for processes that save to disk or write to a database. In this example, we have an `expensive_process` that depends on two parameters: `option` and `add`. Functionally, `add` changes the output, but `option` does not&mdash;`option` is there to provide a parameter

```python
import streamlit as st
import pandas as pd
import time

def expensive_process(option, add):
    with st.spinner('Processing...'):
        time.sleep(5)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C':[7, 8, 9]}) + add
    return (df, add)

cols = st.columns(2)
option = cols[0].selectbox('Select a number', options=['1', '2', '3'])
add = cols[1].number_input('Add a number', min_value=0, max_value=10)

if 'processed' not in st.session_state:
    st.session_state.processed = {}

# Process and save results
if st.button('Process'):
    result = expensive_process(option, add)
    st.session_state.processed[option] = result

if option in st.session_state.processed:
    st.write(f'Option {option} processed with add {add}')
    st.write(st.session_state.processed[option][0])
```

Astute observers may think, "This feels a little like caching." We are only saving results relative to one parameter, but the pattern could easily be expanded to save results relative to both parameters. In that sense, yes, it has some similarities to caching, but also some important differences. When you save results in `st.session_state`, the results are only available to the current user in their current session. If you use [`st.cache_data`](/library/api-reference/performance/st.cache_data) instead, the results are available to all users across all sessions. Furthermore, if you want to update a saved result, you have to clear all saved results for that function to do so.

## Anti-patterns

Here are some simplified examples of how buttons can go wrong. Be on the lookout for these common mistakes.

### Buttons nested inside buttons

```python
import streamlit as st

if st.button('Button 1'):
    st.write('Button 1 was clicked')
    if st.button('Button 2'):
        # This will never be executed.
        st.write('Button 2 was clicked')
```

### Other widgets nested inside buttons

```python
import streamlit as st

if st.button('Sign up'):
    name = st.text_input('Name')

    if name:
        # This will never be executed.
        st.success(f'Welcome {name}')
```

### Nesting a process inside a button without saving to session state

```python
import streamlit as st
import pandas as pd

file = st.file_uploader("Upload a file", type="csv")

if st.button('Get data'):
    df = pd.read_csv(file)
    # This display will go away with the user's next action.
    st.write(df)

if st.button('Save'):
    # This will always error.
    df.to_csv('data.csv')
```
