import pandas as pd
import numpy as np

df = pd.read_csv("http://www2.stat.duke.edu/~mc301/data/gss2016.csv")

df['harass5'].unique()

definate_answers = ['Yes', 'No']
df_yes_no = df[df.harass5.isin(definate_answers)]

df_yes_no.groupby(by='harass5').sum()

df_yes_no.groupby("harass5").count()

pct = df_yes_no.groupby('harass5').agg({'harass5': 'count'})
pct.apply(lambda x: 100*x/x.sum())

[np.random.choice(df_yes_no.harass5, len(df), replace=True) for _ in range(1000)]

reps = np.array([np.random.choice(df_yes_no.harass5, len(df), replace=True) for _ in range(1000)])
mean = pd.DataFrame(reps)
mean

output = []
sum_yes = []
sum_no = []
niters = 1000
for _ in range(niters):
  sample = np.random.choice(df_yes_no.harass5, len(df_yes_no), replace=True)
  unique, counts = np.unique(sample, return_counts=True)
  yes, no = counts
  sum_yes.append(yes)
  sum_no.append(no)

full = [sum_yes, sum_no]
  
bootstrapped = pd.DataFrame(list(zip(sum_yes, sum_no)), columns = ['yes', 'no'])

total = len(df_yes_no)
f = lambda x: x / total

pcts = bootstrapped.apply(f)
pcts.describe()



df_yes_no.groupby(['born']).size()
df_yes_no.groupby(['educ']).size()



df_yes_no = df_yes_no[df_yes_no['educ'] != "No answer"]

df_yes_no.count('advfront')

df_yes_no['advfront']

df_yes_no.groupby('polviews').count()


d = {
  'Extremely liberal': 'Liberal',
  'Slightly liberal': 'Liberal',
  'Slghtly conservative': 'Conservative',
  'Extrmly conservative': 'Conservative'
}

df_yes_no['polviews_col'] = df_yes_no.polviews.map(d).fillna(df_yes_no['polviews'])
  
df_yes_no.groupby('polviews_col').count()

lib_con = ['Liberal', 'Conservative']

only_lib_con = df_yes_no[df_yes_no.polviews_col.isin(lib_con)]

groupped = only_lib_con.groupby(['polviews_col','wrkstat'])
counts = groupped.size()

 new_df = counts.to_frame(name = 'size').reset_index()
 
 only_lib_con.count()
 
 new_df['pct'] = new_df['size'] / 839
 new_df