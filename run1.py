# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:07:02 2019

@author: mw
"""

import mysql.connector
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from pandas import DataFrame

connection = mysql.connector.connect(host='localhost',
                                         database='twitter',
                                         user='root')

le = LabelEncoder()

sql_select_Query = "select * from feeds_twitter_1706"
df = pd.read_sql(sql_select_Query, connection)
df_match = pd.DataFrame({'Topik/Category':['5. Friso Category']*df.shape[0],
                  'Row ID':df['id'],
                  'Published Date':df['published_date'],
                  'Author':df['author_id'],
                  'Content':df['content'],
                  'Buzz':1+df['num_replies']+df['num_rts'],
                  'Buzz exc Like':1+df['num_replies']+df['num_rts'],
                  'Potential Reach':df['followers']+df['num_reach'],
                  'Original Reach':df['followers'],
                  'Viral Reach':df['num_reach'],
                  'Viral Score':df['num_reach']/(1+df['followers']),
                  'Engagement':df['num_replies']+df['num_rts'],
                  'Engagement exc Like':df['num_replies']+df['num_rts'],
                  'Replies':df['num_replies'],
                  'Retweets':df['num_rts'],
                  'Comments':0*df.shape[0],
                  'Likes':0*df.shape[0],
                  'Shares':0*df.shape[0],
                  'Dislikes':0*df.shape[0],
                  'Favorites':0*df.shape[0],
                  'Views':0*df.shape[0],
                  'Link URL':df['link'],
                  'Image URL':['-']*df.shape[0],
                  'Video URL':['-']*df.shape[0],
                  'Sentiment':df['sentiment_value']*df.shape[0],
                  'Media Type':['-']*df.shape[0],
                  'Mood':df['misc'],#['-']*df.shape[0],
                  
                  
            'label':le.fit_transform(df['sentiment_value']),
            'alpha':['a']*df.shape[0],
            'text':df['summary'].replace(r'\n',' ',regex=True)})


#export_excel = df.to_excel (r'C:\Users\mw\Documents\application\result.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path


