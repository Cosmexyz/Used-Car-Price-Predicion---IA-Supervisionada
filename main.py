#Arquivo principal do projeto
import pandas as pd 

df = pd.read_csv('data/used_cars.csv')
print(df.shape)
print('-' * 120)
print(df.columns)
print('-' * 120)
print(df.head())
print('-' * 120)
print(df.info())