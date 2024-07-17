# Give an algorithm for deleting the tree
from binary_tree import create_binary_tree, level_order
from size_binary_tree import size_of_binary_tree


def delete_tree_recursion(root):
    if root is None:
        return

    # before deleting root, first delete both subtrees
    delete_tree_recursion(root.left)
    delete_tree_recursion(root.right)

    # delete current node only after deleting subtrees
    print(root.value, end=' ')
    root.left = None
    root.right = None
    del root


def delete_tree_iteration(root):
    if root is None:
        return

    queue = [root]
    while len(queue) != 0:
        root = queue.pop(0)

        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        print(root.value, end=' ')
        root.left = root.right = None
        del root


def main():
    root = create_binary_tree()
    print("print: ", end=' ')
    level_order(root)
    print()
    print("size: ", size_of_binary_tree(root))
    print("deleted nodes: ", end=' ')
    delete_tree_iteration(root)
    print()
    print("size: ", size_of_binary_tree(root))
    print("print: ", end=' ')
    level_order(root)


main()
