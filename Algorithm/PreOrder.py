def PreOrder(tree):
    if tree:
        print(tree.getRootVal())
        PreOrder(tree.getLeftChild())
        PreOrder(tree.getRightChild())
