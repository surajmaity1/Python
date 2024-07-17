# algorithm for searching an element in binary tree.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def new_node(data):
    return Node(data)


def create_binary_tree():
    root = new_node(1)
    root.left = new_node(2)
    root.right = new_node(3)
    root.left.left = new_node(4)
    root.left.right = new_node(5)
    root.right.left = new_node(6)
    root.right.right = new_node(7)
    return root


def search_recursion(root, data):
    if root:
        if root.data == data:
            return True
        # otherwise recurse down
        left_found = search_recursion(root.left, data)

        if left_found is True:
            return True

        return search_recursion(root.right, data)
    else:
        return False


def search_iteration(root, data):
    if root is None:
        return False

    queue = [root]

    while len(queue) != 0:
        root = queue.pop(0)

        if data == root.data:
            return True

        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

    return False


def main():
    root = create_binary_tree()
    for item in range(1, 10):
        print("search_recursion: ", item, " ", search_recursion(root, item), end= ' ')
        print("search_iteration: ", item, " ", search_iteration(root, item))


main()
