# <center> Davis-Putnam (DPLL) procedure </center>

Martin Davis, Hillary Putnam, George Logemann, and Donald Loveland (1962)

# dp(ATOMS, S)

    dp(in  ATOMS : set of propositional atoms;
       S : Set of propositional formulas in CNF)

``return``: either a valuation on ATOMS satisfying S or NIL if none exists.

V : array[ATOMS];

    { for (A in ATOMS) do V[A] = UNBOUND;
        return dp1(ATOMS,S,V) }
    end dp

# dp1 (ATOMS, S, V)
    dp1(ATOMS,S,V) {                             # call S,V by value 
    loop {    #Loop as long as there are easy cases to cherry pick 

    #  BASE OF THE RECURSION: SUCCESS OR FAILURE 
    if (S is empty)    # Success: All clauses are satisfied   
       { for (A in ATOMS)
           if (V[A] == UNBOUND) then assign V[A] either TRUE or FALSE;
         return(V);
       }

    else if (some clause in S is empty) 
    #  Failure: Some clause 
          then return NIL;            
          # is unsatisfiable under V 
    
    #  EASY CASES: PURE LITERAL ELIMINATION AND FORCED ASSIGNMENT 
    else if (there exists a literal L in S  % Pure literal elimination 
               such that the negation of L does not appear in S)
          then { V = obviousAssign(L,V);
                 delete every clause containing L from S;
               }

    else if (there exists a clause C in S       %  Forced assignment 
                containing a single literal L)
           then { V = obviousAssign(L,V)
                  S = propagate(atom(L), S, V);
                }

    else exitloop;  %  No easy cases found 
    }   %  end loop 


    #  HARD CASE: PICK SOME ATOM AND TRY EACH ASSIGNMENT IN TURN 
  pick atom A such that V[A] == UNBOUND;   %  Try one assignment 
  V[A] = TRUE;
  S1 = copy(S);
  S1 = propagate(A, S1, V);
  VNEW = dp1(ATOMS,S1,V);
  if (VNEW != NIL) then return(VNEW); % Found a satisfying valuation

%  If V[A] = TRUE didn't work, try V[A] = FALSE;
  V[A] = FALSE;
  S1 = propagate(A, S, V);
  return(dp1(ATOMS,S1,V)); % Either found a satisfying valuation or backtrack
} end dp1

% Propagate the effect of assigning atom A to be value V.
% Delete every clause where A appears with sign V
% Delete every literal where A appears with sign not V.
 
propagate(A,S,V) {
  for (each clause C in S)_ do
     if ((A in C and V[A]==TRUE) or (~A in C and V[A]==FALSE))
      then delete C from S
     else if (A in C and V[A]==FALSE) then delete A from C
     else if (~A in C and V[A]==TRUE) then delete ~A from C;
  return S;
}
end propagate.

% Given a literal L with atom A, make V[A] the sign indicated by L.

obviousAssign(L,V) {
  if (L is an atom A) then V[A] = TRUE;
  else if (L has the form ~A) then V[A] = FALSE;
}