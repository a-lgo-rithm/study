import sys

treeCounts = {}

for tree in sys.stdin:
    if tree == '\n':
        break
    
    if tree.rstrip() in treeCounts:
        treeCounts[tree.rstrip()] += 1
    else:
        treeCounts[tree.rstrip()] = 1


treeSpecies = sorted(treeCounts.keys())
total = sum(treeCounts.values())

for tree in treeSpecies:
    percentage = treeCounts[tree] / total * 100
    print(f'{tree} {percentage:.4f}')
