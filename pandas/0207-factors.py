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


# reverse factor orderes
cats=gm['continent'].cat.categories[::-1]
gm['continent'] = gm['continent'].astype(pd.CategoricalDtype(categories= cats, ordered = True))
gm.head(50)

# manually reset order
cat_type = pd.CategoricalDtype(categories=['Europe', 'Africa', 'Americas', 'Asia', 'Oceania'], ordered = True)
gm['continent'] = gm['continent'].astype(cat_type)
gm.head(50)

# reorder by population order in 2009
year07 = gm[gm['year'] == 2007]
bypop07 = year07.groupby('continent').sum().sort_values('pop', ascending=False).index.values.tolist()
bypop07 = pd.Series(bypop07)

continents07 = pd.CategoricalDtype(bypop07, ordered=True)

year07['continent'] = year07['continent'].astype(continents07)
cats = year07['continent'].cat.categories
cats