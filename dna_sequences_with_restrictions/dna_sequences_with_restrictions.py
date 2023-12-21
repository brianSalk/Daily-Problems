# A DNA sequence consists of a combination of 0 or more of each A,T,C, and G.
# each A,T,C, or G represents a nucleotide
# Given that we know the following about a newly discovered species:
# -- there cannot be more than three adjacent A's in a single gene
# -- there must be at least one G
# -- there must be at least two T's
# how many genes of length 7 nucleotides can there be in this species?
from itertools import combinations_with_replacement, permutations

if __name__ == "__main__":
    ans = set()
    every = set()
    for comb in combinations_with_replacement(("A", "T", "C", "G"), 7):
        for perm in permutations(comb):
            perm = "".join(perm)
            if ("G" in perm and perm.count("T") > 1) and "AAAA" not in perm:
                ans.add(perm)
            every.add(perm)
    print(ans)
    print(len(ans))
