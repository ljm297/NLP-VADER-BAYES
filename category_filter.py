import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CATEGORY = 1

file = pd.read_csv('./input/USvideos.csv',error_bad_lines=False)
df = pd.DataFrame(file,columns=['video_id','title','channel_title','category_id','tags','views','likes','dislikes',
'comment_total','thumbnail_link','date'])

res = df.loc[df['category_id'] == CATEGORY]
print(res.info())

f = open("./input/youtube/temp_videos.csv",'w')
res.to_csv("./input/youtube/temp_videos.csv", index=False)

main = pd.read_csv("./input/UScomments.csv",error_bad_lines=False)
par = pd.read_csv("./input/youtube/temp_videos.csv",error_bad_lines=False)

#transform the dataframes to lists of dictionaries
main_dict=main.to_dict(orient='records')
par_dict=par.to_dict(orient='records')

#create a list of dictionaries that use only 'label' and 'value' as keys
par_dict = [{'video_id':i['video_id']} for i in par_dict]

#search for records in main that the pair of label-value exists in the previous list
result = [i for i in main_dict if {'video_id':i['video_id']} in par_dict]

#change back to dataframe and save to csv
result=pd.DataFrame(result)

result.to_csv('./input/youtube/temp_comments.csv', index=False)