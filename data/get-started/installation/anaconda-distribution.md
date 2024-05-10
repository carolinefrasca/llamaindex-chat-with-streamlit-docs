---
title: Install Streamlit using Anaconda Distribution
slug: /get-started/installation/anaconda-distribution
---

# Install Streamlit using Anaconda Distribution

This page walks you through installing Streamlit locally using Anaconda Distribution. At the end, you'll build a simple "Hello world" app and run it. You can read more about [Getting started with Anaconda Distribution](https://docs.anaconda.com/free/anaconda/getting-started/) in Anaconda's docs. If you prefer to manage your Python environments via command line, check out how to [Install Streamlit using command line](/get-started/installation/command-line).

## Prerequisites

1. **A code editor**

   Anaconda Distribution includes Python and basically everything you need to get started.
   The only thing left for you to choose is a code editor.

   Our favorite editor is [VS Code](https://code.visualstudio.com/download), which is also what we
   use in all our tutorials.

1. **Knowledge about environment managers**

   Environment managers create virtual environments to isolate Python package installations between
   projects. For a detailed introduction to Python environments, check out
   [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

   But don't worry! In this guide we'll teach you how to install and use an environment manager
   (Anaconda).

## Install Anaconda Distribution

1. Go to [anaconda.com/download](https://www.anaconda.com/download).

2. Install Anaconda Distribution for your OS.

## Create an environment using Anaconda Navigator

3. Open Anaconda Navigator (the graphical interface included with Anaconda Distribution).

4. You can decline signing in to Anaconda if prompted.

5. In the left menu, click "**Environments**".
   ![Open your environments list in Anaconda Navigator](/images/get-started/Anaconda-Navigator-environment-1.png)

6. At the bottom of your environments list, click "**Create**".
   ![Click "Create" to open the Create new environment dialog](/images/get-started/Anaconda-Navigator-environment-2-create.png)

7. Enter "streamlitenv" for the name of your environment.

8. Click "**Create**."
<div style={{ maxWidth: '50%', margin: 'auto' }}>
    <Image alt="Finalize your new conda environment" src="/images/get-started/Anaconda-Navigator-environment-3-name.png" />
</div>

## Activate your environment

9. Click the green play icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>play_circle</i>) next to your environment.

10. Click "**Open Terminal**."
    ![Open a new terminal with your environment activated](/images/get-started/Anaconda-Navigator-environment-6-activate.png)

11. A terminal will open with your environment activated. Your environment's name will appear in parentheses at the beginning of your terminal's prompt to show that it's activated.

## Install Streamlit in your environment

12. In your terminal, type:

    ```bash
    pip install streamlit
    ```

13. To validate your installation, enter:

    ```bash
    streamlit hello
    ```

    If this doesn't work, use the long-form command:

    ```bash
    python -m streamlit hello
    ```

14. The Streamlit Hello example app will automatically open in your browser. If it doesn't, open your browser and go to the localhost address indicated in your terminal, typically `http://localhost:8501`. Play around with the app!

15. Close your terminal.

## Create a `Hello World` app and run it

17. Open VS Code with a new project.

18. Create a Python file named `app.py` in your project folder.
    ![Create a new file called app.py](/images/get-started/hello-world-1-new-file.png)

19. Copy the following code into `app.py` and save it.

    ```python
    import streamlit as st

    st.write("Hello World")
    ```

20. Click your Python interpreter in the lower-right corner, then choose your `streamlitenv` environment from the drop-down.
    ![Set your Python interpreter to your `streamlitenv` environment](/images/get-started/hello-world-3-change-interpreter.png)

21. Right-click `app.py` in your file navigation and click "**Open in integrated terminal**".
    ![Open your terminal in your project folder](/images/get-started/hello-world-4-open-terminal.png)

22. A terminal will open with your environment activated. Confirm this by looking for "(streamlitenv)" at the beginning of your next prompt.
    If it is not there, manually activate your environment with the command:

    ```bash
    conda activate streamlitenv
    ```

23. In your terminal, type:

    ```bash
    streamlit run app.py
    ```

    If this doesn't work, use the long-form command:

    ```bash
    python -m streamlit run app.py
    ```

    ![Start your Streamlit app with `streamlit run app.py`](/images/get-started/hello-world-5-streamlit-run.png)

24. Your app will automatically open in your browser. If it doesn't for any reason, open your browser and go to the localhost address indicated in your terminal, typically `http://localhost:8501`.

25. Change `st.write` to `st.title` and save your file:

    ```python
    import streamlit as st

    st.title("Hello World")
    ```

26. In your browser, click "**Always rerun**" to instantly rerun your app whenever you save a change to your file.
    ![Automatically rerun your app when your source file changes](/images/get-started/hello-world-6-always-rerun.png)

27. Your app will update! Keep making changes and you will see your changes as soon as you save your file.
    ![Your app updates when you resave your source file](/images/get-started/hello-world-7-updated-app.png)

28. When you're done, you can stop your app with `Ctrl+C` in your terminal or just by closing your terminal.

## What's next?

Read about our [Basic concepts](/get-started/fundamentals/main-concepts) and try out more commands in your app.
