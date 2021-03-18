import pandas as pd
from pyprojroot import here

df = pd.read_csv(here("pandas/data/london.csv"))
df.shape

df['date'] = pd.to_datetime(df['EventDate'], format='%Y%m%d',errors ='coerce')
df = df[pd.notnull(df['date'])]
# There were a few entry errors we lose about 100 obs
df.shape

df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month

df['yearfreq']=df.groupby(by='year')['year'].transform('count')

# Which month has the most plays?
df.groupby('month').agg(count = ('EventDate', 'count')).sort_values('count', ascending=False)
# Note plays were more ocmmon in the winder months from nov-feb

# .dayofweek Monday=0, Sunday=6.
df['dayOfWeek'] = pd.DatetimeIndex(df['date']).dayofweek + 1
# .dayofweek + 1 Monday=1, Sunday=7.
dayOfWeek={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
df['weekday'] = df['date'].dt.dayofweek.map(dayOfWeek)
df.groupby('weekday').agg(count = ('EventDate', 'count')).sort_values('count', ascending=False)
# tues saturday friday have the most plays and the fewest on 

Theatres = df.groupby('TheatreCode').agg(count = ('EventDate', 'count'), 
                              min = ('date', 'min'),
                              max = ('date', 'max'))

Theatres.sort_values('count', ascending=False)

Theatres['duration'] = Theatres['max'] - Theatres['min']

Theatres.sort_values('duration', ascending=False).head()
#The top 5 longest running theaters. 