#python3 
from sys import exit
import argparse
import pandas as pd
from naiveBayes import NaiveBayes
from confusionMatrix import pretty_Result
from knn import KNN

"""

@ Author: Zhebin Yin
@ Date: Apr. 20, 2023
@ Version: 1

"""

def mainSolver():
    parser = argparse.ArgumentParser(description= "Supervised learning algorithms.")

    parser.add_argument("-train" , type = str ,required=True, 
                        help= "the training csv file.")
    parser.add_argument("-test", type=str, required=False,
                        help=" the testing csv data file.")
    parser.add_argument("-K", type = int, default= 0, required=False,
                        help="if > 0 indicates to use kNN and also the value of K (if 0, do Naive Bayes').")
    parser.add_argument("-C", type = float, default=0, required=False, 
                        help= "if > 0 indicates the Laplacian correction to use (0 means don't use one).")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, required=False, 
                         help="outputs each predicted vs actual label")
    parser.add_argument("-centroids", type=str, nargs="+", default=None,
                        help="if a list of centroids is provided those should be used for kMeans.")
    parser.add_argument("-e", const=str, nargs="?", default="e2",
                        help="-d e2 or -d manh indicating euclidean distance squared or manhattan distance to use")
    args = parser.parse_args()
    

    if args.K < 0:
        print("ValError: K can't be negative")
        exit(1)
    if args.C < 0:
        print("ValError: C can't be negative")
        exit(1)
    if args.C > 0 and args.K > 0:
        print("Error: Either C or K.")
        exit(1)

    if args.centroids == None:
        if(args.test == None):
            print("Error: please provide test data.")
            exit(1)
        trainFile = pd.read_csv(args.train, header=None)
        testFile = pd.read_csv(args.test, header=None)
        delta = args.C # Laplacian Correction for Naive Bayes


        if args.K > 0:
            knn = KNN(args.K, args.verbose, trainFile, testFile)
            knn.loadData()
            predictions = knn.knn()
            print(predictions)
            pretty_Result(predictions, testFile)
        else:
            train_df = trainFile.astype(str)
            test_df = testFile.astype(str)
            nb = NaiveBayes(delta, args.verbose, train_df, test_df)
            predictions = nb.train()
            pretty_Result(predictions, test_df)


    else: # kmeans
        if(args.test !=None):
            print("Error: please do not provide extra file.")
            exit(1)
        trainFile = pd.read_csv(args.train, header=None)
        
                
    
    

    


if __name__ == '__main__':
    mainSolver()
