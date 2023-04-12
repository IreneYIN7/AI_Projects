from collections import defaultdict
from inputParser import inputParser
from typing import TypedDict, Dict, Union, Tuple, List


"""
Construct a list of MarkovNode from input file.
"""


class MarkovNode(TypedDict):
    """
    Markov node type
    """
    name: str
    reward: float
    edges: Union[List[str], None]
    probDict: Union[Dict[str, float], None]
    policy: Union[Tuple[str, float], None]
    score: float


def constructMarkovNode(file):
    markovNodes : Dict[str, MarkovNode] = {}
    parser = inputParser()
    parser.getInputData(file)
    nodeNames = parser.edgeListDict.keys() | parser.rewardList.keys()

    for node in nodeNames:
        markov_node = MarkovNode()
        markov_node["name"] = node
        # assign reward
        if node in parser.rewardList:
            markov_node["reward"] = parser.rewardList[node]
        else:
            markov_node["reward"] =  0.0

        markov_node["score"] = markov_node["reward"]

        if node not in parser.edgeListDict or len(parser.edgeListDict[node]) == 0:
            # terminal state
            markov_node["edges"] = None
            markov_node["probDict"] = None
            markov_node["policy"] = None
            if node in parser.probListDict:
                raise ValueError(f"Invalid probability.")
            
        else:
            # intermediate state
            edges = parser.edgeListDict[node]
            markov_node["edges"] = edges
            if node in parser.probListDict:
                probList = parser.probListDict[node]
                if len(probList) == 1:
                    # decision node
                    markov_node["policy"] = (edges[0], probList[0])
                    markov_node["probDict"] = None
                else:
                    # chance node
                    if(len(probList)!= len(edges)):
                        raise ValueError(f"Prob Length doesn't match num edges.")
                    markov_node["probDict"] = dict(zip(edges, probList))
                    markov_node["policy"] = None
            else:
                # node which does not have prob -  it is assumed to be a decision node with p=1
                if len(edges) == 1:
                    markov_node["probDict"] = {edges[0]: 1.0}
                    markov_node["policy"] = None
                else:
                    markov_node["policy"] = (edges[0], 1.0)
                    markov_node["probDict"] = None

        markovNodes[node] = markov_node
    return markovNodes

        