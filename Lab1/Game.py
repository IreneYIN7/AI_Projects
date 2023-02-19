from collections import *

"""
The GameTree should be constructed by the gameNode

@ Author: Zhebin Yin
@ Data: Feb. 16, 2023
@ Version: 3
"""

class GameNode:
    def __init__(self,name, value = None, parent = None) -> None:
        self.Name = name     # string
        self.value = value   # value of the leaf
        self.parent = parent # node's parent
        self.children = []   # node's children
    
    def addChild(self, childNode):
        self.children.append(childNode)


def buildGameTree(graphInput):
    root = GameNode(graphInput.root)
    build_subtree(root, root, graphInput)
    return root


def build_subtree(node, parent, graphInput):
    for child_name in graphInput.graph[node.Name]:
        child_node = GameNode(child_name, parent=node)
        parent.addChild(child_node)
        build_subtree(child_node, child_node,graphInput)
