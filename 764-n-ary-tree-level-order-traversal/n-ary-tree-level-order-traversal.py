"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, level, data):
            if root == None:
                return
            if len(data) <= level:
                data.append([])
            data[level].append(root.val)
            level+=1
            for child in root.children:
                dfs(child, level, data)

            return data

        
        return dfs(root, 0, [])
