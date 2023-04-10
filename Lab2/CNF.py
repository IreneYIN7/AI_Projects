# python3
from graph import*
import copy
"""
This is the CNF generator.
Convert the graph into the CNF languagne.

@ Author: Zhebin Yin
@ Date: Feb. 25, 2023
@ Version: 1
"""

class cnf:
    def __init__(self, numColor, graph) -> None:
        self.numColor = numColor
        if numColor == 2:
            self.colors = ["R", "G"]
        elif numColor == 3:
            self.colors = ["R", "G", "B"]
        elif numColor == 4:
            self.colors = ["R", "G", "B", "Y"]
        self.graph = graph
        self.nodeList = list(graph.keys())
        self.clauses = []
        self.atoms = []

    def graphConstraints(self):
        """
        Construct CNF which shows the rule 1 and rule 2.
        """
        result = []
        for node in self.graph:
            rule1 = self.atLeastOneColor(node)
            result.append(rule1)
            rule2 = self.distinctColor(node)
            result += rule2
            rule3 = self.atMostOneColor(node)
            # print the CNF clauses.
            # print(rule1)
            # for line in rule2:
            #     print(line)
            # for l in rule3:
            #     print(l)
        return result 


    def atLeastOneColor(self, curNode):
        """
        Given the current node, construct the CNF which shows the rule 1:
        "Every node has at least one color"
        Note: No \n given in the result.
        """
        cnf_Rule1 = ""
        clause = []
        for color in self.colors:
            atom = curNode + "_" + color
            self.atoms.append(atom)
            clause.append(atom)
            cnf_Rule1 += atom + " "
        self.clauses.append(clause)
        return cnf_Rule1

    def distinctColor(self, curNode):
        """
        Given the current Node, construct CNF which shows the rule 2 for each possible color:
        "No adjacent same colors rhs for every edge, distinct clause for each color"
        Note: No \n given in the result.
        """
        cnf_Rule2 = []
        
        for color in self.colors:
            clauses = []
            for node in self.graph[curNode]:
                clause = "!" + curNode + "_" + color 
                clauses.append(clause)
                clause2 = "!" + node + "_" + color
                clauses.append(clause2)
                rule = clause + " " + clause2
                cnf_Rule2.append(rule)
                self.clauses.append(clauses)
                clauses = []
        return cnf_Rule2


    def atMostOneColor(self, curNode):
        """
        At most one color for each vertex.
        Color(WA,R) =>¬[Color(WA,G) v Color(WA,B)]
        ! Color(WA, R) v ![Color(WA,G) v Color(WA,B)]
        ! Color(WA, R) v ! Color(WA, G) ^ ! Color(WA, B)

        ! Color(WA, R) v ! Color(WA, G)
        ! Color(WA, R) v ! Color(WA, B)
        ["R", "G", "B"]
        """
        cnf_Rule3 = []
        for color in self.colors:
            # copy the color list
            colorList = copy.deepcopy(self.colors)
            clauses = []
            # remove the current color
            colorList.remove(color)
            for nextColor in colorList:
                clause1 = "!" + curNode + "_" + color
                clauses.append(clause1)
                clause2 = "!" + curNode + "_" + nextColor
                clauses.append(clause2)
                rule = clause1 + " " + clause2
                cnf_Rule3.append(rule)
                self.clauses.append(clauses)
                clauses = []
            
        return cnf_Rule3
            

