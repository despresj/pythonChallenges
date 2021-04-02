import pandas as pd
import re

pd.set_option("display.max_rows", 101)
xl_file = pd.ExcelFile("data/MSF_Catagories.xlsx", engine='openpyxl')

dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}

df = dfs['Report1']

def the_col_cleaner(df):
    cols = df.columns
    df.columns = [re.sub(r'\W+', '', x.replace('$','dollars')).lower() for x in cols]
    return(df)

the_col_cleaner(df)

df['allperiods'] = df['allperiods'].str.replace('Latest 52 Wks - W/E', '')

for column in df.columns:
    print(df[column])
    
xl_file1 = pd.ExcelFile("data/MSF_UPC.xlsx", engine='openpyxl')
dfs = {sheet_name: xl_file1.parse(sheet_name) 
          for sheet_name in xl_file1.sheet_names}

dfs.keys()

dfs['Report1']

cleaned = the_col_cleaner(dfs['Report1'])
cleaned.columns

def exceldict(path):
    xl_file1 = pd.ExcelFile(path, engine='openpyxl')
    dfs = {sheet_name: xl_file1.parse(sheet_name) 
            for sheet_name in xl_file1.sheet_names}
    return dfs

dfs = exceldict("data/KUSA Price List - Frozen Veggie.xlsx")

dfs['Frozen Foods'].columns = dfs['Frozen Foods'].iloc[2]

dfs['Frozen Foods'].columns 
for key in dfs.keys():
    print(dfs[key])