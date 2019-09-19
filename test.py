import pandas as pd

def Run():
  xlName = input('请输入文件名(带上excel格式 .xls或.xlsx):')
  sheet1 = input('请输入需操作表的名称:')
  sheet2 = input('请输入数据来源表的名称:')
  df=pd.read_excel(xlName, sheet_name = sheet1)
  ef=pd.read_excel(xlName, sheet_name = sheet2)

  #第一张表的匹配列名
  s1Name = df.ix[:,['合同编号']].values
  #第二张表的匹配列名
  s2Name = ef.ix[:,['合同号']].values
  #第一张表的金额
  s1Amount = 0
  #第二张表的金额
  s2Amount = ef.ix[:,['回款金额']].values
  #需操作列的序号
  colIndex = 0

  for z in range(len(df.columns.values)):
    if df.columns.values[z] == '回款金额':
      colIndex = z
  
  len1 = len(s1Name)
  len2 = len(s2Name)
  
  # 获取第一张表的数据与第二张表的进行匹配
  for i in range(len1):
    for j in range(len2):
      if(s1Name[i] == s2Name[j]):
        df['回款金额'][i] = s2Amount[j]

  write = pd.ExcelWriter('new.xlsx')
  df.to_excel(write,sheet_name = sheet1,index=False)
  ef.to_excel(write,sheet_name = sheet2,index=False)
  write.save()
  print('写入成功，文件名：new.xlsx')

Run()