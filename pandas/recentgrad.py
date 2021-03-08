import pandas as pd
from pyprojroot import here

college_recent_grads = pd.read_csv(here("data/recent-grads.csv"))

college_recent_grads.head()

colnames = college_recent_grads.columns

# - Which major has the lowest unemployment rate?
unemp = college_recent_grads[['major', 'unemployment_rate']]
unemp.sort_values(by='unemployment_rate').head(20)

# - Which major has the highest percentage of women?
women_major = college_recent_grads[['major', 'sharewomen']]
women_major = women_major.sort_values(by="sharewomen", ascending=False)
women_major.round(3).head(20)


college_recent_grads['IQR'] = college_recent_grads['p75th'] - college_recent_grads['p25th']
college_recent_grads['IQR'].sort_values()

college_recent_grads.iloc[73]
# Note the IQR = 0...probally not accurate

# Find range of numeric values 
ran = lambda x: x.max() - x.min()
std = lambda x: x.std()
mean = lambda x: x.mean()
skew = lambda x: x.skew()



numeric_cols = college_recent_grads.select_dtypes(include='int64')
ranges = numeric_cols.apply(ran)
ranges = pd.DataFrame(ranges)
ranges.columns = ['range']
ranges['mean'] =  numeric_cols.apply(mean)
ranges['standardDev'] =  numeric_cols.apply(std)
ranges['third_moment'] = numeric_cols.apply(skew)
summarystats = ranges.T
print(summarystats)
