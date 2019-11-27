import pandas as pd
x1 = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
x2 = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics': [85,81,83]}
x3 = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS': [90,79,93]}
x4 = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT': [93,89,88]}

df1 = pd.DataFrame(x1, columns = ['Student','Math'])
df2 = pd.DataFrame(x2, columns = ['Student','Electronics'])
df3 = pd.DataFrame(x3, columns = ['Student','GEAS'])
df4 = pd.DataFrame(x4, columns = ['Student','ESAT'])

df12 = pd.merge(df1,df2)
df123= pd.merge(df12,df3)
df1234=pd.merge(df123,df4)

final = pd.melt(df1234, id_vars = ['Student'], value_vars =['Math','Electronics','GEAS','ESAT'],var_name = 'Subjects',value_name = 'Grades').sort_values('Student')
