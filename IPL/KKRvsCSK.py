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


#### Records of CSK vs KKR (matches dataset)
cskkr =matches[np.logical_or(np.logical_and(matches['team1']=='Chennai Super Kings',matches['team2']=='Kolkata Knight Riders'),np.logical_and(matches['team2']=='Chennai Super Kings',matches['team1']=='Kolkata Knight Riders'))]
cskkr


# # Q1.

# In[5]:


# Head to head CSK vs KKR across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(cskkr['winner'],order=cskkr['winner'].value_counts().index)
plt.text(-0.1,7,str(cskkr['winner'].value_counts()['Chennai Super Kings']),size=29,color='black')
plt.text(0.9,5,str(cskkr['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('CSK vs KKR - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =cskkr[cskkr['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head CSK vs KKR across last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1.7,str(df_season_record_df['winner'].value_counts()['Chennai Super Kings']),size=29,color='black')
plt.text(0.9,0.5,str(df_season_record_df['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('CSK vs KKR - head to head')
plt.show()


# In[8]:


#For deliveries dataset
kkrcsk=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Chennai Super Kings',deliveries['bowling_team']== 'Kolkata Knight Riders'),np.logical_and(deliveries['bowling_team']=='Chennai Super Kings',deliveries['batting_team']=='Kolkata Knight Riders'))]
kkrcsk


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
kkrcsk_2season = kkrcsk[kkrcsk['match_id'] >= 7898]
kkrcsk_2season


# ## Q5.

# In[10]:


# No balls bowled across all season's
noballs_allseason = kkrcsk['noball_runs'].sum()
print("No balls across all season's =",noballs_allseason)
### Total matches all season's
total_matches = kkrcsk['match_id'].nunique()
print("Total matches h2h =",total_matches)
total_matches_all = (noballs_allseason/total_matches).round(3)
print("Average no balls per match =",total_matches_all.round(2))


# In[11]:


## No balls match wise all season's
noballs_all = pd.DataFrame(kkrcsk.groupby(['match_id']).sum()['noball_runs'])
noballs_all   


# In[12]:


# No balls bowled in last 2 season's
noballs_2season = kkrcsk_2season['noball_runs'].sum()
print("No balls bowled in last 2 season's =", noballs_2season)
## Total matches played in last 2 season's h2h
total_match_2season = kkrcsk_2season['match_id'].nunique()
print("Total matches played in last 2 season's h2h =", total_match_2season)
average_noballs_2season = noballs_2season/total_match_2season
print("Average no balls bowled in last 2 seasons h2h =",average_noballs_2season)


# In[13]:


## No balls match wise last 2 season's
noballs_all = pd.DataFrame(kkrcsk_2season.groupby(['match_id']).sum()['noball_runs'])
noballs_all   


# # Q2.

# In[14]:


def overs(over):
 team_csk=kkrcsk_2season[kkrcsk_2season.batting_team=='Chennai Super Kings']
 team_kkr=kkrcsk_2season[kkrcsk_2season.batting_team=='Kolkata Knight Riders']
 overs_csk=team_csk[(team_csk['over'] <= over)]
 overs_kkr=team_kkr[(team_kkr['over'] <= over)]
 runs_csk=overs_csk[overs_csk['batting_team']=='Chennai Super Kings'].sum()['total_runs']
 runs_kkr=overs_kkr[overs_kkr['batting_team']=='Kolkata Knight Riders'].sum()['total_runs']
 runs_per_match_kkr=runs_kkr/overs_kkr['match_id'].nunique()
 runs_per_match_csk=runs_csk/overs_csk['match_id'].nunique()
 print("Average runs per match in all season's during h2h of Csk =",runs_per_match_csk.round())
 print("Average runs per match in all season's during h2h of kkr =",runs_per_match_kkr.round())


# In[15]:


overs(8)


# In[16]:


overs(9)


# In[17]:


overs(10)


# ## Considering the average runs made per over by two teams to make a prediction

# # Q4.

# In[18]:


## Checking for 4&6 in same over for last 3 matches
def match(matchid):
 df = kkrcsk_2season[kkrcsk_2season.match_id == matchid]
 dfx = df[df.batsman_runs >= 4]
 dataframe = pd.DataFrame(dfx.groupby(['match_id','over','ball','inning']).sum()['batsman_runs'])
 print(dataframe)


# ## Considering last 3 matches played head to head

# In[19]:


match(7926)


# ## Only 1 over in which 4 & 6 in same over in 1st match

# In[20]:


match(11314)


# ## 4 overs with 4&6 in same over in 2nd match

# In[21]:


match(11320)


# ## 3 overs with 4&6 in same over in 3rd match

# # Q3.

# In[22]:


## Records of chahar against KKR
chahar = kkrcsk[kkrcsk.bowler == 'DL Chahar']
chahar


# In[23]:


## creating a function to check his wickets/over if any present
def match(matchid):
 chahar = kkrcsk[kkrcsk.bowler == 'DL Chahar']
 chahar_matchid = chahar[chahar.match_id == matchid]
 print(chahar_matchid[['match_id','over','ball','player_dismissed']])


# In[24]:


match(7898)


# ## ^ Just bowled 1 over in his 1st match against KKR and was wicketless

# In[25]:


match(11314)


# ## ^ For 2nd match against kkr taken wicket in his 6th,10th,16th ball

# In[26]:


match(11320)


# ## ^For 3rd match he was wicketless
