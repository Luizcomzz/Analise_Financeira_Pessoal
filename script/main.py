import pandas as pd
import sqlite3 as sql

def carregar_dados(caminho):
    return pd.read_csv(caminho, header=0, encoding= "utf-8")


def tratar_dados(df):
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
    df['categoria'] = df['descricao'].apply(categorizar) #definir a variável categoria
    df['mes'] = df['data'].dt.to_period('M').astype(str)

    return df

def categorizar(descricao):
    descricao = descricao.lower()
    
    if "uber" in descricao or "99" in descricao or "gasolina" in descricao or "estacionamento" in descricao or "top" in descricao:
        return "Transporte"
    elif "ifood" in descricao or "restaurante" in descricao or "lanche" in descricao or "almoço" in descricao:
        return "Alimentação"
    elif "farmacia" in descricao or "consulta" in descricao or "dentista" in descricao:
        return "Saúde"
    elif "livro" in descricao or "curso" in descricao:
        return "Educação"
    elif "passeio" in descricao or "passagem" in descricao or "netflix" in descricao or "prime" in descricao or "forró" in descricao:
        return "Lazer"
    elif "fatura nu" in descricao:
        return "Cartão"
    else:
        return "Outros"

#criar uma tabela utilizando sql
def criar_tabela(df, nome_banco):
    conn = sql.connect(nome_banco)

    df.to_sql("gastos", conn, if_exists="replace", index=False)

    return conn

# Aqui pode consultar da mesma forma que faz com SQL
def consultar_total(conn): #consulta do valor total gasto nessa tabela 
    consulta = """
    SELECT
    SUM(valor) AS gastos
    FROM gastos
    """
    return pd.read_sql_query(consulta, conn)

def consultar_categorias(conn): #consulta de gastos por categorias
    consulta = """
    SELECT
        categoria,
        SUM(valor) AS total
    FROM gastos
    GROUP BY categoria
    ORDER BY total DESC
    """
    return pd.read_sql_query(consulta, conn)

def consultar_ticket_medio(conn): #consultar gasto médio por mês
    consulta = """
    SELECT 
        mes,
        AVG(valor) AS media
    FROM gastos
    GROUP BY mes
    ORDER BY mes DESC 
    """
    return pd.read_sql_query(consulta, conn)

def consultar_evolucao(conn): #consultar evolução dos gastos em relação aos meses 
    consulta = """
    SELECT
        mes,
        SUM(valor) AS total
    FROM gastos
    GROUP BY mes
    ORDER BY mes
    """
    return pd.read_sql_query(consulta, conn)

def consultar_percentual(conn): #consulta de percentual gastos por categoria 
    consulta = """
    SELECT
        categoria,
        SUM(valor) AS total,
        ROUND( SUM(valor) * 100.0 / (SELECT SUM(valor) FROM gastos), 2) AS percentual
    FROM gastos
    GROUP BY categoria
    ORDER BY total DESC
    """
    return pd.read_sql_query(consulta, conn)

def exportar_dados(df): #exportar dados tratados
    df.to_csv("data/dados_tratados.csv", index=False)

def main():
    df = carregar_dados("data/finanças_2026.csv")

    df = tratar_dados(df)

    conn = criar_tabela(df, "financas.db")

    print(consultar_total(conn), end= "\n\n")
    print(consultar_categorias(conn), end= "\n\n")
    print(consultar_evolucao(conn), end= "\n\n")
    print(consultar_ticket_medio(conn), end= "\n\n")
    print(consultar_percentual(conn), end= "\n\n")

    exportar_dados(df)

    conn.close()

if __name__ == "__main__":
    main()