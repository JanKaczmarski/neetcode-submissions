from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # perimiter is the number of edges connected to water or
        # the bourder of grid
        res = 0
        q = deque()
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            found = False
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                    found = True
                    break
            if found:
                break

        while q:
            i, j = q.popleft()
            if visited[i][j]:
                continue
            visited[i][j] = True
            print(i, j, res)
            # border with water
            if i - 1 >= 0 and grid[i - 1][j] == 0:
                res += 1
            if i + 1 < n and grid[i + 1][j] == 0:
                res += 1
            if j - 1 >= 0 and grid[i][j - 1] == 0:
                res += 1
            if j + 1 < m and grid[i][j + 1] == 0:
                res += 1
            # border of grid
            if i - 1 < 0:
                res += 1
            if i + 1 >= n:
                res += 1
            if j - 1 < 0:
                res += 1
            if j + 1 >= m:
                res += 1

            # add neigh island
            if i - 1 >= 0 and grid[i - 1][j] == 1 and not visited[i - 1][j]:
                q.append((i - 1, j))
            if i + 1 < n and grid[i + 1][j] == 1 and not visited[i + 1][j]:
                q.append((i + 1, j))
            if j - 1 >= 0 and grid[i][j - 1] == 1 and not visited[i][j - 1]:
                q.append((i, j - 1))
            if j + 1 < m and grid[i][j + 1] == 1 and not visited[i][j + 1]:
                q.append((i, j + 1))

            #print(i, j, res)

        return res
