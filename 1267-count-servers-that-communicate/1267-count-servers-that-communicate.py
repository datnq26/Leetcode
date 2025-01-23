from collections import deque

class Solution(object):
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])
        directions = list()
        for i in range(n):
            directions.append((0, i + 1))
            directions.append((0, -i - 1))
        
        for i in range(m):
            directions.append((i + 1, 0))
            directions.append((-i - 1, 0))
            
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        sum = 0
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    sum += 1
                    break
        return sum
    