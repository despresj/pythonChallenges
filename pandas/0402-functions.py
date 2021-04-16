from numpy.lib.function_base import quantile
import pandas as pd
import numpy as np

from pyprojroot import here

my_gm = pd.read_csv(here("pandas/data/my_gm.csv"))

my_gm

min(my_gm.lifeExp)
max(my_gm.lifeExp)


def mean(x):
    return sum(x) / len(x)

def get_xtile(obj, quant):
    return obj.quantile(quant)

def get_xtile(obj, quant=[.20, .80]):
    if len(quant) != 2:
        print("hey were trying to get the range! \nGive me two quantiles to subtract!")
    elif 0 < quant[0] < quant[1] < 1:
        return obj.quantile(quant).diff().iloc[1]
    else:
        print("No! Give me quantiles satistying 0 < lower < upper < 1")


get_xtile(my_gm['lifeExp'],  quant=[.4, .5, 0.4])
get_xtile(my_gm['lifeExp'],  quant=[.8, .5])
get_xtile(my_gm['lifeExp'],  quant=[.4, .5])

my_gm_numeric = my_gm.select_dtypes(include='number')
