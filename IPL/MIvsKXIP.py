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


#### Records of MI vs KXIP (matches dataset)
mikxip=matches[np.logical_or(np.logical_and(matches['team1']=='Mumbai Indians',matches['team2']=='Kings XI Punjab'),np.logical_and(matches['team2']=='Mumbai Indians',matches['team1']=='Kings XI Punjab'))]
mikxip


# In[5]:


# Head to head MI vs Kxip across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(mikxip['winner'],order=mikxip['winner'].value_counts().index)
plt.text(-0.1,7,str(mikxip['winner'].value_counts()['Mumbai Indians']),size=29,color='white')
plt.text(0.9,3,str(mikxip['winner'].value_counts()['Kings XI Punjab']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs KXIP - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record = mikxip[mikxip['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head csk vs dc last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.05,2,str(df_season_record_df['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.text(0.95,0.5,str(df_season_record_df['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs KXIP - head to head')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head, MI have dominated KXIP.
# # Hence according to the recent form and analysis Mumbai Indians will win today's match.

# In[8]:


#For deliveries dataset
kxipmi=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Mumbai Indians',deliveries['bowling_team']== 'Kings XI Punjab'),np.logical_and(deliveries['bowling_team']=='Mumbai Indians',deliveries['batting_team']=='Kings XI Punjab'))]
kxipmi


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
kxipmi_2season = kxipmi[kxipmi['match_id'] >= 7927]
kxipmi_2season


# In[10]:


# Last 2 season's dismissal kind of Q de kock with MI against KXIP
decock_records_strike = kxipmi_2season[kxipmi_2season.batsman == 'Q de Kock']
decock_records_strike_dismissaltype = decock_records_strike[decock_records_strike.player_dismissed == 'Q de Kock']
decock_records_strike_dismissaltype[['match_id','batsman','dismissal_kind','bowler']]


# In[11]:


# Allseason's dismissal kind of Q de kock with MI against KXIP
decock_records_strike_all = kxipmi[kxipmi.batsman == 'Q de Kock']
decock_records_strike_dismissaltype_all = decock_records_strike_all[decock_records_strike_all.player_dismissed == 'Q de Kock']
final_decock_all = decock_records_strike_dismissaltype_all[['match_id','batsman','dismissal_kind','bowler']]
final_decock_all


# In[21]:


# Allseason's dismissal kind of Q de kock with all franchise's against KXIP
decock_all_franchise = deliveries[deliveries.batsman == 'Q de Kock']
decock_allteams = decock_all_franchise[decock_all_franchise.player_dismissed == 'Q de Kock']
decock_allteams_withkxip = decock_allteams[decock_allteams.bowling_team == 'Kings XI Punjab']
df_final_qdk = decock_allteams_withkxip[['batsman','bowling_team','bowler']]
df_final_qdk['type'] = ['Seam','Seam','Spin','Seam','Spin']
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(13,8)
sns.countplot(df_final_qdk['type'],order=df_final_qdk['type'].value_counts().index)
plt.text(-0.1,1.5,str(df_final_qdk['type'].value_counts()['Seam']),size=29,color='white')
plt.text(0.9,0.75,str(df_final_qdk['type'].value_counts()['Spin']),size=29,color='white')
plt.xlabel('Type of bowler',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Q de kock  dismissal kind',fontsize=15)
plt.show()


# ## Looking at Q de kock record against kxip bowlers he have been dismissed by seamer's more often.Also,in current season(2020) he has been dismissed in all his matches by seamer's.
# ## Also, KXIP has good seamers,so most probably by bouncer or good length ball will take his wicket.
# ## Hence,according to prediction Q de kock will be dismissed by a SEAMER in today's match

# In[13]:


# Allseason's dismissal kind of Rahul with KXIP against MI
Rahul_records_strike_all = kxipmi[kxipmi.batsman == 'KL Rahul']
Rahul_records_strike_dismissaltype = Rahul_records_strike_all[Rahul_records_strike_all.player_dismissed == 'KL Rahul']
Rahul_records_strike_dismissaltype[['match_id','batsman','dismissal_kind','bowler']]


# In[14]:


# All season's dismissal kind of Rahul with all franchises against MI
records_strike_all = deliveries[deliveries.bowling_team == 'Mumbai Indians']
rahul_records_strike_all = records_strike_all[records_strike_all.batsman == 'KL Rahul']
rahul_against_mi = rahul_records_strike_all[rahul_records_strike_all.player_dismissed == 'KL Rahul']
rahul_final = rahul_against_mi[['batsman','bowling_team','dismissal_kind','bowler']]
rahul_final


# In[15]:


# All season's dismissal kind of Rahul with all franchises against MI
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(13,8)
sns.countplot(rahul_final['dismissal_kind'],order=rahul_final['dismissal_kind'].value_counts().index)
plt.text(-0.1,2.5,str(rahul_final['dismissal_kind'].value_counts()['caught']),size=29,color='black')
plt.text(0.9,0.5,str(rahul_final['dismissal_kind'].value_counts()['bowled']),size=29,color='black')
plt.text(1.9,0.5,str(rahul_final['dismissal_kind'].value_counts()['run out']),size=29,color='black')
plt.xlabel('Dismissal Type',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('KL Rahul dismissal kind',fontsize=15)
plt.show()


# ## Considering the previous 2 season's record Rahul has been dismissed by CAUGHT. Also,his overall record against MI with all franchises shows that he has been caught in 5 out of his 7 matches against MI.
# ## Hence,according to prediction Rahul will be dimissed by dismissal kind of CAUGHT in today's match.

# In[16]:


## Average wickets lost by kxip in powerplay during h2h in all season's
team_kxip=kxipmi[kxipmi.batting_team=='Kings XI Punjab']
overs=team_kxip[(team_kxip['over'] <= 5)]
wickets=overs[overs['batting_team']=='Kings XI Punjab'].count()['player_dismissed']
wickets_per_match=wickets/overs['match_id'].nunique()
print("Average wickets per match in all season's in powerplay during h2h of KXIP =",wickets_per_match)


# In[17]:


## Average wickets lost by kxip in powerplay during h2h in last 2 season's
team_kxip_2season=kxipmi_2season[kxipmi_2season.batting_team=='Kings XI Punjab']
overs_2season=team_kxip_2season[(team_kxip_2season['over'] <= 5)]
wickets_2season=overs_2season[overs_2season['batting_team']=='Kings XI Punjab'].count()['player_dismissed']
wickets_per_match_2season =wickets_2season/overs_2season['match_id'].nunique()
print("Average wickets per match in last 2 season's in powerplay during h2h of KXIP =",wickets_per_match_2season)


# ## Looking at record of previous 2 season's record KXIP have lost an average of 0.25 wickets, which means a wicket in 4 matches.However looking at the overall season's record of KXIP against MI they have lost in an average of 1 wicket against MI in powerplay.
# ## Hence,according to prediction KXIP will loose wickets in range 0-1 in powerplay in today's match.

# In[18]:


## Average wickets fallen in h2h in allseason's
Total_wickets_allseason_h2h = kxipmi['player_dismissed'].count()
Total_matches_h2h = kxipmi['match_id'].nunique()
average_wickets_allseason = Total_wickets_allseason_h2h/Total_matches_h2h
print("Average wickets in h2h in all season's =",average_wickets_allseason)


# In[19]:


## Average wickets fallen in h2h in last 2 season's
Total_wickets_2season_h2h = kxipmi_2season['player_dismissed'].count()
Total_matches_h2h_2season = kxipmi_2season['match_id'].nunique()
average_wickets_2season = Total_wickets_2season_h2h/Total_matches_h2h_2season
print("Average wickets in h2h in last 2 season's =",average_wickets_2season)


# ## The wickets fallen in an average in last 2 season's in H2H has been 10.75 ~~ 11 . Also,considering overall season's record of H2H total wickets lost have been approximately equal to 12 in an average.
# ## Considering,an additional factor of ground (Dubai) the average wickets fallen in an match this season has been in range 11-15 .
# ## Hence, according to prediction total wickets that would fall in today's match will be in range 11-15 . 
