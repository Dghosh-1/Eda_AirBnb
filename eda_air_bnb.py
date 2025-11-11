#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Load and clean data

# In[5]:
def load_data(path="compressed_data.csv"):
    df = pd.read_csv(path, low_memory=False)
    df['last review'] = pd.to_datetime(df['last review'], errors='coerce')
    df.fillna({'reviews per month': 0, 'last review': df['last review'].min()}, inplace=True)
    df.drop(columns=["lisence", "house_rules"], errors='ignore', inplace=True)
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    df.drop_duplicates(inplace=True)
    return df

# #  Distribution of Listing Prices
# 

# In[14]:


def price_distribution(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['price'], bins=40, kde=True, color='#E74C3C',
                 edgecolor='black', alpha=0.8, ax=ax)
    ax.set_title("Distribution of Listing Prices", fontsize=16, fontweight="bold")
    ax.set_xlabel("Price ($)")
    ax.set_ylabel("Frequency")
    return fig


# #  Room Type Distribution

# In[7]:


def room_type_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x='room type', data=df, color='skyblue', ax=ax)
    ax.set_title("Room Type Distribution", fontsize=16, fontweight="bold")
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Count")
    return fig


# #  Listings Across Neighbourhoods

# In[8]:


def listings_by_neighbourhood(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(x='neighbourhood group', data=df,
                  order=df['neighbourhood group'].value_counts().index,
                  color='lightgreen', ax=ax)
    ax.set_title("Listings by Neighbourhood Group", fontsize=16, fontweight="bold")
    ax.set_xlabel("Neighbourhood Group")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    return fig


# #  Relation Between Price and Room Type

# In[9]:


def price_vs_room_type(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='room type', y='price', data=df, palette='Set2', ax=ax)
    ax.set_title("Price vs Room Type", fontsize=16, fontweight="bold")
    ax.set_xlabel("Room Type")
    ax.set_ylabel("Price ($)")
    return fig


# #  Number of Reviews Over Time

# In[10]:


def reviews_over_time(df):
    df['last review'] = pd.to_datetime(df['last review'])
    reviews = df.groupby(df['last review'].dt.to_period('M')).size()
    fig, ax = plt.subplots(figsize=(12, 6))
    reviews.plot(kind='line', color='red', ax=ax)
    ax.set_title("Number of Reviews Over Time", fontsize=16, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Reviews")
    return fig


# # Correlation Heatmap

# In[13]:


def correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(14, 10))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='crest', linewidths=0.4, square=True, ax=ax)
    ax.set_title("Feature Correlation Heatmap", fontsize=18, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(rotation=0, fontsize=10)
    plt.tight_layout()
    return fig



# In[ ]:




