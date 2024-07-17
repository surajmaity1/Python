
#                1
#               / \
#              2   3
#             / \  / \
#            4   5 6  7

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def new_node(value):
    return Node(value=value)


def create_binary_tree():
    root = new_node(1)
    root.left = new_node(2)
    root.right = new_node(3)
    root.left.left = new_node(4)
    root.left.right = new_node(5)
    root.right.left = new_node(6)
    root.right.right = new_node(7)
    return root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.value, end=' ')
        in_order(root.right)


def pre_order(root):
    if root:
        print(root.value, end=' ')
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end=' ')


def level_order(root):
    if root is None:
        return

    queue = [root]

    while len(queue) != 0:
        root = queue.pop(0)
        print(root.value, end=' ')
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


def level_order_reverse(root):
    if root is None:
        return

    stack = []
    queue = [root]

    while len(queue) != 0:
        pop = queue.pop(0)

        if pop.right:
            queue.append(pop.right)
        if pop.left:
            queue.append(pop.left)

        stack.append(pop)

    while len(stack) != 0:
        print(stack.pop().value, end=' ')


def main():
    root = create_binary_tree()
    print("In Order: ", end=' ')
    in_order(root)
    print("\nPre Order: ", end=' ')
    pre_order(root)
    print("\nPost Order: ", end=' ')
    post_order(root)
    print("\nLevel Order: ", end=' ')
    level_order(root)
    print("\nReverse Level Order: ", end=' ')
    level_order_reverse(root)


# main()
