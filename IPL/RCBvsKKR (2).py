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


# In[4]:


## Replacing Delhi daredevils with Delhi Capitals
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[5]:


matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[13]:


#### Records of RcB vs KKR (matches dataset)
rcbkkr =matches[np.logical_or(np.logical_and(matches['team1']=='Royal Challengers Bangalore',matches['team2']=='Kolkata Knight Riders'),np.logical_and(matches['team2']=='Royal Challengers Bangalore',matches['team1']=='Kolkata Knight Riders'))]
rcbkkr


# In[23]:


# Head to head KKR vs RCB across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(rcbkkr['winner'],order=rcbkkr['winner'].value_counts().index)
plt.text(-0.1,7,str(rcbkkr['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='white')
plt.text(0.9,3,str(rcbkkr['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Rcb vs KKR- head to head')
plt.show()


# In[153]:


#H2H previous 2 season's
df_season_record =rcbkkr[rcbkkr['season'] >=2019]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[171]:


##### Head to head rcb vs kkr last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.05,0.5,str(df_season_record_df['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.text(0.95,0.5,str(df_season_record_df['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('KKR vs RCB - head to head last 2 season')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head,KKR have dominated RCB.
# # However, looking at current season ipl RCB have won the h2h played at start of season & in last match in overall season in 2019 RCB won against  KKR. Also if they chase they will win the match as per their record in current ipl season.
# # Hence according to the recent form and analysis RCB will win today's match.

# In[24]:


#For deliveries dataset
kkrrcb=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Royal Challengers Bangalore',deliveries['bowling_team']== 'Kolkata Knight Riders'),np.logical_and(deliveries['bowling_team']=='Royal Challengers Bangalore',deliveries['batting_team']=='Kolkata Knight Riders'))]
kkrrcb


# In[26]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
kkrrcb_2season = kkrrcb[kkrrcb['match_id'] >= 7896]
kkrrcb_2season


# In[43]:


## RCB death overs runs in h2h
team_rcb=kkrrcb[kkrrcb.batting_team=='Royal Challengers Bangalore']
overs=team_rcb[(team_rcb['over'] >= 15)]
runs=overs[overs['batting_team']=='Royal Challengers Bangalore'].sum()['total_runs']
runs_per_match=runs/overs['match_id'].nunique()
print("Average runs per match in all season's in death overs during h2h of RCB =",runs_per_match.round())


# In[44]:


## RCB death overs runs for last 2 season's in h2h
team_rcb=kkrrcb_2season[kkrrcb_2season.batting_team=='Royal Challengers Bangalore']
overs=team_rcb[(team_rcb['over'] >= 15)]
runs=overs[overs['batting_team']=='Royal Challengers Bangalore'].sum()['total_runs']
runs_per_match=runs/overs['match_id'].nunique()
print("Average runs per match in last 2 season's in death overs during h2h of RCB =",runs_per_match.round())


# ## Looking at average runs scored in death is 56 in overall season record.
# ## Also in Recent they scored at average of 40-60 in this season's ipl
# ## Hence according to prediction they will score in range 46-60 in todays match 

# In[53]:


# Overall performance of RCB from 31st ball to 120th ball in H2H
df_batting=kkrrcb[kkrrcb.batting_team=='Royal Challengers Bangalore']
df_overs=df_batting[df_batting.over>=5 ]
df_wickets=df_overs['player_dismissed'].count()
average=df_wickets/df_overs['match_id'].nunique()
print("Overall season's record of average wickets fallen for RCB in h2h in 31st to 120th ball =",average.round(2))


# In[51]:


# Overall performance of RCB in last 2 years from 31st ball to 120th ball in H2H
df_batting_2season=kkrrcb_2season[kkrrcb_2season.batting_team=='Royal Challengers Bangalore']
df_overs_2season=df_batting_2season[df_batting_2season.over>=5 ]
df_wickets_2season=df_overs_2season['player_dismissed'].count()
average_2season=df_wickets_2season/df_overs_2season['match_id'].nunique()
print("Last 2 season's average wickets fallen for rcb in h2h in 31st to 120th ball =",average_2season.round(2))


# ## Looking at the analysis average wickets lost in 5-20th is 4 wickets.
# ## However in current season(2020) they have lost in average 2-3 wickets
# ## Hence according to analysis they will lose 2-3 wickets in 5-20th over.

# In[148]:


# Ab de villiers record against KKR in last 2 season
score = df_batting_2season[df_batting_2season.batsman == 'AB de Villiers'].batsman_runs.sum()
matches = df_batting_2season['match_id'].nunique()
average = score/matches
avgruns = average.round()


# In[151]:


# Average balls to score 30 runs
abd = df_batting_2season[df_batting_2season.batsman == 'AB de Villiers']
balls = abd['ball'].count() - abd['wide_runs'].sum()  - abd['bye_runs'].sum() - abd['legbye_runs'].sum()
x = (balls/matches).round()
((x/avgruns)*30).round()


# ## According to analysis abd takes around 16 balls to score 30 runs in last 2 season against kkr.
# ## Hence according to prediction he will take less than 18 balls to score 30 runs.
