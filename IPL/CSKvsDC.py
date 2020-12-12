#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


deliveries = pd.read_csv('C:/Users/SONY/Desktop/IPL/deliveries.csv')
deliveries


# In[3]:


matches = pd.read_csv('C:/Users/SONY/Desktop/IPL/matches.csv')
matches


# In[4]:


# Replacing DD with DC in deliveries dataset
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[5]:


# Replacing DD with DC in matches dataset
matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[6]:


#### Records of DC vs CSK (matches dataset)
cskdc=matches[np.logical_or(np.logical_and(matches['team1']=='Chennai Super Kings',matches['team2']=='Delhi Capitals'),np.logical_and(matches['team2']=='Chennai Super Kings',matches['team1']=='Delhi Capitals'))]
cskdc


# In[7]:


# Head to head CSK vs DC across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(cskdc['winner'],order=cskdc['winner'].value_counts().index)
plt.text(-0.1,7,str(cskdc['winner'].value_counts()['Chennai Super Kings']),size=29,color='white')
plt.text(0.9,3,str(cskdc['winner'].value_counts()['Delhi Capitals']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('CSK vs DC - head to head')
plt.show()


# In[8]:


#H2H previous 2 season's
df_season_record = cskdc[cskdc['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[9]:


# Head to head csk vs dc last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.05,2,str(df_season_record_df['winner'].value_counts()['Chennai Super Kings']),size=29,color='black')
plt.text(0.95,0.5,str(df_season_record_df['winner'].value_counts()['Delhi Capitals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('CSK vs DC - head to head')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head, CSK have dominated DC.
# # Hence according to the recent form and analysis Chennai Super Kings will win today's match.

# In[10]:


#For deliveries dataset
dccsk=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Chennai Super Kings',deliveries['bowling_team']=='Delhi Capitals'),np.logical_and(deliveries['bowling_team']=='Chennai Super Kings',deliveries['batting_team']=='Delhi Capitals'))]
dccsk


# In[11]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
dccsk_2season = dccsk[dccsk['match_id'] >= 7923]
dccsk_2season


# In[41]:


## Wickets taken by csk in 91-120 balls in h2h over last 2 season's(2018-19)
team_2season_csk_wicketstaken_h2h  =dccsk_2season[dccsk_2season.batting_team=='Delhi Capitals']
overs=team_2season_csk_wicketstaken_h2h[(team_2season_csk_wicketstaken_h2h['over']>=15)]
wickets_2season=overs[overs['batting_team']=='Delhi Capitals'].count()['player_dismissed']
totalmatch2season = dccsk_2season['match_id'].nunique()
average_w_2season = wickets_2season/totalmatch2season
print("Total wickets taken by csk in h2h in last 2 season's 2018-2019 in 91-120 balls =",wickets_2season)
print("Total matches h2h last 2 season =",totalmatch2season)
print("Average wickets taken by csk in h2h in last 2 season's in 91-120 balls =",average_w_2season.round(2))


# In[42]:


## Wickets taken by csk in 91-120 balls in h2h over all season's
team_csk_wicketstaken_h2h_allseason =dccsk[dccsk.batting_team=='Delhi Capitals']
overs=team_csk_wicketstaken_h2h_allseason[(team_csk_wicketstaken_h2h_allseason['over']>=15)]
wickets=overs[overs['batting_team']=='Delhi Capitals'].count()['player_dismissed']
totalmatch = dccsk['match_id'].nunique()
average_w_all = (wickets/totalmatch).round(2)
print("Total wickets taken by csk in h2h in all season's in 91-120 balls =",wickets)
print("Total matches h2h all season =",totalmatch)
print("Average wickets taken by csk in h2h in all season's in 91-120 balls =",average_w_all.round(1))


# ## Considering the overall average wickets taken by csk in 91 to 120 balls of overall season's record as well as recent season record's it comes out to be 2.
# ## Also, considering the ground the match where is going to take place has small dimensions hence the chances of getting out is slightly lesser.
# ## Keeping in mind those factors, CSK will take wickets in range 0-2 in today's match.

# In[23]:


# No balls in all season's h2h
noballs_all =dccsk['noball_runs'].sum()
average_noballs = noballs_all/totalmatch
average_noballs.round(2)


# In[15]:


# No balls in last 2 season's (2018-2019) h2h
noballs_2season = dccsk_2season['noball_runs'].sum()
average_noballs_2season = noballs_2season/totalmatch2season
average_noballs_2season


# ## Considering the no balls bowled in overall season's record in h2h it comes to be 0.8 ~~ 1.Also taking in consideration the recent 2 season's of h2h the no of no balls bowled have been in average 0-1.
# ## Hence,according to prediction  number of no balls in today's match would be in range 0-1

# In[16]:


## Runs scored by csk last 2 season
csk_total_2season = dccsk_2season[dccsk_2season.batting_team == 'Chennai Super Kings'].total_runs.sum()
averageruns_2season = csk_total_2season/totalmatch2season
averageruns_2season.round()


# ## Considering the recent season's (2018-19) record of score of csk in h2h against dc it has been 170+ 
# ## Also, considering the first innings score in sharjah this season it has been 180+ 
# ## Hence,according to above factors csk will score 175 or more runs in today's match

# In[35]:


# Average runs scored by csk in first 42 balls (6.6 overs)
overs1to6 = dccsk_2season[dccsk_2season.over <= 6  ]
overs1to6csk = overs1to6[overs1to6.batting_team == 'Chennai Super Kings']
average_runs_overs1to6 =(overs1to6csk['total_runs'].sum())/totalmatch2season
print("Average Runs in first 42 balls =",average_runs_overs1to6)
# Average runs scored by csk in first 60 balls (9.6 overs)
overs1to9 = dccsk_2season[dccsk_2season.over <= 9]
overs1to9csk = overs1to9[overs1to9.batting_team == 'Chennai Super Kings']
average_runs_overs1to9 =(overs1to9csk['total_runs'].sum())/totalmatch2season
print("Average Runs in first 60 balls =",average_runs_overs1to9)
# average runs scored by csk in first 72 balls (11.6 overs)
overs1to11 = dccsk_2season[dccsk_2season.over <= 11]
overs1to11csk = overs1to11[overs1to11.batting_team == 'Chennai Super Kings']
average_runs_overs1to11 =(overs1to11csk['total_runs'].sum())/totalmatch2season
print("Average Runs in first 72 balls =",average_runs_overs1to11)
# average runs scored by csk in first 78 balls (12.6 overs)
overs1to12 = dccsk_2season[dccsk_2season.over <= 12]
overs1to12csk = overs1to12[overs1to12.batting_team == 'Chennai Super Kings']
average_runs_overs1to12 =(overs1to12csk['total_runs'].sum())/totalmatch2season
print("Average Runs in first 78 balls =",average_runs_overs1to12)


# ## From the above code it is clear that taking under consideration last 2 season's(5 matches)  of csk runs in different overs patch,they have taken an average of 78 balls to score 100 runs against DC.
# ## Hence,according to prediction csk will take 71 or more balls to score 100 runs today
