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
kxiprr =matches[np.logical_or(np.logical_and(matches['team1']=='Kings XI Punjab',matches['team2']=='Rajasthan Royals'),np.logical_and(matches['team2']=='Kings XI Punjab',matches['team1']=='Rajasthan Royals'))]
kxiprr


# # Q1.

# In[5]:


# Head to head KXIP vs RR across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(kxiprr['winner'],order=kxiprr['winner'].value_counts().index)
plt.text(-0.1,5,str(kxiprr['winner'].value_counts()['Rajasthan Royals']),size=29,color='black')
plt.text(0.9,4,str(kxiprr['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('KXIP vs RR - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =kxiprr[kxiprr['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head KXIP vs RR across last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1.7,str(df_season_record_df['winner'].value_counts()['Kings XI Punjab']),size=29,color='black')
plt.text(0.9,0.5,str(df_season_record_df['winner'].value_counts()['Rajasthan Royals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Kxip vs RR - head to head')
plt.show()


# In[8]:


#For deliveries dataset
rrkxip=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Kings XI Punjab',deliveries['bowling_team']== 'Rajasthan Royals'),np.logical_and(deliveries['bowling_team']=='Kings XI Punjab',deliveries['batting_team']=='Rajasthan Royals'))]
rrkxip 


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
rrkxip_2season = rrkxip[rrkxip['match_id'] >= 7931]
rrkxip_2season


# # Q5.

# In[10]:


## Records of Shami against RR
Shami = rrkxip[rrkxip.bowler == 'Mohammed Shami']
Shami


# ## From above dataframe we see that Shami has played only 2 matches against RR,playing for Kings XI Punjab

# In[11]:


## creating a function to check his wickets/over if any present
def match(matchid):
 Shami = rrkxip[rrkxip.bowler == 'Mohammed Shami']
 Shami_matchid = Shami[Shami.match_id == matchid]
 print(Shami_matchid[['match_id','over','ball','player_dismissed']])


# In[12]:


match(11140)


# ## ^  Bowled 4 over's in his 1st match against RR and got his first wicket in 23rd ball.

# In[13]:


match(11323)


# ## ^ For 2nd match against RR took his 1st wicket in 13th ball & 2nd wicket in 19th ball. 

# # Q4.

# In[14]:


## Dots including legbyes & byes balls previous 2 season's h2h
dots = rrkxip_2season[rrkxip_2season.total_runs == 0]
dots_t = dots['total_runs'].count()
print("Total dots =",dots_t)
totalmatch = df_season_record_df['id'].count()
print("Total matches =",totalmatch)
avg_dots= (dots_t/totalmatch).round()
print("Avg dots per match =",avg_dots)


# In[15]:


## Dots excluding legbyes & byes balls last 2 season's h2h
df_bye = rrkxip_2season[rrkxip_2season.bye_runs > 0]
byecount = df_bye['bye_runs'].count()
df_legbye = rrkxip_2season[rrkxip_2season.legbye_runs > 0]
legbyecount = df_legbye['legbye_runs'].count()
dots_t = dots['total_runs'].count() - legbyecount - byecount
print("Total dots =",dots_t)
totalmatch = df_season_record_df['id'].count()
print("Total matches =",totalmatch)
avg_dots= (dots_t/totalmatch).round()
print("Avg dots per match =",avg_dots)


# In[16]:


## Dots including legbyes & byes balls all season's h2h
dots_all = rrkxip[rrkxip.total_runs == 0]
dots_all_t = dots_all['total_runs'].count()
print("Total dots =",dots_all_t)
totalmatch_all = kxiprr['id'].count()
print("Total matches =",totalmatch_all)
avg_dots_all= (dots_all_t/totalmatch_all).round()
print("Avg dots per match =",avg_dots_all)


# In[17]:


## Dots excluding legbyes & byes balls all season's h2h
df_bye = rrkxip[rrkxip.bye_runs > 0]
byecount = df_bye['bye_runs'].count()
df_legbye = rrkxip[rrkxip.legbye_runs > 0]
legbyecount = df_legbye['legbye_runs'].count()
dots_all = rrkxip[rrkxip.total_runs == 0]
dots_all_t = dots_all['total_runs'].count() - legbyecount - byecount
print("Total dots =",dots_all_t)
totalmatch_all = kxiprr['id'].count()
print("Total matches =",totalmatch_all)
avg_dots_all= (dots_all_t/totalmatch_all).round()
print("Avg dots per match =",avg_dots_all)


# # Q2.

# In[18]:


## Last 2 season overall ratio
def batsman(batsman_name):
 batsman = rrkxip_2season[rrkxip_2season.batsman == batsman_name]
 boundary_runs = batsman[batsman.batsman_runs >= 4]
 final_boundary_runs = boundary_runs['batsman_runs'].sum()
 total_runs = batsman['batsman_runs'].sum()
 ratio = (final_boundary_runs/total_runs).round(3)
 print(batsman_name)
 print(ratio)


# In[19]:


## RR batsman
batsman('JC Buttler')
batsman('BA Stokes')
batsman('SPD Smith')
batsman('SV Samson')
batsman('S Gopal')
batsman('J Archer')


# In[20]:


## KXIP batsman
batsman('CH Gayle')
batsman('KL Rahul')
batsman('N Pooran')
batsman('MA Agarwal')
batsman('Mandeep Singh')


# In[21]:


## For other batsman for KXIP
def batsman(batsman_name):
 batsman = deliveries[deliveries.batsman == batsman_name]
 batsman_final = batsman[batsman.bowling_team == 'Rajasthan Royals']
 boundary_runs = batsman_final[batsman_final.batsman_runs >= 4]
 final_boundary_runs = boundary_runs['batsman_runs'].sum()
 total_runs = batsman_final['batsman_runs'].sum()
 ratio = (final_boundary_runs/total_runs).round(3)
 print(batsman_name)
 print(ratio)


# In[22]:


## For maxwell
batsman('GJ Maxwell')


# In[23]:


## For other batsman for RR
def batsman(batsman_name):
 batsman = deliveries[deliveries.batsman == batsman_name]
 batsman_final = batsman[batsman.bowling_team == 'Kings XI Punjab']
 boundary_runs = batsman_final[batsman_final.batsman_runs >= 4]
 final_boundary_runs = boundary_runs['batsman_runs'].sum()
 total_runs = batsman_final['batsman_runs'].sum()
 ratio = (final_boundary_runs/total_runs).round(3)
 print(batsman_name)
 print(ratio)


# In[24]:


## For Uthappa & Tewatia
batsman('RV Uthappa')
batsman('R Tewatia')


# # Q3.

# In[25]:


# OPP of players for batsman for last 2 seasons.
def OPP(name):
     player = rrkxip_2season[rrkxip_2season.batsman == name]
     runs = player['total_runs'].sum()-player['extra_runs'].sum()
     boundaries = player[player.batsman_runs >= 4]
     boundaries_runs = boundaries['batsman_runs'].sum()
     ones_twos=player['total_runs'].sum()-player['extra_runs'].sum()-boundaries['batsman_runs'].sum()
     total_balls= player['ball'].count()- player['wide_runs'].sum() - player['noball_runs'].sum()
     y=ones_twos
     z=runs/total_balls
     x=(z+boundaries_runs-y)/total_balls
     print('The OPP for', name, 'is', x.round(2))


# In[26]:


OPP('JC Buttler')
OPP('BA Stokes')
OPP('SPD Smith')
OPP('SV Samson')
OPP('S Gopal')
OPP('J Archer')
OPP('CH Gayle')
OPP('KL Rahul')
OPP('N Pooran')
OPP('MA Agarwal')
OPP('Mandeep Singh')


# In[27]:


# OPP of players for bowlers for last 2 seasons.
def OPP_bowlers(bowlername):
 bowler= rrkxip_2season[rrkxip_2season.bowler == bowlername]
 boundary_runs = bowler[bowler.batsman_runs >= 4]
 boundary_runs_final=boundary_runs['batsman_runs'].sum()
 boundary_count = boundary_runs['batsman_runs'].count()
 balls = bowler['ball'].count() 
 opp = (boundary_runs_final/boundary_count)/(balls)
 print("OPP for bowler of",bowlername,'is',opp.round(2))   


# In[28]:


OPP_bowlers('J Archer')
OPP_bowlers('Mohammed Shami')
OPP_bowlers('BA Stokes')
OPP_bowlers('S Gopal')

