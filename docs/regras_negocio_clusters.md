# Regras de Negócio — Clusterização de Escolas Privadas

## Filtro geral

Todas as classificações são aplicadas em escolas privadas e em funcionamento:

- `TP_CATEGORIA_ESCOLA_PRIVADA == 1`
- `TP_SITUACAO_FUNCIONAMENTO == 1`

## Lógica de classificação

Cada critério atendido soma 1 ponto para o respectivo cluster.  
Se a escola atingir o número mínimo de pontos definidos para um cluster, será classificada naquele selo.  

---

## Cluster: Uno (Tecnológica)

**Objetivo**: identificar escolas com infraestrutura tecnológica.

**Pontuação Minima**: 8

**Palavras-chave utilizadas na exploração inicial**:
- internet
- informática
- computador
- laboratório
- rede
- multimídia
- conectividade
- tecnologia

**Critérios para pontuação**:
- Possui laboratório de informática  
- Possui computadores técnicos ou administrativos  
- Possui computadores desktop em uso pelos alunos  
- Possui notebooks em uso pelos alunos  
- Quantidade de notebooks > 0  
- Possui acesso à internet  
- Internet voltada ao uso dos alunos  
- Internet voltada à aprendizagem  
- Possui rede local (cabo, wireless ou ambos)

**Variáveis utilizadas**:
- `IN_LABORATORIO_INFORMATICA`
- `IN_COMPUTADOR`
- `IN_DESKTOP_ALUNO`
- `IN_COMP_PORTATIL_ALUNO`
- `QT_COMP_PORTATIL_ALUNO`
- `IN_INTERNET`
- `IN_INTERNET_ALUNOS`
- `IN_INTERNET_APRENDIZAGEM`
- `TP_REDE_LOCAL`

---

## Cluster: Kepler (Popular)

**Objetivo**: identificar escolas com infraestrutura básica e popular, compatível com mensalidades acessíveis.

**Pontuação Minima**: 13

**Palavras-chave utilizadas na exploração inicial**:
- internet  
- informática  
- laboratório  
- equipamento multimídia  
- equipamento  
- biblioteca  
- coordenação pedagógica  
- coordenador  
- formação docente  
- estrutura  
- recurso  
- mensalidade  
- valor  
- preço  
- gratuidade  
- cobrança  
- custo  
- pagamento  
- bolsa  
- financeiro

**Critérios para pontuação**:
- Possui biblioteca  
- Possui biblioteca ou sala de leitura  
- Possui laboratório de ciências  
- Possui laboratório de informática  
- Possui acesso à internet  
- Internet voltada ao uso dos alunos  
- Internet voltada ao uso administrativo  
- Internet voltada à aprendizagem  
- Internet voltada à comunidade  
- Acesso à internet por computadores  
- Acesso à internet por dispositivos pessoais  
- Possui banda larga  
- Possui bibliotecário  
- Quantidade de bibliotecários < 100  
- Possui coordenador pedagógico  
- Quantidade de coordenadores pedagógicos < 100  
- Possui pedagogo  
- Quantidade de pedagogos < 100  
- Possui monitores  
- Quantidade de monitores < 100

**Variáveis utilizadas**:
- `IN_BIBLIOTECA`
- `IN_BIBLIOTECA_SALA_LEITURA`
- `IN_LABORATORIO_CIENCIAS`
- `IN_LABORATORIO_INFORMATICA`
- `IN_INTERNET`
- `IN_INTERNET_ALUNOS`
- `IN_INTERNET_ADMINISTRATIVO`
- `IN_INTERNET_APRENDIZAGEM`
- `IN_INTERNET_COMUNIDADE`
- `IN_ACESSO_INTERNET_COMPUTADOR`
- `IN_ACES_INTERNET_DISP_PESSOAIS`
- `IN_BANDA_LARGA`
- `IN_PROF_BIBLIOTECARIO`
- `QT_PROF_BIBLIOTECARIO`
- `IN_PROF_COORDENADOR`
- `QT_PROF_COORDENADOR`
- `IN_PROF_PEDAGOGIA`
- `QT_PROF_PEDAGOGIA`
- `IN_PROF_MONITORES`
- `QT_PROF_MONITORES`

## Cluster: Farias (ENEM)

**Objetivo**: identificar escolas com foco acadêmico forte e alta preparação para exames como ENEM e vestibulares.

**Pontuação Mínima**: 10

**Palavras-chave utilizadas na exploração inicial**:
- comercial  
- particular  
- privada  
- urbana  
- categoria  
- rede  
- ensino médio  
- medio  
- etapa  
- modalidade  
- matrícula  
- turma  
- docente  
- professor  
- formação  
- escolaridade  
- pos-graduação  
- graduação  
- equipe pedagógica  
- internet  
- parceria  

**Critérios para pontuação**:
- Possui acesso à internet  
- Internet voltada ao uso dos alunos  
- Possui banda larga  
- Turno principal da escola é diurno  
- Possui etapa do ensino médio  
- Número de matrículas no ensino médio informado  
- Número de matrículas no ensino médio — tempo integral informado  
- Número de docentes do ensino médio informado  
- Número de turmas do ensino médio informado  
- Número de turmas do ensino médio — tempo integral informado  

**Variáveis utilizadas**:
- `IN_INTERNET`  
- `IN_INTERNET_ALUNOS`  
- `IN_BANDA_LARGA`  
- `TP_TURNO_FUNCIONAMENTO`  
- `IN_ETAPA_ENS_MEDIO`  
- `QT_MAT_MED`  
- `QT_MAT_MED_INT`  
- `QT_DOC_MED`  
- `QT_TUR_MED`  
- `QT_TUR_MED_INT`

---

## Cluster: Compartilha (Estrutura Pedagógica)

**Objetivo**: identificar escolas com equipe pedagógica estruturada (professores e coordenadores capacitados), com potencial para desenvolver seu próprio sistema de ensino.

**Pontuação Mínima**: 5

**Palavras-chave utilizadas na exploração inicial**:
- professor  
- docente  
- pedagógico  
- coordenador  
- formação  
- escolaridade  
- equipe pedagógica  
- sistema próprio  
- autonomia pedagógica  

**Critérios para pontuação**:
- Possui coordenador pedagógico  
- Quantidade de coordenadores pedagógicos ≥ 5  
- Possui pedagogo  
- Quantidade de pedagogos ≥ 10  
- Número de docentes da educação básica ≥ 10  
- Número de docentes da educação infantil ≥ 10  
- Número de docentes de creche ≥ 10  
- Número de docentes da pré-escola ≥ 10  
- Número de docentes do ensino fundamental ≥ 10  
- Número de docentes do ensino fundamental – anos iniciais ≥ 10  
- Número de docentes do ensino fundamental – anos finais ≥ 10  
- Número de docentes do ensino médio ≥ 10  
- Número de docentes da educação profissional ≥ 10  
- Número de docentes da educação profissional técnica ≥ 10

**Variáveis utilizadas**:
- `IN_PROF_COORDENADOR`
- `QT_PROF_COORDENADOR`
- `IN_PROF_PEDAGOGIA`
- `QT_PROF_PEDAGOGIA`
- `QT_DOC_BAS`
- `QT_DOC_INF`
- `QT_DOC_INF_CRE`
- `QT_DOC_INF_PRE`
- `QT_DOC_FUND`
- `QT_DOC_FUND_AI`
- `QT_DOC_FUND_AF`
- `QT_DOC_MED`
- `QT_DOC_PROF`
- `QT_DOC_PROF_TEC`
