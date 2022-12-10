dirs = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1),
}
h = (0,0)
t = (0,0)
locs = set()
locs.add(t)


for dir, distance in map(str.split,open("day09.txt").read().split('\n')):
    x,y = dirs[dir]
    print(f"{dir} {distance}")
    for _ in range(int(distance)):
        # Move H
        hx, hy = h
        h = (hx+x, hy+y)
        print(f"move H from {(hx,hy)} to {h}")
        tx, ty = t
        hx, hy = h
        # Get distance
        dx = hx-tx
        dy = hy-ty
        if abs(dx) == 2 and dy ==0: # X movement
            tx += 1 if dx > 0 else -1
        elif abs(dy) == 2 and dx==0: # Y movement
            ty += 1 if dy > 0 else -1    
        elif abs(dx) <= 1 and abs(dy) <= 1:
            pass # No need to move
        else: # diagonal move
            if abs(dx) == 1 and abs(dy) == 2:
                tx += dx
                ty += 1 if dy > 0 else -1
            elif abs(dx) == 2 and abs(dy) == 1:
                ty += dy
                tx +=1 if dx > 0 else -1
            else:
                raise Exception("Shouldn't get here")
        print(f"move T from {t} to {(tx,ty)}")
        # Move T
        t = tx, ty
        # Add 
        locs.add(t)
        
print(len(locs))





