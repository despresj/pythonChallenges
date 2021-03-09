from numpy.core.fromnumeric import repeat
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
reference_gdp = np.tile(reference_gdp, reps)

# Make gdp percap relative to usa
my_gm['gdpPercapRel'] =  my_gm['gdpPercap']/reference_gdp

my_gm.sort_values(by='gdpPercapRel', ascending=False)
us = my_gm.loc[my_gm['country'] == 'United States']
us[['country', 'year', 'gdpPercapRel']]
