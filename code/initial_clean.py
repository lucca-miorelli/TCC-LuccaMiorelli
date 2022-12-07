import os
import pandas as pd
import numpy as np


################################################################################
##                                  CONSTANTES                                ##
################################################################################

RAW_DATA_PATH       = os.path.join('data', 'raw', 'dados_physchem_mf.xlsx')
PROCESSED_DATA_PATH = os.path.join('data', 'processed', '{}')


################################################################################
##                              CARREGANDO DADOS                              ##
################################################################################

df = pd.read_excel(
    io=RAW_DATA_PATH,
    sheet_name="Dados",
    skiprows=range(1, 4)
)

print(df.head())


################################################################################
##                              LIMPEZA DOS DADOS                             ##
################################################################################

# VISÃO GERAL DOS DADOS BRUTOS
# número de colunas
# informação das colunas
# descrever colunas


# REMOVER COLUNAS NÃO UTILIZADAS


# RENOMEAR COLUNAS


# CORRIGIR TYPES DAS COLUNAS
#
# tempo para minutos


# PREENCHER VALORES NULOS
