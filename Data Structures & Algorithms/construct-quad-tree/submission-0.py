"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c) -> 'Node':
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break

            if allSame:
                return Node(grid[r][c] == 1, True)

            half = n // 2
            topleft = dfs(half, r, c)
            topright = dfs(half, r, c + half)
            bottomleft = dfs(half, r + half, c)
            bottomright = dfs(half, r + half, c + half)

            return Node(False, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)
