#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:13:09 2022

@author: nico
"""
import numpy as np
import pandas as pd


# 1. Pedir ao utilizador o nome e localização de um ficheiro de dados a analisar.
# 1.1 Abrir ficheiro
def open_file(fname: str) -> pd.DataFrame:
    """Opens a fname where fname is a path to a .csv file
    Returns a pandas DataFrame with the data"""
    data = pd.read_csv(fname, sep=",")
    return data


# 2. Calcular as seguintes estatísticas descritivas para cada variável:
# • Média;
# • Desvio Padrão;
# • 1º quartil;
# • Mediana;
# • 3º quartil.


def mean(vec):
    """Calculate the mean of a numpy vec array, returns floating point number"""
    out = np.sum(vec) / len(vec)
    assert out == np.mean(vec)
    return out


def data_means(data):
    """Calculate the mean of each column of the data table"""
    means = []
    for col in data.columns:
        means.append(mean(data[col]))
    return np.array(means)


def std(data) -> float:
    print("std")


def quartis(col) -> (float, float, float):
    """Retorna o 1o 2o e 3o qualrtil de uma variavel das colunas de uma tablea"""
    ...


# 3. Calcular as seguintes estatísticas de relação entre as duas variáeis:
# • Covariância;
# • Correlação.


def covariance(vec1, vec2):
    ...


def corr():
    ...


if __name__ == "__main__":
    fname = input("Insert file name: ")
    if not fname:
        fname = "./marriage_data.csv"
    print(f"{fname=}")

    data = open_file(fname)

    means = [
        mean(data["OSMarriages"]),
        mean(data["SSMarriages"]),
        mean(data["MaleCivil"]),
        mean(data["FemaleCivil"]),
    ]

    means = []
    for col in data.columns:
        means.append(mean(data[col]))

    means = data_means(data)
    # print stuff
    for c, m in zip(data.columns, means):
        print(c)
        print("Mean: ", m)
        print("\n")
