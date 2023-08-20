---
title: st.camera_input
slug: /library/api-reference/widgets/st.camera_input
description: st.camera_input displays a widget to upload images from a camera
---

<Autofunction function="streamlit.camera_input" />

To read the image file buffer as bytes, you can use `getvalue()` on the `UploadedFile` object.

```python
import streamlit as st

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
```

<Important>

`st.camera_input` returns an object of the `UploadedFile` class, which a subclass of BytesIO. Therefore it is a "file-like" object. This means you can pass it anywhere where a file is expected, similar to `st.file_uploader`.

</Important>

## Image processing examples

You can use the output of `st.camera_input` for various downstream tasks, including image processing. Below, we demonstrate how to use the `st.camera_input` widget with popular image and data processing libraries such as [Pillow](https://pillow.readthedocs.io/en/stable/installation.html), [NumPy](https://numpy.org/), [OpenCV](https://pypi.org/project/opencv-python-headless/), [TensorFlow](https://www.tensorflow.org/), [torchvision](https://pytorch.org/vision/stable/index.html), and [PyTorch](https://pytorch.org/).

While we provide examples for the most popular use-cases and libraries, you are welcome to adapt these examples to your own needs and favorite libraries.

### Pillow (PIL) and NumPy

Ensure you have installed [Pillow](https://pillow.readthedocs.io/en/stable/installation.html) and [NumPy](https://numpy.org/).

To read the image file buffer as a PIL Image and convert it to a NumPy array:

```python
import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
```

### OpenCV (cv2)

Ensure you have installed [OpenCV](https://pypi.org/project/opencv-python-headless/) and [NumPy](https://numpy.org/).

To read the image file buffer with OpenCV:

```python
import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
```

### TensorFlow

Ensure you have installed [TensorFlow](https://www.tensorflow.org/install/).

To read the image file buffer as a 3 dimensional uint8 tensor with TensorFlow:

```python
import streamlit as st
import tensorflow as tf

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)
```

### Torchvision

Ensure you have installed [Torchvision](https://pypi.org/project/torchvision/) (it is not bundled with PyTorch) and [PyTorch](https://pytorch.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with `torchvision.io`:

```python
import streamlit as st
import torch
import torchvision

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with `torchvision.io`:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torchvision.io.decode_image(
        torch.frombuffer(bytes_data, dtype=torch.uint8)
    )

    # Check the type of torch_img:
    # Should output: <class 'torch.Tensor'>
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```

### PyTorch

Ensure you have installed [PyTorch](https://pytorch.org/) and [NumPy](https://numpy.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with PyTorch:

```python
import streamlit as st
import torch
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with PyTorch:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torch.ops.image.decode_image(
        torch.from_numpy(np.frombuffer(bytes_data, np.uint8)), 3
    )

    # Check the type of torch_img:
    # Should output: <class 'torch.Tensor'>
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```
