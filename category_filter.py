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