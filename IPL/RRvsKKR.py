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


#### Records of RR vs KKR(matches dataset)
rrkkr =matches[np.logical_or(np.logical_and(matches['team1']=='Rajasthan Royals',matches['team2']=='Kolkata Knight Riders'),np.logical_and(matches['team2']=='Rajasthan Royals',matches['team1']=='Kolkata Knight Riders'))]
rrkkr


# # Q1.

# In[5]:


# Head to head RR vs KKR across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(rrkkr['winner'],order=rrkkr['winner'].value_counts().index)
plt.text(-0.1,5,str(rrkkr['winner'].value_counts()['Rajasthan Royals']),size=29,color='black')
plt.text(0.9,5,str(rrkkr['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RR vs KKR - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =rrkkr[rrkkr['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head RR vs KKR across last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1.5,str(df_season_record_df['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.text(0.9,0.3,str(df_season_record_df['winner'].value_counts()['Rajasthan Royals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RR vs KKR- head to head last 2 season')
plt.show()


# In[8]:


#For deliveries dataset
kkr_rr=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Rajasthan Royals',deliveries['bowling_team']== 'Kolkata Knight Riders'),np.logical_and(deliveries['bowling_team']=='Rajasthan Royals',deliveries['batting_team']=='Kolkata Knight Riders'))]
kkr_rr 


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
kkr_rr_2season = kkr_rr[kkr_rr['match_id'] >= 7932]
kkr_rr_2season


# # Q2.

# In[10]:


# Total wickets fallen in KKR vs RR match in season 2018-2019
wickets = kkr_rr_2season['player_dismissed'].value_counts()
wickets_final = wickets.sum()
Total_matches_headtohead = kkr_rr_2season['match_id'].nunique()
Average_wickets = wickets_final/Total_matches_headtohead
print("Total wickets fallen =",wickets_final)
print("Total matches head to head in last 2 season's =",Total_matches_headtohead)
print("Average number of wickets fallen in KKR vs RR match =",Average_wickets.round())


# In[11]:


# Total wickets fallen in KKR vs RR match across all season's
wickets_all_season = kkr_rr['player_dismissed'].value_counts()
wicket_all_df = wickets_all_season.sum()
Total_matches_headtohead = kkr_rr['match_id'].nunique()
Average_wickets = wicket_all_df/Total_matches_headtohead
print("Total wickets fallen =",wicket_all_df)
print("Total matches head to head across all seasons's =",Total_matches_headtohead)
print("Average number of wickets fallen in RR vs KKR match =",Average_wickets.round())


# # Q3.

# In[12]:


## Last 2 season overall ratio
def batsman(batsman_name):
 batsman = kkr_rr_2season[kkr_rr_2season.batsman == batsman_name]
 boundary_runs = batsman[batsman.batsman_runs >= 4]
 nonboundary_runs = batsman[batsman.batsman_runs < 4]
 final_nonboundary_runs = nonboundary_runs['batsman_runs'].sum()
 final_boundary_runs = boundary_runs['batsman_runs'].sum()
 total_runs = batsman['batsman_runs'].sum()
 ratio = ((final_boundary_runs-final_nonboundary_runs)/total_runs).round(3)
 print(batsman_name,'ratio =',ratio)


# In[13]:


## RR batsman
batsman('JC Buttler')
batsman('BA Stokes')
batsman('SPD Smith')
batsman('SV Samson')
batsman('S Gopal')
batsman('J Archer')


# In[14]:


## KKR Batsman
batsman('AD Russell')
batsman('KD Karthik')
batsman('N Rana')
batsman('SP Narine')
batsman('S Gill')
batsman('R Singh')


# In[15]:


## For other batsman for RR & KKR
def batsman(batsman_name):
 batsman = deliveries[deliveries.batsman == batsman_name]
 boundary_runs = batsman[batsman.batsman_runs >= 4]
 nonboundary_runs = batsman[batsman.batsman_runs < 4]
 final_nonboundary_runs = nonboundary_runs['batsman_runs'].sum()
 final_boundary_runs = boundary_runs['batsman_runs'].sum()
 total_runs = batsman['batsman_runs'].sum()
 ratio = ((final_boundary_runs-final_nonboundary_runs)/total_runs).round(3)
 print(batsman_name,'ratio =',ratio)


# In[16]:


## For Uthappa & Tewatia
batsman('RV Uthappa')
batsman('R Tewatia')


# In[17]:


## For Morgan,Tripathi,Cummins
batsman('EJG Morgan')
batsman('PJ Cummins')
batsman('RA Tripathi')


# # Q5.

# In[18]:


## Economy rate less than 8 for all bowlers in H2H of RR vs KKR in last 2 season's
economyrate_season = pd.DataFrame(kkr_rr_2season.groupby(['bowler']).agg({'total_runs' : 'sum','ball' : 'count'}))
economyrate_season['Economy Rate'] = 6*economyrate_season['total_runs']/economyrate_season['ball']
economyrate_season = economyrate_season.sort_values(by ='Economy Rate' , ascending = False)
x = economyrate_season[(economyrate_season['Economy Rate'] <8) & (economyrate_season['ball'] > 20)]
x.round(1)


# # Q4.

# In[19]:


## Jofra Archer economy rate and boundary conceded last 2 season's against KKR
jofra = kkr_rr_2season[kkr_rr_2season.bowler == 'J Archer']
jofra_matches_all = jofra['match_id'].nunique()
total_runs_conceded = jofra['batsman_runs'].sum() 
total_balls=jofra['ball'].count() - jofra[jofra.wide_runs >= 1].count() - jofra[jofra.noball_runs >= 1].count()
total_balls_df = total_balls['ball']
boundary_conceded = jofra[jofra.batsman_runs >= 4]
boundary_conceded_final = boundary_conceded['batsman_runs'].count()
avg_boundary = (boundary_conceded_final/jofra_matches_all).round(1)
print('Jofra Archer Average Economy rate =',((total_runs_conceded/total_balls_df)*6).round(2))
print('Average Boundaries conceded =',avg_boundary)


# In[20]:


## Jofra Archer economy rate and boundary conceded last 2 season's against all teams
jofra = deliveries[deliveries.bowler == 'J Archer']
jofra_matches_all = jofra['match_id'].nunique()
total_runs_conceded = jofra['batsman_runs'].sum() 
total_balls=jofra['ball'].count() - jofra[jofra.wide_runs >= 1].count() - jofra[jofra.noball_runs >= 1].count()
total_balls_df = total_balls['ball']
boundary_conceded = jofra[jofra.batsman_runs >= 4]
boundary_conceded_final = boundary_conceded['batsman_runs'].count()
avg_boundary = (boundary_conceded_final/jofra_matches_all).round(1)
print('Jofra Archer Average Economy rate =',((total_runs_conceded/total_balls_df)*6).round(2))
print('Average Boundaries conceded =',avg_boundary)

