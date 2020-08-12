import pandas as pd

rates = pd.read_csv('./ml-25m/ratings.csv')
rating = pd.DataFrame(rates.groupby('movieId').mean()['rating'], columns=['rating'])


def gen_level(x):
    if 0 < x <= 1: return 1
    if 1 < x <= 2: return 2
    if 2 < x <= 3: return 3
    if 3 < x <= 4: return 4
    if 4 < x <= 5: return 5


rating['level'] = rating['rating'].map(lambda x: gen_level(x))
counts = rating.groupby('level')['rating'].count()
print('(0:1]档共有%s部电影' % counts[1])
print('(1:2]档共有%s部电影' % counts[2])
print('(2:3]档共有%s部电影' % counts[3])
print('(3:4]档共有%s部电影' % counts[4])
print('(4:5]档共有%s部电影' % counts[5])

rating['comment'] = rating['rating'].map(lambda x: '推荐' if x > 4 else '不推荐')
rating.to_csv('comment.csv')
