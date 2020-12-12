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


#### Records of MI vs KKR (matches dataset)
mikkr=matches[np.logical_or(np.logical_and(matches['team1']=='Mumbai Indians',matches['team2']=='Kolkata Knight Riders'),np.logical_and(matches['team2']=='Mumbai Indians',matches['team1']=='Kolkata Knight Riders'))]
mikkr


# In[7]:


# Head to head mi vs kkr across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(mikkr['winner'],order=mikkr['winner'].value_counts().index)
plt.text(-0.1,7,str(mikkr['winner'].value_counts()['Mumbai Indians']),size=29,color='white')
plt.text(0.9,3,str(mikkr['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs KKR - head to head')
plt.show()


# In[8]:


#H2H previous 3 season's
df_season_record = mikkr[mikkr['season'] >=2017]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[9]:


# Head to head mi vs kkr last 3 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,3,str(df_season_record_df['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.text(0.9,0.5,str(df_season_record_df['winner'].value_counts()['Kolkata Knight Riders']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs KKR - head to head')
plt.show()


# # Looking at previous 3 season's record(recent form) & overall season's record in head to head, MI have dominated KKR.
# # Hence according to the recent form and analysis Mumbai Indians will win today's match.

# In[10]:


#For deliveries dataset
kkrmi=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Mumbai Indians',deliveries['bowling_team']=='Kolkata Knight Riders'),np.logical_and(deliveries['bowling_team']=='Mumbai Indians',deliveries['batting_team']=='Kolkata Knight Riders'))]
kkrmi


# In[11]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
kkrmi_2season_deliveries = kkrmi[kkrmi['match_id'] >= 7930]
kkrmi_2season_deliveries


# In[12]:


# Last 2 season's dismissal kind of Rohit Sharma
rohit_records_strike = kkrmi_2season_deliveries[kkrmi_2season_deliveries.batsman == 'RG Sharma']
rohit_records_strike_dismissaltype = rohit_records_strike[rohit_records_strike.player_dismissed == 'RG Sharma']
rohit_records_strike_dismissaltype[['match_id','batsman','dismissal_kind','bowler']]


# In[13]:


rohit_records_allseason = kkrmi[kkrmi.batsman == 'RG Sharma']
rohit_records_allseason_dismissaltype = rohit_records_allseason[rohit_records_allseason.player_dismissed == 'RG Sharma']
dataframe_rohit = rohit_records_allseason_dismissaltype[['match_id','batsman','dismissal_kind','bowler']]
dataframe_rohit


# In[14]:


# Replacing (caught and bowled) record to caught dismissal_kind
dataframe_rohit_cleaned =dataframe_rohit.replace({'caught and bowled' : 'caught'})
dataframe_rohit_cleaned


# In[15]:


sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(13,8)
sns.countplot(dataframe_rohit_cleaned['dismissal_kind'],order=dataframe_rohit_cleaned['dismissal_kind'].value_counts().index)
plt.text(-0.1,4,str(dataframe_rohit_cleaned['dismissal_kind'].value_counts()['caught']),size=29,color='black')
plt.text(0.9,2,str(dataframe_rohit_cleaned['dismissal_kind'].value_counts()['lbw']),size=29,color='black')
plt.text(1.9,1,str(dataframe_rohit_cleaned['dismissal_kind'].value_counts()['bowled']),size=29,color='black')
plt.xlabel('Dismissal Type',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('Rohit Sharma dismissal kind',fontsize=15)
plt.show()


# # Looking at the overall records and record of last 2 season's Rohit sharma has been dismissed with dismissal_kind of caught for most number of times.Also,looking at his dismissal type in 2020 (Current season) he has been dismissed by caught kind for all the matches (7/7) .
# # Hence, according to prediction rohit sharma will be dismissed by dismissal_kind of Caught.

# In[21]:


#Total runs scored in season 2017 (3 matches in total)
total_season_2017 = kkrmi[kkrmi['match_id'] == 53].total_runs.sum() + kkrmi[kkrmi['match_id'] == 7].total_runs.sum() + kkrmi[kkrmi['match_id'] == 58].total_runs.sum()
print("Total runs scored in 2017 season h2h =",total_season_2017)


# In[20]:


# Total runs scored in last 2 season's 2018-2019 (4 matches in total)
total_season_2018_2019 = kkrmi_2season_deliveries['total_runs'].sum()
print("Total runs scored in last 2 season's 2018-2019 =",total_season_2018_2019)


# In[23]:


# Taking average of last 3 season's score to get average in a single match (In total 7 matches i.e. 4 in 2018-2019 & 3 in 2017)
average_runs_mikkr_3season = ((total_season_2017 + total_season_2018_2019)/7).round(2)
print("Total runs scored in average in last 3 season's 2017-18-19 =",average_runs_mikkr_3season)


# ## Looking at the average score in head to head of previous 3 season's (2017-18-19) the score has been around 332-333 (average).
# ## Hence, according to prediction the total runs that would be scored today will be in range of 321-340. 

# In[34]:


team_mi=kkrmi[kkrmi.batting_team=='Mumbai Indians']
overs=team_mi[(team_mi['over']>=7) & (team_mi['over']<=15)]
wickets=overs[overs['batting_team']=='Mumbai Indians'].count()['player_dismissed']
wickets_per_match=wickets/overs['match_id'].nunique()
print("Average wickets per match in all season's in h2h =",wickets_per_match.round(2))


# In[35]:


team_mi=kkrmi_2season_deliveries[kkrmi_2season_deliveries.batting_team=='Mumbai Indians']
overs=team_mi[(team_mi['over']>=7) & (team_mi['over']<=15)]
wickets=overs[overs['batting_team']=='Mumbai Indians'].count()['player_dismissed']
wickets_per_match=wickets/overs['match_id'].nunique()
print("Average wickets per match in last 2 season's 2018-2019 =",wickets_per_match)


# ## Looking at the record's of overall season of MI and of recent last 2 season's(2018-2019),MI have lost in average around 2 wickets in overs between 6-15.Now, considering other factors  like this season(2020) record of MI they have lost maximum of 3 wickets in 6-15 overs in only one match.In other 6 matches they have lost 2  or less wickets in that range of overs 6-15.
# ## Hence,according to prediction MI will loose 0-2 wickets in overs 6-15 .

# In[38]:


kkr_fours_allseason=kkrmi[kkrmi['batting_team']=='Kolkata Knight Riders']
fours=kkr_fours_allseason[kkr_fours_allseason['total_runs']==4].count()['total_runs']
fours_allseason_kkr=fours/kkr_fours_allseason['match_id'].nunique()
print("Average number of fours in all season by kkr against MI =",fours_allseason_kkr)


# In[40]:


kkr_fours_allseason=kkrmi_2season_deliveries[kkrmi_2season_deliveries['batting_team']=='Kolkata Knight Riders']
fours=kkr_fours_allseason[kkr_fours_allseason['total_runs']==4].count()['total_runs']
fours_2season_kkr=fours/kkr_fours_allseason['match_id'].nunique()
print("Average number of fours in last 2 season's by kkr against MI =",fours_2season_kkr)


# ## For the last 2 season's record of KKR they have got in an average of around 14 fours against MI.
# ## For overall season record they have got an average of around 13 fours against MI.
# ## Now considering,other factors such as stadium & this year's record(2020) of KKR in number of fours.Firstly,considering the ground ABU Dhabi has longer dimensions than other two stadiums in Dubai.Hence, number of fours would be greater than sixes.Secondly,KKR have scored in an average of about 12 fours per match in 2020 in Abu Dhabi.
# ## Also,considering the players Gill,Karthik,Rana have hit in an average of about 8-9 fours in an average together.
# ## Hence, according to prediction the overall fours of KKR in Today's match would be in range 13 or more.

# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




