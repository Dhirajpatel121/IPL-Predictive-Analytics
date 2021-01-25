#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Team Annihilators- MehulKumar Patel,Dhiraj Patel
# Emails: dhiru474@gmail.com,mkpatel.p64@gmail.com
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.simplefilter('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


matches = pd.read_csv('C:/Users/SONY/Desktop/Projects/IPL/matches.csv')
deliveries = pd.read_csv('C:/Users/SONY/Desktop/Projects/IPL/deliveries.csv')


# In[4]:


matches.head(3)


# In[5]:


deliveries.head(3)


# # 1. ***Data Cleaning and Rearranging***

# ## Checking for null values

# In[6]:


matches.isnull().sum()


# ## Rearrange & Rename 

# In[7]:


matches.city = matches.city.fillna("-")
matches.umpire1 = matches.umpire1.fillna("-")
matches.umpire2 = matches.umpire2.fillna("-")
matches = matches.replace('Rising Pune Supergiants', 'Rising Pune Supergiant')
matches = matches.replace('Pune Warriors', 'Rising Pune Supergiant')
matches = matches.replace('Deccan Chargers', 'Sunrisers Hyderabad')
matches = matches.replace('Delhi Daredevils', 'Delhi Capitals')


# ## Removing unwanted columns

# In[8]:


matches.drop(columns=["umpire3"], inplace = True)
matches.drop(columns=["umpire2"], inplace = True)
matches.drop(columns=["umpire1"], inplace = True)


# ## Checking for null rows

# In[9]:


is_NaN = matches.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = matches[row_has_NaN]
rows_with_NaN


# ## Drop all null values

# In[10]:


matches.dropna(inplace=True)
matches.isnull().sum()


# In[11]:


matches.info()


# In[12]:


matches.describe([0.10,0.25,0.50,0.75,0.90,0.95,0.99]).T


# # 2. ***Deep-dive Analysis into Dataset with Visualization's***

# ## -> Wins by each team

# In[13]:


# Total no. of wins by each team
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
               '#005DB7','#C23E25','#E82865']
        ,alpha=0.8)
count=0
for i in wins['winner']:
    plt.text(count-0.15,i-4,str(i),size=15,color='black',rotation=90)
    count+=1
plt.title('Total wins by each team',fontsize=20)
plt.xlabel('Teams',fontsize=15)
plt.ylabel('Total no. of matches won(2008-2019)',fontsize=14)
plt.show()


# ## -> Most MOM Awards

# In[14]:


# Man of Match Awards
players=pd.DataFrame(matches['player_of_match'].value_counts())
players['name']=players.index
players=players.head(20)
fig=plt.gcf()
fig.set_size_inches(18.5,10.5)
plt.xticks(rotation=90,fontsize=0)
plt.yticks([0,2,4,6,8,10,12,14,16,18,20],[0,2,4,6,8,10,12,14,16,18,20],fontsize=15)
plt.bar(players['name'], players['player_of_match'],
        color=['#CD202D','#EF2920','#D4480B','#15244C','#FFFF48','#EF2920',
               '#FFFF48','#FFFF48','#292734','#FFFF48','#ECC5F2','#EF2920',
               '#292734','#15244C','#005DB7','#005DB7','#292734','#15244C',
               '#FFFF48','#CD202D'],alpha=0.8)
count=0
for i in players['player_of_match']:
    plt.text(count,7,players['name'][count]+': '+str(i),rotation=90,color='black',size=18)
    count+=1
plt.title('Top 20 players with most "Man of the match" awards',fontsize=20)
plt.xlabel('Players',fontsize=20)
plt.ylabel('No. of times won',fontsize=18)
plt.tight_layout()
plt.show()


# ## -> Top Run-scorers

# In[15]:


# Most Runs by a player

#Create new dataframe
most_runs = pd.DataFrame()
# the 'batsman_runs' column, sort them and fetch top 10 results
most_runs['Total Runs'] = deliveries.groupby('batsman').sum()['batsman_runs'].sort_values(ascending = False).head(5)

#Give a name to the index and reset the index to make it a column
most_runs.index.names = ['Batsman']
most_runs.reset_index(inplace=True)

#Plot the graph
plt.figure(figsize=(10,6))
font = {'color':  'darkcyan',
        'weight': 'bold',
        'size': 30,
        }
plt.title('Most Runs',fontdict=font)
ax = sns.barplot(x='Batsman',y='Total Runs',data = most_runs,palette='gist_rainbow')
ax.xaxis.label.set_color('darkcyan')
ax.yaxis.label.set_color('darkcyan')
ax.xaxis.label.set_size(10)
ax.yaxis.label.set_size(10)
ax.tick_params(axis='both', colors='darkcyan', labelsize=14)

#Display the actual values on the bars
for p in ax.patches:
    ax.annotate(format(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()-500), ha = 'center',
                va = 'center', xytext = (0, 10), textcoords = 'offset points',fontweight = 'bold',fontsize=15)


# ## -> Top wicket takers

# In[16]:


#the top Ten blower's with highest wickets

#Create new dataframe
wickets = pd.DataFrame()
dismissal = pd.DataFrame()

dismissal = deliveries[(deliveries['player_dismissed'].notnull()) & (~deliveries['dismissal_kind'].isin(['run out','retired hurt','obstructing the field']))]
wickets['Wickets'] = dismissal.groupby('bowler').count()['player_dismissed'].sort_values(ascending=False).head(5)

#Give name to the index and reset the index to make it a column
wickets.index.names = ['Bowler']
wickets.reset_index(inplace=True)


#Plot the graph
plt.figure(figsize=(16,6))
font = {'color':  'darkcyan',
        'weight': 'bold',
        'size': 30,
        }
plt.title('Most Wickets',fontdict=font)
ax = sns.barplot(x='Bowler',y='Wickets',data = wickets,palette='gist_rainbow')
ax.xaxis.label.set_color('darkcyan')
ax.yaxis.label.set_color('darkcyan')
ax.xaxis.label.set_size(20)
ax.yaxis.label.set_size(20)
ax.tick_params(axis='both', colors='darkcyan', labelsize=14)
plt.xticks(rotation=45)

#Display the actual values on the bars
for p in ax.patches:
    ax.annotate(format(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()-15), ha = 'center',
                va = 'center', xytext = (0, 10), textcoords = 'offset points',fontweight = 'bold',fontsize=15)


# In[17]:


from plotly import tools
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=False)


# ## -> Total Wins & Win percentage by team

# In[18]:


matches_played=pd.concat([matches['team1'],matches['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['wins']=matches['winner'].value_counts().reset_index()['winner']
matches_played.set_index('Team',inplace=True)


# In[19]:


matches_played.reset_index().head(8)


# In[20]:


win_percentage = round(matches_played['wins']/matches_played['Total Matches'],3)*100
win_percentage.head(3)


# In[21]:


trace1 = go.Bar(x=matches_played.index,y=matches_played['Total Matches'],
                name='Total Matches',opacity=0.4)

trace2 = go.Bar(x=matches_played.index,y=matches_played['wins'],
                name='Matches Won',marker=dict(color='red'),opacity=0.4)

trace3 = go.Bar(x=matches_played.index,
               y=(round(matches_played['wins']/matches_played['Total Matches'],3)*100),
               name='Win Percentage',opacity=0.6,marker=dict(color='gold'))

data = [trace1, trace2, trace3]

layout = go.Layout(title='Match Played, Wins And Win Percentage',xaxis=dict(title='Team'),
                   yaxis=dict(title='Count'),bargap=0.2,bargroupgap=0.1)

fig = go.Figure(data=data, layout=layout)
iplot(fig)


# ## -> Which stadium has hosted most matches?

# In[22]:


venue_matches=matches.groupby('venue').count()[['id']].sort_values(by='id',ascending=False).head()
ser = pd.Series(venue_matches['id']) 
ser


# In[23]:


venue_matches=matches.groupby('venue').count()[['id']].reset_index()

data = [{"x": venue_matches['id'],"y": venue_matches['venue'], 
          "marker": {"color": "lightblue", "size": 12},
         "line": {"color": "red","width" : 2,"dash" : 'dash'},
          "mode": "markers+lines", "name": "Women", "type": "scatter"}]

layout = {"title": "Stadiums and Matches", 
          "xaxis": {"title": "Matches Played", }, 
          "yaxis": {"title": "Stadiums"},
          "autosize":False,"width":900,"height":1000,
          "margin": go.layout.Margin(l=340, r=0,b=100,t=100,pad=0)}

fig = go.Figure(data=data, layout=layout)
iplot(fig)


# ## -> Total & Average Runs scored each season

# In[24]:


batsmen = matches[['id','season']].merge(deliveries, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
season=batsmen.groupby(['season'])['total_runs'].sum().reset_index()
avgruns_each_season=matches.groupby(['season']).count().id.reset_index()
avgruns_each_season.rename(columns={'id':'matches'},inplace=1)
avgruns_each_season['total_runs']=season['total_runs']
avgruns_each_season['average_runs_per_match']=avgruns_each_season['total_runs']/avgruns_each_season['matches']


# In[25]:


fig = {"data" : [{"x" : season["season"],"y" : season["total_runs"],
                  "name" : "Total Run","marker" : {"color" : "lightblue","size": 12},
                  "line": {"width" : 3},"type" : "scatter","mode" : "lines+markers" },
        
                 {"x" : season["season"],"y" : avgruns_each_season["average_runs_per_match"],
                  "name" : "Average Run","marker" : {"color" : "brown","size": 12},
                  "type" : "scatter","line": {"width" : 3},"mode" : "lines+markers",
                  "xaxis" : "x2","yaxis" : "y2",}],
       
        "layout" : {"title": "Total and Average run per Season",
                    "xaxis2" : {"domain" : [0, 1],"anchor" : "y2",
                    "showticklabels" : False},"margin" : {"b" : 111},
                    "yaxis2" : {"domain" : [.55, 1],"anchor" : "x2","title": "Average Run"},                    
                    "xaxis" : {"domain" : [0, 1],"tickmode":'linear',"title": "Year"},
                    "yaxis" : {"domain" :[0, .45], "title": "Total Run"}}}

iplot(fig)


# ## -> Boundary & Remaining Runs by each season

# In[26]:


Season_boundaries=batsmen.groupby("season")["batsman_runs"].agg(lambda x: (x==6).sum()).reset_index()
fours=batsmen.groupby("season")["batsman_runs"].agg(lambda x: (x==4).sum()).reset_index()
Season_boundaries=Season_boundaries.merge(fours,left_on='season',right_on='season',how='left')
Season_boundaries=Season_boundaries.rename(columns={'batsman_runs_x':'6"s','batsman_runs_y':'4"s'})
Season_boundaries['6"s'] = Season_boundaries['6"s']*6
Season_boundaries['4"s'] = Season_boundaries['4"s']*4
Season_boundaries['total_runs'] = season['total_runs']


# In[27]:


trace1 = go.Bar(
    x=Season_boundaries['season'],
    y=Season_boundaries['total_runs']-(Season_boundaries['6"s']+Season_boundaries['4"s']),
    name='Remaining runs',opacity=0.6)

trace2 = go.Bar(
    x=Season_boundaries['season'],
    y=Season_boundaries['4"s'],
    name='Run by 4"s',opacity=0.7)

trace3 = go.Bar(
    x=Season_boundaries['season'],
    y=Season_boundaries['6"s'],
    name='Run by 6"s',opacity=0.7)


data = [trace1, trace2, trace3]
layout = go.Layout(title="Run Distribution per year",barmode='stack',xaxis = dict(tickmode='linear',title="Year"),
                                    yaxis = dict(title= "Run Distribution"))

fig = go.Figure(data=data, layout=layout)
iplot(fig)


# ## -> How often is 200 or more runs being chased?

# In[28]:


high_scores=deliveries.groupby(['match_id', 'inning','batting_team','bowling_team'])['total_runs'].sum().reset_index()
high_scores1=high_scores[high_scores['inning']==1]
high_scores2=high_scores[high_scores['inning']==2]
high_scores1=high_scores1.merge(high_scores2[['match_id','inning', 'total_runs']], on='match_id')
high_scores1.rename(columns={'inning_x':'inning_1','inning_y':'inning_2','total_runs_x':'inning1_runs','total_runs_y':'inning2_runs'},inplace=True)
high_scores1=high_scores1[high_scores1['inning1_runs']>=200]
high_scores1['is_score_chased']=1
high_scores1['is_score_chased'] = np.where(high_scores1['inning1_runs']<=high_scores1['inning2_runs'], 'yes', 'no')


# In[29]:


slices=high_scores1['is_score_chased'].value_counts().reset_index().is_score_chased
list(slices)
labels=['No','Yes']
slices


# In[30]:


trace0 = go.Pie(labels=labels, values=slices,
              hoverinfo='label+value')

layout=go.Layout(title='200 score chased ?')
fig = go.Figure(data=[trace0], layout=layout)
iplot(fig)


# ## -> Which team scores most in different patches of overs?

# In[31]:


x=['Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Lions',
    'Rising Pune Supergiant', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Delhi Daredevils', 'Kings XI Punjab',
    'Chennai Super Kings', 'Rajasthan Royals', 'Deccan Chargers',
    'Kochi Tuskers Kerala', 'Pune Warriors', 'Rising Pune Supergiants', 'Delhi Capitals']

y = ['SRH','MI','GL','RPS','RCB','KKR','DC','KXIP','CSK','RR','SRH','KTK','PW','RPS','DC']

matches.replace(x,y,inplace = True)
deliveries.replace(x,y,inplace = True)


# In[32]:


runs_per_over = deliveries.pivot_table(index=['over'],columns='batting_team',values='total_runs',aggfunc=sum)
runs_per_over.reset_index(inplace=True)
runs_per_over.drop(['KTK','PW','RPS','GL'],axis=1,inplace=True)


# In[33]:


trace1 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['CSK'],name='CSK',marker= dict(color= "blue",size=12))
trace2 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['DC'],name='DC')
trace3 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['KKR'],name='KKR')
trace4 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['KXIP'],name='KXIP')
trace5 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['MI'],name='MI')
trace6 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['RCB'],name='RCB')
trace7 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['RR'],name='RR')
trace8 = go.Scatter(x=runs_per_over['over'],y = runs_per_over['SRH'],name='SRH')

data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8]

layout = go.Layout(title='Average Run in Each Over',xaxis = dict(tickmode='linear',title="Over"),
                                    yaxis = dict(title= "Runs"))

fig = go.Figure(data=data,layout=layout)
iplot(fig)


# ## -> Powerplay dismissals in each innings by year

# In[34]:


season=matches[['id','season','winner']]
complete_data=deliveries.merge(season,how='inner',left_on='match_id',right_on='id')
powerplay_data=complete_data[complete_data['over']<=6]
powerplay_dismissals=powerplay_data.dropna(subset=['dismissal_kind']).groupby(['season','match_id','inning'])['dismissal_kind'].agg(['count']).reset_index().groupby('season')['count'].max()
powerplay_dismissals=powerplay_dismissals.reset_index()

powerplay_dismissals_first=powerplay_data[ powerplay_data['inning']==1].dropna(subset=['dismissal_kind']).groupby(['season','match_id','inning'])['dismissal_kind'].agg(['count']).reset_index().groupby('season')['count'].mean()
powerplay_dismissals_first=powerplay_dismissals_first.reset_index()

powerplay_dismissals_second=powerplay_data[ powerplay_data['inning']==2].dropna(subset=['dismissal_kind']).groupby(['season','match_id','inning'])['dismissal_kind'].agg(['count']).reset_index().groupby('season')['count'].mean()
powerplay_dismissals_second=powerplay_dismissals_second.reset_index()


# In[35]:


trace1 = go.Bar(x=powerplay_dismissals.season,y=powerplay_dismissals["count"],
                name='Max',opacity=0.4)

trace2 = go.Bar(x=powerplay_dismissals_first.season,y=powerplay_dismissals_first["count"],name='Inning 1',
                marker=dict(color='red'),opacity=0.4)

trace3 = go.Bar(x=powerplay_dismissals_second.season,y=powerplay_dismissals_second["count"],name='Inning 2',
                marker=dict(color='lime'),opacity=0.4)

data = [trace1, trace2, trace3]
layout = go.Layout(title='Powerplay Average Dismissals per Year',
                   xaxis=dict(title='Year',tickmode='linear'),
                   yaxis=dict(title='Run'),bargap=0.2,bargroupgap=0.1)

fig = go.Figure(data=data, layout=layout)
iplot(fig)


# ## -> Top players with highest Average & Strike Rate 

# In[36]:


df_strike_rate = deliveries.groupby(['batsman']).agg({'ball':'count','batsman_runs':'mean'}).sort_values(by='batsman_runs',ascending=False)
df_strike_rate.rename(columns ={'batsman_runs' : 'strike rate'}, inplace=True)
df_runs_per_match = deliveries.groupby(['batsman','match_id']).agg({'batsman_runs':'sum'})
df_total_runs = df_runs_per_match.groupby(['batsman']).agg({'sum' ,'mean','count'})
df_total_runs.rename(columns ={'sum' : 'batsman run','count' : 'match count','mean' :'average score'}, inplace=True)
df_total_runs.columns = df_total_runs.columns.droplevel()
df_sixes = deliveries[['batsman','batsman_runs']][deliveries.batsman_runs==6].groupby(['batsman']).agg({'batsman_runs':'count'})
df_four = deliveries[['batsman','batsman_runs']][deliveries.batsman_runs==4].groupby(['batsman']).agg({'batsman_runs':'count'})
df_batsman_stat = pd.merge(pd.merge(pd.merge(df_strike_rate,df_total_runs, left_index=True, right_index=True),
                                    df_sixes, left_index=True, right_index=True),df_four, left_index=True, right_index=True)


# In[37]:


df_batsman_stat.rename(columns = {'ball' : 'ball', 'strike rate':'strike_rate','batsman run' : 'batsman_run',
                                  'match count' : 'match_count','average score' : 'average_score' ,'batsman_runs_x' :'six',
                                  'batsman_runs_y':'four'},inplace=True)
df_batsman_stat['strike_rate'] = df_batsman_stat['strike_rate']*100
df_batsman_stat.sort_values(by='batsman_run',ascending=False,inplace=True)
#df_batsman_stat.sort_values(by='batsman_run',ascending=False)
df_batsman_stat.reset_index(inplace=True)


# In[38]:


average_score=df_batsman_stat.sort_values(by='average_score',ascending=False)
average_score=average_score[average_score['match_count']>50].head(10)

strike_rate=df_batsman_stat.sort_values(by='strike_rate',ascending=False)
strike_rate=strike_rate[strike_rate['match_count']>50].head(10)


# In[39]:


trace1 = go.Bar(x=average_score['batsman'],y=average_score['average_score'],
                name='Average Score',marker=dict(color='gold'),opacity=0.6,showlegend=False)

trace2 = go.Bar(x=strike_rate['batsman'],y=strike_rate['strike_rate'],
                name='Strike Rate',marker=dict(color='brown'),opacity=0.6,showlegend=False)

fig = tools.make_subplots(rows=1, cols=2, subplot_titles=('Highest Average Score','Highest Strike Rate'))

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)

fig['layout']['xaxis1'].update(title='Player')
fig['layout']['xaxis2'].update(title='Player')

iplot(fig)


# ## -> Top scorer in each category 

# In[40]:


toppers=deliveries.groupby(['batsman','batsman_runs'])['total_runs'].count().reset_index()
toppers=toppers.pivot('batsman','batsman_runs','total_runs')
toppers.reset_index(inplace=True)


# In[41]:


top_6 = toppers.sort_values(6,ascending=False).head(10)
top_4 = toppers.sort_values(4,ascending=False).head(10)
top_2 = toppers.sort_values(2,ascending=False).head(10)
top_1 = toppers.sort_values(1,ascending=False).head(10)


# In[42]:


trace1 = go.Scatter(x=top_6.batsman,y =top_6[6],name='6"s',marker =dict(color= "blue",size = 9),line=dict(width=2,dash='dash'))
trace2 = go.Scatter(x=top_4.batsman,y = top_4[4],name='4"s',marker =dict(color= "orange",size = 9),line=dict(width=2,dash='longdash'))
trace3 = go.Scatter(x=top_2.batsman,y = top_2[2],name='2"s',marker =dict(color= "green",size = 9),line=dict(width=2,dash='dashdot'))
trace4 = go.Scatter(x=top_1.batsman,y = top_1[1],name='1"s',marker =dict(color= "red",size = 9),line=dict(width=2,dash='longdashdot'))

fig = tools.make_subplots(rows=4, cols=1, subplot_titles=('Top 6"s Scorer','Top 4"s Scorer',
                                                          'Top 2"s Scorer','Top 1"s Scorer'))

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 3, 1)
fig.append_trace(trace4, 4, 1)

fig['layout'].update(title='Top Scorer in each Category',showlegend=False)
iplot(fig)


# ## -> Who has scored the most centuries & half-centuries?

# In[43]:


cen = deliveries.groupby(['batsman','match_id']).agg({'batsman_runs':'sum'})
cen = cen[cen['batsman_runs']>=100]
cen = cen.groupby(['batsman']).agg({'count'})
cen.columns = cen.columns.droplevel()
cen = cen.sort_values(by='count',ascending=False).reset_index()
half_cen = deliveries.groupby(['batsman','match_id']).agg({'batsman_runs':'sum'})
half_cen = half_cen[half_cen['batsman_runs']>=50]
half_cen = half_cen[half_cen['batsman_runs']<100]
half_cen = half_cen.groupby(['batsman']).agg({'count'})
half_cen.columns = half_cen.columns.droplevel()
half_cen = half_cen.sort_values(by='count',ascending=False).reset_index()
df_big = pd.merge(cen,half_cen, on='batsman',how='right')
df_big = df_big.fillna(0)
batsman_stats = pd.merge(df_batsman_stat,df_big, on='batsman',how='left').fillna(0)
batsman_stats.rename(columns = {'count_x' : '100s', 'count_y' : '50s'},inplace=True)


# In[44]:


centuries = batsman_stats.sort_values(by='100s').tail(15)
half_centuries = batsman_stats.sort_values(by='50s').tail(15)


# In[45]:


fig = {"data" : [{"x" : centuries["batsman"],"y" : centuries["100s"],
                  "name" : "100s","marker" : {"color" : "lightblue","size": 12},
                  "line": {"width" : 3},"type" : "scatter","mode" : "lines+markers" ,
                  "xaxis" : "x1","yaxis" : "y1"},
        
                 {"x" : half_centuries["batsman"],"y" : half_centuries["50s"],
                  "name" : "50s","marker" : {"color" : "brown","size": 12},
                  "type" : "scatter","line": {"width" : 3},"mode" : "lines+markers",
                  "xaxis" : "x2","yaxis" : "y2"}],
       
        "layout" : {"title": "Total centuries and half-centuries by top batsman",
                    "xaxis2" : {"domain" : [0, 1],"anchor" : "y2",
                    "showticklabels" : True},"margin" : {"b" : 111},
                    "yaxis2" : {"domain" : [.55, 1],"anchor" : "x2","title": "50s"},                    
                    "xaxis" : {"domain" : [0, 1],"tickmode":'linear',"title": "Batsman"},
                    "yaxis" : {"domain" :[0, .45], "anchor" : "x2","title": "100s"}}}

iplot(fig)

