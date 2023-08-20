---
title: Install the Snowflake Connector for Python on Streamlit Community Cloud
slug: /knowledge-base/dependencies/snowflake-connector-python-streamlit-cloud
---

# Install the Snowflake Connector for Python on Streamlit Community Cloud

The Snowflake Connector for Python is available on [PyPI](https://pypi.org/project/snowflake-connector-python/) and the installation instructions are found in the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/python-connector-install.html#step-1-install-the-connector). When installing the connector, Snowflake recommends installing specific versions of its dependent libraries. The steps below will help you install the connector and its dependencies on Streamlit Community Cloud:

1. Determine the version of the Snowflake Connector for Python you want to install.
2. Determine the version of Python you want to use on Streamlit Community Cloud.
3. To install the connector and the dependent libraries, select the [requirements file](https://github.com/snowflakedb/snowflake-connector-python/tree/main/tested_requirements) for that version of the connector and Python.
4. Add the raw GitHub URL of the requirements file to your `requirements.txt` file and prepend `-r` to the line.
   For example, if you want to install version `2.7.9` of the connector on Python 3.9, add the following line to your `requirements.txt` file:

   ```bash
   -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.7.9/tested_requirements/requirements_39.reqs
   ```

5. On Streamlit Community Cloud, select the appropriate version of Python for your app by clicking "Advanced settings" before you deploy the app:
<div style={{ maxWidth: '65%', marginBottom: '-3em', marginLeft: '6em', marginTop: '-2em' }}>
    <Image src="/images/streamlit-community-cloud/deploy-an-app-advanced.png" />
</div>

That's it! You're ready to use the Snowflake Connector for Python on Streamlit Community Cloud. ❄️🎈

<Tip>

As the Snowflake dependencies [requirements files](https://github.com/snowflakedb/snowflake-connector-python/tree/main/tested_requirements) (`.reqs`) contain the pinned version of the connector, there is **no need** add a separate entry for the connector to requirements.txt.

</Tip>

Additional resources:

- [Installing the Python Connector](https://docs.snowflake.com/en/user-guide/python-connector-install.html#step-1-install-the-connector)
- [Unable to Deploy streamlit app with snowflake-connector-python](https://discuss.streamlit.io/t/unable-to-deploy-streamlit-app-with-snowflake-connector-python/27318)
- [Prerequisite Python packages for the Snowflake Connector](https://docs.snowflake.com/en/user-guide/python-connector-install.html#label-python-connector-prerequisites-python-packages)
