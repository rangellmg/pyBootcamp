import pandas as pd
import matplotlib as mpl

df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
excel_file = pd.ExcelFile("https://pycourse.s3.amazonaws.com/temperature.xlsx")
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')

# Leitura de dados
# print(df)
# print(df2)

# n = 3
# print(df.head(n))
# print(df.tail(n))
#
# print(df.dtypes)
# print(df.describe())
# print(df.info())
# print(df.columns)

# Indexação
# print(df.head())
# print(df['date'])
# print(df[['date', 'classification']])
# print(type(df[['date', 'classification']]))
# print(df.iloc[:, 1])
# print(df.loc[:, 'temperatura'])
# print(df.iloc[:, 1:3])
# print(df.loc[:, 'temperatura':])

# Indexação booleana
df['date'] = pd.to_datetime(df['date'])
# print(df.dtypes)
df = df.set_index('date')
# print(df)
# cond = df.index <= '2020-03-01'
# print(df[cond])
# print(df.loc[df.index <= '2020-03-01', ['classification']])
# print(df.iloc[df.index <= '2020-03-01', [-1]])

# Ordenação
# print(df.sort_values(by='temperatura'))
# print(df.sort_values(by='classification'))
# print(df.sort_values(by=['classification', 'temperatura']))
# print(df.sort_values(by='temperatura', ascending=False))
# print(df.sort_index())
# print(df.sort_index(ascending=False))

# Visualização
# df.plot()
# df.plot(figsize=(10, 5))
# df.plot(figsize=(10, 5), grid=True)
# df.plot(style='-o', figsize=(10, 5), grid=True)
# df.plot(style='--', figsize=(10, 5), grid=True)
# df.plot(style='-.',figsize=(10, 5), grid=True)
# df.plot(style='-o', linewidth=2.5, figsize=(10, 5), grid=True)
# df.plot(style='-o', linewidth=2.5, color='red', figsize=(10, 5), grid=True)
# df.plot(style ='-o', linewidth=2.5, color='#b05dcf', figsize=(10, 5), grid=True)