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


## Replacing Delhi Daredevils with Delhi Capitals in Matches & Deliveries dataset
matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[5]:


## Record at Dubai stadium in 2020 ipl season
Dubai_2020 = pd.read_csv('C:/Users/SONY/Desktop/IPL/Dubai.csv')
Dubai_2020


# In[6]:


#### Records of MI vs DC (matches dataset) (2008-2019)
midc=matches[np.logical_or(np.logical_and(matches['team1']=='Mumbai Indians',matches['team2']=='Delhi Capitals'),np.logical_and(matches['team2']=='Mumbai Indians',matches['team1']=='Delhi Capitals'))]
midc


# In[7]:


#For deliveries dataset
dcmi=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Mumbai Indians',deliveries['bowling_team']=='Delhi Capitals'),np.logical_and(deliveries['bowling_team']=='Mumbai Indians',deliveries['batting_team']=='Delhi Capitals'))]
dcmi


# In[8]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
dcmi_2season = dcmi[dcmi['match_id'] >= 7902]
dcmi_2season


# # Toss Decision & average winning/par score

# In[9]:


## What's an ideal winning score/par score at Dubai?
runs = Dubai_2020['Winner Score'].sum()
matches = Dubai_2020['Matchno'].nunique()
avg_winning_score = runs/matches
print('Average winning/par score at Dubai is =',avg_winning_score.round())


# ### If Batting first,average winning/par score should be anywhere above 170.

# In[10]:


Toss_win_winner= Dubai_2020[Dubai_2020.Toss == Dubai_2020.Winner]
Toss_win_winner[['Toss','TossDecision','Winner','Winner Score']]


# ### Looking at recent 3 Matches at Dubai the team that has won toss & fielded first have won.
# ### Hence,the if we win the toss we should field first. 

# # Match-ups for DC batsman (Which type of bowler to bowl to whom?)

# In[11]:


def player(playername):
 player = dcmi_2season[dcmi_2season.batsman == playername]
 dismissal_record = player.dropna()
 records= dismissal_record[['bowler','dismissal_kind']]
 print('Dismissal record of',playername,':',records)


# ## For MI vs DC matches last 2 season h2h

# In[12]:


player('S Dhawan')


# In[13]:


player('SS Iyer')


# In[14]:


player('RR Pant')


# In[15]:


player('AR Patel')


# In[16]:


player('P Shaw')


# ## For Stoinis & Rahane 

# In[17]:


## For other batsman of DC (Rahane & Stoinis)
def other(playername):
 df = deliveries[deliveries.bowling_team == 'Mumbai Indians']   
 player = df[df.batsman == playername]
 dismissal_record = player.dropna()
 records= dismissal_record[['bowler','dismissal_kind']]
 print('Dismissal record of',playername,':',records)


# In[18]:


other('MP Stoinis')


# In[19]:


other('R Ashwin')


# In[20]:


other('AM Rahane')


# ## For all season's against MI,Records of DC Batsman

# In[21]:


other('S Dhawan')
print('------')
other('SS Iyer')
print('------')
other('P Shaw')
print('------')
other('RR Pant')
print('------')
other('AR Patel')


# # Match-ups for MI batsman (Which bowler to attack & which bowler to defend)

# In[22]:


def MI(playername):
 player = dcmi_2season[dcmi_2season.batsman == playername]
 dismissal_record = player.dropna()
 records= dismissal_record[['bowler','dismissal_kind']]
 print('Dismissal record of',playername,':',records)


# In[23]:


MI('RG Sharma')
print('------')
MI('AS Yadav')
print('------')
MI('Ishan Kishan')
print('------')
MI('HH Pandya')
print('------')
MI('KA Pollard')
print('------')
MI('KH Pandya')
print('------')
MI('Q de Kock')


# ## Apart from 3 dismissal against(Mishra,Lamichanne,AR Patel) out of which 2 are not playing because of injury/transfer,it would be ideal to attack the spinners for MI to gain momentum/score quick runs.

# In[24]:


## Checking out Ashwin record against MI
mi = deliveries[deliveries.batting_team == 'Mumbai Indians']
ashwin = mi[mi.bowler == 'R Ashwin']
wickets = ashwin['player_dismissed'].count()
matches = ashwin['match_id'].nunique()
avg_wickets_againstMI = wickets/matches
print('Avg wickets = ',avg_wickets_againstMI.round(1))
runsconceded = ashwin['total_runs'].sum()
noball = ashwin[ashwin.noball_runs >= 1]
wides = ashwin[ashwin.wide_runs >= 1]
legit_balls = ashwin['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
Economyrate = (runsconceded/legit_balls)*6
print('Economy Rate of Ashwin against MI =',Economyrate.round(1))


# ## Although ashwin has a ER below 7,he has avg wickets which is less than 1(so in avg 0-1 wickets per match).Hence,calculated risk against Ashwin would be ideal to score runs against him.

# In[25]:


## Records of Rabada against MI
mi = dcmi_2season[dcmi_2season.batting_team == 'Mumbai Indians']
Rabada = mi[mi.bowler == 'K Rabada']
filtered = Rabada.dropna()
print('Rabada Record against MI',filtered[['bowler','player_dismissed','over']])
print('----------------------------------')
runsconceded = Rabada['total_runs'].sum()
noball = Rabada[Rabada.noball_runs >= 1]
wides = Rabada[Rabada.wide_runs >= 1]
legit_balls = Rabada['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
Economyrate = (runsconceded/legit_balls)*6
print('Economy Rate of Rabada against MI =',Economyrate.round(1))


# ## Taken all of his wickets in death overs.

# In[26]:


## Which player has max. contribution for DC
def playern(playername):
 dc_score=dcmi_2season[dcmi_2season.batting_team=='Delhi Capitals'].sum()['total_runs']
 average_score=dc_score/dcmi_2season['match_id'].nunique()
 print("DC average score against MI is =",average_score.round(2))

 dc_player=dcmi_2season[dcmi_2season.batsman == playername] 
 dc_player_runs=dc_player['batsman_runs'].sum()
 print(playername,"runs against MI is =",dc_player_runs)

 matches_played=dc_player['match_id'].nunique()
 print('Matches played by',playername, 'against MI is =' ,matches_played)
 average=dc_player_runs/matches_played ;
 print('Average score of',playername,'against MI =',average.round(2))
 contribution_player=(average*100/average_score)
 print('The % contribution of',playername,'in total DC runs =',contribution_player.round())


# In[27]:


playern('SS Iyer')
print('--------------------------------')
playern('RR Pant')
print('--------------------------------')
playern('P Shaw')
print('--------------------------------')
playern('S Dhawan')
print('--------------------------------')
playern('AR Patel')


# ## Pant & Dhawan has highest contribution

# In[28]:


## Which over does DC score most,the phase in which MI can try to concede minimum runs?
delhi = dcmi_2season[dcmi_2season.batting_team == 'Delhi Capitals']
powerplay_overs = delhi[delhi.over <= 6]
pp_runs = powerplay_overs['total_runs'].sum()
match = delhi['match_id'].nunique()
avg_pp_runs = pp_runs/match
middleovers=delhi[(delhi.over > 6) & (delhi.over< 15)]
middle_runs = middleovers['total_runs'].sum()
middle_avg_runs = middle_runs/match
death_over = delhi[delhi.over >= 15]
death_runs = death_over['total_runs'].sum()
death_avg_runs = death_runs/match
print('Powerplay runs overs 1-6 for DC =',avg_pp_runs.round())
print('Middleover runs overs 7-14 for DC =',middle_avg_runs.round()) 
print('Death over runs overs 15-20 for DC =',death_avg_runs.round())


# ## MI have conceded most runs in death overs at an average of 74 in last 4 games against DC.Hence,death overs must be bowled by best bowlers of MI.

# In[29]:


## Who conceded least runs for MI in death overs,retrieving for current bowlers
def miplayer(player):
 delhi = dcmi[dcmi.batting_team == 'Delhi Capitals']
 death_over = delhi[delhi.over >= 15]
 bowler = death_over[death_over.bowler == player]
 conceded = bowler['batsman_runs'].sum()
 noball = bowler[bowler.noball_runs >= 1]
 wides = bowler[bowler.wide_runs >= 1]
 legit_balls = bowler['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
 Economy = (conceded/legit_balls)*6
 print('Economy of',player,'in death overs against DC is =',Economy.round(1))


# In[30]:


miplayer('JJ Bumrah')
miplayer('KH Pandya')
miplayer('HH Pandya')
miplayer('KA Pollard')
miplayer('RD Chahar')


# In[31]:


## For trent boult against MI which he played with DC
def dcplayer(player):
 delhi = deliveries[deliveries.batting_team == 'Mumbai Indians']
 death_over = delhi[delhi.over >= 15]
 bowler = death_over[death_over.bowler == player]
 conceded = bowler['batsman_runs'].sum()
 noball = bowler[bowler.noball_runs >= 1]
 wides = bowler[bowler.wide_runs >= 1]
 legit_balls = bowler['ball'].count() - wides['wide_runs'].count() - noball['noball_runs'].count()
 Economy = (conceded/legit_balls)*6
 print('Economy of',player,'in death overs against DC is =',Economy.round(1))


# In[32]:


dcplayer('TA Boult')


# ## Trent boult & bumrah have best economy at death,however krunal and pollard have low economy as well but its because they have bowled hardly 1-2 overs in death.

# In[33]:


## Record of MI bowlers in death in 2020 ipl season
MI_2020 = pd.read_csv('C:/Users/SONY/Desktop/IPL/wickets2020mi.csv')


# In[34]:


## Most wickets for MI season 2020
sns.barplot('total_wickets','bowler',data=MI_2020)


# In[35]:


## Most wickets for MI in death overs season 2020
sns.barplot('death_wickets','bowler',data=MI_2020)


# ## As Delhi have higher scoring rate at death overs,however taking wickets at death is of utmost importance to restrict DC to less total if they bat First.So taking wickets at death would be ideal.According to data Trent boult & Bumrah are best to bowl at death as taking wickets also slows down the scoring rate.
# 
