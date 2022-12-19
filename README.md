# NLP-VADER-BAYES

## Input

two files below are from kaggle dataset:
[Trending YouTube Video Statistics and Comments](https://www.kaggle.com/datasets/datasnaek/youtube?select=UScomments.csv)
```
UScomments.csv
USvideos.csv
```

Inside the input folder we use ``youtube-comments-sentiment-analysis.ipynb``
to filter these two files and in our code, we only consider one type of video comments (Film & Animation, video_category_id = 1):

```
CATE1_comments.csv
CATE1_videos.csv
```

## Output
``sentiment_out.csv`` contains the output of VADER algorithm. Every row is a comment and has a tag of positive, negative, or neutral tag.

## Naive Bayes Classifier Implement
The model is mainly based on a Naive Bayes Classifier written from scratch instead of 
implementing the python built-in NB classifiers.

The classifier is in `sentimental-analysis-using-naive-bayes-classifier.ipynb`

Details of training and testing can also be found in the same file.


## Referece
Data Cleaning and Vader Algorithm Usage:

https://www.kaggle.com/code/ankumagawa/sentimental-analysis-using-naive-bayes-classifier#3.-SENTIMENTAL-ANALYSIS

https://www.kaggle.com/code/tanmay111/youtube-comments-sentiment-analysis