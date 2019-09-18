import pandas as pd

def Run():
  # https://www.cnblogs.com/liulinghua90/p/9935642.html
  df=pd.read_excel('test.xlsx',sheet_name='Sheet1')
  print(len(df.columns.values))
  
  ef=pd.read_excel('test.xlsx',sheet_name='Sheet2')
  print(ef)
Run()