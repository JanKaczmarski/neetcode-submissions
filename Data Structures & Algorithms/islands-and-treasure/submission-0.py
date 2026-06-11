INF = 2147483647
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start BFS at each treasure chest - keep the distance from land
        # cell to closets chest and update if better distance is reached
        # TIME: O(k*N), k number of chests and N number of land tiles
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                
                q = deque()
                q.append((1, i+1, j))
                q.append((1, i-1, j))
                q.append((1, i, j+1))
                q.append((1, i, j-1))

                while q:
                    dist, x, y = q.popleft()
                    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == -1:
                        continue
                    
                    # better path already exists
                    if grid[x][y] <= dist:
                        continue

                    grid[x][y] = dist
                    q.append((dist + 1, x + 1, y))
                    q.append((dist + 1, x - 1, y))
                    q.append((dist + 1, x, y + 1))
                    q.append((dist + 1, x, y - 1))

        
                    
