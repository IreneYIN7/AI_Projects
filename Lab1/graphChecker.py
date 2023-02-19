import re
from Game import *
from collections import defaultdict
"""
Check if the input graph is valid or not.
1. construct a Graph. Check if the graph is a valid search tree.

2. record the leaf node value - using dictionary


@ Author: Zhebin Yin
@ Date: Feb. 13, 2023
@ Version: 3
"""
class Graph():
    """
    Graph constructor.
    self.graph: contains all the node and edges.
    addEdge() : add edge into the self.graph.
    isCyclic() : check if there is a cylcle in the graph
    """
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.parent = []
        self.nodes = defaultdict(list) # a list of all nodes in graph
        self.root = None

    def addEdge(self, v, e):
        self.graph[v].append(e)

        self.nodes[v].append(e)

        if not v in self.parent:
            self.parent.append(v)
    
    def addLeaf(self, v):
        self.nodes[v] = []

    def findRoot(self):
        """
        Find the root of the graph
        """
        root = None
        for node in self.graph:
            if self.can_reach_all_nodes(node):
                root = node
        if root == None:
            print("Error: Graph has NO ROOT or has Multiple Roots!!")
            exit(1)
        else:
            return root


    def can_reach_all_nodes(self, node):
        """
        Return true if the node can reach to all the other nodes in the garph
        """
        def dfs(node, visited):
            visited.add(node)
            for neighbor in self.nodes[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        visited = set()
        dfs(node, visited)

        # Check if the set of visited nodes is the same as the set of all nodes in the graph
        return visited == set(self.nodes.keys())

    def checkMissingLeaf(self, leafDict):
        """
        Check if the inputGraph is missing leaf value, if leave value missing, report error
        """
        leaf = []
        for v in self.nodes:
            if self.nodes[v] == []:
                leaf.append(v)
        if len(leaf) != len(leafDict):
            print("Error: Missing Leaf Value or Missing Node")
            exit(1)

    def DAGChecker(self):
        if self.has_cycle():
            print("Error: Graph is not acyclic!")
            exit(1)

    def has_cycle(self):
        """
        Check if the given graph has cycle or not using Depth First Search (DFS)
        True if has cycle
        False otherwise
        """
        visited = defaultdict(int)
        
        def dfs(node):
            visited[node] = 1
            for neighbor in self.nodes[node]:
                if visited[neighbor] == 1:
                    # Cycle found
                    return True
                elif visited[neighbor] == 0:
                    if dfs(neighbor):
                        return True
            visited[node] = 2
            return False
            
        for node in self.nodes:
            if visited[node] == 0:
                if dfs(node):
                    return True
                    
        return False

def getInput(inputfile): 
    """
    Helper func to get the pure data from input file
    """
    input_data = []
    with inputfile as file:
        for line in file:
            if not line.strip():
                continue  # Skip to next line
            inputLine = line.split("\n")[0]
            if ('=' not in inputLine) and (':' not in inputLine):
                raise ValueError(f"Invalid input: {inputLine}")
            data = re.findall('[\w-]+', inputLine)
            input_data.append(data)
    return input_data


def setGraph(inputfile):
    """
    Construct a graph with given input string list - contains nodes and edges.
    As well as check the validity of the constructed graph.
    If the input is valid, return the constructed graph and the leaf value dictionary
    """
    inputData = getInput(inputfile)

    inputGraph = Graph()
    leafDict = getLeafNodeValue(inputData)
    # construct a graph
    for item in inputData:
        node = item[0]
        for i in range(1, len(item)):
            # if curent line is not a leaf with value 
            if(not re.match(r'^-?[0-9]+$',item[i])):
                inputGraph.addEdge(node, item[i])
            else:
                # add leaf
                inputGraph.addLeaf(node)
                
    # check validity of the graph
    inputGraph.root = inputGraph.findRoot()
    inputGraph.checkMissingLeaf(leafDict)
    inputGraph.DAGChecker()
    
    return inputGraph, leafDict


def getLeafNodeValue(input):
    """
    Given a list of string, extract the leaf node value.
    """
    leafDict = dict()
    for i in range(0, len(input)):
        item = input[i]
        node = item[0]
        last = item[len(item) - 1]
        if(re.match(r'^-?[0-9]+$',last)):
            leafDict[node] = int(last)
    return leafDict

