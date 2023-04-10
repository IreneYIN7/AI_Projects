# python3
import copy
"""
This is the DPLL solver which takes in the CNF clauses and find the valid solution.

@ Author: Zhebin Yin
@ Date: Feb. 26, 2023
@ Version: 2
"""
def format(atom):
    color = ""
    atomName = ""
    color = atom[len(atom) - 1] # given fact that color always at the last index
    atomName = atom[:len(atom) - 2] # given fact that before _R is the name of the atom
    if color == "R":
        color = "Red"
    elif color == "B":
        color = "Blue"
    elif color == "G":
        color = "Green"
    elif color == "Y":
        color = "Yellow"
    return (color, atomName)

def convertToSlution(atoms, clauses, verbose):
    V = dp(atoms, clauses, verbose)
    if V is not None:
        for atom in V:
            if V[atom] == True:
                color, atomName = format(atom)

                print(atomName,"=", color)


def dp(atoms, clauses, verbose):
    """
    atoms : set of propositional atoms;
    clauses : Set of propositional formulas in CNF
    return: either a valuation on ATOMS satisfying S or NIL if none exists.
    """
    V = dict()
    for atom in atoms:
        V[atom] = None
    V = dp1(atoms, clauses, V, verbose)
    if V is None:
        print("No valid DPLL solution exists for this CNF.")
        exit(-1)
    return V

def dp1(atoms,clauses,V, verbose):
    loop = True
    while loop: # loop until a solution is found or no easy cases remain
        # base case:
        # failure: unsatisfiable clause
        loop = False
        for clause in clauses:
            if len(clause) == 0:
                return None
        # success: all clauses are satisfied
        if len(clauses) == 0:   
            for atom in atoms:
                if V[atom] == None:
                    if verbose: 
                        print("Unbound ", atom, "= False")
                    V[atom] = False
            return V
        
        # ease case:
        # unit literal
        for clause in clauses:
            if len(clause) == 1:
                V = obviousAssign(clause[0], V, verbose)
                clauses = propagate(clause[0], clauses, V)
                loop = True
                break
        # Pure Literal
        for atom in atoms:
            clauses = pureLiteral(atom, clauses, V, verbose)
    
    clauses_copy = copy.deepcopy(clauses)
    new_V = copy.deepcopy(V)
    picked = None
    for atom in atoms:
        if V[atom] == None:
            new_V[atom] = True
            picked = atom
            break
    if verbose:
        print("Hard guess ", atom, "= True")
    clauses_copy = propagate(picked, clauses_copy, new_V)
    new_V = dp1(atoms, clauses_copy, new_V, verbose)
    if new_V != None:
        return new_V
    else:
        if verbose:
            print("contradiction: backtrack guess ", atom, "= False")
        clauses_copy = copy.deepcopy(clauses)
        new_V = copy.deepcopy(V)
        new_V[picked] = False
        clauses_copy = propagate(picked, clauses_copy, new_V)
        return dp1(atoms, clauses_copy, new_V, verbose)


def pureLiteral(atom, clauses, V, verbose):
    has_atom = False
    has_neg_atom = False
    neg_atom = "!" + atom
    for clause in clauses:
        if atom in clause:
            has_atom = True
        if neg_atom in clause:
            has_neg_atom = True
    if has_atom and not has_neg_atom:
        if verbose:
            print("Easy case: pure literal ", atom, "= True")
        V[atom] = True
        return update(atom, clauses)
    elif not has_atom and has_neg_atom:
        if verbose:
            print("Easy case: pure literal ", atom, "= False")
        V[atom] = False
        return update(neg_atom, clauses)
    else:
        return clauses
    
def propagate(atom, clauses, V):
    if "!" in atom:
        atom = atom.replace("!","")
    negAtom = "!" + atom
    for i, clause in enumerate(clauses):
        if (atom in clause and V[atom] == True) or (negAtom in clause and V[atom] == False):
            clauses[i] = None
        elif atom in clause and V[atom] == False:
            clauses[i].remove(atom)
        elif negAtom in clause and V[atom] == True:
            clauses[i].remove(negAtom)
    return [clause for clause in clauses if type(clause)==list]

def update(atom, clauses):

    for idx, clause in enumerate(clauses):
        if atom in clause:
            clauses[idx] = None
    return [clause for clause in clauses if type(clause)==list]
    

def obviousAssign(atom, V, verbose):
    if atom[0] == "!":
        if verbose:
            print("Easy case: unit literal", atom[1:], "= False")
        V[atom.replace("!","")] = False
    else:
        if verbose:
            print("Easy case: unit literal ", atom, "= True")
        V[atom] = True
    return V


if __name__ == "__main__":
    atoms = ['WA_R', 'WA_G', 'WA_B', 'NT_R', 'NT_G', 'NT_B', 'SA_R', 'SA_G', 'SA_B', 'Q_R', 'Q_G', 'Q_B', 'NSW_R', 'NSW_G', 'NSW_B', 'V_R', 'V_G', 'V_B', 'T_R', 'T_G', 'T_B']
    clauses = [['WA_R', 'WA_G', 'WA_B'], ['!WA_R', '!NT_R'], ['!WA_R', '!SA_R'], ['!WA_G', '!NT_G'], ['!WA_G', '!SA_G'], ['!WA_B', '!NT_B'], ['!WA_B', '!SA_B'], ['NT_R', 'NT_G', 'NT_B'], ['!NT_R', '!WA_R'], ['!NT_R', '!SA_R'], ['!NT_R', '!Q_R'], ['!NT_G', '!WA_G'], ['!NT_G', '!SA_G'], ['!NT_G', '!Q_G'], ['!NT_B', '!WA_B'], ['!NT_B', '!SA_B'], ['!NT_B', '!Q_B'], ['SA_R', 'SA_G', 'SA_B'], ['!SA_R', '!WA_R'], ['!SA_R', '!NT_R'], ['!SA_R', '!Q_R'], ['!SA_R', '!NSW_R'], ['!SA_R', '!V_R'], ['!SA_G', '!WA_G'], ['!SA_G', '!NT_G'], ['!SA_G', '!Q_G'], ['!SA_G', '!NSW_G'], ['!SA_G', '!V_G'], ['!SA_B', '!WA_B'], ['!SA_B', '!NT_B'], ['!SA_B', '!Q_B'], ['!SA_B', '!NSW_B'], ['!SA_B', '!V_B'], ['Q_R', 'Q_G', 'Q_B'], ['!Q_R', '!NT_R'], ['!Q_R', '!SA_R'], ['!Q_R', '!NSW_R'], ['!Q_G', '!NT_G'], ['!Q_G', '!SA_G'], ['!Q_G', '!NSW_G'], ['!Q_B', '!NT_B'], ['!Q_B', '!SA_B'], ['!Q_B', '!NSW_B'], ['NSW_R', 'NSW_G', 'NSW_B'], ['!NSW_R', '!Q_R'], ['!NSW_R', '!SA_R'], ['!NSW_R', '!V_R'], ['!NSW_G', '!Q_G'], ['!NSW_G', '!SA_G'], ['!NSW_G', '!V_G'], ['!NSW_B', '!Q_B'], ['!NSW_B', '!SA_B'], ['!NSW_B', '!V_B'], ['V_R', 'V_G', 'V_B'], ['!V_R', '!SA_R'], ['!V_R', '!NSW_R'], ['!V_G', '!SA_G'], ['!V_G', '!NSW_G'], ['!V_B', '!SA_B'], ['!V_B', '!NSW_B'], ['T_R', 'T_G', 'T_B']]
    
    atoms_trian = ['1_R', '1_G', '2_R', '2_G', '3_R', '3_G', '4_R', '4_G', '5_R', '5_G', '6_R', '6_G', '7_R', '7_G', '8_R', '8_G', '9_R', '9_G', '10_R', '10_G']
    clauses_trian = [['1_R', '1_G'], ['!1_R', '!2_R'], ['!1_R', '!3_R'], ['!1_G', '!2_G'], ['!1_G', '!3_G'], ['2_R', '2_G'], ['!2_R', '!1_R'], ['!2_R', '!3_R'], ['!2_R', '!4_R'], ['!2_R', '!5_R'], ['!2_G', '!1_G'], ['!2_G', '!3_G'], ['!2_G', '!4_G'], ['!2_G', '!5_G'], ['3_R', '3_G'], ['!3_R', '!1_R'], ['!3_R', '!2_R'], ['!3_R', '!5_R'], ['!3_R', '!6_R'], ['!3_G', '!1_G'], ['!3_G', '!2_G'], ['!3_G', '!5_G'], ['!3_G', '!6_G'], ['4_R', '4_G'], ['!4_R', '!2_R'], ['!4_R', '!5_R'], ['!4_R', '!7_R'], ['!4_R', '!8_R'], ['!4_G', '!2_G'], ['!4_G', '!5_G'], ['!4_G', '!7_G'], ['!4_G', '!8_G'], ['5_R', '5_G'], ['!5_R', '!2_R'], ['!5_R', '!3_R'], ['!5_R', '!4_R'], ['!5_R', '!6_R'], ['!5_R', '!8_R'], ['!5_R', '!9_R'], ['!5_G', '!2_G'], ['!5_G', '!3_G'], ['!5_G', '!4_G'], ['!5_G', '!6_G'], ['!5_G', '!8_G'], ['!5_G', '!9_G'], ['6_R', '6_G'], ['!6_R', '!3_R'], ['!6_R', '!5_R'], ['!6_R', '!9_R'], ['!6_R', '!10_R'], ['!6_G', '!3_G'], ['!6_G', '!5_G'], ['!6_G', '!9_G'], ['!6_G', '!10_G'], ['7_R', '7_G'], ['!7_R', '!4_R'], ['!7_R', '!8_R'], ['!7_G', '!4_G'], ['!7_G', '!8_G'], ['8_R', '8_G'], ['!8_R', '!4_R'], ['!8_R', '!5_R'], ['!8_R', '!7_R'], ['!8_R', '!9_R'], ['!8_G', '!4_G'], ['!8_G', '!5_G'], ['!8_G', '!7_G'], ['!8_G', '!9_G'], ['9_R', '9_G'], ['!9_R', '!5_R'], ['!9_R', '!6_R'], ['!9_R', '!8_R'], ['!9_G', '!5_G'], ['!9_G', '!6_G'], ['!9_G', '!8_G'], ['10_R', '10_G'], ['!10_R', '!6_R'], ['!10_G', '!6_G']]

    atoms3 = ['1_R', '1_G', '1_B', '2_R', '2_G', '2_B', '3_R', '3_G', '3_B', '4_R', '4_G', '4_B', '5_R', '5_G', '5_B', '6_R', '6_G', '6_B', '7_R', '7_G', '7_B', '8_R', '8_G', '8_B', '9_R', '9_G', '9_B', '10_R', '10_G', '10_B']
    clauses3 = [['1_R', '1_G', '1_B'], ['!1_R', '!2_R'], ['!1_R', '!3_R'], ['!1_G', '!2_G'], ['!1_G', '!3_G'], ['!1_B', '!2_B'], ['!1_B', '!3_B'], ['2_R', '2_G', '2_B'], ['!2_R', '!1_R'], ['!2_R', '!3_R'], ['!2_R', '!4_R'], ['!2_R', '!5_R'], ['!2_G', '!1_G'], ['!2_G', '!3_G'], ['!2_G', '!4_G'], ['!2_G', '!5_G'], ['!2_B', '!1_B'], ['!2_B', '!3_B'], ['!2_B', '!4_B'], ['!2_B', '!5_B'], ['3_R', '3_G', '3_B'], ['!3_R', '!1_R'], ['!3_R', '!2_R'], ['!3_R', '!5_R'], ['!3_R', '!6_R'], ['!3_G', '!1_G'], ['!3_G', '!2_G'], ['!3_G', '!5_G'], ['!3_G', '!6_G'], ['!3_B', '!1_B'], ['!3_B', '!2_B'], ['!3_B', '!5_B'], ['!3_B', '!6_B'], ['4_R', '4_G', '4_B'], ['!4_R', '!2_R'], ['!4_R', '!5_R'], ['!4_R', '!7_R'], ['!4_R', '!8_R'], ['!4_G', '!2_G'], ['!4_G', '!5_G'], ['!4_G', '!7_G'], ['!4_G', '!8_G'], ['!4_B', '!2_B'], ['!4_B', '!5_B'], ['!4_B', '!7_B'], ['!4_B', '!8_B'], ['5_R', '5_G', '5_B'], ['!5_R', '!2_R'], ['!5_R', '!3_R'], ['!5_R', '!4_R'], ['!5_R', '!6_R'], ['!5_R', '!8_R'], ['!5_R', '!9_R'], ['!5_G', '!2_G'], ['!5_G', '!3_G'], ['!5_G', '!4_G'], ['!5_G', '!6_G'], ['!5_G', '!8_G'], ['!5_G', '!9_G'], ['!5_B', '!2_B'], ['!5_B', '!3_B'], ['!5_B', '!4_B'], ['!5_B', '!6_B'], ['!5_B', '!8_B'], ['!5_B', '!9_B'], ['6_R', '6_G', '6_B'], ['!6_R', '!3_R'], ['!6_R', '!5_R'], ['!6_R', '!9_R'], ['!6_R', '!10_R'], ['!6_G', '!3_G'], ['!6_G', '!5_G'], ['!6_G', '!9_G'], ['!6_G', '!10_G'], ['!6_B', '!3_B'], ['!6_B', '!5_B'], ['!6_B', '!9_B'], ['!6_B', '!10_B'], ['7_R', '7_G', '7_B'], ['!7_R', '!4_R'], ['!7_R', '!8_R'], ['!7_G', '!4_G'], ['!7_G', '!8_G'], ['!7_B', '!4_B'], ['!7_B', '!8_B'], ['8_R', '8_G', '8_B'], ['!8_R', '!4_R'], ['!8_R', '!5_R'], ['!8_R', '!7_R'], ['!8_R', '!9_R'], ['!8_G', '!4_G'], ['!8_G', '!5_G'], ['!8_G', '!7_G'], ['!8_G', '!9_G'], ['!8_B', '!4_B'], ['!8_B', '!5_B'], ['!8_B', '!7_B'], ['!8_B', '!9_B'], ['9_R', '9_G', '9_B'], ['!9_R', '!5_R'], ['!9_R', '!6_R'], ['!9_R', '!8_R'], ['!9_G', '!5_G'], ['!9_G', '!6_G'], ['!9_G', '!8_G'], ['!9_B', '!5_B'], ['!9_B', '!6_B'], ['!9_B', '!8_B'], ['10_R', '10_G', '10_B'], ['!10_R', '!6_R'], ['!10_G', '!6_G'], ['!10_B', '!6_B']]
    # V = dp(atoms_trian, clauses_trian, True)
    # for atom in V:
    #     print(atom,"=", V[atom])
    tiny = ['4_R', '4_G', '3_R', '3_G', '1_R', '1_G', '2_R', '2_G']
    tiny2 = [['4_R', '4_G'], ['!4_R', '!3_R'], ['!4_R', '!1_R'], ['!4_G', '!3_G'], ['!4_G', '!1_G'], ['3_R', '3_G'], ['!3_R', '!4_R'], ['!3_R', '!2_R'], ['!3_G', '!4_G'], ['!3_G', '!2_G'], ['1_R', '1_G'], ['!1_R', '!4_R'], ['!1_R', '!2_R'], ['!1_G', '!4_G'], ['!1_G', '!2_G'], ['2_R', '2_G'], ['!2_R', '!3_R'], ['!2_R', '!1_R'], ['!2_G', '!3_G'], ['!2_G', '!1_G']]
    V = dp(tiny, tiny2, False)
    print("talbe is : ", V)
    for atom in V:
        print(atom,"=", V[atom])
    
        