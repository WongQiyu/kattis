dr = [0, 1, 1, 1, 0, -1, -1, -1]  # E/SE/S/SW/W/NW/N/NE
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def dfs(r, c):
    grid[r][c] = '.' #convert cell (r,c) which is a '#' unvisited to '.' so you wont visit again
    for d in range(8): #try up to 8 neighbors
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= m or nc < 0 or nc >= n: continue #outside the grid dont crash
        if grid[nr][nc] != '#': continue # not another black skip
        dfs(nr, nc) # only 2 black neighbors of (r,c) will be found


m, n = map(int, input().split())
grid = [list(input()) for _ in range(m)]
numCC = 0
for row in range(m):
    for col in range(n):
        if grid[row][col] == '#':
            numCC += 1
            dfs(row, col)
print(numCC)