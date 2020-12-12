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


# In[24]:


## Replacing Delhi daredevils with Delhi Capitals
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[5]:


matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[18]:


#### Records of Kxip vs DC (matches dataset)
kxipdc=matches[np.logical_or(np.logical_and(matches['team1']=='Delhi Capitals',matches['team2']=='Kings XI Punjab'),np.logical_and(matches['team2']=='Delhi Capitals',matches['team1']=='Kings XI Punjab'))]
kxipdc


# In[20]:


# Head to head DC vs Kxip across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(kxipdc['winner'],order=kxipdc['winner'].value_counts().index)
plt.text(-0.1,7,str(kxipdc['winner'].value_counts()['Kings XI Punjab']),size=29,color='white')
plt.text(0.9,3,str(kxipdc['winner'].value_counts()['Delhi Capitals']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('DC vs KXIP - head to head')
plt.show()


# In[26]:


#H2H previous 2 season's
df_season_record =kxipdc[kxipdc['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[29]:


# Head to head csk vs dc last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.05,2,str(df_season_record_df['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.text(0.95,0.5,str(df_season_record_df['winner'].value_counts()['Delhi Capitals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Dc vs KXIP - head to head')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head, KXIP have dominated DC.
# # Hence according to the recent form and analysis Kings XI Punjab will win today's match.

# In[25]:


#For deliveries dataset
dckxip=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Delhi Capitals',deliveries['bowling_team']== 'Kings XI Punjab'),np.logical_and(deliveries['bowling_team']=='Delhi Capitals',deliveries['batting_team']=='Kings XI Punjab'))]
dckxip


# In[31]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
dckxip_2season = dckxip[dckxip['match_id'] >= 7895]
dckxip_2season


# In[81]:


gayle_record = dckxip[dckxip.batsman == 'CH Gayle']
totalruns_dc = gayle_record['batsman_runs'].sum()
totalballs_dc = gayle_record['ball'].count()
Strikerate_dc = (totalruns_dc/totalballs_dc)*100
print("Gayle strike rate vs DC with KXIP =",Strikerate_dc.round())

gaylevsdc = deliveries[deliveries.bowling_team == 'Delhi Capitals']
gayle = gaylevsdc[gaylevsdc.batsman == 'CH Gayle']
totalrungayle = gayle['batsman_runs'].sum()
totalballgayle = gayle['ball'].count() - gayle['wide_runs'].sum() - gayle['noball_runs'].sum()
strikerategayle_all = (totalrungayle/totalballgayle)*100
print("Gayle strike rate vs DC with all franchises =",strikerategayle_all.round())


# ## Looking at Chris Gayle strike-rate against DC playing with KXIP,& also with other franchises it has been above 130. Hence,his strike rate today will be above 130.

# In[70]:


df = gaylevsdc[gaylevsdc.player_dismissed == 'CH Gayle'].count()
totalout_gayle = df['player_dismissed']
totalmatchgayle = gayle['match_id'].nunique()
gayle_notout = gayle['match_id'].nunique() - totalout_gayle
print("Gayle not out =",gayle_notout)
print("Gayle out =",totalout_gayle)


# ## Looking at Chris Gayle dismissal against DC in overall season's he has been dismissed in 11 out of 14 innings played against DC. Hence, according to prediction the status of him will be Out
# 

# In[82]:


#Shreyas Iyer contribution against KXIP in last two seasons.

dc_score=dckxip_2season[dckxip_2season.batting_team=='Delhi Capitals'].sum()['total_runs']
average_score=dc_score/dckxip_2season['match_id'].nunique()
print("DC average score against KXIP is =",average_score.round(2))

dc_score=dckxip_2season[dckxip_2season.batting_team=='Delhi Capitals']
dc_iyer=dc_score[dc_score.batsman=='SS Iyer']
dc_iyer_runs=dc_iyer['total_runs'].sum()-dc_iyer['extra_runs'].sum()
print("Shreyas Iyer runs against KXIP is =",dc_iyer_runs)

matches_played=dc_iyer['match_id'].nunique()
print("Matches played by Iyer against KXIP is =",matches_played)
average=dc_iyer_runs/matches_played ;
print('Average score of SS Iyer against KXIP =',average.round(2))
contribution_iyer=(average*100/average_score)
print("The % contribution of Iyer in total DC runs =",contribution_iyer.round(2),"%")


# ## So by analysis of shreyas contribution in runs against KXIP comes out to be around 25% 
# ## Hence, his contribution in DC's total score today will be 18.1% or more

# In[83]:


#Rahul's runs against DC in first six overs
df_six_overs=dckxip[dckxip.over<=6]
df_rahul=df_six_overs[df_six_overs.batsman=='KL Rahul'].sum()['total_runs']
df_rahul_runs=df_rahul-df_six_overs[df_six_overs.batsman=='KL Rahul']['extra_runs'].sum()
print("Rahul's runs against DC in first six overs =",df_rahul_runs)

#Rahul's strike rate against DC in first six overs
df_rahul_total_balls=df_six_overs[df_six_overs.batsman=='KL Rahul'].count()['ball']
wide_balls=df_six_overs[df_six_overs.batsman=='KL Rahul'].sum()['wide_runs']
no_balls=df_six_overs[df_six_overs.batsman=='KL Rahul'].sum()['noball_runs']
df_rahul_balls=df_rahul_total_balls-wide_balls-no_balls
strike_rate=100*(df_rahul_runs/df_rahul_balls)
print("Rahul's strike rate against DC in first six overs =",strike_rate.round())

#Rahul's runs against DC in first six overs
df_six_overs=deliveries[deliveries.over<=6]
df_rahul=df_six_overs[df_six_overs.batsman=='KL Rahul'].sum()['total_runs']
df_rahul_runs=df_rahul-df_six_overs[df_six_overs.batsman=='KL Rahul']['extra_runs'].sum()
print("Rahul's runs in first six overs =",df_rahul_runs)

#Rahul's strike rate against DC in first six overs
df_rahul_total_balls=df_six_overs[df_six_overs.batsman=='KL Rahul'].count()['ball']
wide_balls=df_six_overs[df_six_overs.batsman=='KL Rahul'].sum()['wide_runs']
no_balls=df_six_overs[df_six_overs.batsman=='KL Rahul'].sum()['noball_runs']
df_rahul_balls=df_rahul_total_balls-wide_balls-no_balls
strike_rate=100*(df_rahul_runs/df_rahul_balls)
print("Rahul's strike rate in first six overs =",strike_rate.round())


# ## Looking at Rahul's strike rate in first six overs in all season it has been in an average of 139.
# ## Also considering his record in current season(2020) he has strike rate of around 120-130 in first 6 overs which gradually increases in death and middle overs.
# ## Hence,according to prediction Rahul's strikerate in first 6 overs will be in range 122-137 

# In[87]:


# Overall performance of KXIP bowling without Shami from 31st ball to 120th ball
df_bowler=dckxip[dckxip.bowling_team=='Kings XI Punjab']
df_overs=df_bowler[df_bowler.over>=6 ]
df_other_bowlers=df_overs[df_overs.bowler!='Mohammed Shami']
df_wickets=df_other_bowlers['player_dismissed'].count()
average=df_wickets/df_other_bowlers['match_id'].nunique()
print("Overall season average =",average.round(2))


# In[88]:


# Overall performance of KXIP bowling in last 2 years without Shami from 31st ball to 120th ball
df_bowler=dckxip_2season[dckxip_2season.bowling_team=='Kings XI Punjab']
df_overs=df_bowler[df_bowler.over>=6 ]
df_other_bowlers=df_overs[df_overs.bowler!='Mohammed Shami']
df_wickets=df_other_bowlers['player_dismissed'].count()
average=df_wickets/df_other_bowlers['match_id'].nunique()
print("Last 2 season average =",average.round(2))


# ## According to the analysis in an average wickets taken by KXIP excluding shami has been around 5.
# ## Hence, according to prediction KXIP bowlers will take 5 or more wickets from 31st to 120th ball

# In[ ]:




