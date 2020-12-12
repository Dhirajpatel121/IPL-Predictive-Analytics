#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


deliveries = pd.read_csv('C:/Users/SONY/Desktop/IPL/deliveries.csv')
deliveries


# In[3]:


matches = pd.read_csv('C:/Users/SONY/Desktop/IPL/matches.csv')
matches


# In[4]:


# Replacing DD with DC in deliveries dataset
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[5]:


# Replacing DD with DC in matches dataset
matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[6]:


#### Records of Rcb vs Kxip (matches dataset)
kprcb=matches[np.logical_or(np.logical_and(matches['team1']=='Kings XI Punjab',matches['team2']=='Royal Challengers Bangalore'),np.logical_and(matches['team2']=='Kings XI Punjab',matches['team1']=='Royal Challengers Bangalore'))]


# In[7]:


kprcb


# In[8]:


# Head to head rcb vs kxip across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(kprcb['winner'],order=kprcb['winner'].value_counts().index)
plt.text(-0.1,7,str(kprcb['winner'].value_counts()['Royal Challengers Bangalore']),size=29,color='white')
plt.text(0.9,7,str(kprcb['winner'].value_counts()['Kings XI Punjab']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('rcb vs kxip - head to head')
plt.show()


# ## Both team's have won 12-12 matches head to head across all season's.

# In[9]:


#H2H previous 2 season's
df = kprcb[['season','winner','id']]
df1 = df[df['season'] >= 2018]
df1


# ### However, looking at the recent form of two previous season's RCB have dominated KXIP by winning all 4 matches against them.Keeping this in mind & also the recent form in 2020 of RCB & KXIP.
# ### Hence,according to prediction RCB will win the match today looking at recent form in previous season's & current form.

# In[10]:


#For deliveries dataset
rcbkp=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Kings XI Punjab',deliveries['bowling_team']=='Royal Challengers Bangalore'),np.logical_and(deliveries['bowling_team']=='Kings XI Punjab',deliveries['batting_team']=='Royal Challengers Bangalore'))]
rcbkp


# In[75]:


# No balls bowled across all season's
noballs_allseason = rcbkp['noball_runs'].sum()
print("No balls across all season's =",noballs_allseason)
### Total matches all season's
total_matches = kprcb['id'].nunique()
print("Total matches h2h =",total_matches)
total_matches_all = (noballs_allseason/total_matches).round(3)
print("Average no balls per match =",total_matches_all)


# In[76]:


# No balls bowled in last 2 season's
deliveries_2season = rcbkp[rcbkp['match_id'] >= 7901] 
noballs_2season = deliveries_2season['noball_runs'].sum()
print("No balls bowled in last 2 season's =", noballs_2season)
## Total matches played in last 2 season's h2h
total_match_2season = df1['id'].nunique()
print("Total matches played in last 2 season's h2h =", total_match_2season)
average_noballs_2season = noballs_2season/total_match_2season
print("Average no balls bowled in last 2 seasons h2h =",average_noballs_2season)


# ## Considering both the data of recent form in previous season and overall season record,in H2H around 1-2 no balls are bowled.
# ## Hence according to prediction total no balls that would be bowled today will be in range 1-2 .

# In[78]:


### Total sixes all season's
sixes = rcbkp[rcbkp['batsman_runs'] == 6]
total_sixes = sixes['batsman_runs'].count()
print("Total sixes all season's =",total_sixes)
### Total matches all season's
print("Total matches h2h =",total_matches)
average_six_allseason = (total_sixes/ total_matches).round(2)
print("average sixes per match all seasons =",average_six_allseason)


# In[79]:


### Total sixes in last 2 season's
sixes_2season = deliveries_2season[deliveries_2season['batsman_runs'] == 6]
total_sixes_2season = sixes_2season['batsman_runs'].count()
print("Total sixes last 2 season's =",total_sixes_2season)
## Total matches played in last 2 season's h2h
print("Total matches played in last 2 season's h2h =", total_match_2season)
average_six_2season = total_sixes_2season/total_match_2season
print("Average sixes in last 2 seasons h2h =",average_six_2season)


# ## In last 2 season as well as overall season record in h2h,total average sixes scored were 12.
# ## Hence according to prediction sixes that would be scored today will be in range 11-14 .

# In[17]:


partnership_abdkohli =rcbkp[np.logical_or(np.logical_and(rcbkp['batsman']=='AB de Villiers',rcbkp['non_striker']=='V Kohli'),np.logical_and(rcbkp['non_striker']=='AB de Villiers',rcbkp['batsman']=='V Kohli'))]
partnership_abdkohli


# In[81]:


overall_runs_in_partnership =  partnership_abdkohli['total_runs'].sum()
total_matches_together = partnership_abdkohli['match_id'].nunique()
print("Total runs =",overall_runs_in_partnership)
print("Total matches =",total_matches_together)
Average_runs_together_all = (overall_runs_in_partnership/total_matches_together).round(2)
print("Total runs together in a partnership =",Average_runs_together_all)


# In[20]:


partnership_abdkohli_2season = partnership_abdkohli[partnership_abdkohli['match_id'] >= 7901]
partnership_abdkohli_2season


# In[21]:


total_runs_partnership_2season = partnership_abdkohli_2season['total_runs'].sum()
total_matches_partnership_2season = partnership_abdkohli_2season['match_id'].nunique()
print("Total runs scored together in partnership in last 2 season's =",total_runs_partnership_2season)
print("Total matches played together in partnership in last 2 season's =",total_matches_partnership_2season)


# ### In last 2 season's (4 matches) only once ABD & kohli have played together.
# ### However, if we consider the data across all seasons of rcb vs kxip and their partnership their average partnership has been 17.
# ### Further,considering factors of both players agains kxip bowlers in below code.

# In[24]:


# Virat Kohli Record against Kxip bowlers in last 2 seasons
rcbkp1 =rcbkp[rcbkp['match_id'] >= 7901]
rcbkp1[rcbkp1.player_dismissed == 'V Kohli']


# ## V kohli has been dismissed twice by Shami and once by mujeeb in last 2 season's.Also as above we got average of overall season together to be 17.Also their total runs was 120 and they had scored 86 in one inning together so for rest 6 matches when they played together they scored only 34 (i.e. 120-86) runs in 6 matches which gives average to be around 5.So considering the factors of overall season record and matches along with their record against kxip bowlers we predict the score.
# ## Hence, according to prediction the partnership would be in range 0-15 as apart from 1 inning in which they score 86,other innings they scored only 34 runs from 6 matches hence avg around 5.
# ## Hence, 0-15 runs will scored between them in partnership.

# In[88]:


## Wickets lost by kxip in all season's against rcb
Wick_kxip_allseason = rcbkp[rcbkp.batting_team == 'Kings XI Punjab']
Final_wickets = Wick_kxip_allseason['player_dismissed'].count()
print('Total wickets lost by kxip against rcb all season =',Final_wickets)
print("Total matches h2h =",total_matches)
Average_wickets_allseason = Final_wickets/total_matches
print("Average wickets lost by KXIP against RCB in all seasons =",Average_wickets_allseason)


# In[91]:


## Wickets lost by kxip in last 2 season's against rcb
Wick_kxip_2season = deliveries_2season[deliveries_2season.batting_team == 'Kings XI Punjab']
Final_wickets_2season = Wick_kxip_2season['player_dismissed'].count()
print('Total wickets lost by kxip against rcb last 2 seasons =',Final_wickets_2season) 
print("Total matches played in last 2 season's h2h =", total_match_2season)
Average_wickets_2season = (Final_wickets_2season/total_match_2season).round(2)
print("Average wickets lost by KXIP against RCB in all seasons =",Average_wickets_2season)


# ## Considering,the data of previous two season's as well overall season of h2h,KXIP have lost in average 6-8 wickets against RCB.
# ## Hence according to prediction KXIP will lose wickets in range of 6-8 .
