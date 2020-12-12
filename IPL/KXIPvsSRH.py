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


# In[26]:


#### Records of KXIP vs SRH (matches dataset)
kxipsrh =matches[np.logical_or(np.logical_and(matches['team1']=='Kings XI Punjab',matches['team2']=='Sunrisers Hyderabad'),np.logical_and(matches['team2']=='Kings XI Punjab',matches['team1']=='Sunrisers Hyderabad'))]
kxipsrh


# In[30]:


# Head to head KXIP vs SRH across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(kxipsrh['winner'],order=kxipsrh['winner'].value_counts().index)
plt.text(-0.1,5,str(kxipsrh['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.9,2,str(kxipsrh['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('KXIP vs SRH - head to head')
plt.show()


# In[138]:


#H2H previous 2 season's
df_season_record =kxipsrh[kxipsrh['season'] >=2017]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[141]:


##### Head to head KXIP vs SRH last 3 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,2,str(df_season_record_df['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.95,0.75,str(df_season_record_df['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Kxip vs SRH- head to head last 3 season')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head,SRH have dominated KXIP .
# 
# # Hence according to the recent form and analysis SRH will win today's match.

# In[38]:


#For deliveries dataset
srhkxip=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Kings XI Punjab',deliveries['bowling_team']== 'Sunrisers Hyderabad'),np.logical_and(deliveries['bowling_team']=='Kings XI Punjab',deliveries['batting_team']=='Sunrisers Hyderabad'))]
srhkxip


# In[40]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
srhkxip_2season = srhkxip[srhkxip['match_id'] >= 7909]
srhkxip_2season


# In[46]:


#Rahul contribution against SRH in last two seasons.

kxip_score=srhkxip_2season[srhkxip_2season.batting_team=='Kings XI Punjab'].sum()['total_runs']
average_score=kxip_score/srhkxip_2season['match_id'].nunique()
print("KXIP average score against SRH is =",average_score.round(2))

kxip_rahul=srhkxip_2season[srhkxip_2season.batsman =='KL Rahul']
rahul_kxip_runs=kxip_rahul['batsman_runs'].sum()
print("Rahul runs against SRH is =",rahul_kxip_runs)

matches_played=kxip_rahul['match_id'].nunique()
print("Matches played by Rahul against SRH is =",matches_played)
average=rahul_kxip_runs/matches_played ;
print('Average score of Rahul against SRH =',average.round(2))
contribution_rahul=(average*100/average_score)
print("The % contribution of Rahul in total KXIP runs =",contribution_rahul.round(),"%")


# In[143]:


#Rahul contribution against SRH in all season's

kxip_score=srhkxip[srhkxip.batting_team=='Kings XI Punjab'].sum()['total_runs']
average_score=kxip_score/srhkxip['match_id'].nunique()
print("KXIP average score against SRH is =",average_score.round(2))

kxip_rahul=srhkxip[srhkxip.batsman =='KL Rahul']
rahul_kxip_runs=kxip_rahul['batsman_runs'].sum()
print("Rahul runs against SRH is =",rahul_kxip_runs)

matches_played=kxip_rahul['match_id'].nunique()
print("Matches played by Rahul against SRH is =",matches_played)
average=rahul_kxip_runs/matches_played ;
print('Average score of Rahul against SRH =',average.round(2))
contribution_rahul=(average*100/average_score)
print("The % contribution of Rahul in total KXIP runs =",contribution_rahul.round(),"%")


# ## So by analysis,rahul contribution in runs against srh in last 2 season comes out to be 32% 
# ## Also,his overall record against srh in runs contribution has been 26%
# ## Hence, his contribution in KXIP total score today will be 23% or more in today's match

# In[60]:


## Records of Gayle against srh in first 10 balls 
def gayle(matchid):
 df_gayle = srhkxip_2season[srhkxip_2season.batsman == 'CH Gayle']
 x = df_gayle[df_gayle['match_id'] == matchid]
 y = x[['match_id','batsman_runs']].head(10)
 z = y['batsman_runs'].sum()
 print(z)


# In[61]:


# 1st match against srh in 2019
gayle(7909)


# In[63]:


# 2nd match against srh in 2019
gayle(7918)


# In[64]:


# 3rd match against srh in 2019
gayle(11313)


# In[68]:


# 4th match against srh in 2019
gayle(11339)


# ## Looking at gayle's record in last 2 season's record he has scored 11-18 runs twice time in first 10 balls
# ## Also looking at his record in current season,he has score in an average 15 runs in first 10 balls he has faced.
# ## Hence,according to analysis he will score 11-18 in first 10 balls he faces today.

# In[70]:


## David Warner against kxip
warner_record = srhkxip[srhkxip.batsman == 'DA Warner']
totalruns_kxip = warner_record['batsman_runs'].sum()
totalballs_kxip = warner_record['ball'].count()
Strikerate_kxip = (totalruns_kxip/totalballs_kxip)*100
print("Warner strike rate vs KXIP with SRH =",Strikerate_kxip.round())

warnervskxip = deliveries[deliveries.bowling_team == 'Kings XI Punjab']
warner = warnervskxip[warnervskxip.batsman == 'DA Warner']
totalrunwarner = warner['batsman_runs'].sum()
totalballwarner = warner['ball'].count() - warner['wide_runs'].sum() - warner['noball_runs'].sum()
strikeratewarner_all = (totalrunwarner/totalballwarner)*100
print("Warner strike rate vs KXIP with all franchises =",strikeratewarner_all.round())

df = warnervskxip[warnervskxip.player_dismissed == 'DA Warner'].count()
totalout_warner = df['player_dismissed']
totalmatchwarner = warner['match_id'].nunique()
warner_notout = warner['match_id'].nunique() - totalout_warner
print("Warner not out =",warner_notout)
print("Warner out =",totalout_warner)


# ## Looking at Warner record against KXIP he has dismissed by dismissal kind (Out) in 15 out of 17 matches.
# ## For strikerate,his strike rate has been above 130 against kxip playing with srh as well him against kxip with all franchises.
# ## Hence,according to prediction, his strike rate would be above 130 & he will be dismissed (OUT).

# In[109]:


## SRH runs in h2h
def overs(over):
 team_srh=srhkxip[srhkxip.batting_team=='Sunrisers Hyderabad']
 overs=team_srh[(team_srh['over'] <= over)]
 runs=overs[overs['batting_team']=='Sunrisers Hyderabad'].sum()['total_runs']
 runs_per_match=runs/overs['match_id'].nunique()
 print("Average runs per match in all season's during h2h of SRH =",runs_per_match.round())


# In[83]:


# Checking for all combinations of answers given
overs(5)


# In[101]:


overs(6)


# In[85]:


overs(7)


# In[107]:


## SRH runs in h2h last 2 season's
def overs(over):
 team_srh=srhkxip_2season[srhkxip_2season.batting_team=='Sunrisers Hyderabad']
 overs=team_srh[(team_srh['over'] <= over)]
 runs=overs[overs['batting_team']=='Sunrisers Hyderabad'].sum()['total_runs']
 runs_per_match=runs/overs['match_id'].nunique()
 print("Average runs per match in all season's during h2h of SRH =",runs_per_match.round())


# In[95]:


overs(5)


# In[96]:


overs(6)


# In[97]:


overs(7)


# ## Looking at last season's h2h record (2 matches) in twice occasion srh scores an average of 50 runs in between 5-6 overs(i.e 30-36 balls)
# ## Hence,according to prediction srh will score 50 in between 30-36 balls.
