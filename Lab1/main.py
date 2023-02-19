#!/usr/bin/env python3
#python3 main.py -ab 4 -min "DAGtest.txt"
"""
Main solver of minimax game tree with alpha-beta pruning and max-value cutoff.


@ Version: 1
@ Author: Zhebin Yin
@ Date: Feb. 12, 2023

"""
from sys import exit
import argparse
from graphChecker import setGraph
from Game import buildGameTree
from minimax import *

def mainSolver():
    parser = argparse.ArgumentParser(description= "Launch minimax with the input graph file")

    parser.add_argument("-v", "--v", action="store_true", default=False
                        , help="verbose output")
    parser.add_argument("-ab", action="store_true", default=False,
                        help = "use alpha-beta pruning (by default do max-value)"
                        )
    parser.add_argument("value", type = int,
                        help="indicating the max value n, and min value -n")
    # must be either max or min.
    parser.add_argument('player', choices=['max', 'min'], help="The player at the root of the game tree")
    parser.add_argument('graph_file', type = argparse.FileType('r'), nargs="?", help="The file containing the game tree")
    args = parser.parse_args()
    
    if args.value < 0:
        print("Error: must be a positive number.")
        exit(1)

    # build graph and do the valid graph checking
    graphData, leafDict = setGraph(args.graph_file)
    gameTree = buildGameTree(graphData)

    # Now, graph is valid and do minimax
    minimax = Minimax(gameTree, args.player, leafDict, args.value, args.v)
    if args.ab:
        minimax.alphaBetaSearch(-math.inf, math.inf)
    else:
        minimax.minimax()


if __name__ == '__main__':
    mainSolver()

