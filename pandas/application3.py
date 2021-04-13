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
niters = 100000
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



df.groupby(['born']).size()
df.groupby(['educ']).size()

