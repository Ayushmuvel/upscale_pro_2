class Node:
    # create node class 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def chek_down(root, k):

    if root is None or k < 0:
        return

    # If we reach a k distant node, print it
    if k == 0:
        print(root.value)
        return

    # Recur for left and right subtee
    chek_down(root.left, k - 1)
    chek_down(root.right, k - 1)

def fin_node(root, target, k):
    # when branch end reach
    if root is None:
        return -1

    if root.value == target:
        # find all the node at k distance
        chek_down(root, k)
        return 0

    # Recur for left subtree
    res = fin_node(root.left, target, k)


    if res != -1:
        #target root not found
        if res + 1 == k:
            print(root.value)
        else:
            # check right side of node
            chek_down(root.right, k - res - 2)

        return 1 + res

    # rood not fount in left tree
    dr = fin_node(root.right, target, k)
    if dr != -1:
        if dr + 1 == k:
            print(root.value)
        else:
            chek_down(root.left, k - dr - 2)
        return 1 + dr
    # target not found
    return -1
if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    target = 12
    k = 2
    fin_node(root, target, k)
