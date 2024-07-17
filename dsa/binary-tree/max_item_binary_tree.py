# Give an algorithm for finding maximum element in binary tree.

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


def max_item_level_order(root):
    if root is None:
        return

    queue = [root]
    result = root.value

    while len(queue) != 0:
        root = queue.pop(0)

        if root.value > result:
            result = root.value

        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

    return result


def main():
    root = create_binary_tree()

    if root is None:
        return

    # one way to get max
    # result = max_item_level_order(root)
    # print(result)

    # other way to get max, find max from left and right subtree
    # then compare max between 3 val (root, left, right)
    root_value = root.value
    left_max = max_item_level_order(root.left)
    right_max = max_item_level_order(root.right)

    if left_max > right_max and left_max > root_value:
        print(left_max)
    elif right_max > root_value:
        print(right_max)
    else:
        print(root_value)


main()
