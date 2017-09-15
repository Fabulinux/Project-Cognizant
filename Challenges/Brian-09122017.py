def reverse(tree, node, acc):
    # Store the tree to remove checked nodes
    tmp = btree

    # Extract the values from all the tree
    for child,parent in tree:
        # If root, skip
        if parent == None:
            continue

        # Remove the head and only check what's left
        tmp = tmp[1:]

        # If parent value is deired root node, recurse and check it's children
        if parent == node and child not in acc:
            acc.add(child)
            acc.union(reverse(tmp, child, acc))

    # Add the node if it's not already
    acc.add(p)
    return acc

tree = [('A', None), ('B', 'A'), ('C', 'A'), ('D', 'B'), ('E', 'B'), ('F', 'C'), ('G', 'E')]
if __name__ == "__main__":
    node = str(raw_input().strip())
    tree = raw_input()
    acc = set([])
    print list(reverse(tree, node, acc))
