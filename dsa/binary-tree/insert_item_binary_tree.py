# Give an algorithm for inserting an element into binary tree.
from binary_tree import new_node, level_order, create_binary_tree


def insert_node(root, data):
    head = root

    if root is None:
        head = new_node(data)
        return head

    queue = [root]

    while len(queue) != 0:
        root = queue.pop(0)

        if root.left:
            queue.append(root.left)
        else:
            root.left = new_node(data)
            break

        if root.right:
            queue.append(root.right)
        else:
            root.right = new_node(data)
            break

    # clear all elements from queue
    queue.clear()
    return head


def main():
    root = create_binary_tree()
    print("Before insertion, Nodes: ", end=' ')
    level_order(root)

    print("\nAfter insertion, Nodes: ", end=' ')
    insert_node(root, 8)
    insert_node(root, 9)
    insert_node(root, 10)
    level_order(root)

    print("\nAnother tree: ", end=' ')
    head = insert_node(root=None, data=1)
    insert_node(head, 2)
    insert_node(head, 3)
    level_order(head)


# main()
