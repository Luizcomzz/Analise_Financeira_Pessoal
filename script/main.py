import pandas as pd
import sqlite3 as sql

df = pd.read_csv("data/finanças_2026.csv", header=0, encoding= "utf-8")


#print(df.head()) #verificar os arquivos da base de dados
#print(df.info()) #verificar o tipo de dados de cada coluna 

df.columns = df.columns.str.lower().str.strip()
df = df.rename(columns={
    'descrição': 'descricao',
    'ano_mes': 'data'
})


df['valor'] = (
    df['valor']
    .str.replace('R$', '', regex=False) # remove cifrão
    .str.replace('.', '', regex=False)   # remove milhar
    .str.replace(',', '.', regex=False)  # troca decimal
    .str.strip()
    .astype(float)
)
# converter data para modelo aaaa-mm-dd
df['data'] = pd.to_datetime(df['data']) 

def categorizar(descricao):
    descricao = descricao.lower()
    
    if "uber" in descricao or "99" in descricao or "gasolina" in descricao or "estacionamento" in descricao or "top" in descricao:
        return "Transporte"
    elif "ifood" in descricao or "restaurante" in descricao or "lanche" in descricao or "almoço" in descricao:
        return "Alimentação"
    elif "farmacia" in descricao or "consulta" in descricao:
        return "Saúde"
    elif "livro" in descricao or "curso" in descricao:
        return "Educação"
    elif "passeio" in descricao or "passagem" in descricao or "netflix" in descricao or "prime" in descricao or "forró" in descricao:
        return "Lazer"
    elif "fatura nu" in descricao:
        return "Cartão"
    else:
        return "Outros"

df['categoria'] = df['descricao'].apply(categorizar) #definir a variável categoria
df['mes'] = df['data'].dt.to_period('M').astype(str)

#verificar os gastos totais usando python
#print("total Gastos: ", df['valor'].sum())
      
# verifica os gatos por categoria de maneira descendente usando python
#print(df.groupby('categoria')['valor'].sum().sort_values(ascending=False))

#verificar compras por mês
print(df.groupby('mes')['valor'].sum())
print()
print(df.sort_values(by='valor', ascending=False).head(10))
print()

#criar uma tabela utilizando sql
conn = sql.connect("financas.db")

df.to_sql("gastos", conn, if_exists="replace", index=False)

consulta = """
SELECT
    categoria,
    SUM(valor) AS total
FROM gastos
GROUP BY categoria
ORDER BY total DESC
"""

resultado = pd.read_sql_query(consulta, conn)

print()
print(resultado)

conn.close()
