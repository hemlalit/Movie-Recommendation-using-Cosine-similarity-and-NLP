import os
from django.conf import settings
import pickle

file_path = os.path.join(settings.BASE_DIR, 'projectApp', 'ml_models')
df = pickle.load(open(f'{file_path}/movies.pkl', 'rb'))
similarity_overview = pickle.load(open(f'{file_path}/similarity_overview.pkl', 'rb'))
similarity_genre = pickle.load(open(f'{file_path}/similarity_genre.pkl', 'rb'))

def recommend_movies(movie_name, filter_by='overview'):
    index = df[df['movie_name'] == movie_name].index[0]
    sim = similarity_overview if filter_by == 'overview' else similarity_genre
    scores = list(enumerate(sim[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommendations = [
        {
            'title': df.iloc[i]['movie_name'],
            'overview': df.iloc[i]['overview'],
            'genre': df.iloc[i]['genre']
        }
        for i, _ in sorted_scores
    ]
    return recommendations