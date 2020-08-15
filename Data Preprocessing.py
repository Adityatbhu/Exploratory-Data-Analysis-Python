 # -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:47:18 2020

@author: Aditya Tiwari
"""

import pandas as pd
import numpy as np
import seaborn as sns
from numpy import triu

df= pd.read_csv('C:/Users/Aditya Tiwari/Downloads/House_Price.csv',header=0)

df.head()
df.describe(include='all')
#%% different plots
sns.jointplot(x="n_hot_rooms", y="price", data=df)
sns.countplot(x="airport", data=df)
sns.countplot(x='waterbody', data= df)
df.drop('bus_ter',axis=1, inplace = True)  # droping a column bus_ter
sns.scatterplot(x='rainfall', y='price' , data=df)
sns.pairplot(df) # plots of all the variable

#%% Dealing with Outliiers 
df[(df.rainfall<lv)] # obtaing the rows havinf value less then lv(lower value by percentile)
np.percentile(df.rainfall,[1])[0]   # deciding the pecentile for lower outlier
lv=np.percentile(df.rainfall,[1])[0]
df[(df.rainfall<lv)]
df.rainfall[(df.rainfall<lv)]=0.3*lv
np.percentile(df.n_hot_rooms,[99.5])[0]  #deciding percentile for upper outlier
uv=np.percentile(df.n_hot_rooms,[99.5])[0]
df[(df.n_hot_rooms>uv)]
df.n_hot_rooms[(df.n_hot_rooms>uv)]=3*uv  # removal and replacing of outlier by 3 times of uv(upper value)


df.info()
#%%

df['n_hos_beds']=df['n_hos_beds'].fillna(df['n_hos_beds'].mean())  # fill na by mean




#%% Variable transformation 
df.crime_rate=np.log(1+df.crime_rate)
sns.scatterplot(x='crime_rate',y='price',data=df)

#%% replacing  a columns
df['avg.dist']= (df.dist1+df.dist2+df.dist3+df.dist4)/4


#%% deletion of columns

del df['dist1']
del df['dist2']
del df['dist3']
del df['dist4']


#%% creation of dummy variable

df= pd.get_dummies(df)
del df['waterbody_None']
del df['airport_NO']

#%% correlation matrix

cor=df.corr()
#%% heatmap for correlation matrix
plot=sns.heatmap(pp,square=False,cmap='BuPu',mask='mask',xticklabels=pp.columns.values)
fig=plot.get_figure()
pp=np.tril(cor)

