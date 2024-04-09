#floodfill
'''
def floodFill(image, sr, sc, color):
  if not image:
    return []
  rows, cols = len(image), len(image[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
  org_col = image[sr][sc]
  image[sr][sc] = color
  def traverse(i, j):
    if (i, j) in visited:
      return
    visited.add((i, j))
    # Traverse neighbors.
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols:
        val = image[next_i][next_j]
        #if val != org_col and val != color:
        if val == org_col:
          image[next_i][next_j] = color
          traverse(next_i, next_j)

  traverse(sr, sc)
  return image
print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
print(floodFill([[0,0,0],[0,0,0]],0,0,0))

def dfs(matrix):
  # Check for an empty matrix/graph.
  if not matrix:
    return []
  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
  def traverse(i, j):
    if (i, j) in visited:
      return
    visited.add((i, j))
    # Traverse neighbors.
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols:
        # Add in question-specific checks, where relevant.
        traverse(next_i, next_j)
  for i in range(rows):
    for j in range(cols):
      traverse(i, j)

def graph_topo_sort(num_nodes, edges):
  from collections import deque
  nodes, order, queue = {}, [], deque()
  for node_id in range(num_nodes):
    nodes[node_id] = {'in': 0, 'out': set()}
  #print(nodes)
  #{0: {'in': 0, 'out': set()}, 1: {'in': 0, 'out': set()}, 2: {'in': 0, 'out': set()}, 3: {'in': 0, 'out': set()}}
  for node_id, pre_id in edges:
    nodes[node_id]['in'] += 1
    nodes[pre_id]['out'].add(node_id)
  #print(nodes)
  #{0: {'in': 2, 'out': {3}}, 1: {'in': 0, 'out': {0, 2}}, 2: {'in': 1, 'out': {0}}, 3: {'in': 1, 'out': set()}}
  for node_id in nodes.keys():
    if nodes[node_id]['in'] == 0:
      queue.append(node_id)
  print(queue)
  ##deque([1])
  while len(queue):
    node_id = queue.pop()
    for outgoing_id in nodes[node_id]['out']:
      nodes[outgoing_id]['in'] -= 1
      if nodes[outgoing_id]['in'] == 0:
        queue.append(outgoing_id)
    order.append(node_id)
  return order if len(order) == num_nodes else None


#print(graph_topo_sort(4, [[0, 1], [0, 2], [2, 1], [3, 0]]))
def canFinish(num_nodes: int, edges) -> bool:
  from collections import deque
  nodes, order, queue = {}, [], deque()
  for node_id in range(num_nodes):
    nodes[node_id] = {'in': 0, 'out': set()}
  for node_id, pre_id in edges:
    nodes[node_id]['in'] += 1
    nodes[pre_id]['out'].add(node_id)
  for node_id in nodes.keys():
    if nodes[node_id]['in'] == 0:
      queue.append(node_id)
  while len(queue):
    node_id = queue.pop()
    for outgoing_id in nodes[node_id]['out']:
      nodes[outgoing_id]['in'] -= 1
      if nodes[outgoing_id]['in'] == 0:
        queue.append(outgoing_id)
    order.append(node_id)
  return True if len(order) == num_nodes else False
print(canFinish(2,[[1,0]]))
print(canFinish(2,[[1,0],[0,1]]))

from collections import deque

def bfs(matrix):
  # Check for an empty matrix/graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

  def traverse(i, j):
    queue = deque([(i, j)])
    while queue:
      curr_i, curr_j = queue.popleft()
      if (curr_i, curr_j) not in visited:
        visited.add((curr_i, curr_j))
        # Traverse neighbors.
        for direction in directions:
          next_i, next_j = curr_i + direction[0], curr_j + direction[1]
          if 0 <= next_i < rows and 0 <= next_j < cols:
            # Add in question-specific checks, where relevant.
            queue.append((next_i, next_j))

  for i in range(rows):
    for j in range(cols):
      traverse(i, j)

# just copied clones
class Node:
  def __init__(self, val=0, neighbors=None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []
def cloneGraph(node):
  if node is None:
    return node
  queue = deque([node])
  clones = {node.val: Node(node.val)}
  while queue:
    curr = queue.popleft()
    curr_clone = clones[curr.val]
    for neigh in curr.neighbors:
      if neigh.val not in clones:
        clones[neigh.val] = Node(neigh.val)
        queue.append(neigh)
      curr_clone.neighbors.append(clones[neigh.val])
  return clones[node.val]

from heapq import heappush, heappop
from math import inf
while True:
    n, m, q,s = map(int, input().split())
    if n + m + q + s == 0:
        break
    AL = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int,input().split())
        AL[u].append((v,w))
    dist = [inf] * n
    dist[s] = 0

    pq = [(0,s)]

    while pq:
        d, u = heappop(pq)
        if d > dist[u]: continue
        for v, w in AL[u]:
            if dist[u] + w >= dist[v]: continue
            dist[v] = dist[u] + w
            heappush(pq, (dist[v],v))
    for _ in range(q):
        t = int(input())
        print("Impossible" if dist[t] == inf else dist[t])
    print()


def updateMatrix(mat) :
  q = deque()
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j] == 0:
        q.append((i, j))
      else:
        mat[i][j] = -1
  while q:
    x, y = q.popleft()
    for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nx, ny = x + r, y + c
      if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and mat[nx][ny] == -1:
        mat[nx][ny] = mat[x][y] + 1
        q.append((nx, ny))
  return mat


def orangesRotting(self, grid):
  n, m = len(grid), len(grid[0])
  Q = deque([])
  cnt = 0
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1: cnt += 1
      if grid[i][j] == 2: Q.append((i, j))
  res = 0
  while Q:
    for _ in range(len(Q)):
      i, j = Q.popleft()
      for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
          grid[x][y] = 2
          cnt -= 1
          Q.append((x, y))
    res += 1
  return max(0, res - 1) if cnt == 0 else -1

#Number of Islands - dfs solution

def numIslands(grid):
  if not grid:
    return 0
  rows, cols = len(grid), len(grid[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
  count = 0
  def traverse(i,j):
    for d in directions:
      ni, nj = i + d[0] , j + d[1]
      if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '1' and (ni, nj) not in visited:
        visited.add((ni,nj))
        traverse(ni, nj)
  for x in range(rows):
    for y in range(cols):
      if grid[x][y] == '1' and (x,y) not in visited:
        count += 1
        visited.add((x,y))
        traverse(x,y)
  return count
'''


from collections import deque

def numIslands(grid):
  # Check for an empty matrix/graph.
  if not grid: return 0
  rows, cols = len(grid), len(grid[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
  count = 0

  def traverse(i, j):
    queue = deque([(i, j)])
    while queue:
      curr_i, curr_j = queue.popleft()
      if (curr_i, curr_j) not in visited:
        # Traverse neighbors.
        for direction in directions:
          next_i, next_j = curr_i + direction[0], curr_j + direction[1]
          if 0 <= next_i < rows and 0 <= next_j < cols and grid[next_i][ next_j]=='1' and ( next_i, next_j) not in visited:
            # Add in question-specific checks, where relevant.
            visited.add((next_i, next_j))
            queue.append((next_i, next_j))

  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == '1' and (i, j) not in visited:
        count += 1
        visited.add((i, j))
        traverse(i, j)
  return count

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
