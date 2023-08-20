---
title: Upgrade the Streamlit version of your app on Streamlit Community Cloud
slug: /knowledge-base/deploy/upgrade-streamlit-version-on-streamlit-cloud
---

# Upgrade the Streamlit version of your app on Streamlit Community Cloud

Want to use a cool new Streamlit feature but your app on Streamlit Community Cloud is running an old version of the Streamlit library? If that's you, don't worry! All you need to do is upgrade your app's Streamlit version. Here are five ways to do this, based on how your [app manages dependencies](/streamlit-community-cloud/deploy-your-app/app-dependencies):

## No dependency file

When there is no dependency file in the repo, the app will always use the same Streamlit version that existed when the app was _first_ deployed on Streamlit Community Cloud; even if you reboot the app! In other words, Streamlit Community Cloud automatically pins the version for you so that the app does not break suddenly when rebooted in the future.

You may want to avoid getting into this situation if your app depends on a specific version of Streamlit. That is why we encourage you to use a dependency file and pin your desired version of Streamlit. We cover this in more detail in the sections below.

## `requirements.txt`

1. If the Streamlit version is not pinned (i.e., the requirements file contains a line with `streamlit` and nothing else):
   - Reboot the app as described above.
2. If the Streamlit version is pinned (e.g., `streamlit==1.4.0`):
   - Adapt the pinned version in the requirements file and push it to GitHub.
   - The app on Streamlit Community Cloud will reboot automatically as soon as it detects these changes.

## pipenv/poetry/conda

If you use any of these dependency managers, you probably know what you need to do. 😉

1. On your local computer, run the command to update the Streamlit package:
   - `pipenv update streamlit` or
   - `poetry update streamlit` or
   - With an activated conda environment, run:
     - `pip install -U streamlit` **and**
     - `conda env export`
2. Then push any changes to Pipfile.lock or poetry.lock or environment.yml to GitHub.
3. The app on Streamlit Community Cloud will reboot automatically as soon as it detects these changes.
