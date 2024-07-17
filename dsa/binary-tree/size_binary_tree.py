# Give an algorithm for finding the size of binary tree.

from binary_tree import create_binary_tree
from insert_item_binary_tree import insert_node


# size of binary tree using recursion
def size_of_binary_tree_recursion(root):
    if root is None:
        return 0
    return (size_of_binary_tree_recursion(root.left) +
            1 + size_of_binary_tree_recursion(root.right))


# size of binary tree using level order
def size_of_binary_tree(root):
    size = 0

    if root is None:
        return size

    queue = [root]

    while len(queue) != 0:
        root = queue.pop(0)
        size = size + 1
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return size


def main():
    root = create_binary_tree()
    insert_node(root, 8)
    insert_node(root, 9)
    insert_node(root, 10)
    print(size_of_binary_tree(root=root))
    print(size_of_binary_tree_recursion(root=root))


# main()
