import pandas as pd
import numpy as np
def test_population():
    data=pd.read_csv("task1/input.txt",encoding='utf-16',escapechar='\\',na_values='--')
    count = 0
    col = data["2010"].replace("--",0)
    col = data["2010"].replace(np.NaN,0)
    for population in col:
        count = count + float(population)
    assert int(count) == 7065
