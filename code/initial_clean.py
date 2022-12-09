import os
import pandas as pd
import numpy as np
import csv


################################################################################
##                                  CONSTANTES                                ##
################################################################################

RAW_DATA_PATH       = os.path.join('data', 'raw', 'dados_physchem_mf.xlsx')
PROCESSED_DATA_PATH = os.path.join('data', 'processed', '{}')
DROP_COLS_FILE      = os.path.join('helper', 'drop_cols.csv')
RENAME_COLS_FILE     = os.path.join('helper', 'rename_cols.csv')

cols_to_drop = [
    row[0]
    for row
    in csv.reader(
        open(DROP_COLS_FILE, 'r')
    )
]

rename_cols = {
    row[0]:row[1]
    for row
    in csv.reader(
        open(RENAME_COLS_FILE, 'r')
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

# VISÃO GERAL DOS DADOS BRUTOS

# número de colunas
contar_colunas(df)

# informação das colunas
print(f"Informações das colunas:\n")
# print(df.info())

# descrever colunas numéricas


# REMOVER COLUNAS NÃO UTILIZADAS
print("Removendo colunas desnecessárias...")
df.drop(
    columns=cols_to_drop,
    inplace=True
)
contar_colunas(df)

# RENOMEAR COLUNAS


# CORRIGIR TYPES DAS COLUNAS
#
# tempo para minutos


# PREENCHER VALORES NULOS
