from numpy.core.fromnumeric import repeat, sort
from numpy.lib.arraysetops import unique
import pandas as pd
from numpy import tile
from pyprojroot import here
my_gm = pd.read_csv(here("pandas/data/my_gm.csv"))
my_gm['gdp'] = my_gm['pop'] * my_gm['gdpPercap']
my_gm[['year','country','gdpPercap']].sort_values(by='gdpPercap', ascending=False).head(40)
# Looks about right

us_df = my_gm.loc[my_gm['country'] == 'United States']
reps = my_gm['country'].nunique()

reference_gdp = us_df['gdpPercap'].unique()
reference_gdp = tile(reference_gdp, reps)

# Make gdp percap relative to usa
my_gm['gdpPercapRel'] =  my_gm['gdpPercap']/reference_gdp
# Double Checking Transformation
my_gm.sort_values(by='gdpPercapRel', ascending=False)
us = my_gm.loc[my_gm['country'] == 'United States']
us[['country', 'year', 'gdpPercapRel']]
# That is what we want to see

my_gm['country_continent'] = my_gm['country'] + ' - ' + my_gm['continent']

my_gm['country_continent']

  
# my_gm.rename(columns = {'lifeExp': "life_exp",
#                         'gdpPercap': 'gep_percap',
#                         'gepPercapRel': 'gdp_percap_rel'
#                         })

my_gm[(my_gm['country'] == 'Burundi') & (my_gm['year'] > 1996)]

my_gm[['gdpPercap', 'year','lifeExp']]
  
my_gm.groupby(['continent']).agg(['mean', 'std'])
# get column wise desc stats
my_gm.groupby(['continent']).size()
# my_gm %>% count(continent)

my_gmsum = my_gm[my_gm['year'].isin([1952, 2007])].groupby(['continent', 'year'])
my_gmsum['lifeExp', 'gdpPercap'].agg(['mean', 'median'])
my_gmsum['lifeExp', 'gdpPercap'].agg(['mean', 'median']).T

  
my_gm['pct_pop_change'] = my_gm.groupby('country', sort=False)['pop'].apply(
    lambda x: x.pct_change()).to_numpy()

my_gm['pop_gain'] = my_gm.groupby('country', sort=False)['pop'].apply(
    lambda x: x.diff()).to_numpy()

my_gm.sort_values(by='pop_gain', ascending=True)
asia = my_gm[my_gm['continent'] == "Asia"]

asia[['pop_gain']].value_counts().nlargest(1)

# get records with min and max population gain.
asia.iloc[asia['pop_gain'].idxmax()]
asia.iloc[asia['pop_gain'].idxmin()]