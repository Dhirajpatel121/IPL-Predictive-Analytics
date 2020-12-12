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


#### Records of MI vs RCB (matches dataset)
mircb =matches[np.logical_or(np.logical_and(matches['team1']=='Mumbai Indians',matches['team2']=='Royal Challengers Bangalore'),np.logical_and(matches['team2']=='Mumbai Indians',matches['team1']=='Royal Challengers Bangalore'))]
mircb


# # Q1.

# In[5]:


# Head to head MI vs RCB across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(mircb['winner'],order=mircb['winner'].value_counts().index)
plt.text(-0.1,7,str(mircb['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.text(0.9,5,str(mircb['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('mi vs rcb - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =mircb[mircb['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head MI vs RCB across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1.7,str(df_season_record_df['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.text(0.9,0.5,str(df_season_record_df['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs RCB - head to head')
plt.show()


# In[8]:


#For deliveries dataset
rcbmi=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Mumbai Indians',deliveries['bowling_team']== 'Royal Challengers Bangalore'),np.logical_and(deliveries['bowling_team']=='Mumbai Indians',deliveries['batting_team']=='Royal Challengers Bangalore'))]
rcbmi


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
rcbmi_2season = rcbmi[rcbmi['match_id'] >= 7907]
rcbmi_2season


# # Q5.

# In[10]:


# All season
df_mi=rcbmi[(rcbmi.batting_team=='Mumbai Indians') & (rcbmi.over<=6)]
df_rcb=rcbmi[(rcbmi.batting_team=='Royal Challengers Bangalore') & (rcbmi.over<=6)]
pp_mi=df_mi['total_runs'].sum()/df_mi['match_id'].nunique()
print('Average MI runs are',pp_mi.round(2))
pp_rcb=df_rcb['total_runs'].sum()/df_rcb['match_id'].nunique()
print('Average RCB runs are',pp_rcb.round(2))
print('The difference in runs of both teams should be',abs(pp_mi-pp_rcb).round(2))


# In[11]:


# Last 2 season
df_mi=rcbmi_2season[(rcbmi_2season.batting_team=='Mumbai Indians') & (rcbmi_2season.over<=6)]
df_rcb=rcbmi_2season[(rcbmi_2season.batting_team== 'Royal Challengers Bangalore') & (rcbmi_2season.over<=6)]
pp_mi=df_mi['total_runs'].sum()/df_mi['match_id'].nunique()
print('Average MI runs are',pp_mi)
pp_rcb=df_rcb['total_runs'].sum()/df_rcb['match_id'].nunique()
print('Average RCB runs are',pp_rcb.round(2))
print('The difference in runs of both teams should be',abs(pp_mi-pp_rcb).round(2))


# # Q2.

# In[12]:


## Bowlers wickets/match
def func(bowlername):
 bowler = rcbmi_2season[rcbmi_2season.bowler == bowlername]
 wickets = bowler['player_dismissed'].count()
 avg_wickets = wickets/bowler['match_id'].nunique()
 print(bowlername)
 print("Avg wickets =",avg_wickets.round(2))


# In[13]:


## MI bowlers
func('HH Pandya')
func('JJ Bumrah')
func('KH Pandya')
func('RD Chahar')


# In[14]:


# RCB bowlers
func('YS Chahal')
func('M Ali')
func('Mohammed Siraj')
func('N Saini')
func('Washington Sundar')
func('P Negi')


# In[15]:


## Boult against RCB avg wickets
boult = deliveries[deliveries.bowler == 'TA Boult']
boult_rcb = boult[boult.batting_team == 'Royal Challengers Bangalore']
wickets = boult_rcb['player_dismissed'].count()
matches = boult_rcb['match_id'].nunique()
avg_boult = wickets/matches
avg_boult


# In[16]:


## Morris against MI avg wickets
morris = deliveries[deliveries.bowler == 'CH Morris']
morris_mi = morris[morris.batting_team == 'Mumbai Indians']
wickets = morris_mi['player_dismissed'].count()
matches = morris_mi['match_id'].nunique()
avg_morris= wickets/matches
avg_morris


# # Q3.

# In[17]:


def bowler(bowlername):
 df_bowler = rcbmi_2season[rcbmi_2season.bowler == bowlername]
 total_runs_conceded = df_bowler['batsman_runs'].sum() 
 total_balls=df_bowler['ball'].count() - df_bowler[df_bowler.wide_runs >= 1].count() - df_bowler[df_bowler.noball_runs >= 1].count()
 total_balls_df = total_balls['ball']   
 print(bowlername)
 print('Economy rate =',((total_runs_conceded/total_balls_df)*6).round(2))


# In[18]:


## MI bowlers
bowler('HH Pandya')
bowler('JJ Bumrah')
bowler('KH Pandya')
bowler('RD Chahar')


# In[19]:


# RCB bowlers
bowler('YS Chahal')
bowler('M Ali')
bowler('Mohammed Siraj')
bowler('N Saini')
bowler('Washington Sundar')
bowler('P Negi')


# In[20]:


## For Boult
total_runs_conceded = boult_rcb['batsman_runs'].sum() 
total_balls=boult_rcb['ball'].count() - boult_rcb[boult_rcb.wide_runs >= 1].count() - boult_rcb[boult_rcb.noball_runs >= 1].count()
total_balls_df = total_balls['ball']   
print('Economy rate =',((total_runs_conceded/total_balls_df)*6).round(2))


# In[21]:


## For Morris
total_runs_conceded = morris_mi['batsman_runs'].sum() 
total_balls=morris_mi['ball'].count() - morris_mi[morris_mi.wide_runs >= 1].count() - morris_mi[morris_mi.noball_runs >= 1].count()
total_balls_df = total_balls['ball']   
print('Economy rate =',((total_runs_conceded/total_balls_df)*6).round(2))


# # Q4.

# In[22]:


## strikerate
batsmen_strikerate_season = pd.DataFrame(rcbmi_2season.groupby(['batsman']).agg({'batsman_runs' : 'sum','ball' : 'count'}))
batsmen_strikerate_season['Strike Rate'] = batsmen_strikerate_season['batsman_runs']/batsmen_strikerate_season['ball']*100
batsmen_strikerate_season = batsmen_strikerate_season.sort_values(by ='Strike Rate' , ascending = False)
batsmen_strikerate_season[(batsmen_strikerate_season['Strike Rate'] > 130) & (batsmen_strikerate_season['ball'] > 10)] 

