# python3
import re
from typing import Set, Dict, Union, Tuple, List
from collections import defaultdict

"""
Read the input file and construct input string into MarkovNode.

@ Author: Zhebin Yin
@ Date: Apr. 10, 2023
@ Version: 1

"""

class ParseError(Exception):
    """
    Output Error message when requirements failed to meet
    """
    pass

class inputParser:
    def __init__(self) -> None:
        self.rewardList: Dict[str, float] = {}
        self.probListDict: Dict[str, List[float]] = {}
        self.edgeListDict: Dict[str, List[str]] = {}

    # def rewardListGetter(self):
    #     return self.rewardList

    # def probListDictGetter(self):
    #     return self.probListDict

    # def edgeListDictGetter(self):
    #     return self.edgeListDict

    def getInputData(self, file): 
        """
        Helper func to get the pure data from input file.
        """
        for line in file:
            if not line.strip():
                continue  # Empty line, Skip to next line
            if line.startswith("#"):
                continue 
            inputLine = line.split("\n")[0]
            if ("=" in inputLine):
                node, reward = inputLine.split("=")
                node = node.strip()
                reward = reward.strip()
                self.rewardList[node] = float(reward)

            elif ("%" in inputLine):
                node, prob = line.split("%")
                node = node.strip()
                prob = prob.strip()
                prob = re.sub('\s+', ' ', prob)
                probilities = []
                for p in prob.split(" "):
                    probilities.append(float(p))
                # probilities = [float(x) for x in prob.split(" ")]
                if len(probilities) == 0:
                    raise ParseError(f"Probability list of Node \"{node}\" is empty.")
                elif len(probilities) > 1:
                    probSum = sum(probilities)
                    if abs(probSum - 1.0) > 1e-2:
                        raise ParseError(f"Probability list value of \"{node}\" does not sum to 1.0.")
                self.probListDict[node] = probilities

            elif (":" in inputLine):
                node, edge = line.split(":")
                node = node.strip()
                edge = edge.strip()
                if len(edge) <= 2 or edge[0] != "[" or edge[-1] != "]":
                    raise ParseError(f"Invalid edge \"{edge}\".")
                eList = []
                for e in edge[1:-1].split(","):
                    eList.append(e.strip())
                self.edgeListDict[node] = eList
            else:
                raise ParseError(f"Invalid input \"{line}\".")

        # print("reward list: ", self.rewardList)
        # print("prob list: ", self.probListDict)
        # print("edge list: ", self.edgeListDict)



