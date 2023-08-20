---
title: Optimize performance
slug: /library/api-reference/performance
---

# Optimize performance

Streamlit provides powerful [cache primitives](/library/advanced-features/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

<TileContainer>

<RefCard href="/library/api-reference/performance/st.cache_data" size="half">

#### Cache data

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data
```

</RefCard>

<RefCard href="/library/api-reference/performance/st.cache_resource" size="half">

#### Cache resource

Function decorator to cache functions that return global resources (e.g. database connections, ML models).

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )
```

</RefCard>

<RefCard href="/library/api-reference/performance/st.cache_data.clear" size="half">

#### Clear cached data

Clear all in-memory and on-disk data caches.

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data

if st.checkbox("Clear All"):
  # Clear values from *all* cache_data functions
  st.cache_data.clear()
```

</RefCard>

<RefCard href="/library/api-reference/performance/st.cache_resource.clear" size="half">

#### Clear cached resources

Clear all `st.cache_resource` caches.

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )

if st.checkbox("Clear All"):
  # Clear values from *all* cache_resource functions
  st.cache_data.clear()
```

</RefCard>

</TileContainer>

<Important>

All the below commands were deprecated in version 1.18.0. Use the new commands above instead. Learn more in [Caching](/library/advanced-features/caching).
</Important>
