#python3 
from sys import exit
import argparse
from graph import parseInput
from CNF import *
from dpll import dp, convertToSlution
"""
This is the main solver of the Map/Vertex coloring generator.

@ Author: Zhebin Yin
@ Date: Feb. 23, 2023
@ Version: 1

python3 main.py -v 3 tiny.txt 
"""

def mainSolver():
    parser = argparse.ArgumentParser(description= "A solver of the Map/Vertex coloring generator.")

    parser.add_argument("-v", "--v", action="store_true", default=False
                        , help="verbose output")
    parser.add_argument("ncolors", type = int,
                        help="the number of colors to solve for.")
    parser.add_argument('graph_file', type = argparse.FileType('r'), nargs="?", help="The file containing the graph.")
    args = parser.parse_args()

    graph = parseInput(args.graph_file)
    cnf_converter = cnf(args.ncolors, graph.graph)
    cnf_converter.graphConstraints()
    # print(cnf_converter.clauses)
    # print(cnf_converter.atoms)
    convertToSlution(cnf_converter.atoms, cnf_converter.clauses, args.v)
if __name__ == '__main__':
    mainSolver()
