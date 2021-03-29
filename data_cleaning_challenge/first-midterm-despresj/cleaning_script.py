import pandas as pd
from os import listdir

full_path = "/Users/josephdespres/Documents/Python/pythonChallenges/data_cleaning_proj/first-midterm-despresj/data/"

files = listdir("data")
pd.DataFrame(files)

gtd = pd.read_csv(full_path + files[0], encoding='latin1')
poverty = pd.read_csv(full_path + files[1])
counties = pd.read_csv(full_path + files[2], encoding='latin1')
county_cities = pd.read_csv(full_path + files[3], encoding='latin1')

poverty.columns
counties

