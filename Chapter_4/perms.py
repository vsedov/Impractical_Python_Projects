"""For a total number of columns, find all unique column arrangements.

Builds a list of lists containing all possible unique arrangements of
individual column numbers including negative values for route direction

Input:
-total number of columns

Returns:
-list of lists of unique column orders including negative values for
route cipher encryption direction

"""
from itertools import permutations, product

# build list of lists of column number combinations
# itertools product computes the cartesian product of input iterables 
def perms(num_cols):
    """Take number of columns integer & generate pos & neg permutations."""
    results = []
    columns = list(range(1, num_cols+1))
    for perm in permutations(columns):
        results.extend(
            [i * sign for i, sign in zip(perm, signs)]
            for signs in product([-1, 1], repeat=len(columns))
        )
    return results
