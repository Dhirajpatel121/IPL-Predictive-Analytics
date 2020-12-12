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


#### Records of MI vs SRH (matches dataset)
misrh =matches[np.logical_or(np.logical_and(matches['team1']=='Sunrisers Hyderabad',matches['team2']=='Mumbai Indians'),np.logical_and(matches['team2']=='Sunrisers Hyderabad',matches['team1']=='Mumbai Indians'))]
misrh


# # Q1.

# In[5]:


# Head to head MI vs SRH across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(misrh['winner'],order=misrh['winner'].value_counts().index)
plt.text(-0.1,4,str(misrh['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.9,4,str(misrh['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs SRH - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =misrh[misrh['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


# Head to head MI vs SRH across last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1,str(df_season_record_df['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.9,1,str(df_season_record_df['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs SRH - head to head last 2 season')
plt.show()


# In[8]:


#For deliveries dataset
srhmi=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Mumbai Indians',deliveries['bowling_team']== 'Sunrisers Hyderabad'),np.logical_and(deliveries['bowling_team']=='Mumbai Indians',deliveries['batting_team']=='Sunrisers Hyderabad'))]
srhmi 


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
srhmi_2season = srhmi[srhmi['match_id'] >= 7900]
srhmi_2season


# # Q5.

# In[10]:


# Total wickets fallen in MI vs SRH match in season 2018-2019
wickets = srhmi_2season['player_dismissed'].value_counts()
wickets_final = wickets.sum()
Total_matches_headtohead = srhmi_2season['match_id'].nunique()
Average_wickets = wickets_final/Total_matches_headtohead
print("Total wickets fallen =",wickets_final)
print("Total matches head to head in last 2 season's =",Total_matches_headtohead)
print("Average number of wickets fallen in MI vs SRH match =",Average_wickets.round())


# In[11]:


# Total wickets fallen in MI vs SRH match across all season's
wickets_all_season = srhmi['player_dismissed'].value_counts()
wicket_all_df = wickets_all_season.sum()
Total_matches_headtohead = srhmi['match_id'].nunique()
Average_wickets = wicket_all_df/Total_matches_headtohead
print("Total wickets fallen =",wicket_all_df)
print("Total matches head to head across all seasons's =",Total_matches_headtohead)
print("Average number of wickets fallen in MI vs SRH match =",Average_wickets.round())


# # Q3.

# In[12]:


## Computing smash rate for last 2 season's h2h matches 
def player(batsman_name):
 player = srhmi_2season[srhmi_2season.batsman == batsman_name]
 boundary = player[player.batsman_runs >= 4]
 boundary_final = boundary['batsman_runs'].count()
 noball = player[player.noball_runs >= 1]
 wides = player[player.wide_runs >= 1]
 balls = player['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
 Smashrate = ((boundary_final/balls)*100).round()
 print("Smash rate of",batsman_name,'is =',Smashrate)


# In[13]:


## For MI players
player('RG Sharma')
player('Ishan Kishan')
player('KA Pollard')
player('HH Pandya')
player('KH Pandya')
player('AS Yadav')
player('Q de Kock')


# In[14]:


## For SRH players
player('WP Saha')
player('DA Warner')
player('J Bairstow')
player('KS Williamson')
player('MK Pandey')
player('V Shankar')


# # Q4.

# In[15]:


## Computing Boundary Leaker for h2h of last 2 season's
def BL(bowler_name):
 player = srhmi_2season[srhmi_2season.bowler == bowler_name]
 noball = player[player.noball_runs >= 1]
 wides = player[player.wide_runs >= 1]
 balls = player['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
 boundary_given = player[player.batsman_runs >= 4]['batsman_runs'].count()
 BoundaryLeaker = (1/(balls/boundary_given+1))
 print("BL score for",bowler_name,'is =',BoundaryLeaker.round(2))


# In[16]:


BL('KH Pandya')
BL('JJ Bumrah')
BL('Rashid Khan')
BL('RD Chahar')
BL('V Shankar')
BL('KA Pollard')


# In[17]:


## For other bowlers 
def BLO(bowler_name):
 team = deliveries[deliveries.batting_team == 'Sunrisers Hyderabad']
 player = team[team.bowler == bowler_name]
 noball = player[player.noball_runs >= 1]
 wides = player[player.wide_runs >= 1]
 balls = player['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
 boundary_given = player[player.batsman_runs >= 4]['batsman_runs'].count()
 BoundaryLeaker = (1/(balls/boundary_given+1))
 print("BL score for",bowler_name,'is =',BoundaryLeaker.round(2))


# In[18]:


## MI bowlers
BLO('TA Boult')
BLO('DS Kulkarni')
BLO('NM Coulter-Nile')


# In[19]:


## For other bowlers 
def BLOSRH(bowler_name):
 team = deliveries[deliveries.batting_team == 'Mumbai Indians']
 player = team[team.bowler == bowler_name]
 noball = player[player.noball_runs >= 1]
 wides = player[player.wide_runs >= 1]
 balls = player['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
 boundary_given = player[player.batsman_runs >= 4]['batsman_runs'].count()
 BoundaryLeaker = (1/(balls/boundary_given+1))
 print("BL score for",bowler_name,'is =',BoundaryLeaker.round(2))


# In[20]:


BLOSRH('Sandeep Sharma')
BLOSRH("S Nadeem")
BLOSRH('JO Holder')


# # Q2.

# In[27]:


def stamina_score(name):
    player=deliveries[deliveries.batsman==name]
    balls=player['ball'].count()
    runs=player[player.batsman_runs>=1]
    total_runs=runs['batsman_runs'].sum()
    df=player[player.batsman_runs>=4]
    boundaries=df['batsman_runs'].sum()
    singles=player[player.batsman_runs<4]
    non_boundaries= singles['batsman_runs'].sum()
    crease=deliveries[(deliveries.batsman==name) | (deliveries.non_striker==name)]
    balls_crease=crease['ball'].count()
    x=(non_boundaries/(boundaries+1))
    y=(balls/balls_crease)
    stamina=((x+y)/total_runs)
    print("The stamina_score for",name,"is",stamina.round(6))


# In[31]:


stamina_score('AS Yadav')
stamina_score('RG Sharma')
stamina_score('Ishan Kishan')
stamina_score('KA Pollard')
stamina_score('HH Pandya')
stamina_score('KH Pandya')
stamina_score('Q de Kock')
stamina_score('WP Saha')
stamina_score('DA Warner')
stamina_score('J Bairstow')
stamina_score('KS Williamson')
stamina_score('MK Pandey')
stamina_score('V Shankar')

