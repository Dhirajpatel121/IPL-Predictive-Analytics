#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


deliveries = pd.read_csv('C:/Users/SONY/Desktop/IPL/deliveries.csv')


# In[4]:


deliveries


# In[5]:


matches = pd.read_csv('C:/Users/SONY/Desktop/IPL/matches.csv')


# In[6]:


matches


# In[7]:


# Replacing DD with DC in deliveries dataset
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[8]:


# Replacing DD with DC in matches dataset
matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[10]:


#### Records of DC vs RR (matches dataset)
dcrr=matches[np.logical_or(np.logical_and(matches['team1']=='Delhi Capitals',matches['team2']=='Rajasthan Royals'),np.logical_and(matches['team2']=='Delhi Capitals',matches['team1']=='Rajasthan Royals'))]


# In[11]:


dcrr


# In[12]:


# Head to head DC vs RR
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(dcrr['winner'],order=dcrr['winner'].value_counts().index)
plt.text(-0.1,7,str(dcrr['winner'].value_counts()['Rajasthan Royals']),size=29,color='white')
plt.text(0.9,2,str(dcrr['winner'].value_counts()['Delhi Capitals']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('DC vs RR - head to head')
plt.show()


# ### DELHI HAVE WON 9 OUT 20 GAMES WHERE AS RAJASTHAN HAVE WON 11

# In[15]:


# Previous 2 season's record of Head to head (RR didnt played in 2016,2017)
df = dcrr[['season','winner','id']]
df[df['season'] >= 2016]


# ### ALTHOUGH RAJASTHAN HAVE DOMINATED OVERALL HEAD TO HEAD,DELHI CAPITALS HAVE WON 3 OUT LAST 4 MATCHES PLAYED AGAINST RAJASTHAN ROYALS.(WIN RATIO : 75%)
# ### HENCE ACCORDING TO PREDICTION OF LAST 2 SEASON'S AND CURRENT FORM DELHI CAPITALS WILL WIN TODAY'S MATCH AGAINST RR.

# In[16]:


#For deliveries dataset
rrdc=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Delhi Capitals',deliveries['bowling_team']=='Rajasthan Royals'),np.logical_and(deliveries['bowling_team']=='Delhi Capitals',deliveries['batting_team']=='Rajasthan Royals'))]
rrdc


# In[18]:


dcrr[dcrr['season'] >= 2016]


# # Checking out the match id which will be used for deliveries dataset to retrieve player's information in last 2 years (Here id >= 7899)

# In[19]:


# Previous 2 years data from deliveries dataset
filtered_2years = rrdc[rrdc['match_id'] >= 7899]
filtered_2years


# In[21]:


## No. of runs scored by Smith against DC
## Considering 2 years data of previous season (played only 1 match)
smith_total_runs = filtered_2years[filtered_2years['batsman'].str.contains("SPD Smith")].sum()['batsman_runs']
smith_total_matches = filtered_2years[filtered_2years['batsman'].str.contains("SPD Smith")].nunique()['match_id']
Average_score=(smith_total_runs/smith_total_matches).round(3)
print("Smith runs against DC in 2018-2019 season =",smith_total_runs)
print("Smith total matches against DC in season 2018-19 =",smith_total_matches)
print("Average_score of Smith against DC = ",Average_score)


# In[32]:


## No. of runs scored by Smith against DC in all season's (Played only two games)
smith_total_runs = rrdc[rrdc['batsman'].str.contains("SPD Smith")].sum()['batsman_runs']
smith_total_matches = rrdc[rrdc['batsman'].str.contains("SPD Smith")].nunique()['match_id']
Average_score=(smith_total_runs/smith_total_matches).round(3)
print("Smith runs against DC across all seasons =",smith_total_runs)
print("Smith total matches against DC across all seasons =",smith_total_matches)
print("Average_score of Smith against DC = ",Average_score)


# ## Considering the Steve Smith record against RR in last 2 season. It has been 51.
# ## So, according to prediction Steve Smith will score 41 or more runs in today's match.

# In[23]:


# No of wides in last 2 season's matches played between DC and RR.
wide_balls = filtered_2years['wide_runs'].sum()
Total_matches_headtohead = filtered_2years['match_id'].nunique()
Average_wideballs = wide_balls/Total_matches_headtohead
print("Total number of wide balls in DC vs RR matches =",wide_balls)
print("Total matches head to head =",Total_matches_headtohead)
print("Average number of wide balls per match in DC vs RR match =",Average_wideballs)


# In[33]:


# No of wides across all seasons between DC and RR.
wide_balls = rrdc['wide_runs'].sum()
Total_matches_headtohead = rrdc['match_id'].nunique()
Average_wideballs = wide_balls/Total_matches_headtohead
print("Total number of wide balls in DC vs RR matches =",wide_balls)
print("Total matches head to head =",Total_matches_headtohead)
print("Average number of wide balls per match in DC vs RR match =",Average_wideballs)


# ## Avg.  number of  Wide balls that have been bowled across all season's is 8.35 & across last 2 season's it has been 6.5 . 
# ## Hence, According to the prediction 6 or more wides balls will be bowled in today's match.

# In[39]:


wickets = filtered_2years['player_dismissed'].value_counts()
wickets


# In[40]:


# Total wickets fallen in DC vs RR match in season 2018-2019
wickets_final = wickets.sum()
Total_matches_headtohead = filtered_2years['match_id'].nunique()
Average_wickets = wickets_final/Total_matches_headtohead
print("Total wickets fallen =",wickets_final)
print("Total matches head to head in last 2 season's =",Total_matches_headtohead)
print("Average number of wickets fallen in RR vs DC match =",Average_wickets)


# In[45]:


wickets_all_season = rrdc['player_dismissed'].value_counts()
wicket_all_df = wickets_all_season.sum()


# In[48]:


# Total wickets fallen in DC vs RR match across all season's
wicket_all_df = wickets_all_season.sum() 
Total_matches_headtohead = rrdc['match_id'].nunique()
Average_wickets = wicket_all_df/Total_matches_headtohead
print("Total wickets fallen =",wicket_all_df)
print("Total matches head to head across all seasons's =",Total_matches_headtohead)
print("Average number of wickets fallen in RR vs DC match =",Average_wickets)


# ## In average 11 wickets have fallen in DC vs RR matches. 
# ## Hence, according to prediction the number of wickets that would fall today will be in range 11-15

# In[59]:


## Powerplay runs for DC in last 2 season's against RR
filtered_powerplayover = filtered_2years[filtered_2years['over'] <= 6]
delhi_pp = filtered_powerplayover[filtered_powerplayover['batting_team']== 'Delhi Capitals']
final_runs = delhi_pp['total_runs'].sum()
Total_matches_headtohead = filtered_2years['match_id'].nunique()
Average_runs_pp = final_runs/Total_matches_headtohead
Average_runs_pp


# In[62]:


# Average runs for DC in pp against RR
filtered_powerplayover = rrdc[rrdc['over'] <= 6]
delhi_pp = filtered_powerplayover[filtered_powerplayover['batting_team']== 'Delhi Capitals']
final_runs = delhi_pp['total_runs'].sum()
Total_matches_headtohead1= rrdc['match_id'].nunique()
Average_runs = final_runs/Total_matches_headtohead1  
Average_runs


# ## Considering the overall average powerplay score of DC against RR. It has been 47.65 ~ 48 & also the factor of recent form in 2020 they have an average score of 40-42 in powerplay as well.
# ## Hence, according to prediction dc will score 41-50 runs in powerplay.
