# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 00:10:45 2025

@author: sodre
"""

import pandas as pd
import numpy as np
import io
import os
from pathlib import Path

BASE = Path(__file__).parent if "__file__" in globals() else Path(".")

DATA_DIR = BASE / "data"
DATA_DIR.mkdir(exist_ok= True)

np.random.seed(42)


n = 80

datasample_size = 100

vendedores = np.random.choice(
    ["Matheus", "Luis Eduardo", "Elias", "Nina", "Cauã", "Yuri"],
    size = datasample_size,
    p = [.15, .15, .20, .20, .15, .15],
    )

produtos = np.random.choice(["Pepino", "DVD", "Panela", "Cobertor", "Café", "Marmita"],
                            size = datasample_size,
                            p = [.25, .15, .20, .10, .15, .15],
                            )

valor_base = {"Pepino": 50, "DVD": 10, "Panela": 100, "Cobertor": 30, "Café": 2, "Marmita": 20}
get_preco = np.vectorize(valor_base.get)
valor_base = get_preco(produtos)

valores = valor_base * np.random.normal(1.0, 0.13, size = datasample_size)
valores = np.round(valores, 2)

datas = pd.to_datetime("2025-01-01") + pd.to_timedelta(
    np.random.randint(0,90, size = datasample_size), unit = "D")

regioes = np.random.choice(["sul", "norte", "sudeste ", "Sudeste", "Centro-oeste", "Nordeste"], size = datasample_size)

mascara_de_erros = np.random.rand(datasample_size) < 0.07
valores[mascara_de_erros] = np.nan

duplicatas = np.random.choice(np.arange(datasample_size), size= 7, replace= False)

df_raw = pd.DataFrame({
    "Vendedor": vendedores,
    "Produto": produtos,
    "Valor": valores,
    "Região": regioes,
    "DataVenda": datas,
    })

df_raw = pd.concat([df_raw, df_raw.iloc[duplicatas]], ignore_index= True)
print(df_raw)

print("\n", "#"*60, "\n")

csv_path = DATA_DIR / "vendas.csv"
xlsx_path = DATA_DIR / "vendas.xlsx"


df_raw.to_csv(csv_path, index= False, encoding = "utf-8")

with pd.ExcelWriter(xlsx_path) as writer:
    df_raw.to_excel(writer, index = False, sheet_name= "Vendas")


































