from pandas import DataFrame
from collections import defaultdict
from typing import List, Tuple, Set, Dict

"""

@ Author: Zhebin Yin
@ Date: Apr. 20, 2023
@ Version: 1

1. measure the freqency of each class attributes.
2. measure the frequency of each prediction attributes conditioned on class attributes.
3. get the probability of each perdiction attributes conditioned on the classification attribute from train file.
    a. get the probability(float) and the frequency(str)
4. based on the test file, measure the predicted result based on the product of each probability of 
   perdiction attributes conditioned on the class attributes.
5. get the highest prediction probability (predicted result) given by the model to see if they match the actual result.

"""

class NaiveBayes:
    def __init__ (self, c: float, verbose: bool, train_df: DataFrame, test_df: DataFrame):
        self.delta: float = c        # default = 0
        self.verbose: bool = verbose # defalt = false
        self.trainData: DataFrame = train_df
        self.testData: DataFrame = test_df
        self.condProb: Dict[str, float] = {}     #str: 11T -> A1 = 1 | C = T; 10T -> A0 = 1 | C = T
        self.pretty_condProb: Dict[str, str] = {} 
        self.pureProb: Dict[str, float] = {}
        self.pretty_pureProb: Dict[str, str] = {}
        self.colValSet: List[Set[str]] = []
        self.condProbCounter = defaultdict(int) # count number of each prediction attributes conditioned on different class attributes
        self.pureCondiCounter = defaultdict(int) # count number of different class attributes
        self.finalProb : Dict[str, float] = {}

    def getColumnValue(self):
        for i in self.trainData.keys():
            columnVal = set(self.trainData[i])
            self.colValSet.append(columnVal)

    def getPureProb(self):
        for i in range(len(self.trainData)):
            classAttr = self.trainData.iloc[i, -1]
            if classAttr in self.pureCondiCounter:
                self.pureCondiCounter[classAttr] += 1
            else:
                self.pureCondiCounter[classAttr] = 1
        for classAttrVal in self.colValSet[-1]:
            if classAttrVal in self.pureCondiCounter:
                counter = self.pureCondiCounter[classAttrVal]  
            else:
                counter = 0
            self.pureProb[classAttrVal] = counter/len(self.trainData)
            self.pretty_pureProb[classAttrVal] = f"{counter} / {len(self.trainData)}"

    def getCondProb(self):
        for i in range(len(self.trainData)):
            predictAttr = self.trainData.iloc[i, :-1]
            classAttr = self.trainData.iloc[i, -1]
            for Ai in range(len(predictAttr)):
                preAttrVal = predictAttr[Ai]
                key = "" + preAttrVal + str(Ai) + classAttr
                if key in self.condProbCounter:
                    self.condProbCounter[key] += 1
                else:
                    self.condProbCounter[key] = 1
        for classAttrVal in self.colValSet[-1]:
            for col in range(len(self.colValSet)-1):
                colVal = self.colValSet[col]
                for val in colVal:
                    name = "" + val + str(col) + classAttrVal
                    counter = self.condProbCounter[name] if name in self.condProbCounter else 0
                    self.condProb[name] = (counter + self.delta) / (self.pureCondiCounter[classAttrVal] + self.delta * len(self.colValSet[col]))
                    self.pretty_condProb[name] = f"{(counter + self.delta)} / {(self.pureCondiCounter[classAttrVal] + self.delta * len(self.colValSet[col]))}"

    def train(self):
        """
        Naive Bayes test dataset prediction. 
        If verbose model on, pretty print.
        else print result.
        """
        predictions = []
        self.getColumnValue()
        self.getPureProb()
        self.getCondProb()
        # predict result of given testData
        for i in range(len(self.testData)):
            predictAttr = self.testData.iloc[i, :-1]
            if len(predictAttr) > len(self.colValSet) -1:
                print(f"Error: there is more features than traning data!")
                exit(-1)
            classAttr = self.testData.iloc[i, -1]
            # print(classAttr)
            for classLabel in sorted(self.colValSet[-1]):
                if self.verbose : 
                    self.pretty_print_pureProb(classLabel)
                probProduct = self.pureProb[classLabel]
                for Ai in range(len(predictAttr)):
                    preAttrVal = predictAttr[Ai]
                    key = "" + preAttrVal + str(Ai) + classLabel # key = 10F
                    if key not in self.condProb: 
                        print(f"Warning: P(A{key[len(preAttrVal): len(preAttrVal) + len(Ai)]} = \
                            {key[0:len(preAttrVal)]} | C = {key[len(preAttrVal) + len(Ai)]} ) is not in the training set.")
                        exit(-1)
                    else:
                        if self.verbose:
                            self.pretty_print_condProb(preAttrVal, str(Ai), classLabel, key)
                    probProduct *= self.condProb[key]
                self.finalProb[classLabel] = probProduct
            # now we get the final prob
            for classVal in self.finalProb.keys():
                if self.verbose:
                    self.pretty_print_finalProb(classVal, self.finalProb[classVal])
            
            # get the predicted result and compare with the actual result
            maxProb = max(self.finalProb.values())
            
            predictResult = ""
            for label,prob in self.finalProb.items() :
                if prob == maxProb:
                    predictResult = label 
            predictions.append(predictResult)
            if self.verbose:
                self.pretty_print_resultComparison(predictResult, classAttr)

        # got all predictions
        return predictions


    def pretty_print_pureProb(self, label):
        print(f"P(C={label}) = [{self.pretty_pureProb[label]}]")          
    
    def pretty_print_condProb(self, preAttrVal, Ai, classLabel, key):
        print(f"P(A{Ai}={preAttrVal} | C={classLabel}) = {self.pretty_condProb[key]}")

    def pretty_print_finalProb(self, label, prob):
        print(f"NB (C={label}) = {prob:.6f}")

            
    def pretty_print_resultComparison(self, predictResult, ActualResult):
        if(predictResult == ActualResult):
            print(f"match: '{ActualResult}'")
        else:
            print(f"Fail: got {predictResult} != want {ActualResult}")



        
