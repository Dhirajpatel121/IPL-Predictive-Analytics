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


## Replacing Delhi Daredevils with Delhi Capitals
matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[5]:


#### Records of RCB vs DC(matches dataset)
rcbdc =matches[np.logical_or(np.logical_and(matches['team1']=='Royal Challengers Bangalore',matches['team2']=='Delhi Capitals'),np.logical_and(matches['team2']=='Royal Challengers Bangalore',matches['team1']=='Delhi Capitals'))]
rcbdc


# # Q1.

# In[6]:


# Head to head RCB vs DC across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(rcbdc['winner'],order=rcbdc['winner'].value_counts().index)
plt.text(-0.1,5,str(rcbdc['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='black')
plt.text(0.9,5,str(rcbdc['winner'].value_counts()['Delhi Capitals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('DC vs RCB - head to head')
plt.show()


# In[7]:


#H2H previous 2 season's
df_season_record =rcbdc[rcbdc['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[8]:


# Head to head DC vs RCB across last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1.5,str(df_season_record_df['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='black')
plt.text(0.9,1.5,str(df_season_record_df['winner'].value_counts()['Delhi Capitals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RCB vs DC - head to head last 2 season')
plt.show()


# In[9]:


#For deliveries dataset
dcrcb=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Royal Challengers Bangalore',deliveries['bowling_team']== 'Delhi Capitals'),np.logical_and(deliveries['bowling_team']=='Royal Challengers Bangalore',deliveries['batting_team']=='Delhi Capitals'))]
dcrcb 


# In[10]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
dcrcb_2season = dcrcb[dcrcb['match_id'] >= 7912]
dcrcb_2season


# # Q3.

# In[11]:


## Rabada's Record against RCB
def match(matchid):
 rabada = dcrcb_2season[dcrcb_2season.bowler == 'K Rabada']
 rabada_matchid = rabada[rabada.match_id == matchid]
 print(rabada_matchid[['match_id','over','ball','player_dismissed']])


# In[12]:


match(11311)


# In[13]:


match(11337)


# ## Took wicket in 1st over 7th ball and second over 11th ball in two matches h2h

# # Q2.

# In[14]:


## Strikerate
batsmen_strikerate_season = pd.DataFrame(dcrcb_2season.groupby(['batsman']).agg({'batsman_runs' : 'sum','ball' : 'count'}))
batsmen_strikerate_season['Strike Rate'] = batsmen_strikerate_season['batsman_runs']/batsmen_strikerate_season['ball']*100
batsmen_strikerate_season = batsmen_strikerate_season.sort_values(by ='Strike Rate' , ascending = False)
batsmen_strikerate_season[(batsmen_strikerate_season['Strike Rate'] >= 130) & (batsmen_strikerate_season['ball'] > 39)] 


# In[48]:


# Average fours
def batsman(batsman_name):
 boundary = dcrcb_2season[dcrcb_2season.batsman_runs == 4]
 player = boundary[boundary.batsman == batsman_name]
 boundaries = player['batsman_runs'].count()
 match = player['match_id'].nunique()
 avg_fours = (boundaries/match).round(1)
 print(batsman_name,'avg fours =',avg_fours)


# In[49]:


batsman('RR Pant')
batsman('SS Iyer')
batsman('AB de Villiers')
batsman('V Kohli')
batsman('Washington Sundar')
batsman('M Ali')
batsman('AR Patel')
batsman('S Dhawan')
batsman('P Shaw')
batsman('S Dube')
batsman('MP Stoinis')


# ## 4 players with SR > 130 & boundary with 2 fours atleast

# ## Q4.

# In[51]:


## Economy rate & dots
economyrate_season = pd.DataFrame(dcrcb_2season.groupby(['bowler']).agg({'total_runs' : 'sum','ball' : 'count'}))
economyrate_season['Economy Rate'] = 6*economyrate_season['total_runs']/economyrate_season['ball']
economyrate_season = economyrate_season.sort_values(by ='Economy Rate' , ascending = True)
economyrate_season[(economyrate_season['Economy Rate'] <= 8) & (economyrate_season['ball'] > 39)] 


# In[55]:


## dot balls
dots=dcrcb_2season[dcrcb_2season.total_runs==0]
dotball_season = pd.DataFrame(dots.groupby(['bowler']).agg({'player_dismissed' : 'count','ball' : 'count','match_id' : 'nunique'}))
dotball_season['Dot_balls'] = dotball_season['ball']/dotball_season['match_id']
dotball_season = dotball_season.sort_values(by ='Dot_balls' , ascending = True)
dotball_season[(dotball_season['Dot_balls'] >= 8)]


# In[57]:


## boundaries conceded
boundaries=dcrcb_2season[dcrcb_2season.total_runs>=4]
boundaries_season = pd.DataFrame(boundaries.groupby(['bowler']).agg({'ball' : 'count','match_id' : 'nunique'}))
boundaries_season['average_boundaries'] = boundaries_season['ball']/dotball_season['match_id']
boundaries_season = boundaries_season.sort_values(by ='average_boundaries' , ascending = True)
boundaries_season[(boundaries_season['average_boundaries'] < 4)]


# ### 3 player's matching the given conditions.
