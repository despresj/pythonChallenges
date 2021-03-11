import pandas as pd
from pyprojroot import here


fship = pd.read_csv("pandas/data/The_Fellowship_Of_The_Ring.csv")
ttow =  pd.read_csv("pandas/data/The_Two_Towers.csv")
rking = pd.read_csv("pandas/data/The_Return_Of_The_King.csv")

lotr_untidy = pd.concat([fship, ttow, rking])

lotr_untidy
lotr_tidy = lotr_untidy.melt(value_vars=['Male', 'Female'], id_vars=['Film', 'Race'])
lotr_tidy

lotr_tidy.to_csv('pandas/data/lotr_tidy.csv')

female = pd.read_csv("pandas/data/Female.csv")
male = pd.read_csv("pandas/data/Male.csv")

lotr = pd.concat([female, male])
lotr_tidy = lotr.melt(value_vars=['Elf', 'Hobbit', 'Man'], 
                      id_vars=['Film', 'Gender'], var_name='Race', value_name='wordsSpoken')


lotr_tidy.groupby(['Film', 'Race']).agg('mean').sort_values('wordsSpoken', ascending=False)



table = lotr_tidy.pivot_table(values='wordsSpoken', index=['Film'], columns=['Race', 'Gender'])
lotr_tidy.groupby('Gender').agg('sum')

# Groubby is a life saver lets try to get a sum with untidy data
sum(table['Elf']['Female'] + table['Man']['Female'] + table['Hobbit']['Female'])
# Female
sum(table['Elf']['Male'] + table['Man']['Male'] + table['Hobbit']['Male'])
# Male

lotr_tidy['Race-Gender'] = lotr_tidy['Race'] + ' - ' + lotr_tidy['Gender']


gb = lotr_tidy.groupby('Race-Gender')    
a,b,c,d,e,f= [gb.get_group(x)[['Film', 'Race-Gender', 'wordsSpoken']] for x in gb.groups]

a.head()
b
c
d
e
f