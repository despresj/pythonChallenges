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


reps = np.array([np.random.choice(df_yes_no.harass5, len(df), replace = True) for _ in range(1000)])
Mean = np.count(reps)

# pick up here TODO: get this one col bootstrap pcts.
rep = pd.DataFrame([np.random.choice(df_yes_no.harass5, len(df), replace=True) for _ in range(1000)])

rep.columns = ['answer']

counts = rep.groupby('answer').agg({'answer': 'count'})
counts.apply(lambda x: 100*x/x.sum())


