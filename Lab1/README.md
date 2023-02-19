# Lab 1: Minimax
This is a program that solves a minimax game tree with alpha-beta pruning and max-value cutoff.

---
## Input Graph File
Input should be a text file with the following contents.

* Each line should contain a node description
* A node label should be any string with alphanumeric characters
* A leaf node will have:
    - Using `n=v`. An integer `v` indicating a score (final or possibly from a heuristic evaluator) associated with a node label n
* An internal node will use a colon and comma separated $[]$ indicating parent child labels.

    - Using $n:[n1,n2,...]$ two or more node labels indicating child nodes
* Valid input is a tree or DAG (no cycles) with a value at every leaf node and a single root (node with no incoming edges).

This program would exit gracefully and indicate as best as possible the problem in case of bad arguments or a bad tree file (e.g. a cycle)

eg. - An Input File `.txt`

a: [a1, a2, a3]

a1: [b, c]

a3: [xy, wx]

a2: [b19, b29]

b=-4

c=3 

b19=5 

b29=2

xy=-1

wx=8


## Algorithm

This code would employ the minimax algorithm. It would by default process the full tree/DAG, always applying max-value cutoff, but optionally support Alpha-Beta pruning.

**Evaluation order**: use the node order in the input file. so "x: [c, a, b]" would evaluate c then a then b.

alpha and beta should not be global variables, but rather kept in an instance variable or passed around as a parameter.


--- 

## Data Structure and Functions

There are 4 main `.py` files for this project:
- `main.py` : The Main Solver for Minimax Alpha Beta algorithm. It would parse the input command into piecewise information. [Note: only `-v` (verbose) and `-ab` (alpha-beta prune) is optional]. Please read the more detailed information on the compile rules in the Running/Compiling Program section.
    
    Then, the main solver would first digest the input data, check the validity of the input, and if the input is valid, run corresponding minimax verison.

- `graphChecker.py`: To check if the input graph is valid or not. It would terminate the whole program if the input graph is not valid. (i.e. Missing root / Multiple roots, Missing leaf / Missing Node, and Not Acyclic.) 
    
    Data structure used: Graph (Dictionary). 
    1. construct a Graph. Check if the graph is a valid search tree. If the graph is not 

    2. record the leaf node value - using dictionary data structure.

- `Game.py`: This is the part to construct the data GameTree structure for later minimax and alpha-beta prune operation.

    Data Structure used: gameNode.

    The GameTree is constructed by the gameNode.

- `minimax.py`: The main file to execute Minimax with max-cutoff and alpha-beta prune operations.

    Data structure used: GameNode, and Dinctionary.

    Two main function:
    - alphaBetaSearch : use AlphaBetaPrune (-ab) in the Minimax Technique
    - minimax : use max-cutoff (default) in Minimax Technique





## Output
In regular mode, the program should simply print what the root player should do.

e.g. in the above example (with n=10) if max:

`max(a) chooses a2 for 2`

Whereas if min

`min(a) chooses a1 for 3`

In Verbose mode every internal node should be printed as above or should indicate that its subtree has been pruned due to alpha-beta.


-----
## Running/Compiling Program
A program run should look something like (if python or java could be slightly different):

`minimax [-v] [-ab] n -min/max graph-file`

* -v indicates verbose mode (more later)
* -ab indicates to use alpha-beta pruning (by default do not do A-B but always do max-value). 
Please type `-ab ab` to indicate you are using alpha-beta pruning.
* a number n indicating the max value (and by inference -n is the minimum)
* provide whether the root player is min or max
* a graph file to read (next section)

e.g. a run of

`minimax -v 5 min some-tree.txt`
means load the data from some-tree.txt, solve with min playing at the root, with value range [-5,5], provide verbose output but **do not use alpha-beta pruning** to speed up the search (since -ab was not passed).

eg. `python3 main.py -v -ab 8 max "Multi-levelDAG.txt"`