import pandas as pd


dennys = pd.read_csv("pandas/data/dennys.csv")
laquinta =  pd.read_csv("pandas/data/laquinta.csv")
states = pd.read_csv("pandas/data/states.csv")


dennys.shape
dennys.columns

laquinta.shape
laquinta.columns

stateabbrev = states['abbreviation']

# We need to get only US locations get abbvs from df or 
# pydictionary in another file.
# get us states from another file
# exec(open("pandas/usstates.py").read())
# stateabbrev = us_state_abbrev.values()

nonUSlaq = laquinta[~laquinta['state'].isin(stateabbrev1)]
USlaquinta = laquinta[laquinta['state'].isin(stateabbrev)]
nonUSdenny = dennys[~dennys['state'].isin(stateabbrev1)]
USdenny = dennys[dennys['state'].isin(stateabbrev1)]

laqlat = USlaquinta[['city', 'state', 'longitude', 'latitude']].sort_values(by='latitude')
laqlong = USlaquinta[['city', 'state', 'longitude', 'latitude']].sort_values(by='longitude')

laqlat.head(20)
laqlat.tail(20)

laqlong.head(20)
laqlong.tail(20)

# Now we have only US values.

nonUSlaq[['city', 'state']]
# These would have to be manually entered to get the country

# which states have the fewest dennys and laquinta
USdenny[['address', 'state']].groupby('state').count().sort_values('address').head(10)
USdenny.count(level='state')
USdenny.count()

USlaquinta[['address', 'state']].groupby('state').count().sort_values('address').head(10)

# How many dennys per square mile?

ndennys = USdenny[['address', 'state']].groupby('state').count()
ndennys.columns = ['n']


dennystate = ndennys.merge(states, how='left', left_on='state', right_on='abbreviation')
dennystate['denpersq'] = dennystate['n'] / dennystate['area']
# Which state has the most dennys per sq mile
topdennys = dennystate.sort_values(by='denpersq', ascending=False).head()
topdennys
# How many laquinta's per square mile?

nlaq = USlaquinta[['address', 'state']].groupby('state').count().sort_values('address')
nlaq.columns = ['n']
nlaq = nlaq.merge(states, how='left', left_on='state', right_on='abbreviation')

nlaq['persqmile'] = nlaq['n'] / nlaq['area']

nlaq.sort_values(by='persqmile', ascending=False).head()

dennys['estab'] = 'dennys'
dennys
laquinta['estab'] = 'laquinta'

master = dennys.append(laquinta)
df.loc[df['column_name'] == some_value]
mi = master.loc[master['state'] == "MI"]
mi.head()