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


#### Records of MI vs CSK (matches dataset)
micsk =matches[np.logical_or(np.logical_and(matches['team1']=='Mumbai Indians',matches['team2']=='Chennai Super Kings'),np.logical_and(matches['team2']=='Mumbai Indians',matches['team1']=='Chennai Super Kings'))]
micsk


# In[5]:


# Head to head MI vs CSK across all season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(8,5.2)
sns.countplot(micsk['winner'],order=micsk['winner'].value_counts().index)
plt.text(-0.1,5,str(micsk['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.text(0.9,3,str(micsk['winner'].value_counts()['Chennai Super Kings']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs CSK - head to head')
plt.show()


# In[6]:


#H2H previous 2 season's
df_season_record =micsk[micsk['season'] >=2018]
df_season_record_df = df_season_record[['season','winner','id']]
df_season_record_df


# In[7]:


##### Head to head mi vs csk last 2 season's
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(df_season_record_df['winner'],order=df_season_record_df['winner'].value_counts().index)
plt.text(-0.1,2.5,str(df_season_record_df['winner'].value_counts()['Mumbai Indians']),size=29,color='black')
plt.text(0.95,0.5,str(df_season_record_df['winner'].value_counts()['Chennai Super Kings']),size=29,color='black')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs CSK - head to head last 2 season')
plt.show()


# # Looking at previous 2 season's record(recent form) & overall season's record in head to head,MI have dominated CSK.
# 
# # Hence according to the recent form and analysis MI will win today's match.

# In[8]:


#For deliveries dataset
cskmi=deliveries[np.logical_or(np.logical_and(deliveries['batting_team'] == 'Mumbai Indians',deliveries['bowling_team']== 'Chennai Super Kings'),np.logical_and(deliveries['bowling_team']=='Mumbai Indians',deliveries['batting_team']=='Chennai Super Kings'))]
cskmi


# In[9]:


# Previous 2 season's records of deliveries dataset (filtered with the help of match_id)
cskmi_2season = cskmi[cskmi['match_id'] >= 7894]
cskmi_2season


# # De kock

# In[10]:


## Records of Q de kock against CSK in first 10 balls (played only 1 season with MI & 4 matches against CSK)
def dekock(matchid):
    df_dekock = cskmi_2season[cskmi_2season.batsman == 'Q de Kock']
    x = df_dekock[df_dekock['match_id'] == matchid]
    y = x[['match_id','batsman_runs']].head(10)
    z = y[y.batsman_runs >= 4 ]
    print(z['batsman_runs'].sum())


# In[11]:


# 1st match against csk in 2019;total boundary runs=4
dekock(11151)


# In[12]:


# 2nd match against csk in 2019;total boundary runs=10
dekock(11335)


# In[13]:


# 3rd match against csk in 2019;total boundary runs=8
dekock(11412)


# ## Looking at last 3 matches of qdk against csk in twice of those matches he has scored less than 10 runs in boundaries in first 10 balls.
# ## Hence, according to analysis & prediction today qdk will score total runs of boundaries in range less than 10 runs in first 10 balls.

# # Dot balls ratio

# In[15]:


#  dot balls
def dotballs(bowler_name):
 df_bowler = cskmi_2season[cskmi_2season.bowler == bowler_name]
 total_dot = df_bowler[df_bowler['total_runs'] == 0]
 dots_bowler = total_dot['total_runs'].count()
 total_balls=df_bowler['ball'].count() - df_bowler[df_bowler.wide_runs >= 1].count() - df_bowler[df_bowler.noball_runs >= 1].count()
 total_balls_df = total_balls['ball']   
 print((dots_bowler/total_balls_df).round(3)*100)


# In[16]:


# Chahar dot balls ratio
print("Rahul Chahar dot balls in % :") 
dotballs('RD Chahar')


# In[17]:


# bumrah dot balls ratio
print("Jasprit Bumrah dot balls in % :") 
dotballs('JJ Bumrah')


# In[18]:


# hardik dotball ratio
print("Hardik pandya dot balls in % :") 
dotballs('HH Pandya')


# In[19]:


# krunal dot ball ratio
print("Krunal Pandya dot balls in % :") 
dotballs('KH Pandya')


# In[20]:


## For boult dot ball ratio
csk = deliveries[deliveries.batting_team == 'Chennai Super Kings']
boult_against_csk = csk[csk.bowler == 'TA Boult']
dotballs = boult_against_csk[boult_against_csk['total_runs'] == 0].count()
final_dotballs = dotballs['total_runs']
total_balls = boult_against_csk['ball'].count() - boult_against_csk[boult_against_csk.wide_runs >= 1].count() - boult_against_csk[boult_against_csk.noball_runs >= 1].count()
dfx = (final_dotballs/total_balls)*100
print("Boult dot balls ratio against csk in % =",dfx['ball'].round())


# ## Dot balls ratio of two highest performers have been rahul chahar and krunal.
# ## However in current season chahar has bowled more dot balls and has better economy than krunal 
# ## Hence,according to current form and analysis Rahul chahar will have highest dot ball ratio among Mumbai Bowlers.

# # BLS

# In[21]:


## BLS
def BLS(bowlername):
 record = cskmi_2season[cskmi_2season.bowler == bowlername]
 record_wickets = record['dismissal_kind'].count()
 avg_wickets = record_wickets/cskmi_2season['match_id'].nunique()
 total_dot = record[record['total_runs'] == 0]
 avg_dots_bowler = total_dot['total_runs'].count()/cskmi_2season['match_id'].nunique()
 total_balls= record['ball'].count() - record[record.wide_runs >= 1].count() - record[record.noball_runs >= 1].count()
 total_balls_df = total_balls['ball'] /cskmi_2season['match_id'].nunique()
 total_boundaries = record[record.batsman_runs >= 4]
 total_boundaries_final =total_boundaries['batsman_runs'].count()
 total_boundaries_runs = total_boundaries['batsman_runs'].sum()
 final = (avg_wickets + avg_dots_bowler - (total_boundaries_runs/total_boundaries_final))/total_balls_df
 print('BLS score =' ,final.round(3))


# In[22]:


print("1. Bumrah")
BLS('JJ Bumrah')
print("2. Rahul chahar")
BLS('RD Chahar')
print("3. Krunal pandya")
BLS('KH Pandya')
print("4. Tahir")
BLS('Imran Tahir')
print("5. Deepak chahar")
BLS('DL Chahar')
print("6. SN Thakur")
BLS('SN Thakur')
print("7. HH Pandya")
BLS('HH Pandya')
print("RA Jadeja")
BLS('RA Jadeja')


# ## The BLS score has been highest for deepak chahar.
# ## Hence, according to analysis deepak chahar will have highest BLS score.

# In[27]:


## Looking for last 3 matches 4 &  6 in same over
def match(matchid):
 df = cskmi_2season[cskmi_2season.match_id == matchid]
 dfx = df[df.batsman_runs >= 4]
 dataframe = pd.DataFrame(dfx.groupby(['match_id','over','ball','inning']).sum()['batsman_runs'])
 print(dataframe)


# In[24]:


match(11335)


# In[25]:


match(11412)


# In[26]:


match(11415)


# ##  Looking at last 3 matches record & recent season record(2020) an average of 5-6 overs have happened at sharjah where 4 & 6 have been scored in same over
# ## Hence according to analysis 5-6 overs is the answer.
