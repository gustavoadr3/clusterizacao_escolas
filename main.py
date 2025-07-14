import pandas as pd 
from src.classificacao import classificar_dataframe

COLUNAS_FINAIS = [
    "NU_ANO_CENSO",
    "NO_REGIAO",
    "CO_REGIAO",
    "NO_UF",
    "SG_UF",
    "CO_UF",
    "NO_MUNICIPIO",
    "CO_MUNICIPIO",
    "NO_REGIAO_GEOG_INTERM",
    "CO_REGIAO_GEOG_INTERM",
    "NO_MICRORREGIAO",
    "CO_MESORREGIAO",
    "CO_MICRORREGIAO",
    "NO_DISTRITO",
    "CO_DISTRITO",
    "NO_ENTIDADE",
    "CO_ENTIDADE",
    "Cluster"
]

def main():

    INPUT_PATH = r"data/raw/microdados_ed_basica_2024.csv"
    OUTPUT_PATH = r"data/processed/escolas_clusterizadas.csv"

    # Carrega o DF
    df = pd.read_csv(INPUT_PATH, sep=';', encoding='latin1', low_memory=False)

    # Aplica a classificação
    df_resultado = classificar_dataframe(df)
    df_resultado = df_resultado[df_resultado["Cluster"] != "Outros"]
    df_resultado = df_resultado[COLUNAS_FINAIS].copy()

    # Salva o DF com o cluster
    df_resultado.to_csv(OUTPUT_PATH, index=False)
    print(f"Arquivo salvo com sucesso em: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()