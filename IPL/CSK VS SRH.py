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


# In[3]:


deliveries


# In[4]:


matches = pd.read_csv('C:/Users/SONY/Desktop/IPL/matches.csv')


# In[5]:


matches


# In[6]:


#### Records of CSK vs SRH (matches dataset)
csksrh=matches[np.logical_or(np.logical_and(matches['team1']=='Chennai Super Kings',matches['team2']=='Sunrisers Hyderabad'),np.logical_and(matches['team2']=='Chennai Super Kings',matches['team1']=='Sunrisers Hyderabad'))]


# In[7]:


csksrh


# In[8]:


# Head to head CSK vs SRH
sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(csksrh['winner'],order=csksrh['winner'].value_counts().index)
plt.text(-0.1,7,str(csksrh['winner'].value_counts()['Chennai Super Kings']),size=29,color='white')
plt.text(0.9,2,str(csksrh['winner'].value_counts()['Sunrisers Hyderabad']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('CSK vs SRH - head to head')
plt.show()


# # Chennai Super Kings have won 9 out 12 games played against SRH.

# In[9]:


records = csksrh[csksrh['season'] >= 2015]
records[['season','winner']]


# # Also,in last 3 seasons(2015,2018,2019) CSK have dominated the h2h by winning 6 out 8 matches against SRH.
# # So according to the prediction and recent form of previous seasons,CSK will win today's match

# In[10]:


#For deliveries dataset
srhcsk=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Chennai Super Kings',deliveries['bowling_team']=='Sunrisers Hyderabad'),np.logical_and(deliveries['bowling_team']=='Chennai Super Kings',deliveries['batting_team']=='Sunrisers Hyderabad'))]
srhcsk


# In[11]:


david_warner_total_runs = srhcsk[srhcsk['batsman'].str.contains("DA Warner")].sum()['batsman_runs']
david_warner_total_matches = srhcsk[srhcsk['batsman'].str.contains("DA Warner")].nunique()['match_id']
Average_score=(david_warner_total_runs/david_warner_total_matches).round(3)
print("David Warner's runs against CSK =", david_warner_total_runs)
print("David Warner's total matches against CSK =", david_warner_total_matches)
print("Average_score of David warner against CSK = ",Average_score)


# # David Warner has scored 314 against CSK in total of 6 matches at an average of 52.3 
# # Hence, David Warner will score 40 or more runs according to prediction & his recent form in IPL 2020.

# In[12]:


## Total number of wide balls in SRH vs CSK matches
wide_balls = srhcsk['wide_runs'].sum()
Total_matches_headtohead = srhcsk['match_id'].nunique()
Average_wideballs = wide_balls/Total_matches_headtohead
print("Total number of wide balls in SRH vs CSK matches =",wide_balls)
print("Total matches head to head =",Total_matches_headtohead)
print("Average number of wide balls per match in SRH vs CSK match =",Average_wideballs)


# # Average number of wide balls bowled in h2h of CSK vs SRH has been 7.25 
# # Hence, according to prediction the total wide balls bowled today would be in range 6-8

# In[13]:


## Total runs scored in SRH vs CSK matches
Total_runs = srhcsk['total_runs'].sum()
Total_matches_headtohead = srhcsk['match_id'].nunique()
Average_runs_in_each_match = (Total_runs/Total_matches_headtohead).round(3)
print("Total runs scored in SRH vs CSK matches =",Total_runs)
print("Total matches head to head =",Total_matches_headtohead)
print("Average runs scored in SRH vs CSK matches =",Average_runs_in_each_match)


# # Average  number of runs score in h2h of CSK vs SRH has been 344.667 ~ 345
# # Hence, according to prediction the total runs scored in today's match would be in range 341-360

# In[14]:


## Total wickets csk lost during csk vs srh matches
df = srhcsk[srhcsk.batting_team == 'Chennai Super Kings']
wickets = df['player_dismissed'].value_counts().sum()
Total_matches_headtohead = srhcsk['match_id'].nunique()
Average_wickets_lostbycsk_againstsrh = (wickets/Total_matches_headtohead).round(3)
print("Total wickets lost by CSK batting against SRH =",wickets)
print("Total matches head to head =",Total_matches_headtohead)
print("Average wickets lost by CSK against SRH =",Average_wickets_lostbycsk_againstsrh)


# # Average wickets lost by CSK batting against SRH has been 4.167 
# # Hence,total wickets that would CSK lose today against SRH would be in range 3-5
