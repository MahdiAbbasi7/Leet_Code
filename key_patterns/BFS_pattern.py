"""
Explore nodes level by level in a tree.

Use Case: Level-order traversal.
Example: Traverse a binary tree level by level.

"""

from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root):
    result = []
    queue = deque()

    if root is not None:
        queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(current_level)
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = bfs(root)
print(result)


class TreeNode2:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

    traverse(root)
    return result


root = TreeNode2(1)
root.left = TreeNode2(2)
root.right = TreeNode2(3)
print(inorder_traversal(root))
