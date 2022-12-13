from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None

lines = open("day12.txt").read().split('\n')

dirs = [(-1,0), (1,0), (0,-1), (0,1)]
grid = {}
start= None
end = None
for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char == 'S':
            start = (x,y)
            height = 1
        elif char == 'E':
            end = (x,y)
            height = 26
        else:
            height = ord(char) - ord('a') + 1
        grid[(x,y)] = height
pass

# graph = {}
edges = []
for location in grid:
    # graph[location]= set()
    x,y = location
    for dir in dirs:
        dx, dy = dir
        neighbour = x+dx, y+dy
        if neighbour not in grid:
            pass # outside of grid, can skip
        elif grid[neighbour] - 1 <= grid[location]:
            # graph[location].add(neighbour)
            edges.append((location, neighbour, 1))





print(dijkstra(edges, start, end)[0])
locs = [dijkstra(edges,start_loc,end)[0] for start_loc, height in grid.items() if height == 1]
print(min(locs))
pass