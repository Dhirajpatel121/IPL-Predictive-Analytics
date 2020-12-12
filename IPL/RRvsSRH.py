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


#### Records of RR vs SRH (matches dataset)
rrsrh =matches[np.logical_or(np.logical_and(matches['team1']=='Rajasthan Royals',matches['team2']=='Sunrisers Hyderabad'),np.logical_and(matches['team2']=='Rajasthan Royals',matches['team1']=='Sunrisers Hyderabad'))]
rrsrh


# In[5]:


# Head to head SRH vs RR across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(rrsrh['winner'],order=rrsrh['winner'].value_counts().index)
plt.text(-0.1,4,str(rrsrh['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.9,3,str(rrsrh['winner'].value_counts()['Rajasthan Royals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RR vs SRH- head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =rrsrh[rrsrh['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


##### Head to head rr vs srh last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,1.5,str(df_season_record_df['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='black')
plt.text(0.95,0.5,str(df_season_record_df['winner'].value_counts()['Rajasthan Royals']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RR vs SRH - head to head last 2 season')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head,SRH have dominated RR.
# 
# # Hence according to the recent form and analysis SRH will win today's match.

# In[8]:


#For deliveries dataset
srhrr=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Rajasthan Royals',deliveries['bowling_team']== 'Sunrisers Hyderabad'),np.logical_and(deliveries['bowling_team']=='Rajasthan Royals',deliveries['batting_team']=='Sunrisers Hyderabad'))]
srhrr


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
srhrr_2season = srhrr[srhrr['match_id'] >= 7897]
srhrr_2season


# In[10]:


# No balls bowled across all season's
noballs_allseason = srhrr['noball_runs'].sum()
print("No balls across all season's =",noballs_allseason)

### Total matches all season's
total_matches = srhrr['match_id'].nunique()
print("Total matches h2h =",total_matches)
total_matches_all = (noballs_allseason/total_matches).round(3)
print("Average no balls per match =",total_matches_all.round(2))


# In[11]:


# No balls bowled in last 2 season's
noballs_2season = srhrr_2season['noball_runs'].sum()
print("No balls bowled in last 2 season's =", noballs_2season)

## Total matches played in last 2 season's h2h
total_match_2season = srhrr_2season['match_id'].nunique()
print("Total matches played in last 2 season's h2h =", total_match_2season)
average_noballs_2season = noballs_2season/total_match_2season
print("Average no balls bowled in last 2 seasons h2h =",average_noballs_2season)


# In[12]:


## No balls match wise all season's
noballs_all = pd.DataFrame(srhrr.groupby(['match_id']).sum()['noball_runs'])
noballs_all                       


# In[13]:


## No balls match wise last 2 season
noballs_2season = pd.DataFrame(srhrr_2season.groupby(['match_id']).sum()['noball_runs'])
noballs_2season                       


# ## Looking at last 2 season's & overall season's record in h2h,an average of 0-1 no ball have been bowled.
# ## Hence, according to prediction & analysis 0-1 no ball would be bowled in today's match

# In[14]:


# Allseason's dismissal kind of Warner with Srh against rr
Warner_records_strike_all = srhrr[srhrr.batsman == 'DA Warner']
Warner_records_strike_dismissaltype = Warner_records_strike_all[Warner_records_strike_all.player_dismissed == 'DA Warner']
Warner_records_strike_dismissaltype[['match_id','batsman','dismissal_kind','bowler']]


# In[15]:


# All season's dismissal kind of Warner with all franchises against RR
records_strike_all = deliveries[deliveries.bowling_team == 'Rajasthan Royals']
warner_records_strike_all = records_strike_all[records_strike_all.batsman == 'DA Warner']
warner_against_rr = warner_records_strike_all[warner_records_strike_all.player_dismissed == 'DA Warner']
warner_final = warner_against_rr[['batsman','bowling_team','dismissal_kind','bowler']]
warner_final


# In[16]:


# All season's dismissal kind of Warner with all franchises against RR
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(13,8)
sns.countplot(warner_final['dismissal_kind'],order=warner_final['dismissal_kind'].value_counts().index)
plt.text(-0.1,2.5,str(warner_final['dismissal_kind'].value_counts()['caught']),size=29,color='black')
plt.text(0.9,0.5,str(warner_final['dismissal_kind'].value_counts()['bowled']),size=29,color='black')
plt.text(1.9,0.5,str(warner_final['dismissal_kind'].value_counts()['run out']),size=29,color='black')
plt.text(2.9,0.5,str(warner_final['dismissal_kind'].value_counts()['stumped']),size=29,color='black')
plt.xlabel('Dismissal Type',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Warner dismissal kind',fontsize=15)
plt.show()


# ## Considering the previous 2 season's record Warner has been dismissed by CAUGHT in 4 out of 5 matches . Also,his overall record against RR with all franchises shows that he has been caught in 6 out of his 9 matches against RR.
# ## Hence,according to prediction Warner will be dimissed by dismissal kind of CAUGHT in today's match.
# 

# In[17]:


## Rashid Khan records & balls he will take to get 1st wicket in last 2 season's against rr(Rashid has only played 2 season's i.e. 4 matches against rr)
rashid = srhrr_2season[srhrr_2season.bowler == 'Rashid Khan']
total_wickets_2season = rashid['dismissal_kind'].count()
total_matches_2season = rashid['match_id'].nunique()
total_balls_2season = rashid['ball'].count() - rashid['wide_runs'].sum() - rashid['noball_runs'].sum()
balls_per_wicket = (total_balls_2season/total_wickets_2season)
balls_per_wicket


# In[18]:


## Rashid Khan records & balls he will take to get 1st wicket in overall season's against all franchises
rashid_records_season = deliveries[deliveries.bowler == 'Rashid Khan']
total_wickets_season = rashid_records_season['dismissal_kind'].count()
total_matches_season = rashid_records_season['match_id'].nunique()
total_balls_season = rashid_records_season['ball'].count() - rashid_records_season['wide_runs'].sum() - rashid_records_season['noball_runs'].sum()
balls_per_wicket = (total_balls_season/total_wickets_season)
balls_per_wicket.round()


# In[19]:


## Rashid last 2 season wickets record
wickets=pd.DataFrame(rashid.groupby(['match_id','over']).count()['player_dismissed']).sort_values(by='match_id',ascending=False)
wickets


# ## By Analysis in above dataframe we see that Rashid Khan has taken his first wicket against RR twice in 4 matches between 9-16 Balls.
# ## Hence, according to prediction & analysis Rashid khan will take his first wicket in between 9-16 balls.

# In[20]:


## Records of players against rr in last 2 season's 
smith = srhrr_2season[srhrr_2season.batsman == "SPD Smith"]
buttler = srhrr_2season[srhrr_2season.batsman == "JC Buttler"]
samson = srhrr_2season[srhrr_2season.batsman == "SV Samson"]
smith_runs = smith['batsman_runs'].sum()
buttler_runs = buttler['batsman_runs'].sum()
samson_runs = samson['batsman_runs'].sum()
smith_matches_rr = smith['match_id'].nunique()
buttler_matches_rr = buttler['match_id'].nunique()
samson_matches_rr = samson['match_id'].nunique()
smith_runspermatch = smith_runs/smith_matches_rr
buttler_runspermatch = buttler_runs/buttler_matches_rr
samson_runspermatch = samson_runs/samson_matches_rr
print("smith =",smith_runspermatch.round())
print("buttler =",buttler_runspermatch.round())
print("samson =",samson_runspermatch.round())


# In[21]:


# Other's record against srh in last 2 season
df = srhrr_2season[srhrr_2season.batting_team == 'Rajasthan Royals']
df1 = df[df.batsman != 'SPD Smith']
df2 = df1[df1.batsman != 'JC Buttler']
df3 = df2[df2.batsman != 'SV Samson']
final = df3['batsman_runs'].sum()/df3['match_id'].nunique()
final_avg = final/4  #Let's assume there are around 4 other batsman along with Smith,buttler,samson who contribute to overall runs & so calculated their overall average against srh
others = final_avg.round()
others


# In[22]:


## Last 2 season's performers record for RR against SRH
Rajasthanroyals = srhrr_2season[srhrr_2season.batting_team == 'Rajasthan Royals']
top_performers = pd.DataFrame(Rajasthanroyals.groupby(['batsman']).sum()['batsman_runs'])
top_performers[top_performers['batsman_runs'] >= 20]


# In[23]:


## Last 2 season's individual top scores for RR against SRH
Rajasthanroyals = srhrr_2season[srhrr_2season.batting_team == 'Rajasthan Royals']
top_performers = pd.DataFrame(Rajasthanroyals.groupby(['batsman','match_id']).sum()['batsman_runs'])
top_performers[top_performers['batsman_runs'] >= 20]


# ## Looking at performance of individual players of Rajasthan royals against SRH we observe that Samson has scored maximum runs against SRH with total runs '250' . Also his individual scores in last 2 season against SRH have been (51,40,106,53).Samson has scored with an average of 62 against SRH in last 2 season's (4 matches).
# ## Hence,looking at top performers of RR against SRH. Samson will score the most runs for RR today.

# In[ ]:




