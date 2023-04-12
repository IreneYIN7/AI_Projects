#python3 
from sys import exit
import argparse
from MarkovNode import constructMarkovNode
from mdp import MarkovSolver

"""

@ Author: Zhebin Yin
@ Date: Apr. 10, 2023
@ Version: 1

"""

def mainSolver():
    parser = argparse.ArgumentParser(description= "A Markov process solver.")

    parser.add_argument("-d", "--discount", type = float, default=1.0, 
                        help= "a float discount factor [0, 1] to use on future rewards, defaults to 1.0 if not set.")
    parser.add_argument("-m","--min", action="store_true", default=False,
                        help="minimize values as costs, defaults to false which maximizes values as rewards.")
    parser.add_argument("-t", "--tolerance", type = float, default= 0.01, 
                        help="a float tolerance for exiting value iteration, defaults to 0.01 or 0.001 (matches test outputs).")
    parser.add_argument("-i", "--iteration", type = int, default=100, 
                        help= "an integer that indicates a cutoff for value iteration, defaults to 100.")
    parser.add_argument('mkp_file', type = argparse.FileType('r'), nargs="?", help="The file containing the input of mkp.")
    args = parser.parse_args()
    
     
    markovNodes = constructMarkovNode(args.mkp_file)
    
    # for node in markovNodes.values():
    #     print("node value: ", node)
    mdp = MarkovSolver(markovNodes, args.discount, args.min, args.tolerance, args.iteration)
    mdp.mdpSolver()
    mdp.format()

if __name__ == '__main__':
    mainSolver()
