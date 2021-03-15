import pandas as pd
from pyprojroot import here

gm = pd.read_csv(here("pandas/data/my_gm.csv"))

gm.groupby('continent').count()['country']
gm['country'] = gm['country'].astype('category')

# focus on these countries
h_countries = ["Egypt", "Haiti", "Romania", "Thailand", "Venezuela"]
h_gap = gm[gm['country'].isin(h_countries)]
h_gap['country'] = h_gap['country'].cat.remove_unused_categories()

h_gap

# countries with a pop < 0.25m
small_pop = gm[gm['pop'] < 2.5e5]
small_pop['country'] = small_pop['country'].cat.remove_unused_categories()

# default is alphabetical
gm.groupby('continent').count()['country']
gm['continent'] = gm['continent'].astype('category')

#reverse factor orderes
gm['continent'].cat.categories = gm['continent'].cat.categories[::-1]
gm['continent'].cat.categories

#TODO: Exercize 4 and on


