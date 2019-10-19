import DBConnection
import pandas as pd

sql_select_Query = "select * from feeds_twitter_1706"
df = pd.read_sql(sql_select_Query, DBConnection)
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
                  'Mood':df['misc']})


export_excel = df.to_excel (r'application\excel\result.xlsx', index = None, header=True)