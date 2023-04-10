# <center> Lab2: Map/Vertex coloring via DPLL </center>

## MileStones

- [Ok ] Clarifications

- [OK ] Construct Graph from input file

- [OK ] Build CNF from the graph

- [OK ] Build DPLL Solver

- [OK ] Convert CNF to the result through DPLL

- [OK ] Build solutions

- [OK ] Test

---
## Clarification

This is a program that takes as input in undirected graph, and produces a "coloring" of the vertices such that no two adjacent vertices have the same color. 

---

### Graph constraints to clauses
In order to solve map/vertex coloring with predicate logic, there are 2 types of clauses for very vertex. 

1. Every vertex should have at least one color.

2. No adjacent same colors rhs for every edge, distinct clause for each color.

3. At most one color for each vertex.

[Option 1] Produce BNF -> CNF -> DPLL
[Option 2] Produce CNF -> DPLL 

Note: if do the conversion of BNF to CNF, you need to follow the 5 steps to convert to the correct CNF. 

In this program, I will directly produce CNF by myself, and pass to the DPLL part.

In verbose mode, you should print out the CNF clauses that are being sent to the DPLL solver.

---



## APIs (Use Cases)

1. Create Undirected Graph
    
        Graph  = parseInput(filename)

2. Build CNF Clauses on the graph

        clauses = graphConstraints(graph)

3. Apply DPLL on the CNF Clauses

        assignments = dpll(clauses)

4. Convert to Solution

        solution = converBack(assignments)

## Compiling
To Compile my program:

`python3 main.py [-v] $ncolors $input-file`

- I'm using python3 for this Lab.
- main.py is my main generator.
- `-v` is an optional flag for verbose mode (more later).
- `$ncolors` is the number of colors to solve for.  If 2 use R, G; if 3 RGB; if 4 RGBY.
- `$input-file ` is a graph input file (see next section).

Note: 
- In this program, I assume all the input file is well formatted. 

- This program **DOES NOT** check the bad inputs.

- This program only takes number of colors in the range from 2 to 4. (i.e. 2: [R, G], 3: [R, G, B], 4: [R, G, B, Y])

eg:

`python3 main.py -v 3 tiny.txt`

`python3 main.py 3 tiny.txt`


## Input file
The input text file is a subset of Lab 1 (the ``:`` lines), in that each line should contain a vertex and some neighbors.

- A vertex can be up to 32 characters long and valid characters for a vertex are any other than the 4 special characters used for punctuation: `:` ,  `[` , `]` , `,`
- Blank lines or lines whose first character is '#' should be skipped (allows comments and spacing)
- `x : [y]` implies `y : [x]` [Note: undirected graph], but it may or may not be specified.  Either is valid and 'y' in this example need not have a line with it on the LHS.
- `x : []` is also valid. This means `x` is a solo element (`x` has No adjacent elements). 

Note that the graph is undirected, but only one edge direction is needed to imply the two way relationship (although both directions are legal).
