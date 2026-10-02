import os
import sqlite3
import pandas as pd


# ================================================================
# Constantes — caminhos e configurações centralizadas
# ================================================================
RAW_PATH    = "data/raw/financas_2026.csv"
DB_PATH     = "database/financas.db"
EXPORT_PATH = "data/processed/dados_tratados.csv"

# Dicionário de categorização — adicione palavras-chave aqui
# sem precisar alterar a lógica do código
CATEGORIAS: dict[str, list[str]] = {
    "Transporte"  : ["uber", "99pop", "gasolina", "estacionamento", "posto", "combustivel"],
    "Alimentação" : ["ifood", "restaurante", "lanche", "almoço", "padaria", "mercado"],
    "Saúde"       : ["farmacia", "consulta", "dentista", "hospital", "laboratorio"],
    "Educação"    : ["livro", "curso", "udemy", "alura", "escola", "faculdade"],
    "Lazer"       : ["netflix", "prime", "passagem", "passeio", "forró", "quermesse", "show"],
    "Cartão"      : ["fatura nu", "fatura xp", "fatura inter", "fatura itau"],
}


# ================================================================
# INGESTÃO
# ================================================================

def carregar_dados(caminho: str) -> pd.DataFrame:
    """
    Lê o CSV de transações financeiras e retorna um DataFrame.

    Parâmetros:
        caminho (str): Caminho para o arquivo CSV.

    Retorna:
        pd.DataFrame: Dados brutos carregados.

    Lança:
        FileNotFoundError: Se o arquivo não existir.
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    return pd.read_csv(caminho, encoding="utf-8")


# ================================================================
# CATEGORIZAÇÃO
# ================================================================

def categorizar(descricao: str) -> str:
    """
    Classifica uma transação em uma categoria com base em
    palavras-chave definidas no dicionário CATEGORIAS.

    Parâmetros:
        descricao (str): Texto descritivo da transação.

    Retorna:
        str: Nome da categoria encontrada ou 'Outros'.
    """
    descricao_lower = descricao.lower()

    for categoria, palavras_chave in CATEGORIAS.items():
        if any(palavra in descricao_lower for palavra in palavras_chave):
            return categoria

    return "Outros"


# ================================================================
# TRATAMENTO
# ================================================================

def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Executa o pipeline de limpeza e enriquecimento do DataFrame.

    Etapas:
        1. Padronização de nomes de colunas
        2. Conversão do valor monetário (R$ → float)
        3. Conversão da data para datetime
        4. Categorização automática das transações
        5. Extração do período mensal

    Parâmetros:
        df (pd.DataFrame): DataFrame bruto.

    Retorna:
        pd.DataFrame: DataFrame tratado e enriquecido.
    """
    df = df.copy()

    # 1. Padronização de colunas
    df.columns = df.columns.str.lower().str.strip()
    df = df.rename(columns={"descrição": "descricao", "ano_mes": "data"})

    # 2. Conversão monetária: "R$ 1.234,56" → 1234.56
    df["valor"] = (
        df["valor"]
        .str.replace("R$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
        .astype(float)
    )

    # 3. Conversão temporal
    df["data"] = pd.to_datetime(df["data"])

    # 4. Categorização automática
    df["categoria"] = df["descricao"].apply(categorizar)

    # 5. Período mensal para agrupamentos
    df["mes"] = df["data"].dt.to_period("M").astype(str)

    return df


# ================================================================
# PERSISTÊNCIA
# ================================================================

def persistir_banco(df: pd.DataFrame, caminho_banco: str) -> None:
    """
    Persiste o DataFrame na tabela 'gastos' do banco SQLite.
    Usa context manager para garantir fechamento seguro da conexão.

    Parâmetros:
        df (pd.DataFrame): DataFrame tratado.
        caminho_banco (str): Caminho para o arquivo .db.
    """
    with sqlite3.connect(caminho_banco) as conn:
        df.to_sql("gastos", conn, if_exists="replace", index=False)


# ================================================================
# CONSULTAS ANALÍTICAS
# ================================================================

def consultar_banco(caminho_banco: str) -> None:
    """
    Executa e exibe as principais consultas analíticas sobre os gastos.

    Parâmetros:
        caminho_banco (str): Caminho para o banco SQLite.
    """
    consultas = {
        "Total gasto no período": """
            SELECT ROUND(SUM(valor), 2) AS total_gasto
            FROM gastos
        """,
        "Gastos por categoria": """
            SELECT
                categoria,
                ROUND(SUM(valor), 2)                                          AS total,
                ROUND(SUM(valor) * 100.0 / (SELECT SUM(valor) FROM gastos), 2) AS percentual
            FROM gastos
            GROUP BY categoria
            ORDER BY total DESC
        """,
        "Evolução mensal": """
            SELECT mes, ROUND(SUM(valor), 2) AS total
            FROM gastos
            GROUP BY mes
            ORDER BY mes
        """,
        "Ticket médio por mês": """
            SELECT mes, ROUND(AVG(valor), 2) AS media_por_transacao
            FROM gastos
            GROUP BY mes
            ORDER BY mes DESC
        """,
    }

    with sqlite3.connect(caminho_banco) as conn:
        for titulo, sql in consultas.items():
            print(f"\n=== {titulo} ===")
            print(pd.read_sql_query(sql, conn).to_string(index=False))


# ================================================================
# EXPORTAÇÃO
# ================================================================

def exportar_dados(df: pd.DataFrame, caminho: str) -> None:
    """
    Exporta o DataFrame tratado para CSV com formato monetário brasileiro.

    Parâmetros:
        df (pd.DataFrame): DataFrame tratado.
        caminho (str): Caminho de destino do CSV.
    """
    df_export = df.copy()
    df_export["valor"] = df_export["valor"].map(lambda x: f"{x:.2f}".replace(".", ","))
    df_export.to_csv(caminho, index=False, encoding="utf-8-sig")
    print(f"\nBase exportada para: {caminho}")


# ================================================================
# MAIN
# ================================================================

def main() -> None:
    """Orquestra o pipeline completo de análise financeira pessoal."""
    print("Pipeline financeiro iniciado.\n")

    try:
        df       = carregar_dados(RAW_PATH)
        df_clean = tratar_dados(df)

        persistir_banco(df_clean, DB_PATH)
        consultar_banco(DB_PATH)
        exportar_dados(df_clean, EXPORT_PATH)

        print("\nPipeline concluído com sucesso!")

    except FileNotFoundError as e:
        print(f"\n[ERRO] {e}")
        print("Adicione o arquivo CSV em data/raw/ e tente novamente.")


if __name__ == "__main__":
    main()