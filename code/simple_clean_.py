import os
import pandas as pd
import numpy as np
import csv
import codecs


################################################################################
##                                  CONSTANTES                                ##
################################################################################

RAW_DATA_PATH       = os.path.join('data', 'raw', 'dados_physchem_mf.xlsx')
PROCESSED_DATA_PATH = os.path.join('data', 'processed', '{}')
KEEP_COLS_FILE      = os.path.join('helper', 'keep_cols_simple.csv')
RENAME_COLS_FILE     = os.path.join('helper', 'rename_cols.csv')

# Somente colunas utilizadas em estudo preliminar da Maltaria
keep_cols = [
    row[0]
    for row
    in csv.reader(
        open(KEEP_COLS_FILE, 'r', encoding="utf8")
    )
]

rename_cols = {
    row[0]:row[1]
    for row
    in csv.reader(
        open(RENAME_COLS_FILE, 'r', encoding="utf8")
    )
}


################################################################################
##                                   FUNÇÕES                                  ##
################################################################################

def contar_colunas(dataframe):
    """
    Conta e printa o número de colunas da base de dados.
    """

    print(f"Existem {len(dataframe.columns.values)} colunas neste dataset.\n")

    return None


################################################################################
##                              CARREGANDO DADOS                              ##
################################################################################

df = pd.read_excel(
    io=RAW_DATA_PATH,
    sheet_name="Dados",
    skiprows=range(1, 4)
)

print(f"{df.head()}\n")


################################################################################
##                              LIMPEZA DOS DADOS                             ##
################################################################################

# WORK IN PROGRESS

##############################
#     RENOMEAR COLUNAS      #
##############################

rename_cols["Grau \nmaceração"] = rename_cols['Grau \\nmaceração']
del rename_cols['Grau \\nmaceração']

df.rename(
    columns=rename_cols,
    inplace=True
)
print(df.columns)

####################################
#    FILTRAR COLUNAS UTILIZADAS    #
####################################

print("Filtrando somente colunas necessárias...")

data = df[keep_cols].copy()
contar_colunas(data)

print(data.info())

#################################
#  CORRIGIR TIPOS DAS COLUNAS   #
#################################

# tempo para minutos
tempo_cols = [
    "tempo_carregamento_germinador",
    "tempo_germinacao",
    "tempo_primeira_camada_secador",
    "ciclo_secagem",
]

print(data[tempo_cols])
data[tempo_cols] = data[tempo_cols].apply(pd.to_datetime, errors='coerce')
print(type(data[tempo_cols]["tempo_carregamento_germinador"][0]))

# floats
float_cols = [
    "total_periodo_seco",
    "total_periodo_umido",
    "grau_maceracao",
    "umidade_final",
    "temperatura_co2",
    "FAN",
]

data[float_cols] = data[float_cols].apply(pd.to_numeric, errors='coerce')
print(data.info())


#################################
#    PREENCHER VALORES NULOS    #
#################################

# verificar quantidade de valores nulos por coluna
print(data.isnull().sum() / len(data))