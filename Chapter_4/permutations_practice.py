"""For a total number of columns, find all unique column arrangements.

Builds a list of lists containing all possible unique arrangements of
individual column numbers including negative values for route direction
(read up column vs. down).

Input:
-total number of columns

Returns:
-list of lists of unique column orders including negative values for
route cipher encryption direction

"""

import math
from itertools import permutations, product

#------BEGIN INPUT-----------------------------------------------------------

# Input total number of columns:
num_cols = 4

#------DO NOT EDIT BELOW THIS LINE--------------------------------------------




# generate listing of individual column numbers
columns = list(range(1, num_cols+1))
print(f"columns = {columns}")

# build list of lists of column number combinations
# itertools product computes the cartesian product of input iterables 
def perms(columns):
    """Take number of columns integer & generate pos & neg permutations."""
    results = []
    for perm in permutations(columns):
        results.extend(
            [i * sign for i, sign in zip(perm, signs)]
            for signs in product([-1, 1], repeat=len(columns))
        )
    return results

col_combos = perms(columns)
print(*col_combos, sep="\n")  # comment-out for num_cols > 4!
print(f"Factorial of num_cols without negatives = {math.factorial(num_cols)}")
print(f"Number of column combinations = {len(col_combos)}")
