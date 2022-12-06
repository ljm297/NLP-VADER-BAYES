# NLP-VADER-BAYES

## Input

two files below are from kaggle dataset:
[Trending YouTube Video Statistics and Comments](https://www.kaggle.com/datasets/datasnaek/youtube?select=UScomments.csv)
```
UScomments.csv
USvideos.csv
```

Inside the input folder we filtered these two files and in our code, we only consider one type of video comments (Film & Animation, video_category_id = 1):

```
temp_comments.csv
temp_videos.csv
```

## Output
``sentiment_out.csv`` contains the output of VADER algorithm. Every row is a comment and has a tag of positive, negative, or neutral tag.
