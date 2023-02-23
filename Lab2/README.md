# <center> Lab2: Map/Vertex coloring via DPLL </center>

## MileStones

- [Ok ] Clarifications

- [] Construct Graph from input file

- [] Build CNF from the graph

- [] Build DPLL Solver

- [] Convert CNF to the result through DPLL

- [] Build solutions

- [] Test

---
## Clarification

This is a program that takes as input in undirected graph, and produces a "coloring" of the vertices such that no two adjacent vertices have the same color. 

---

### Graph constraints to clauses
In order to solve map/vertex coloring with predicate logic, there are 2 types of clauses for very vertex. 

1. Every vertex should have at least one color.

2. No adjacent same colors rhs for every edge, distinct clause for each color.

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

## Compile
A program run should look like:

`solver [-v] $ncolors $input-file`


- `-v` is an optional flag for verbose mode (more later)
- `$ncolors` is the number of colors to solve for.  If 2 use R, G; if 3 RGB; if 4 RGBY.
- `$input-file ` is a graph input file (see next section)

In this program, I assume all the input file is well formatted. 

This program **DOES NOT** check the bad inputs.

## Input file
The input text file is a subset of Lab 1 (the ':' lines), in that each line should contain a vertex and some neighbors.

- A vertex can be up to 32 characters long and valid characters for a vertex are any other than the 4 special characters used for punctuation: `:` ,  `[` , `]` , `,`
- Blank lines or lines whose first character is '#' should be skipped (allows comments and spacing)
- `x : [y]` implies `y : [x]` [Note: undirected graph], but it may or may not be specified.  Either is valid and 'y' in this example need not have a line with it on the LHS.
- `x : []` is also valid 

Note that the graph is undirected, but only one edge direction is needed to imply the two way relationship (although both directions are legal).
