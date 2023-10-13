import pandas as pd
films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])
