#python3 
from sys import exit
import argparse
import pandas as pd
from naiveBayes import NaiveBayes
from confusionMatrix import pretty_Result
from knn import KNN

"""

@ Author: Zhebin Yin
@ Date: Apr. 22, 2023
@ Version: 1

"""

class Kmean:
    def __init__(self, d, verbose, inputFile):
        self.distanceMode = d # default e2
        self.verbose = verbose
        self.data = inputFile
