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


#Cleaning delieveries dataset to set new name
deliveries.batting_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[7]:


deliveries.bowling_team.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[8]:


#Cleaning matches dataset to set new name
matches.team1.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.team2.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.toss_winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)
matches.winner.replace({'Delhi Daredevils' : 'Delhi Capitals'},regex=True,inplace=True)


# In[9]:


matches.isnull().sum()


# In[10]:


matches.drop(['umpire3'], axis = 1, inplace = True)


# In[11]:


print(matches['winner'].unique())
print(matches['city'].unique())


# In[12]:


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


# In[13]:


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


# In[14]:


midc=matches[np.logical_or(np.logical_and(matches['team1']=='Mumbai Indians',matches['team2']=='Delhi Capitals'),np.logical_and(matches['team2']=='Mumbai Indians',matches['team1']=='Delhi Capitals'))]


# In[15]:


midc


# In[16]:


sns.set(style='dark')
fig=plt.gcf()
fig.set_size_inches(10,8)
sns.countplot(midc['winner'],order=midc['winner'].value_counts().index)
plt.text(-0.1,9,str(midc['winner'].value_counts()['Mumbai Indians']),size=29,color='white')
plt.text(0.9,9,str(midc['winner'].value_counts()['Delhi Capitals']),size=29,color='white')
plt.xlabel('Winner',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.yticks(fontsize=0)
plt.title('MI vs DC - head to head')
plt.show()

# 12 wins each


# In[17]:


midc_table = midc[['toss_winner','toss_decision','winner','season']]


# In[18]:


midc_table.loc[midc_table['season'] >= 2017]

#From this we conclude if delhi wins toss the probability of it winning is 50% however if Mumbai losses toss it has won 2 out of 4 times too..
#Looking at the ground records at Abu dhabi mostly the team which has won the toss has opted to BAT first and win ratio for same is 8:2 8 wins 2 losses
#So the trend is win toss BAT first and get a much higher chance to win match


# In[20]:


#**Decision upon winning the toss by both teams**

sns.set(style='darkgrid')
fig=plt.gcf()
fig.set_size_inches(18.5,8)
ax=sns.countplot(midc['toss_winner'],order=midc['toss_winner'].value_counts().index,palette='Set2',hue=matches['toss_decision'])
plt.title('Toss decision statistics for both team',fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.xlabel('Toss winner',fontsize=15)
plt.ylabel('Count ',fontsize=15)
plt.legend(['Bat first','Field first'],loc='best',fontsize=15)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (1, 10), 
                   textcoords = 'offset points')
plt.show()    


# In[22]:


# Best Performers
sns.set(style='darkgrid')
fig=plt.gcf()
fig.set_size_inches(18.5,8)
ax=sns.countplot(midc['player_of_match'],order=midc['player_of_match'].value_counts().index,palette='Set2')
plt.title('All man of the match awards in MI-DC games',fontsize=15)
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


# In[23]:


dcmi=deliveries[np.logical_or(np.logical_and(deliveries['batting_team']=='Mumbai Indians',deliveries['bowling_team']=='Delhi Capitals'),np.logical_and(deliveries['bowling_team']=='Mumbai Indians',deliveries['batting_team']=='Delhi Capitals'))]
dcmi


# In[24]:


batsmen_strikerate_season = pd.DataFrame(dcmi.groupby(['batsman']).agg({'batsman_runs' : 'sum','ball' : 'count'}))
batsmen_strikerate_season['Strike Rate'] = batsmen_strikerate_season['batsman_runs']/batsmen_strikerate_season['ball']*100
batsmen_strikerate_season = batsmen_strikerate_season.sort_values(by ='batsman_runs' , ascending = False)
batsmen_strikerate_season[batsmen_strikerate_season['batsman_runs'] > 250]


# In[26]:


#### Runs scored by Rohit sharma against DC

batsmen_score = pd.DataFrame(dcmi.groupby(['batsman']).sum()['batsman_runs'])
batsmen_score[batsmen_score['batsman_runs']>=500]


# Runs scored = 563;
# Total matches = 18;
# Avg = 31.2 
# So approx on this prediction rohit will score around 30-40

# In[27]:


# Rabada prediction
bowlers_list = dcmi["bowler"].unique().tolist()
bowlers_list[0:20]


# In[28]:


dismissal_kind_vc = dcmi['dismissal_kind'].value_counts()
dismissals_not_by_bowler = ['run out','retired hurt']
dismissals_by_bowler_vc = dismissal_kind_vc.drop(labels = dismissals_not_by_bowler)
plt.figure(figsize=(18,5))
most_wickets_vc = dcmi[dcmi['dismissal_kind'].isin(dismissals_by_bowler_vc.index)]['bowler'].value_counts()
print(most_wickets_vc.head(12))
most_wickets_vc = most_wickets_vc[most_wickets_vc >= 6]
g = sns.barplot(x = most_wickets_vc.index, y = most_wickets_vc)
for p in g.patches:
    g.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')


# So, Rabada has taken 6 wickets against MI until now in 4 matches,so he will take 2 wickets according to the prediction and his current form.
