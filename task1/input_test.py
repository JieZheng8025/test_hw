import pandas as pd
def test_input():
    data=pd.read_csv("task1/input.txt",encoding='utf-16',escapechar='\\',na_values='--',index_col=0)
    assert len(data.columns)==31
    assert len(data.index)==225
