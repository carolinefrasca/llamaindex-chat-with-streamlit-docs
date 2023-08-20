---
title: Display progress and status
slug: /library/api-reference/status
---

# Display progress and status

Streamlit provides a few methods that allow you to add animation to your
apps. These animations include progress bars, status messages (like
warnings), and celebratory balloons.

<TileContainer>
<RefCard href="/library/api-reference/status/st.progress">

<Image pure alt="screenshot" src="/images/api/progress.jpg" />

#### Progress bar

Display a progress bar.

```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.spinner">

<Image pure alt="screenshot" src="/images/api/spinner.jpg" />

#### Spinner

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.toast">

<Image pure alt="screenshot" src="/images/api/toast.jpg" />

#### Toast

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```

</RefCard>
<RefCard href="/library/api-reference/status/st.balloons">

<Image pure alt="screenshot" src="/images/api/balloons.jpg" />

#### Balloons

Display celebratory balloons!

```python
st.balloons()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.snow">

<Image pure alt="screenshot" src="/images/api/snow.jpg" />

#### Snowflakes

Display celebratory snowflakes!

```python
st.snow()
```

</RefCard>
<RefCard href="/library/api-reference/status/st.error">

<Image pure alt="screenshot" src="/images/api/error.jpg" />

#### Error box

Display error message.

```python
st.error("We encountered an error")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.warning">

<Image pure alt="screenshot" src="/images/api/warning.jpg" />

#### Warning box

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.info">

<Image pure alt="screenshot" src="/images/api/info.jpg" />

#### Info box

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.success">

<Image pure alt="screenshot" src="/images/api/success.jpg" />

#### Success box

Display a success message.

```python
st.success("Match found!")
```

</RefCard>
<RefCard href="/library/api-reference/status/st.exception">

<Image pure alt="screenshot" src="/images/api/exception.jpg" />

#### Exception output

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

#### Stqdm

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/Socvest/streamlit-custom-notification-box">

<Image pure alt="screenshot" src="/images/api/components/custom-notification-box.jpg" />

#### Custom notification box

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-emojis.jpg" />

#### Streamlit Extras

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(emoji="🎈", font_size=54,
  falling_speed=5, animation_length="infinite",)
```

</ComponentCard>

</ComponentSlider>
