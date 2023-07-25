#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# In[8]:


with open('t20_json_files/t20_wc_match_results.json') as f:
    data=json.load(f)
df_match = pd.DataFrame(data[0]['matchSummary'])
df_match.head()


# In[10]:


df_match.shape


# In[12]:


df_match.rename({'scorecard': 'match_id'}, axis=1, inplace=True)


# In[13]:


df_match.head()


# In[20]:


match_ids_dict = {}

for index, row in df_match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' Vs ' + row['team1']
    
    match_ids_dict[key1] = row["match_id"]
    match_ids_dict[key2] = row["match_id"]
    
match_ids_dict


# **batting summary

# In[16]:


with open('t20_json_files/t20_wc_batting_summary.json') as f:
    data=json.load(f)
    
    all_records = []
    
    for rec in data:
        all_records.extend(rec['battingSummary'])

df_batting = pd.DataFrame(all_records)
df_batting.head()


# In[17]:


df_batting["out/not_out"] = df_batting.dismissal.apply(lambda x: "out" if len(x) > 0 else "not out")
df_batting.head()


# In[18]:


df_batting.drop(columns=["dismissal"], inplace=True)
df_batting.head(10)


# In[19]:


df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace("â€",""))
df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace("\xa0",""))
df_batting.head(11)


# In[21]:


df_batting["match_id"] = df_batting["match"].map(match_ids_dict)

df_batting.head()


# In[ ]:




