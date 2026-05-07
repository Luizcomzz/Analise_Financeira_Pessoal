Sistema de Análise Financeira Pessoal com Pipeline Automatizado
Desenvolvimento de um pipeline analítico para tratamento, categorização e análise de dados financeiros pessoais, utilizando Python, Pandas e SQL, com integração a dashboard interativo no Power BI para geração de insights sobre comportamento de consumo e suporte à tomada de decisão orientada por dados.

Objetivo:
Criar um sistema que regitre os dados financeiros, que gere relatórios, indentifique padrões e ajude a tomar decisão baseada nas suas proprias informações pessoais

Competencias técnicas aplicadas
Durante o desenvolvimento do projeto foram aplicados conhecimentos em:

Importação de bases CSV e Excel
Limpeza e padronização de colunas
Conversão de tipos monetários e temporais
Transformação e enriquecimento de dados
Programação em Python
Estruturação modular de funções
Aplicação de regras condicionais
Exportação automatizada de bases tratadas
Banco de dados
Modelagem relacional simples com SQLite
Criação e atualização de tabelas
Consultas analíticas em SQL
Visualização Analitica
Integração com Power BI
Construção de indicadores e filtros interativos
Exploração visual de padrões financeiros
Metodologia
A etapa inicial consistiu na ingestão de dados financeiros a partir de planilhas previamente utilizadas para controle pessoal.

Foram exploradas duas possibilidades de leitura:

Importação via CSV Importação via Excel

A escolha pelo formato CSV ocorreu pela simplicidade de integração e melhor previsibilidade durante o tratamento automatizado. Tratamento e Padronização

A preparação da base envolveu quatro etapas principais:

1º. Normalização estrutural
Padronização dos nomes das colunas para evitar inconsistências de leitura.

2º. Conversão monetária
Transformação dos valores do padrão textual brasileiro para formato numérico processável.

3º. Conversão temporal
Padronização de datas para análises mensais e integração com ferramentas analíticas.

4º. Enriquecimento categórico
Classificação automática das transações com base em palavras-chave presentes na descrição.

A categorização foi construída por meio de regras condicionais baseadas em correspondência textual.

Essa abordagem permitiu automatizar a classificação inicial das despesas e estruturar análises comparativas entre categorias de consumo. Embora parte das análises pudesse ser realizada exclusivamente com Pandas, a utilização de SQL foi mantida por seu valor estratégico no projeto.

A integração com banco relacional permitiu:

simular cenários mais próximos de aplicações corporativas
praticar consultas analíticas
estruturar persistência de dados
reforçar conhecimentos em modelagem e extração O processo reforçou a importância de pausas estratégicas durante debugging, permitindo retomada com maior clareza analítica. Um aprendizado importante foi compreender o versionamento como processo iterativo.
Inicialmente houve preocupação excessiva com número de commits, porém o projeto evidenciou que o histórico de evolução representa rastreabilidade técnica e demonstra capacidade de refinamento contínuo.

Evoluções Futuras
Curto prazo
Refatoração da lógica de categorização via dicionários
Médio prazo
Inclusão de tabelas de receitas
Longo prazo
Modelagem integrada de gastos, receitas e investimentos
Automação da ingestão de dados
Expansão para visão consolidada patrimonial
Tecnologias utilizadas:
Google Sheets: criação de planilhas em nuvem
Python: linguagem de programação
Pandas: trabalhar com banco de dados e integralos
SQLite: consultar banco de dados
Power BI: Apresentação de Dashboard
Como executar:
1. Instale Python na sua máquina, por meio deste link
2. Faça um clone desse repositório na sua máquina:
Crie uma pasta no seu computador para esse programa, recomendo colocar o nome finanças pessoais
Abra o git bash ou terminal dentro dessa pasta
Copie a URL do repositório
Digite git clone <URL copiada> e pressione enter
3. Instale as bibliotecas necessárias pelo terminal, dentro dessa pasta criada:
Pandas: import pandas as pd
SQLite3: import sqlite3 as sql
**4. Importe o modelo de planilhade dados automatica, porem vai ter que usar o google apps script ai posso te passar o codigo que usei e precisa ativar na primeira vez que usar