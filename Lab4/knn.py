from pandas import DataFrame
import math


"""

@ Author: Zhebin Yin
@ Date: Apr. 22, 2023
@ Version: 1

Souce: https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761


"""

class KNN:
    def __init__(self, k: float, verbose: bool, train_df: DataFrame, test_df: DataFrame):
        self.k = k
        self.verbose = verbose
        self.trainData = train_df
        self.testData = test_df
        self.data = []

    def loadData(self):
        for i in range(len(self.trainData)):
            self.data.append((self.trainData.iloc[i, :-1], self.trainData.iloc[i, -1]))


    def knn(self):
        predictions = []
        print("distance")
        for i in range(len(self.testData)):
            testData = self.testData.iloc[i, :-1]
            neighbor_distances = self.getDistance(testData)
            print(neighbor_distances)
            choices = {}
            for i in range(self.k):
                # no need to vote
                if i >= len(neighbor_distances):
                    break
                label = neighbor_distances[i][1]
                distance = neighbor_distances[i][0]
                if distance == 0:
                    voteVal = math.inf
                else:
                    voteVal = 1 / distance
                if label in choices:
                    choices[label] += voteVal
                else:
                    choices[label] = voteVal
            
            sorted_choices = sorted(choices.items(), key=lambda x: x[1], reverse=True)
            predictions.append(sorted_choices[0][0])
        if self.verbose:
            self.pretty_print_resultComparison(predictions, self.testData)
        return predictions
    
    def getDistance(self, testData):
        for i in range(len(testData)):
            neighbor_distances = []
            for i in range(len(self.data)):
                distance = 0
                for j in range(len(testData)):
                    distance += (testData[j] - self.data[i][0][j]) ** 2
                neighbor_distances.append((distance, self.data[i][1]))
            neighbor_distances.sort(key=lambda x: x[0])
        return neighbor_distances

    def pretty_print_resultComparison(self, predictions, testFile):
        for i in range(len(testFile)):
            print(f"want={testFile.iloc[i, -1]} got={predictions[i]}")

