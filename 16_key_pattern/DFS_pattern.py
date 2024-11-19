"""
Explore as deep as possible along a branch before backtracking.

Use Case: Searching in trees or graphs.
Example: Finding all root-to-leaf paths.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, path, result):
    if node is None:
        return

    path.append(node.val)

    if node.left is None and node.right is None:
        result.append(list(path))

    dfs(node.left, path, result)
    dfs(node.right, path, result)

    path.pop()


def find_paths(root):
    result = []
    dfs(root, [], result)
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = find_paths(root)
print(result)
