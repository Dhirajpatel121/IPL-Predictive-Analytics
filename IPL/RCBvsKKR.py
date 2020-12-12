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


import seaborn as sns
sns.set(style='darkgrid')
fig=plt.gcf()
fig.set_size_inches(18.5,10.5)
wins=pd.DataFrame(matches['winner'].value_counts())
wins['name']=wins.index
plt.xticks(rotation=90,fontsize=12)
plt.yticks(fontsize=16)
plt.bar(wins['name'],
        wins['winner'],
        color=['#15244C','#FFFF48','#292734','#EF2920','#CD202D','#ECC5F2',
               '#294A73','#D4480B','#242307','#FD511F','#158EA6','#E82865',
               '#005DB7','#C23E25']
        ,alpha=0.8)
count=0
for i in wins['winner']:
    plt.text(count-0.15,i-4,str(i),size=15,color='black',rotation=90)
    count+=1
plt.title('Total wins by each team',fontsize=20)
plt.xlabel('Teams',fontsize=15)
plt.ylabel('Total no. of matches won(2008-2019)',fontsize=14)
plt.show()


# In[7]:


fig=plt.gcf()
fig.set_size_inches(18.5,10.5)
sns.countplot(matches['venue'],order=matches['venue'].value_counts().index,palette='Set2')
plt.xticks(rotation=90,fontsize=11.5)
plt.yticks(fontsize=16)
plt.xlabel('Stadium',fontsize=20)
plt.ylabel('Count',fontsize=20)
plt.title('No. of games hosted in each stadium',fontsize=15)
count=0
venues=pd.DataFrame(matches['venue'].value_counts())
venues['name']=matches['venue'].value_counts().index
for i in venues['venue']:
    plt.text(count-0.2,i-2,str(i),rotation=90,color='black',size=12)
    count+=1
plt.show()


# In[8]:


#### Records of KKR vs RCB

rcbkkr=matches[np.logical_or(np.logical_and(matches['team1']=='Royal Challengers Bangalore',matches['team2']=='Kolkata Knight Riders'),np.logical_and(matches['team2']=='Royal Challengers Bangalore',matches['team1']=='Kolkata Knight Riders'))]


# In[9]:


rcbkkr


# In[10]:


sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(rcbkkr['winner'],order=rcbkkr['winner'].value_counts().index)
plt.text(-0.1,9,str(rcbkkr['winner'].value_counts()['Kolkata Knight Riders']),size=20,color='white')
plt.text(0.9,9,str(rcbkkr['winner'].value_counts()['Royal Challengers Bangalore']),size=20,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('RCB vs KKR - head to head')
plt.show()

# Out of 24 matches 14 have been won by KKR and 10 by RCB


# In[11]:


rcbkkr_table = rcbkkr[['toss_winner','toss_decision','winner','season']]


# In[12]:


# Toss Decision of last 5  years between RCB vs KKR
rcbkkr_table.loc[rcbkkr_table['season'] >= 2015]


# Ans 2: **In last 5 seasons over head to head matches between 2 teams the one which has won the toss has fielded first.However,looking at the recent form both teams have defended total well in ipl 2020 and hence the one which wins the toss will bat first and try to defend that total.**

# Ans 1: **Also looking at the last 3 seasons data and predicting which team wins according to data comes out to be kkr,KKR has dominated the h2h for last 3 season(most recent seasons) with winning 5 out of 6 matches against RCB in 2017,2018,2019.So,KKR will win the match according to prediction.**

# In[13]:


#**Decision upon winning the toss by both teams across all seasons**

sns.set(style='darkgrid')
fig=plt.gcf()
fig.set_size_inches(18.5,8)
ax=sns.countplot(rcbkkr['toss_winner'],order=rcbkkr['toss_winner'].value_counts().index,palette='Set2',hue=matches['toss_decision'])
plt.title('Toss decision statistics for both team',fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.xlabel('Toss winner',fontsize=15)
plt.ylabel('Count ',fontsize=15)
plt.legend(['Field first','Bat first'],loc='best',fontsize=15)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (1, 10), 
                   textcoords = 'offset points')
plt.show()    


# In[14]:


# Best Performers in rcb vs kkr matches
sns.set(style='darkgrid')
fig=plt.gcf()
fig.set_size_inches(18.5,8)
ax=sns.countplot(rcbkkr['player_of_match'],order=rcbkkr['player_of_match'].value_counts().index,palette='Set2')
plt.title('All man of the match awards in rcb-kkr games',fontsize=15)
plt.yticks([1,2,3],[1,2,3],fontsize=15)
plt.xticks(fontsize=15,rotation=90)
plt.xlabel('Man of the match',fontsize=15)
plt.ylabel('Count',fontsize=15)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (1, 10), 
                   textcoords = 'offset points')
plt.show()


# In[15]:


#For deliveries
kkrrcb=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Royal Challengers Bangalore',deliveries['bowling_team']=='Kolkata Knight Riders'),np.logical_and(deliveries['bowling_team']=='Royal Challengers Bangalore',deliveries['batting_team']=='Kolkata Knight Riders'))]
kkrrcb


# In[24]:


#Total fours by V Kohli
most_fours = kkrrcb[kkrrcb['batsman_runs'] == 4]['batsman'].value_counts()
most_fours[0:5]


# **Virat Kohli has scored 58 fours against KKR until now.**

# In[19]:


## Total matches of Virat kohli against KKR
total_matches = kkrrcb.groupby('batsman')['match_id'].nunique()
total_matches[total_matches >= 15]


# **Virat Kohli has played 21 matches against KKR**

# Ans 5: **Virat Kohli has scored 58 boundaries(4's) against KKR and number of matches played is equal to 21.So by average we get 58/21 ~ 3.Also, looking at the recent form he has scored 40+ in last 3 matches.Considering the factor of ground as well which is sharjah and the dimensions are quite small.So Virat Kohli would score 5 or more boundaries(4's) today according to the prediction.**

# In[20]:


total_matches[total_matches == 4]


# **Total matches played by Dinesh Karthik against RCB is 4**

# In[60]:


## Total Runs scored by Dinesh Karthik
batsmen_score = pd.DataFrame(kkrrcb.groupby(['batsman']).sum()['batsman_runs'])
batsmen_score[batsmen_score['batsman_runs'] == 88]


# Ans 3: **Total Runs scored by Dinesh Karthik is 88 runs and total matches played is 4.So,in average he has scored around 22 runs in each match.So,he will score 21-35 runs in the Rcb vs KKR match according to prediction.**

# In[34]:


## Total number of No balls in RCB vs KKR matches
kkrrcb['noball_runs'].sum()


# Ans 4: **Total No balls bowled in KKR vs RCB matches is 23.Total matches Head to head as we have retrieved at start was 24.So dividing sum/n i.e.(23/24) to get average of no balls we get it as approximately equal to 1.So, Total number of no balls that would be bowled today will be 1.**

# In[ ]:




