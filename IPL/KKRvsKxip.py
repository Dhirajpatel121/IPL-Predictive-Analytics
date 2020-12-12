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


#### Records of KXIP vs KKR (matches dataset)
kkrkxip =matches[np.logical_or(np.logical_and(matches['team1']=='Kolkata Knight Riders',matches['team2']=='Kings XI Punjab'),np.logical_and(matches['team2']=='Kolkata Knight Riders',matches['team1']=='Kings XI Punjab'))]
kkrkxip


# # Q1.

# In[5]:


# Head to head KKR vs KXIP across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(kkrkxip['winner'],order=kkrkxip['winner'].value_counts().index)
plt.text(-0.1,7,str(kkrkxip['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.text(0.9,5,str(kkrkxip['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('KKR vs KXIP - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =kkrkxip[kkrkxip['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head KKR vs KXIP across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1.7,str(df_season_record_df['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.text(0.9,0.5,str(df_season_record_df['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('KKR vs KXIP - head to head')
plt.show()


# In[8]:


#For deliveries dataset
kxipkkr=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Kolkata Knight Riders',deliveries['bowling_team']== 'Kings XI Punjab'),np.logical_and(deliveries['bowling_team']=='Kolkata Knight Riders',deliveries['batting_team']=='Kings XI Punjab'))]
kxipkkr


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
kxipkkr_2season = kxipkkr[kxipkkr['match_id'] >= 7911]
kxipkkr_2season


# # Q 4.

# In[10]:


#Maxwell contribution against KKR in all seasons.

kxip_score=kxipkkr[kxipkkr.batting_team=='Kings XI Punjab'].sum()['total_runs']
average_score=kxip_score/kxipkkr['match_id'].nunique()
print("KXIP average score against KKR is =",average_score.round(2))
kxip=kxipkkr[kxipkkr.batting_team=='Kings XI Punjab']
kxip_maxwell=kxip[kxip.batsman=='GJ Maxwell']
kxip_maxwell_runs=kxip_maxwell['total_runs'].sum()-kxip_maxwell['extra_runs'].sum()
print("Maxwell total runs against KKR is =",kxip_maxwell_runs)
matches_played=kxip_maxwell['match_id'].nunique()
print("Matches played by Maxwell against KKR is =",matches_played)
average=kxip_maxwell_runs/matches_played ;
print('Average score of Maxwell against KKR =',average.round(2))
contribution_maxwell=(average*100/average_score)
print("The % contribution of Maxwell in total KXIP runs =",contribution_maxwell.round(2),"%")


# # Q 2.

# In[11]:


## Dots including legbyes & byes balls previous 2 season's h2h
dots = kxipkkr_2season[kxipkkr_2season.total_runs == 0]
dots_t = dots['total_runs'].count()
print("Total dots =",dots_t)
totalmatch = df_season_record_df['id'].count()
print("Total matches =",totalmatch)
avg_dots= dots_t/totalmatch
print("Avg dots per match =",avg_dots)


# In[12]:


## Dots excluding legbyes & byes balls last 2 season's
df_bye = kxipkkr_2season[kxipkkr_2season.bye_runs > 0]
byecount = df_bye['bye_runs'].count()
df_legbye = kxipkkr_2season[kxipkkr_2season.legbye_runs > 0]
legbyecount = df_legbye['legbye_runs'].count()
dots_t = dots['total_runs'].count() - legbyecount - byecount
print("Total dots =",dots_t)
totalmatch = df_season_record_df['id'].count()
print("Total matches =",totalmatch)
avg_dots= dots_t/totalmatch
print("Avg dots per match =",avg_dots)


# In[13]:


## Dots including legbyes & byes balls all season's h2h
dots_all = kxipkkr[kxipkkr.total_runs == 0]
dots_all_t = dots_all['total_runs'].count()
print("Total dots =",dots_all_t)
totalmatch_all = kkrkxip['id'].count()
print("Total matches =",totalmatch_all)
avg_dots_all= dots_all_t/totalmatch_all
print("Avg dots per match =",avg_dots_all)


# In[14]:


## Dots excluding legbyes & byes balls all season's h2h
df_bye = kxipkkr[kxipkkr.bye_runs > 0]
byecount = df_bye['bye_runs'].count()
df_legbye = kxipkkr[kxipkkr.legbye_runs > 0]
legbyecount = df_legbye['legbye_runs'].count()
dots_all = kxipkkr[kxipkkr.total_runs == 0]
dots_all_t = dots_all['total_runs'].count() - legbyecount - byecount
print("Total dots =",dots_all_t)
totalmatch_all = kkrkxip['id'].count()
print("Total matches =",totalmatch_all)
avg_dots_all= dots_all_t/totalmatch_all
print("Avg dots per match =",avg_dots_all)


# # Q 5.

# In[15]:


# No balls bowled across all season's
noballs_allseason = kxipkkr['noball_runs'].sum()
print("No balls across all season's =",noballs_allseason)
total_matches = kxipkkr['match_id'].nunique()
print("Total matches h2h =",total_matches)
total_matches_all = (noballs_allseason/total_matches).round(3)
print("Average no balls per match =",total_matches_all.round(2))


# In[16]:


# No balls bowled in last 2 season's
noballs_2season = kxipkkr_2season['noball_runs'].sum()
print("No balls bowled in last 2 season's =", noballs_2season)
## Total matches played in last 2 season's h2h
total_match_2season = kxipkkr_2season['match_id'].nunique()
print("Total matches played in last 2 season's h2h =", total_match_2season)
average_noballs_2season = noballs_2season/total_match_2season
print("Average no balls bowled in last 2 seasons h2h =",average_noballs_2season)


# In[17]:


## No balls match wise last 2 season h2h
noballs_2season = pd.DataFrame(kxipkkr_2season.groupby(['match_id']).sum()['noball_runs'])
noballs_2season 


# # Q 3.

# In[20]:


## Last 2 season's h2h wickets fallen in 15-20th over
df_overs=kxipkkr_2season[kxipkkr_2season.over>=15 ]
df_wickets=df_overs['player_dismissed'].count()
average=df_wickets/df_overs['match_id'].nunique()
print("Average wickets in last 2 season's =",average.round(2))


# In[23]:


## Overall season's h2h wickets fallen in 15-20th over
df_overs=kxipkkr[kxipkkr.over>=15 ]
df_wickets=df_overs['player_dismissed'].count()
average=df_wickets/df_overs['match_id'].nunique()
print("Average wickets in all season's =",average.round())

