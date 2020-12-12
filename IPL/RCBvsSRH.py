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


#### Records of RCB vs SRH (matches dataset)
rcbsrh =matches[np.logical_or(np.logical_and(matches['team1']=='Sunrisers Hyderabad',matches['team2']=='Royal Challengers Bangalore'),np.logical_and(matches['team2']=='Sunrisers Hyderabad',matches['team1']=='Royal Challengers Bangalore'))]
rcbsrh


# # Q1.

# In[5]:


# Head to head RCB vs SRH across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(rcbsrh['winner'],order=rcbsrh['winner'].value_counts().index)
plt.text(-0.1,5,str(rcbsrh['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.9,4,str(rcbsrh['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RCB vs SRH - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =rcbsrh[rcbsrh['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head RCB vs SRH across last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1,str(df_season_record_df['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.9,1,str(df_season_record_df['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RCB vs SRH- head to head last 2 season')
plt.show()


# In[8]:


#For deliveries dataset
srhrcb=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Sunrisers Hyderabad',deliveries['bowling_team']== 'Royal Challengers Bangalore'),np.logical_and(deliveries['bowling_team']=='Sunrisers Hyderabad',deliveries['batting_team']=='Royal Challengers Bangalore'))]
srhrcb 


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
srhrcb_2season = srhrcb[srhrcb['match_id'] >= 7932]
srhrcb_2season


# # Q5.

# In[10]:


## Dots including legbyes & byes balls previous 2 season's h2h
dots = srhrcb_2season[srhrcb_2season.total_runs == 0]
dots_t = dots['total_runs'].count()
print("Total dots =",dots_t)
totalmatch = df_season_record_df['id'].count()
print("Total matches =",totalmatch)
avg_dots= (dots_t/totalmatch).round()
print("Avg dots per match =",avg_dots)


# In[11]:


## Dots excluding legbyes & byes balls last 2 season's h2h
df_bye = srhrcb_2season[srhrcb_2season.bye_runs > 0]
byecount = df_bye['bye_runs'].count()
df_legbye = srhrcb_2season[srhrcb_2season.legbye_runs > 0]
legbyecount = df_legbye['legbye_runs'].count()
dots_t = dots['total_runs'].count() - legbyecount - byecount
print("Total dots =",dots_t)
totalmatch = df_season_record_df['id'].count()
print("Total matches =",totalmatch)
avg_dots= (dots_t/totalmatch).round()
print("Avg dots per match =",avg_dots)


# In[12]:


## Dots including legbyes & byes balls all season's h2h
dots_all = srhrcb[srhrcb.total_runs == 0]
dots_all_t = dots_all['total_runs'].count()
print("Total dots =",dots_all_t)
totalmatch_all = rcbsrh['id'].count()
print("Total matches =",totalmatch_all)
avg_dots_all= (dots_all_t/totalmatch_all).round()
print("Avg dots per match =",avg_dots_all)


# In[13]:


## Dots excluding legbyes & byes balls all season's h2h
df_bye = srhrcb[srhrcb.bye_runs > 0]
byecount = df_bye['bye_runs'].count()
df_legbye = srhrcb[srhrcb.legbye_runs > 0]
legbyecount = df_legbye['legbye_runs'].count()
dots_all = srhrcb[srhrcb.total_runs == 0]
dots_all_t = dots_all['total_runs'].count() - legbyecount - byecount
print("Total dots =",dots_all_t)
totalmatch_all = rcbsrh['id'].count()
print("Total matches =",totalmatch_all)
avg_dots_all= (dots_all_t/totalmatch_all).round()
print("Avg dots per match =",avg_dots_all)


# # Q2.

# In[19]:


# Average runs in all season's SRH vs RCB matches. 
runs=srhrcb['total_runs'].sum()
total_matches=srhrcb['match_id'].nunique()
average_runs=runs/total_matches
print('The average runs in all RCB vs SRH matches are',average_runs.round())


# In[20]:


# Average runs in SRH vs RCB matches of last 2 seasons
runs=srhrcb_2season['total_runs'].sum()
total_matches=srhrcb_2season['match_id'].nunique()
average_runs=runs/total_matches
print('The average runs in RCB vs SRH matches in last 2 seasons =',average_runs.round())


# # Q4.

# In[41]:


# All season
df_srh=srhrcb[(srhrcb.batting_team=='Sunrisers Hyderabad') & (srhrcb.over<=6)]
df_rcb=srhrcb[(srhrcb.batting_team=='Royal Challengers Bangalore') & (srhrcb.over<=6)]
pp_srh=df_srh['player_dismissed'].count()/df_srh['match_id'].nunique()
print('Average SRH wickets are',pp_srh.round(1))
pp_rcb=df_rcb['player_dismissed'].count()/df_rcb['match_id'].nunique()
print('Average RCB wickets are',pp_rcb.round(1))
print('The difference in wickets of both teams should be',abs(pp_srh-pp_rcb).round(1))


# In[42]:


# Last 2 season 
df_srh=srhrcb_2season[(srhrcb_2season.batting_team=='Sunrisers Hyderabad') & (srhrcb_2season.over<=6)]
df_rcb=srhrcb_2season[(srhrcb_2season.batting_team== 'Royal Challengers Bangalore') & (srhrcb_2season.over<=6)]
pp_srh=df_srh['player_dismissed'].count()/df_srh['match_id'].nunique()
print('Average SRH wickets are',pp_srh.round(1))
pp_rcb=df_rcb['player_dismissed'].count()/df_rcb['match_id'].nunique()
print('Average RCB wickets are',pp_rcb.round(1))
print('The difference in wickets of both teams should be',abs(pp_srh-pp_rcb).round(1))


# # Q3.

# In[197]:


## Difference in balls to reach 80 runs after once being reached 50.
def func(matchid,over1,over2,over3,over4): 
 match = srhrcb_2season[srhrcb_2season.match_id == matchid]
 team = match[match.batting_team == 'Royal Challengers Bangalore']
 x=team[team.over <= over1].total_runs.sum()
 y=team[team.over <= over2].total_runs.sum()
 match_srh = srhrcb_2season[srhrcb_2season.match_id == matchid]
 team_srh = match_srh[match_srh.batting_team == 'Sunrisers Hyderabad']
 a = team_srh[team_srh.over <= over3].total_runs.sum()
 b = team_srh[team_srh.over <= over4].total_runs.sum()  
 print('Match id :',matchid)   
 print('FOR RCB :')
 print('Runs for over1 to reach approximate fifty =',x)
 print('Runs for over2 to reach next 30 runs =',y)
 print('Difference in runs =',y-x)
 print('Difference in overs to reach 30 runs after 50 =',over2-over1) 
 print('FOR SRH :')
 print('Runs for over3 to reach approximate fifty =',a)
 print('Runs for over4 to reach next 30 runs =',b)
 print('Difference in runs =',b-a)
 print('Difference in overs to reach 30 runs after 50 =',over4-over3)
 print('Difference in approximate balls is =',(abs((over2-over1)-(over4-over3)))*6)


# In[183]:


## Calling function for last 4 matches {functions works for all combination's}
func(7932,5,10,8,12)


# In[196]:


func(7944,7,10,5,9)


# In[194]:


func(11147,10,13,5,9)


# In[191]:


func(11345,6,10,6,12)

