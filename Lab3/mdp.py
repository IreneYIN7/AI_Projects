from MarkovNode import MarkovNode
from collections import defaultdict
import copy
from typing import Dict, List

class MarkovSolver:
    """
    A generic MDP solver.
    """
    def __init__(self, nodeDict: Dict[str, MarkovNode], discount = 1.0, min = False, tol = 0.001, iterations = 100) -> None:
        
        self.nodeDict = nodeDict # Dictionary: key - node, value - MarkovNode
        self.min = min
        self.discountRate = discount
        self.tolerance = tol
        self.iteration = iterations
    
    
    def bellman_equ(self, curNode: MarkovNode):
        """
        calculate the new score of the current node - helper of bellmen equation
        """
        if curNode['edges'] is None:
            # terminal node
            return curNode['reward']
        score_val = 0.0
        if curNode["policy"] is None: # if chance node
            if curNode['policy'] is None:
                for edge in curNode['edges']:
                    score_val += curNode['probDict'][edge] * self.nodeDict[edge]['score']
        else:
            name, sucess_rate = curNode['policy']
            for e in curNode['edges']:
                if e == name:
                    score_val += sucess_rate * self.nodeDict[e]['score']
                else:
                    score_val += ((1 - sucess_rate) / (len(curNode['edges']) - 1)) *  self.nodeDict[e]['score']
        return curNode['reward'] + self.discountRate * score_val

    def value_iteration(self):
        """
        Get the score of all nodes for each iteration
        """
        for i in range(self.iteration):
            data = self.value_iteration_helper()
            # print("data at i : ", i, " is: ", data)
            if data <= self.tolerance:
                return True
        return False
        
            
    def value_iteration_helper(self):
        newNodesDict: Dict[str, MarkovNode] = {}
        
        data = 0.0
        for node in self.nodeDict.values():
            newNode = copy.deepcopy(node)
            # print("node: ", node.name, "reward: ", newNode.reward)
            # print("edge: ", newNode.edges, "prob: ", newNode.probDict, "successR: ", newNode.successRate)
            # print("score: ", newNode.score)
            newNode['score'] = self.bellman_equ(node)
            newNodesDict[node['name']] = newNode
            diff = abs(newNode['score'] - node['score'])
            if diff > data:
                data = diff      #

        self.nodeDict = newNodesDict
        return data
    
    def greedyPolicyComputation(self):
        """
        update the policy 
        """
        newPolicy = False
        for node in self.nodeDict.values():
            if node['policy'] is None:
                continue
            # update policy for each node
            isupdate = False
            edgeNext = node['policy'][0]
            val = self.nodeDict[edgeNext]['score']
            for e in node['edges']:
                if e != edgeNext:
                    eScore = self.nodeDict[e]['score']
                    if(self.min and eScore < val) or (not self.min and eScore > val):
                        edgeNext = e
                        val = eScore
            if edgeNext != node['policy'][0]:
                node['policy']  = (edgeNext, node['policy'][1])
                isupdate = True
            if isupdate:
                newPolicy = True
        return newPolicy


    def mdpSolver(self):
        while True:
            if self.value_iteration():
                if not self.greedyPolicyComputation(): # if policy didn't change
                    break

    def format(self) -> None:
        """
        Print the current value and policy of all nodes.
        """
        policy = [f"{node['name']} -> {node['policy'][0]}" for node in self.nodeDict.values() if node['policy'] is not None]
        print('\n'.join(sorted(policy)))
        print()
        for node in sorted(self.nodeDict.values(), key=lambda x: x['name']):
            print(f"{node['name']}={node['score']:.3f}", end=" ")
        print()
        
        
