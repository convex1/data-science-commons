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

deoth first traversal (BFS) - we go depth of the tree - vertically first for each level
depth first traversal (DFS) - we go by each depth i.e. going vertically down to the bottom from the node first,
then going on the next horizontal node.

HERE we introdue the code for DFS.

Complexity - O(N) - since it traverses across all nodes

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

#In this example - we try to find the longest depth of the tree i.e. longest distance from root (top)
#to a leaf node (bottom)
def find_longest_path(root):

    def dfs(node, temp_len):

        temp_len += 1

        if node.left == None and node.right == None:
            if temp_len > max_len:
                max_len = temp_len
            return max_len

        if node.left != None:
            left = dfs(node.left, temp_len)
        else:
            left = 0

        if node.right != None:
            dfs(node.right, temp_len)
        else:
            right = 0

        return max(left, right)

    return dfs(root, 0)


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
