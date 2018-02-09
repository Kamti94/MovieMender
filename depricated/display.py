import pandas as pd
import numpy as np
#import statsmodels.formula.api as sm
#import scipy.sparse as sp
#from scipy.sparse.linalg import svds

#Reading users file:
#from statsmodels.tools.eval_measures import rmse

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('D:/Be project/u.user', sep='|', names=u_cols,
encoding='latin-1')

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
data = pd.read_csv('D:/Be project/u.data', sep='\t', names=r_cols,
encoding='latin-1')
ratings = pd.read_csv('D:/Be project/ua.base', sep='\t', names=r_cols,
encoding='latin-1')


#Reading items file:
i_cols = ['movie_id', 'movie_title' ,'release_date','video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv('D:/Be project/u.item', sep='|', names=i_cols,
 encoding='latin-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)
movie_stats = lens.groupby('movie_title').agg({'rating': [np.size, np.mean]})
atleast_100 = movie_stats['rating']['size'] >= 110
final=movie_stats[atleast_100].sort_values([('rating', 'mean')], ascending=False)

#print(final.loc['Pather Panchali (1955)'])
#print(final.iloc[0].name)
