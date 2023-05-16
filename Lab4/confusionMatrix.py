from pandas import DataFrame
from collections import defaultdict
from typing import List, Tuple, Set, Dict


def record(predictions, testData):
    # similar to confusion matrix (true false talbe)
    MatrixTable = {}
    # actual result
    for i in range(len(testData)):
        actualResult = testData.iloc[i, -1]
        fillMatrix(MatrixTable, actualResult, "actual")
        predResult = predictions[i]
        if actualResult == predResult:
            fillMatrix(MatrixTable, actualResult, "TruePositive")
        
        fillMatrix(MatrixTable, predResult, "predict")
    return MatrixTable

    
def pretty_Result(predictions, testData):
    MatrixTable = record(predictions, testData)
    for label in sorted(MatrixTable.keys()):
        print(
            f"Label={label} Precision={MatrixTable[label]['TruePositive']}/{MatrixTable[label]['predict']} Recall={MatrixTable[label]['TruePositive']}/{MatrixTable[label]['actual']}")


def fillMatrix(MatrixTable, label, type):
        if label not in MatrixTable:
            MatrixTable[label] = {"TruePositive": 0, "predict": 0, "actual": 0}
        MatrixTable[label][type] += 1
