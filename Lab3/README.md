# <center> Lab3: Markov process solver. </center>

## MileStones

- [Ok ] Clarifications

- [OK ] Construct MarkovNodes Dictionary from input file

- [OK ] Build MDP Solver

    - [OK ] Build Value Iteration

    - [OK ] Build Greedy Approach 

---
## Clarification

This is a generic Markov process solver.



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

## class

1. `class inputParser`

    Read the input file and construct input string into data chunks: `rewardList`, `ProbListDict`, and `edgeListDict` for later construct markov nodes dictionary.

2. `class MarkovNode`

    A type class which clarify the types and variables a markov node needs.


3. `class MarkovSolver`

    The main solver of MDP.

## APIs (Use Cases)


1. Parse input file into MarkovNode Dictionary
    
        markovNodes = constructMarkovNode(args.mkp_file)

2. Apply MDP solver to get data

        mdp.mdpSolver()

3. Format output

        mdp.format()

## Compiling
To Compile my program:

`python3 main.py -t 0.0001 -i 100 some-input.txt`

- I'm using python3 for this Lab.
- main.py is my main generator.
- -d : a float discount factor [0, 1] to use on future rewards, defaults to 1.0 if not set
- -m : minimize values as costs, defaults to false which maximizes values as rewards
- -t : a float tolerance for exiting value iteration, defaults to 0.01 or 0.001 (matches test outputs)
- -i : an integer that indicates a cutoff for value iteration, defaults to 100


Note: 
- In this program, I assume all the input file is well formatted. 

eg:

`python3 main.py -t 0.0001 -i 100 some-input.txt`

`python3 main.py -d 0.9 -t 0.0001 -i 150 input.txt`

`python3 main.py -m -tol 0.0001 -i 150 input.txt`
