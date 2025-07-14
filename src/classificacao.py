from src.clusters.uno import pontuar_uno
from src.clusters.kepler import pontuar_kepler
from src.clusters.farias_brito import pontuar_farias
from src.clusters.compartilha import pontuar_compartilha

# Função principal de classificação
def classificar_cluster(row):
    if pontuar_uno(row) >= 8:
        return "Uno"
    elif pontuar_kepler(row) >= 13:
        return "Kepler"
    elif pontuar_farias(row) >= 5:
        return "Farias Brito"
    elif pontuar_compartilha(row) >= 5:
        return 'Compartilha'
    else:
        return 'Outros'

# Função filtros obrigatórios
def aplicar_filtros_gerais(df):
    return df[
        (df["TP_CATEGORIA_ESCOLA_PRIVADA"] == 1) &
        (df["TP_SITUACAO_FUNCIONAMENTO"] == 1)
    ].copy()

# Executar funcões
def classificar_dataframe(df):
    df_filtrado = aplicar_filtros_gerais(df)
    df_filtrado["Cluster"] = df_filtrado.apply(classificar_cluster, axis=1)
    return df_filtrado