import pandas as pd

df = pd.read_csv("data/finanças_2026.csv", header=0, encoding= "utf-8")


print(df.head()) #verificar os arquivos da base de dados
print(df.info()) #verificar o tipo de dados de cada coluna 

df.columns =  df.columns.str.lower().str.strip() #transformar todos os nomes em minusculos e exclui espaço em branco

