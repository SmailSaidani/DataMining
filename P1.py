import csv
from collections import defaultdict
import pydotplus
import numpy as np


# La classe arbre
class Tree:
    def __init__(self, value=None, trueBranch=None, falseBranch=None, results=None, col=-1, summary=None, data=None):
        self.value = value
        self.trueBranch = trueBranch
        self.falseBranch = falseBranch
        self.results = results
        self.col = col
        self.summary = summary
        self.data = data


def calculateDiffCount(datas):
    # Résumer l'ensemble des données
    # return results Set{type1:type1Count,type2:type2Count ... typeN:typeNCount}

    results = {}
    for data in datas:
        if data[-1] not in results:
            results[data[-1]] = 1
        else:
            results[data[-1]] += 1
    return results


def gini(rows):
    # calculer la valeur du gini

    length = len(rows)
    results = calculateDiffCount(rows)
    imp = 0.0
    for i in results:
        imp += results[i] / length * results[i] / length
    return 1 - imp


def splitDatas(rows, value, column):
    # separe les donnees (splitDatas par value,column)
    # retourne  2 parties(list1,list2)

    list1 = []
    list2 = []
    if (isinstance(value, int) or isinstance(value, float)):  #pour les valeurs int et float
        for row in rows:
            if (row[column] >= value):
                list1.append(row)
            else:
                list2.append(row)
    else:  #  pour les valeurs chaines de charactere
        for row in rows:
            if row[column] == value:
                list1.append(row)
            else:
                list2.append(row)

    return (list1, list2)
