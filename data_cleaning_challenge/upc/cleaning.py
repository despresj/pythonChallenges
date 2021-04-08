import pandas as pd
import re

pd.set_option("display.max_rows", 30)

def exceldict(path):
    xl_file1 = pd.ExcelFile(path, engine='openpyxl')
    dfs = {sheet_name: xl_file1.parse(sheet_name) 
            for sheet_name in xl_file1.sheet_names}
    return dfs

catagories = exceldict("data/MSF_Catagories.xlsx")
catagories
for key in catagories.keys():
    print(key)

def n_sheets(dict):
    output = str(len(dict.keys())) + " sheets"
    print(output)
    print("------")
    for key in dict.keys():
        print(key)

n_sheets(catagories)

a, b, c = categories.values()
a # not helpful
b # not helpful
c

report = catagories['Report1']

def the_col_cleaner(df):
    cols = df.columns
    df.columns = [re.sub(r'\W+', '', x.replace('$','dollars')).lower() for x in cols]
    return(df)

msf = the_col_cleaner(report)

msf['allperiods'] = msf['allperiods'].str.replace('Latest 52 Wks - W/E', '')
msf['allproducts'] = msf['allproducts'].str.replace('MORNINGSTAR FARMS-', '')

msf[['product', 'category', 'upc1']] = msf['allproducts'].str.split('-', 2, expand=True)

upc = msf['upc'].astype(float)
upc1= msf['upc1'].astype(float)

upc[upc != upc1]
# same info drop?
msf_clean = msf[['dollars', 'units', 'product', 'category', 'upc']]
msf_clean

# UPC

upc_dict = exceldict("data/MSF_UPC.xlsx")

n_sheets(upc_dict)

# sepaerate sheets
a, b, c = upc_dict.values()
a # not helpful
b # not helpful
c

upc = the_col_cleaner(upc_dict['Report1'])
upc

for df in upc_dict:
    print(upc_dict[df])
    print("|||||||||||||||||||||||||||||||||||")

upc_cleaned = the_col_cleaner(upc_dict['Report1'])
upc_cleaned.columns



veggies = exceldict("data/KUSA Price List - Frozen Veggie.xlsx")

veggies

dfs['Frozen Foods'].columns = dfs['Frozen Foods'].iloc[2]

dfs['Frozen Foods'].columns 
for key in dfs.keys():
    print(dfs[key])
    
    
