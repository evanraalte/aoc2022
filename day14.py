formations = map(lambda x: x.split(" -> "), open("day14.txt").read().split('\n'))
grid = set()
lowest_y = 0
for formation in formations:
    prev_point = None
    for point in formation:
        x,y = tuple(map(int, point.split(",")))
        grid.add((x,y))
        if prev_point:
            px,py = prev_point
            if px == x: # vertical line
                for ty in range(y,py, 1 if y < py else -1):
                    grid.add((x,ty))
            else: # horizontal line
                for tx in range(x,px, 1 if x < px else -1):
                    grid.add((tx,y))
        prev_point = (x,y)
        lowest_y = max(y, lowest_y)


def drop_sand(grid, partb=False):
    grid = grid.copy()
    last_sand_came_to_rest = True
    units_fallen = 0
    full = False
    while last_sand_came_to_rest:
        sx, sy = (500,0)
        last_sand_came_to_rest = False
        drop = False
        while sy < lowest_y+2:
            if partb and sy == lowest_y + 1: # on the bottom
                drop = True
            elif (sx,sy + 1) not in grid:
                sy = sy +1
            elif (sx -1, sy + 1) not in grid:
                sx = sx - 1
                sy = sy + 1
            elif (sx +1, sy + 1) not in grid:
                sx = sx + 1
                sy = sy + 1
            else:
                drop = True
            if drop:
                if (sx,sy) in grid:
                    last_sand_came_to_rest = False
                    break
                units_fallen +=1
                # print(f"{units_fallen} {(sx,sy)}")
                grid.add((sx, sy))
                last_sand_came_to_rest = True  
                break   
    return units_fallen 
print(drop_sand(grid))
print(drop_sand(grid,partb=True))
