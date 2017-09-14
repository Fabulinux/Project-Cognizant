def reverse(btree, p, acc):
    tmp = btree
    for child,parent in btree:
        if parent == None:
            continue
        tmp = tmp[1:]
        if parent == p and child not in acc:
            acc.add(child)
            acc.union(reverse(tmp, child, acc))

    acc.add(p)
    return acc

tree = [('A', None), ('B', 'A'), ('C', 'A'), ('D', 'B'), ('E', 'B'), ('F', 'C'), ('G', 'E')]

acc = set([])
print list(reverse(tree, 'A', acc))
