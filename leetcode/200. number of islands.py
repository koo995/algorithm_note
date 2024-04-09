class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:        
        def find_island(point:tuple) -> int:
            y, x = point
            visited[y][x] = 1
            if grid[y][x] == "0":
                return 0
            for i in range(4):
                n_y, n_x = y + dy[i], x + dx[i]
                if 0 <= n_y <len(grid) and 0 <= n_x < len(grid[0]) and grid[n_y][n_x] == "1" and visited[n_y][n_x] == 0:
                    find_island((n_y, n_x))
            return 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 1: # 방문했다면 피한다
                    continue
                count += find_island((i, j))
        return count
    
    # 아래의 풀이가 훨씬 간결하네...
    def numIslands2(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >- len(grid[0]) or\
                    grid[i][j] != '1':
                        return
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
        
    
sol = Solution()
sol.numIslands([["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]])