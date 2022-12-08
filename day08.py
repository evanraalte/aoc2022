lines = open("day08.txt").read().split('\n')

columns = len(lines)
rows= len(lines[0])

height_grid = {
    (c,r): int(lines[r][c]) for c in range(columns) for r in range(rows) 
}

visible_grid = {
    (x,y): False for x in range(columns) for y in range(rows) 
}
# Scan left to right
highest_tree = {r: -1 for r in range(rows)}
for x in range(columns):

    for y in range(rows):
        if height_grid[(x,y)] > highest_tree[y]:
            visible_grid[(x,y)] = True
            highest_tree[y] = height_grid[(x,y)]

# Scan right to left
highest_tree = {r: -1 for r in range(rows)}
for x in range(columns-1,-1, -1):
    for y in range(rows):
        if height_grid[(x,y)] > highest_tree[y]:
            visible_grid[(x,y)] = True
            highest_tree[y] = height_grid[(x,y)]


# # Scan top to bottom
highest_tree = {c: -1 for c in range(columns)}
for y in range(rows):
    for x in range(columns):
        if height_grid[(x,y)] > highest_tree[x]:
            visible_grid[(x,y)] = True
            highest_tree[x] = height_grid[(x,y)]

# Scan bottom to top
highest_tree = {c: -1 for c in range(columns)}
for y in range(rows-1, -1, -1):
    for x in range(columns):
        if height_grid[(x,y)] > highest_tree[x]:
            visible_grid[(x,y)] = True
            highest_tree[x] = height_grid[(x,y)]

print(sum(1 for v in visible_grid.values() if v))


# Part B
scenic_score_grid = {
    (c,r): {"up": None, "down": None, "left": None, "right": None} for c in range(columns) for r in range(rows) 
}

def get_scenic_score(position):
    x,y = position
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    prod = 1
    for dir in dirs:
        dx,dy = dir
        xn,yn = x+dx, y+dy
        l = 1
        try:
            while  height_grid[(xn,yn)] < height_grid[(x,y)]:
                l +=1
                xn,yn = xn+dx, yn+dy
        except KeyError:
            l -= 1
        prod = prod*(l)
    return prod   

print(max(get_scenic_score((c,r)) for c in range(columns) for r in range(rows)))