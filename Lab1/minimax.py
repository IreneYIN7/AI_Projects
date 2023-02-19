"""
Minimax with max-cutoff and alpha-beta prune.
Two main function:
- alphaBetaSearch : use AlphaBetaPrune (-ab) in the Minimax Technique
- minimax : use max-cutoff (default) in Minimax Technique

@ Author: Zhebin Yin
@ Date: Feb. 14, 2023
@ Version: 1
"""

import math

MIN = -math.inf
MAX = math.inf

class Minimax:
    
    def __init__(self, root, rootMinMax, leafDict, range, verbose = False) ->None:
        """
        * game_tree: the GameTree 
        * root: GameNode -- Root of the game tree
        * currentNode: GameNode -- the current tree node
        * successors: List of next possible GameNodes -- child of the current node.
        * rootMinMax: root as max or root as min
        * verbose : True - indicate processes, Flase - indicate just result
        * nextMove : the best nextMove
        * n : the absolute value of the biggest/smallest of the leaf node values.
        """
        # self.game_tree = gameTree   # GameTree
        self.root = root   # GameNode
        self.currentNode = None     # GameNode
        self.successors = []        # List of GameNodes
        self.rootMinMax = rootMinMax # str
        self.n = range               # int
        self.verbose = verbose      # boolean
        self.leafVal = leafDict     # dictionary 
        
    def alphaBetaSearch(self, alpha, beta):
        self.alphaBetaSearchHelper(self.root, self.rootMinMax, alpha, beta)

    def alphaBetaSearchHelper(self, node, maxmin, alpha, beta):
        # base case
        self.rootMinMax = maxmin
        if self.isleaf(node):
            return self.getValue(node)
        
        # minimax with alpha beta
        if (self.rootMinMax == 'max'):
            best_val = MIN
            self.getSuccessors(node)
            for state in self.successors:
                curVal = self.alphaBetaSearchHelper(state, 'min', alpha, beta)
                if(curVal > best_val):
                    best_val = curVal
                    nextMove = state
                alpha = max(alpha, best_val)
                if beta <= alpha:
                    nextMove = None
                    break
            self.foramting(node, best_val, 'max', nextMove)
            return best_val
        else:
            best_val = MAX
            self.getSuccessors(node)
            for state in self.successors:
                curVal = self.alphaBetaSearchHelper(state, 'max', alpha, beta)
                if(curVal <  best_val):
                    best_val = curVal
                    nextMove = state
                beta = min(beta, best_val)
                if beta <= alpha:
                    nextMove = None
                    break
                # if not pruned, then print when verbose = true
            self.foramting(node, best_val, 'min', nextMove)
            return best_val


    def minimax(self):
        """
        Minimax with maxcutoff
        """
        if (self.rootMinMax == 'max'):
            self.max_value(self.root) 

        else:
            self.min_value(self.root)
        
    def max_value(self, node):
        """
        Find the max value of the current state and record the best next move
        """
        # print ("MiniMax->MAX: Visited Node :: " + node.Name)
        # if node is leaf -> get value
        if self.isleaf(node):
            return self.getValue(node)

        maxVal = MIN
        self.getSuccessors(node)
        for state in self.successors:
            curVal = self.min_value(state)
            if(maxVal <  curVal):
                maxVal = curVal
                nextMove = state
            if(maxVal == self.n):
                break
        self.foramting(node, maxVal, 'max', nextMove)
        return maxVal

    def min_value(self, node):
        # print ("MiniMax->MIN: Visited Node :: " + node.Name)
        if self.isleaf(node):
            return self.getValue(node)

        minVal = math.inf
        self.getSuccessors(node)
        for state in self.successors:
            curVal = self.max_value(state)
            if(minVal >  curVal):
                minVal = curVal
                nextMove = state
            if(minVal == -self.n):
                break
        self.foramting(node, minVal, 'min', nextMove)
        return minVal
        
    # successor states in a game tree are the child nodes…
    def getSuccessors(self, node):
        if not self.isleaf(node):
            self.successors = node.children
        else:
            print("No child")

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)
    def isleaf(self, node):
        if node.children == []:
            return True

    def getValue(self, node):
        if self.isleaf(node):
            return self.leafVal[node.Name]
    
    def foramting(self, node, Val, maxmin, nextMove):
        """
        Formatting output
        """
        if nextMove != None:
            if self.verbose:
                print("{maxmin} ({nodeParent}) chooses {node} for {val}".format(maxmin = maxmin, nodeParent = node.Name, node = nextMove.Name, val =  Val))
            if(not self.verbose and node == self.root):
                # if not verbose - indicate just the root choice and value
                print("{maxmin} ({nodeParent}) chooses {node} for {val}".format(maxmin = maxmin, nodeParent = self.root.Name, node =  nextMove.Name, val =  Val))
