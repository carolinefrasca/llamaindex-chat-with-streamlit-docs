---
title: Use Streamlit in Snowflake
slug: /get-started/installation/streamlit-in-snowflake
---

# Use Streamlit in Snowflake to code in a secure environment

Snowflake is a single, global platform that powers the Data Cloud. If you want to use a secure platform with role-based access control, this is the option for you! This page walks you through creating a trial Snowflake account and building a simple "Hello world" app. Your trial account comes with an account credit so you can try out the service without entering any payment information.

<Note>

Streamlit in Snowflake is currently based on Streamlit version 1.22.0 with some [Limitations and unsupported features](https://docs.snowflake.com/en/developer-guide/streamlit/limitations). We are working on supporting newer versions and more features.

</Note>

## Prerequisites

All you need is an email address! Everything else happens in your 30-day trial account.

## Create an account

1. Go to <a href="https://signup.snowflake.com/?utm_source=streamlit&utm_medium=referral&utm_campaign=na-us-en-&utm_content=-ss-streamlit-docs" target="_blank">signup.snowflake.com</a>. (This link will open in a new tab.)

2. Fill in your information and click "**CONTINUE**."

3. Select "**Standard**" for your Snowflake edition and "**Amazon Web Services**" for your cloud provider.

4. Choose the region nearest you, accept the terms, and click "**GET STARTED**."

<div style={{ maxWidth: '50%', margin: 'auto' }}>
    <Image alt="Choose your Snowflake edition, provider, and region" src="/images/get-started/SiS-region.png" />
</div>

5. Answer or skip a few questions to let us know more about yourself.

6. A message will display to confirm "You're now signed up!" Go to your email and click on the activation link. (Within your link, note the subdomain. This is your Snowflake account identifier. `https://<account_identifier>.snowflakecomputing.com`)

7. Set your username and password. This will be an admin user account within your Snowflake account. Your Snowflake account can have multiple users within it.

8. If you are not signed in after setting your password, follow the instructions to enter your Snowflake account identifier before entering your username and password. If you've accidentally closed your browser, you can log in at [app.snowflake.com](https://app.snowflake.com/).

9. Congratulations! You have a trial Snowflake account. The first thing you will see are some sample databases. (This interface is called Snowsight. Check out the Snowflake docs for a [quick tour](https://docs.snowflake.com/en/user-guide/ui-snowsight-quick-tour).)

   ![Sample databases in your new trial Snowflake account](/images/get-started/SiS-1-landing-page.png)

## Accept the use of Anaconda on your Snowflake account

10. In the left navigation, go to "**Admin**" then "**Billing & Terms**."

11. In the "**Anaconda**" section, click "**Enable**."

12. Accept the terms. The "**Anaconda**" section will now show "**Acknowledged**."

## Create a warehouse and database to hold your Streamlit apps

13. Click on your name in the left navigation. Hover over "**Switch Role**" and select "**ACCOUNTADMIN**" to use your account in the context of an admin.

14. In the left navigation under "**Admin**," click on "**Warehouses**."

15. In the upper-right corner, click the blue "<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>add</i> **Warehouse**" button.

16. Enter "STREAMLITWAREHOUSE" for the name and keep the defaults of "Standard" type and "X-Small" size. Click "**Create Warehouse**."

17. In the left navigation, go to "**Data**" then "**Databases**." (This is back where you started!)

18. In the upper-right corner, click the blue "<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>add</i> **Database**" button.

19. Enter "STREAMLITAPPSDB" for the name. Click "**Create**."

20. Yay! You now have a new database to hold all your Streamlit apps.

    ![New database in your new trial Snowflake account](/images/get-started/SiS-2-databases.png)

## Create a "Hello World" Streamlit app

21. In the left navigation, click on "**Streamlit**."

22. In the upper-right corner, click the blue "<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>add</i> **Streamlit App**" button.

23. Enter "Hello World" for the name of your app. Your new warehouse and database should already be filled in, along with the "PUBLIC" schema for your database. Click "**Create**." (Note that the app will run with the rights of "ACCOUNTADMIN" for simplicity. You can curate your roles and permissions to choose who can create and access apps.)

    ![Create your first Streamlit in Snowflake app](/images/get-started/SiS-3-create-app.png)

24. Your new app, prefilled with example code, will open in editing mode. The left panel shows your code. The right panel shows the resulting app.

25. You can explore the example if you want, but we'll proceed here with a simpler example. (Don't worry! You can always make another app to get the same example again.) Delete the code on the left and replace it with:

    ```python
    import streamlit as st

    st.write("Hello World")
    ```

26. In the upper-right corner, click the blue "<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>play_arrow</i> **Run**" button to make the running app reflect your changes.

27. Hooray! You just wrote a Streamlit app.

![Hello World in Streamlit in Snowflake app](/images/get-started/SiS-4-hello-world-1.png)

28. Change `st.write` to `st.title`:

    ```python
    import streamlit as st

    st.title("Hello World")
    ```

29. In the upper-right corner, click the blue "<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>play_arrow</i> **Run**" button to make the running app reflect your changes.

30. You've just edited your app. It's that easy.

    ![Hello World in Streamlit in Snowflake app](/images/get-started/SiS-5-hello-world-2.png)

31. When you're done, click "<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>chevron_left</i> **Streamlit Apps**" in the upper-left corner to go back to Snowsight.

## Returning to your app

32. When you are ready to return to your app, go to your Snowsight interface. (If you are returning to the site, you can log in at [app.snowflake.com](https://app.snowflake.com/).)

33. In the left navigation, go to "**Streamlit**."

34. Click on "**Hello World**." (If you don't see your app, check that you have your role set to "ACCOUNTADMIN" as above.)

    ![Return to your Streamlit in Snowflake app](/images/get-started/SiS-6-hello-world-return.png)

35. Your app will open in viewing mode. Just click "**Edit**" in the upper-right corner to modify your app again.

    ![Change to editing mode in Streamlit in Snowflake](/images/get-started/SiS-7-hello-world-edit.png)

## What's next?

Read about our [Basic concepts](/get-started/fundamentals/main-concepts) and try out more commands in your app. To create more apps in your account, you can proceed from [Create a "Hello World" Streamlit app](#create-a-hello-world-streamlit-app). The warehouse and database setup do not need to be repeated.

For more information about creating and managing Streamlit in Snowflake apps, check out the [Snowflake docs](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit).
