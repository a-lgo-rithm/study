import sys

tree = dict()
for line in sys.stdin:
    if line.rstrip() in tree:
        tree[line.rstrip()] += 1
    else:
        tree[line.rstrip()] = 1

total = sum(tree.values())

for key in sorted(tree.keys()):
    print(key, '%.4f' % (tree[key] / total * 100))
