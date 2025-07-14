# Clusterização de Escolas Privadas

Este projeto realiza a **clusterização de escolas privadas** brasileiras com base em variáveis do Censo Escolar, classificando-as nos seguintes selos:

- **Uno** (Tecnológica)
- **Kepler** (Popular)
- **Farias Brito** (Foco em vestibulares/ENEM)
- **Compartilha** (Estrutura pedagógica)

---

## Estrutura do Projeto

```text
clusterizacao_escolas/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── clusters/
│   │   ├── compartilha.py
│   │   ├── farias_brito.py
│   │   ├── kepler.py
│   │   └── uno.py
│   ├── classificacao.py
│   └── main.py
├── docs/
│   └── regras_negocio_clusters.md
├── README.md
├── requirements.txt
├── pyproject.toml
└── poetry.lock
```


## Como executar o projeto

### 1. Clone o repositório

git clone https://github.com/gustavoadr3/clusterizacao_escolas.git
cd clusterizacao_escolas

### 2. Estrutura de pastas
Antes de executar o projeto, crie a seguinte estrutura de pastas (caso não existam):

mkdir -p data/raw
mkdir -p data/processed

Essas pastas são utilizadas para armazenar os arquivos de entrada (raw) e os resultados processados (processed)

### 3. Crie o ambiente Poetry e instale as dependências
```text
pip install poetry
poetry install
poetry shell
```


### 4. Execute a aplicação
poetry run python main.py

### Resultado 
O script principal gera o arquivo final com os clusters em data/processed/escolas_clusterizadas.csv

Obs.: Somente escolas classificadas como Uno, Kepler, Farias Brito ou Compartilha são mantidas. As classificadas como Outros são excluídas.

### Regras de negócio
As regras de classificação e os critérios de pontuação de cada selo estão documentados em docs/regras_negocio_clusterizacao.md
