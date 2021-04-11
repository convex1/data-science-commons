"""

BINARY TREE IS ONE OF THE COMMON DATA STRUCTURES

Binary tree has two possible childs for each node (parent node)

                  root node
                    /    \
                   /      \
        child node 1      child node 2
          /  \
        /     \
child node 1  child node 2


There are two traversal operations - breadth first search and depth first search

breadth first traversal - we go by each level of the tree - horizontally first for each level
depth first traversal - we go by each depth i.e. going vertically down to the bottom from the node first,
then going on the next horizontal node.


"""



from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque([root])
    while len(queue) != 0:
        len_queue = len(queue)
        for node in list(queue):
            if node.left != None:
                queue.append(node.left)

            if node.right != None:
                queue.append(node.right)
        temp_list = deque()
        # add to result and remove visited nodes
        i = 0
        counter = 0

        while counter < len_queue:
            temp_list.append(queue[i].val)
            queue.popleft()
            counter += 1

        result.append(list(temp_list))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Traverse binary tree by level", traverse(root))


main()
