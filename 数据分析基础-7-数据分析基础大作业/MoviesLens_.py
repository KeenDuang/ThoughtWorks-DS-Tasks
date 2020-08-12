import pandas as pd
import math
import datetime
import matplotlib.pyplot as plt

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
time_2006_start = pd.to_datetime('2018-01-01')
time_2006_end = pd.to_datetime('2019-01-01')
time_diff_start = (time_2006_start - time_start).total_seconds()
time_diff_end = (time_2006_end - time_start).total_seconds()
rating_2018 = rating[(rating['timestamp'] >= time_diff_start) & (rating['timestamp'] < time_diff_end)]
users_2018_rating_num = rating_2018['userId'].nunique()  # 2018年评分人数

print('不同的用户数：' + str(users_num))
print('不同的电影数：' + str(movies_num))
print('不同的电影种类数：' + str(genres_num))
print('没有外部链接的电影数：' + str(no_link_num))
print('2018年进行过电影评分的用户数：' + str(users_2018_rating_num))

rating_2018 = rating[(rating['timestamp'] >= time_diff_start) & (rating['timestamp'] < time_diff_end)]
tag_2018 = tag[(tag['timestamp'] >= time_diff_start) & (tag['timestamp'] < time_diff_end)]
rating_ = pd.DataFrame(rating_2018.groupby('movieId').mean()['rating'])
tag_ = pd.DataFrame(tag_2018.groupby('movieId')['tag'].unique())
rating_ = pd.merge(rating_, tag_, how='left', left_index=True, right_index=True)


def gen_tag(x):
    try:
        if len(x) > 0:
            return '|'.join(x)
    except TypeError:
        pass


rating_.loc[:, 'tag'] = rating_['tag'].map(gen_tag)
rating_2018_good = rating_[rating_['rating'] >= 5]
rating_2018_good.to_csv('2018年评分5分以上的电影.csv')  # 2018年评分5分以上的电影及其对应的标签导出

rating_TheAvengers = rating[rating['movieId'] == 89745]
rating_TheAvengers.loc[:, 'timestamp'] = rating_TheAvengers['timestamp'].map(lambda x:
                                                                             time_start + datetime.timedelta(seconds=x))
rating_TheAvengers.loc[:, 'period'] = rating_TheAvengers['timestamp'].map(lambda x: x.to_period('M'))
rating_month = rating_TheAvengers.groupby('period')['rating'].mean()
plt.figure(figsize=(11, 8), dpi=120)
rating_month.plot(color='DarkBlue')
plt.xlabel('Month')
plt.ylabel('Rating')
plt.show()                                             # 电影复仇者联盟（The Avengers）每个月评分的平均值变化曲线图
