# Sistema de Análise Financeira Pessoal com Pipeline Automatizado


Sistema de análise financeira pessoal desenvolvido com Python, SQLite e Power BI, com foco em tratamento, categorização e análise automatizada de transações financeiras, permitindo geração de insights sobre comportamento de consumo e apoio à tomada de decisão baseada em dados.


## Objetivo:

Criar um sistema capaz de:
* Registrar transações financeiras pessoais
* Automatizar tratamento e categorização dos dados
* Identificar padrões de gastos
* Gerar relatórios e visualizações interativas
* Apoiar decisões financeiras com base em dados históricos
O projeto surgiu da necessidade de transformar um controle financeiro manual em um processo estruturado e orientado por dados.

## Dashboard

<p align="center">
  <img src="\dashboard\visual_finances.jpg" width="900">
</p>

* Gastos por categoria
* Evolução financeira mensal
* Comparação entre despesas
* Distribuição percentual dos gastos
* Identificação de padrões de consumo


## Competencias técnicas aplicadas
Durante o desenvolvimento do projeto foram aplicados conhecimentos em:
* Importação de bases CSV e Excel
* Limpeza e padronização de colunas
* Conversão de tipos monetários e temporais
* Transformação e enriquecimento de dados
 
### Programação em Python
* Manipulação de dados com Pandas
* Limpeza e transformação de dados
* Estruturação modular de funções
* Aplicação de regras condicionais
* Exportação automatizada de bases tratadas


### SQL/SQLite
* Modelagem relacional simples
* Criação e atualização de tabelas
* Consultas analíticas
* Organização de dados estruturados


### Power BI
* Construção de dashboards interativos
* Desenvolvimento de KPIs financeiros
* Storytelling com dados
*Filtros dinâmicos e visualização analítica


### Engenharia e Tratamento de Dados
* Importação de arquivos CSV e Excel
* Padronização de colunas
* Conversão de formatos monetários
* Tratamento de datas
* Enriquecimento categórico




## Metodologia
A etapa inicial consistiu na ingestão de dados financeiros a partir de planilhas previamente utilizadas para controle pessoal.


Foram exploradas duas possibilidades de leitura:


Importação via CSV
Importação via Excel


A escolha pelo formato CSV ocorreu pela simplicidade de integração e melhor previsibilidade durante o tratamento automatizado.
Tratamento e Padronização


A preparação da base envolveu quatro etapas principais:


* 1º. Normalização estrutural


Padronização dos nomes das colunas para evitar inconsistências de leitura.


* 2º. Conversão monetária


Transformação dos valores do padrão textual brasileiro para formato numérico processável.


* 3º. Conversão temporal


Padronização de datas para análises mensais e integração com ferramentas analíticas.


* 4º. Enriquecimento categórico


Classificação automática das transações com base em palavras-chave presentes na descrição.


A categorização foi construída por meio de regras condicionais baseadas em correspondência textual.


Essa abordagem permitiu automatizar a classificação inicial das despesas e estruturar análises comparativas entre categorias de consumo.
Embora parte das análises pudesse ser realizada exclusivamente com Pandas, a utilização de SQL foi mantida por seu valor estratégico no projeto.


A integração com banco relacional permitiu:


* simular cenários mais próximos de aplicações corporativas
* praticar consultas analíticas
* estruturar persistência de dados
* reforçar conhecimentos em modelagem e extração


## Principais aprendizados


Durante o desenvolvimento, alguns aprendizados importantes surgiram:
* A importância da padronização de dados antes da análise
* O valor do versionamento incremental com Git/GitHub
* A utilidade do SQL mesmo em projetos pessoais
* A necessidade de debugging estruturado e refinamento contínuo
O projeto também reforçou a ideia de que múltiplos commits representam rastreabilidade técnica e evolução do desenvolvimento.


## Evoluções Futuras

### Curto prazo
* Refatoração da lógica de categorização via dicionários

### Médio prazo
* Inclusão de tabelas de receitas
* Melhoria de organização por categorias

### Longo prazo
* Modelagem integrada de gastos, receitas e investimentos
* Automação completa da ingestão de dados
* Consolidação patrimonial


## Tecnologias utilizadas:


* [Google Sheets](https://developers.google.com/workspace/sheets?hl=pt-br/): criação de planilhas em nuvem
* [Python](https://www.python.org/): linguagem de programação
* [Pandas](https://pypi.org/project/SpeechRecognition/](https://pandas.pydata.org/)): trabalhar com banco de dados e integralos
* [SQLite](https://pypi.org/project/gTTS/](https://sqlite.org/)): consultar banco de dados
* [Power BI](https://pypi.org/project/playsound/](https://www.microsoft.com/pt-br/power-platform/products/power-bi/desktop)): Apresentação de Dashboard
 
## Como executar:


### **1. Instale `Python` na sua máquina, por meio [deste link](https://www.python.org/)**


### **2. Faça um clone [desse repositório](https://github.com/Luizcomzz/Analise_Financeira_Pessoal.git) na sua máquina:**


* Crie uma pasta no seu computador para esse programa, recomendo colocar o nome **finanças pessoais**
* Abra o `git bash` ou `terminal` dentro dessa pasta
* Copie a [URL](https://github.com/Luizcomzz/Analise_Financeira_Pessoal.git) do repositório
* Digite `git clone <URL copiada>` e pressione `enter`


### **3. Instale as bibliotecas necessárias pelo terminal, dentro dessa pasta criada:**


* Pandas: `pip install pandas`
* SQLite3: `import sqlite3 as sql`


### **4. Importe o modelo de [planilha](https://docs.google.com/spreadsheets/d/1YnmxyQ9UEySS7x8o_XhC5K4v2xB2Np2OQDJj7tapOdI/edit?usp=sharing) de dados automatica, porem vai ter que usar o google apps script ai posso te passar o codigo que usei e precisa ativar na primeira vez que usar