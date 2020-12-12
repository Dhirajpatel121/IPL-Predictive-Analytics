#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.simplefilter('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


deliveries=pd.read_csv('C:/Users/SONY/Desktop/IPL/deliveries.csv')
matches=pd.read_csv('C:/Users/SONY/Desktop/IPL/matches.csv')


# In[3]:


matches.shape


# In[4]:


deliveries.shape


# In[5]:


matches.columns


# In[6]:


deliveries.columns


# In[7]:


matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[8]:


matches.head(3)


# ### Here df1 is the dataframe obtained from matches dataset which includes all the matches between SRH and DC

# ### Q.1

# In[9]:


df1=matches[np.logical_or(np.logical_and(matches['team1']=='Sunrisers Hyderabad',matches['team2']=='Delhi Capitals'),np.logical_and(matches['team2']=='Sunrisers Hyderabad',matches['team1']=='Delhi Capitals'))]


# In[72]:


# Head to head SRH vs DC across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df1['winner'],order=df1['winner'].value_counts().index)
plt.text(-0.1,5,str(df1['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.9,5,str(df1['winner'].value_counts()['Delhi Capitals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Sunrisers Hyderabad vs Delhi Capitals - head to head')
plt.show()


# In[11]:


# Last 2 season performance of both the teams against each other.
last2_seasons=df1[df1.season>=2018]
last2_seasons


# In[12]:


# Last two seasons 2018,2019 ipl matches results
winner=last2_seasons.groupby(['winner']).size().reset_index(name='win_counts')
winner=winner.sort_values("win_counts",ascending=False)
winner.groupby("winner").head(2)


# In[53]:


###Here df2 is the dataframe obtained from DELIVERIES dataset which includes all the matches 
df2=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Sunrisers Hyderabad',deliveries['bowling_team']=='Delhi Capitals'),np.logical_and(deliveries['bowling_team']=='Sunrisers Hyderabad',deliveries['batting_team']=='Delhi Capitals'))]
df2.head(5)


# In[52]:


# Dataframe consisting data of last two seasons only.
matches_last2_seasons=df2[df2.match_id>=7929]
matches_last2_seasons.head(5)


# # Q.2

# In[15]:


# Average runs in all SRH vs DC matches. 
runs=df2['total_runs'].sum()
total_matches=df2['match_id'].nunique()
average_runs=runs/total_matches
print('The average runs in all DC vs SRH matches are',average_runs.round(2))


# In[16]:


# Average runs in SRH vs DC matches of last 2 seasons
runs=matches_last2_seasons['total_runs'].sum()
total_matches=matches_last2_seasons['match_id'].nunique()
average_runs=runs/total_matches
print('The average runs in DC vs SRH matches in last 2 seasons =',average_runs.round(2))


# ## Q.4

# In[17]:


df_srh=df2[(df2.batting_team=='Sunrisers Hyderabad') & (df2.over<=6)]
df_dc=df2[(df2.batting_team=='Delhi Capitals') & (df2.over<=6)]
pp_srh=df_srh['total_runs'].sum()/df_srh['match_id'].nunique()
print('Average SRH runs are',pp_srh)
pp_dc=df_dc['total_runs'].sum()/df_dc['match_id'].nunique()
print('Average DC runs are',pp_dc.round(2))
print('The difference in runs of both teams should be',abs(pp_srh-pp_dc).round(2))


# In[18]:


df_srh=matches_last2_seasons[(matches_last2_seasons.batting_team=='Sunrisers Hyderabad') & (matches_last2_seasons.over<=6)]
df_dc=matches_last2_seasons[(matches_last2_seasons.batting_team=='Delhi Capitals') & (matches_last2_seasons.over<=6)]
pp_srh=df_srh['total_runs'].sum()/df_srh['match_id'].nunique()
print('Average SRH runs are',pp_srh)
pp_dc=df_dc['total_runs'].sum()/df_dc['match_id'].nunique()
print('Average DC runs are',pp_dc.round(2))
print('The difference in runs of both teams should be',abs(pp_srh-pp_dc).round(2))


# ## Q.5

# In[19]:


extras=df2['extra_runs'].sum()
average_extras=extras/df2['match_id'].nunique()
average_extras.round(2)


# In[20]:


extras=matches_last2_seasons['extra_runs'].sum()
average_extras=extras/matches_last2_seasons['match_id'].nunique()
average_extras.round(2)


# ## Q.3

# In[42]:


x =matches_last2_seasons.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)


# In[71]:


## Last 2 season dismissal kind
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(13,8)
sns.countplot(x['dismissal_kind'],order=x['dismissal_kind'].value_counts().index)
plt.text(-0.1,12,str(x['dismissal_kind'].value_counts()['caught']),size=29,color='black')
plt.text(1,5,str(x['dismissal_kind'].value_counts()['run out']),size=29,color='black')
plt.xlabel('Dismissal Type',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('dismissal kind',fontsize=15)
plt.show()


# In[63]:


y = x[x.dismissal_kind == 'caught']
wickets_by_caught = y['dismissal_kind'].count()
matches = matches_last2_seasons['match_id'].nunique()
avg_wickets_caught_2season = wickets_by_caught/matches
print("avg wickets caught 2 season =",avg_wickets_caught_2season)


# In[70]:


total_match = df2['match_id'].nunique()
final = df2[df2.dismissal_kind == 'caught']
wickets_caught = final['dismissal_kind'].count()
avg_caught_overall=wickets_caught/total_match
print("avg wickets caught all season =",avg_caught_overall.round(2))


# In[ ]:




