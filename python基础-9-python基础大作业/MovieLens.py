import pandas as pd
import math
import datetime

tag = pd.read_csv('./ml-25m/tags.csv')
rating = pd.read_csv('./ml-25m/ratings.csv')
movie = pd.read_csv('./ml-25m/movies.csv')
link = pd.read_csv('./ml-25m/links.csv')
genome_scores = pd.read_csv('./ml-25m/genome-scores.csv')
genome_tags = pd.read_csv('./ml-25m/genome-tags.csv')

users_num = (tag['userId'].append(rating['userId'])).nunique()  # 用户id
movies_num = movie['movieId'].nunique()  # 电影id

genres = []
for i in range(len(movie)):
    genres.extend(movie['genres'][i].split('|'))
genres_num = pd.Series(genres).nunique()  # 电影种类

idx = []
for i in range(len(link)):
    if math.isnan(link['imdbId'][i]) and math.isnan(link['tmdbId'][i]):
        idx.append(i)
no_link_num = pd.Series(idx).nunique()  # 没有外部链接的电影

time_start = pd.to_datetime('1970-01-01')
time_2006_start = pd.to_datetime('2006-01-01')
time_2006_end = pd.to_datetime('2007-01-01')
time_diff_start = (time_2006_start - time_start).total_seconds()
time_diff_end = (time_2006_end - time_start).total_seconds()
rating_2018 = rating[(rating['timestamp'] >= time_diff_start) & (rating['timestamp'] < time_diff_end)]
users_2018_rating_num = rating_2018['userId'].nunique()  # 2018年评分人数

print('不同的用户数：' + str(users_num))
print('不同的电影数：' + str(movies_num))
print('不同的电影种类数：' + str(genres_num))
print('没有外部链接的电影数：' + str(no_link_num))
print('2018年进行过电影评分的用户数：' + str(users_2018_rating_num))
