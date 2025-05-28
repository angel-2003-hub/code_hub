#TASK-1
#PROGRAM 1

import pandas as pd
url='https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv'
data=pd.read_csv(url)
df=pd.DataFrame(data)
read=df.head()
print(read)

#PROGRAM 2

df=pd.read_csv('Cars.csv')
data=pd.DataFrame(df)
read_data=data.head()
read_tail=data.tail()
print("first few rows of the DataFrame:")
print(read_data)
print("last few rows of the DataFrame:")
print(read_tail)
print(data.shape)
print(data.describe)

#TASK-2

data={'Name':['John','Jane','Babu','Peter','Leju'],
      'Age':[25,30,35,40,55],
      'City':['New York','London','Paris','UK','Germany']}
df=pd.DataFrame(data)
print("DataFrame Creation:")
print(df)
print("The first five rows of the DataFrame")
print(df.head())
print(df.info())

#TASK-3

data={'Department':['MCA','MCA','MBA','MBA','MCA'],
      'Employee ID':['001','002','003','004','005'],
      'Salary':[25000,62000,90000,99000,90000],
      'Work Experience':[8,17,10,11,25],
      'Age':[29,40,32,39,45]}
df=pd.DataFrame(data)
print(df)
dep=df.groupby('Department')['Salary'].mean()

filter_data=dep[dep>60000]

print(dep)
department=df.groupby(['Department','Work Experience']).agg({'Salary':['sum', 'median'],'Age':['sum','mean']})
print(filter_data)
print(department)
custom_agg=df.groupby('Department')['Salary'].min()
print(custom_agg)

