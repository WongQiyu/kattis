



dr = (1, 1, 0,-1,-1,-1, 0, 1)
dc = (0, 1, 1, 1, 0,-1,-1,-1)
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
cc = 0

def dfs(r, c):
  grid[r][c] = '.'
  for d in range(8):
    nr, nc = r + dr[d], c + dc[d]
    if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
    if grid[nr][nc] != '#': continue
    dfs(nr,nc)
for row in range(R):
  for col in range(C):
    if grid[row][col] == '#':
      cc+= 1
      dfs(row,col)
print(cc)


