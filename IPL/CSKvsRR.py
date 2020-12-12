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


deliveries = pd.read_csv('C:/Users/SONY/Desktop/IPL/deliveries.csv')
deliveries


# In[3]:


matches = pd.read_csv('C:/Users/SONY/Desktop/IPL/matches.csv')
matches


# In[20]:


#### Records of MI vs KXIP (matches dataset)
cskrr=matches[np.logical_or(np.logical_and(matches['team1']=='Chennai Super Kings',matches['team2']=='Rajasthan Royals'),np.logical_and(matches['team2']=='Chennai Super Kings',matches['team1']=='Rajasthan Royals'))]
cskrr


# In[23]:


# Head to head MI vs Kxip across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(cskrr['winner'],order=cskrr['winner'].value_counts().index)
plt.text(-0.1,7,str(cskrr['winner'].value_counts()['Chennai Super Kings']),size=29,color='white')
plt.text(0.9,3,str(cskrr['winner'].value_counts()['Rajasthan Royals']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('CSK vs RR - head to head')
plt.show()


# In[28]:


#H2H previous 2 season's
df_season_record =cskrr[cskrr['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[30]:


# Head to head csk vs dc last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.05,2,str(df_season_record_df['winner'].value_counts()['Chennai Super Kings']),size=29,color='black')
plt.text(0.95,0.5,str(df_season_record_df['winner'].value_counts()['Rajasthan Royals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('CSK vs RR - head to head')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head, CSK have dominated RR.
# # Hence according to the recent form and analysis Chennai Super Kings will win today's match.

# In[35]:


#For deliveries dataset
rrcsk=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Chennai Super Kings',deliveries['bowling_team']== 'Rajasthan Royals'),np.logical_and(deliveries['bowling_team']=='Chennai Super Kings',deliveries['batting_team']=='Rajasthan Royals'))]
rrcsk


# In[37]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
rrcsk_2season = rrcsk[rrcsk['match_id'] >= 7910]
rrcsk_2season


# In[70]:


## Average runs scored by RR in powerplay during h2h in all season's
team_rr=rrcsk[rrcsk.batting_team=='Rajasthan Royals']
overs=team_rr[(team_rr['over'] <= 6)]
runs=overs[overs['batting_team']=='Rajasthan Royals'].sum()['total_runs']
runs_per_match=runs/overs['match_id'].nunique()
print("Average runs per match in all season's in powerplay during h2h of RR =",runs_per_match.round())


# In[69]:


## Average runs scored by RR in powerplay during h2h in last 2 season's
rr_2season=rrcsk_2season[rrcsk_2season.batting_team=='Rajasthan Royals']
overs_2season=rr_2season[(rr_2season['over'] <= 6)]
runs_2season=overs_2season[overs_2season['batting_team']=='Rajasthan Royals'].sum()['total_runs']
runs_per_match_2season =runs_2season/overs_2season['match_id'].nunique()
print("Average wickets per match in last 2 season's in powerplay during h2h of RR =",runs_per_match_2season.round())


# ## RR will score in range of 40-49 runs in powerplay according to analysis

# In[104]:


## Wickets taken by Jofra archer in last 5 overs in all season's against csk
overs_jofra = rrcsk[(rrcsk['over'] >= 15)]
jofra = overs_jofra[overs_jofra.bowler == 'J Archer']
dismissed_jofra_all = jofra['player_dismissed'].count()
jofra_matches_all = jofra['match_id'].nunique()
wickets = dismissed_jofra_all/jofra_matches_all
wickets.round(2)


# In[105]:


## Wickets taken by Jofra archer in last 5 overs in all season's against all teams
overs_jofra = deliveries[(deliveries['over'] >= 15)]
jofra = overs_jofra[overs_jofra.bowler == 'J Archer']
dismissed_jofra_all = jofra['player_dismissed'].count()
jofra_matches_all = jofra['match_id'].nunique()
wickets = dismissed_jofra_all/jofra_matches_all
wickets


# ## Jofra archer will take 1 wicket according to analysis it comes 0.75 his avg. at death but also considering this season's record of him in death overs.Hence , he will take 1 wicket today in death overs.

# In[130]:


## Strike rate of steven smith against csk across all season's
df = rrcsk[rrcsk.batsman == 'SPD Smith']
totalruns_smith = df['batsman_runs'].sum()
totalballsfaced_smith = df['ball'].count()-df['wide_runs'].sum()-df['noball_runs'].sum()
strikerate_smith = ((totalruns_smith/totalballsfaced_smith)*100).round(2)
strikerate_smith


# ## Strike rate of steven smith has been below 120 against CSK in all season's.Hence, his strike rate today will be below 120 according to analysis.

# In[147]:


## economy chahar in all season against rr
chahar = rrcsk[rrcsk.bowler == 'DL Chahar']
conceded_chahar_all = chahar['total_runs'].sum() - chahar['legbye_runs'].sum() - chahar['bye_runs'].sum()
balls_matches_all = chahar['ball'].count() - chahar['wide_runs'].sum() - chahar['noball_runs'].sum()
economy_rate = ((conceded_chahar_all/balls_matches_all)*6).round(2)
economy_rate


# ## Economy rate of chahar against rr has been in average about 7.33 also considering his record in current season his economy rate has been above 7.5 . 
# ## Hence according to analysis chahar economy rate will be in range 7.31 - 8.2  
