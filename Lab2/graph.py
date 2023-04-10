# python3
import re
from collections import defaultdict

"""
Read the input file and construct input string into graph.

@ Author: Zhebin Yin
@ Date: Feb. 23, 2023
@ Version: 1


"""

class Graph:
    """
    Graph constructor.
    self.graph: contains all the node and edges.
    addEdge() : add edge into the self.graph.
    """
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.root = None

    def addEdge(self, v, e):
        if e not in self.graph[v]:
            self.graph[v].append(e)
        if v not in self.graph[e]:
            self.graph[e].append(v)
    
    def addVertex(self, v):
        self.graph[v] = []





def getInput(inputfile): 
    """
    Helper func to get the pure data from input file.
    """
    input_data = []
    with inputfile as file:
        for line in file:
            if not line.strip():
                continue  # Empty line, Skip to next line
            inputLine = line.split("\n")[0]
            if inputLine[0] == "#":
                continue  # comment line, skip to next line
            if (':' not in inputLine):
                raise ValueError(f"Invalid input: {inputLine}")
            data = re.findall('[\w-]+', inputLine)
            input_data.append(data)
    return input_data


def parseInput(inputfile):
    """
    Construct a graph with given input string list - contains nodes and edges.
    """
    inputData = getInput(inputfile)
    inputGraph = Graph()
    # construct a graph
    for item in inputData:
        node = item[0]
        if len(item) == 1:
            inputGraph.addVertex(node) 
        for i in range(1, len(item)):
            inputGraph.addEdge(node, item[i])

    return inputGraph


