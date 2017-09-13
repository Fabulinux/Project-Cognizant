def reverse(btree, p, acc):
    for child,parent in btree:
        if parent == p and p not in acc:
            acc += child
            return reverse(btree, child, acc)

    if p not in acc:
        return acc.append(p)
    else:
        return acc

print reverse(tree, 'B', [])
