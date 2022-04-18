import pandas as pd

Course = ['math', 'Chinese', 'English']
Harry_Number = ['18','18','18']
Cici_Number = ['20','20','20']
dataframe = pd.DataFrame({'Course':Course,'Harry':Harry_Number,'Cici':Cici_Number})
dataframe.to_csv("result.csv",index=False,sep=' ')