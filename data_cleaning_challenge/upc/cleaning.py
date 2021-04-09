import pandas as pd
import re
import os
pd.set_option("display.max_rows", 100)

veggie, upc, cat =  ['data/'+ x for x in  os.listdir("data")]

def exceldict(path):
    xl_file1 = pd.ExcelFile(path, engine='openpyxl')
    dfs = {sheet_name: xl_file1.parse(sheet_name) 
            for sheet_name in xl_file1.sheet_names}
    return dfs

catagories = exceldict(cat)

def n_sheets(dict):
    output = str(len(dict.keys())) + " sheets"
    print(output)
    print("------")
    for key in dict.keys():
        print("- " + key)

n_sheets(catagories)

def sheet_viewer(dict):
    
    for key, value in dict.items():
        print("key: " + key)
        print(value)

sheet_viewer(catagories)

report = catagories['Report1']

def the_col_cleaner(df):
    cols = df.columns
    df.columns = [re.sub(r'\W+', '', x.replace('$','dollars')).lower() for x in cols]
    return(df)

msf = the_col_cleaner(report)

msf['allperiods'] = msf['allperiods'].str.replace('Latest 52 Wks - W/E', '')
msf['allproducts'] = msf['allproducts'].str.replace('MORNINGSTAR FARMS-', '')

msf[['product', 'category', 'upc1']] = msf['allproducts'].str.split('-', 2, expand=True)
# same info drop?
msf_clean = msf[['dollars', 'units', 'product', 'category', 'upc']]
# msf_clean

# UPC
upc_dict = exceldict(upc)

# n_sheets(upc_dict)

# sheet_viewer(upc_dict)

upc = the_col_cleaner(upc_dict['Report1'])
# set(upc['foodretailers'])

upc['foodretailers'] = upc['foodretailers'].str.replace(" Total TA", "").str.replace(" Total US TA", "").str.replace(" Food", "")
upc['weeks'] = upc['weeks'].str.replace("1 W/E ", "")

# upc

# Veggies
veggies = exceldict(veggie)

n_sheets(veggies)

sheet_viewer(veggies)

frozen = veggies['Frozen Foods']
frozen.columns = frozen.iloc[0]

the_col_cleaner(frozen)
