dirs = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1),
}
h = (0,0)
t = (0,0)

NUM_KNOTS = 10
# knots = [(0,0)]*NUM_KNOTS
knots = {n: (0,0) for n in range(NUM_KNOTS)}
locs = set()
locs.add(t)


def move_t(h,t):
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
        ty += 1 if dy > 0 else -1
        tx +=1 if dx > 0 else -1
    return tx, ty


for dir, distance in map(str.split,open("day09.txt").read().split('\n')):
    x,y = dirs[dir]
    # print(f"{dir} {distance}")
    for _ in range(int(distance)):
        hx, hy = knots[0] # move 'real' head in the set direction
        # print(f"move H from {knots[0]} to {(hx+x, hy+y)}")
        knots[0] = (hx+x, hy+y)

        for knot_idx in range(1, NUM_KNOTS): # Let the other knots follow
            h = knots[knot_idx-1]
            t = knots[knot_idx]
            # print(f"move T from {t} to {move_t(h,t)}")
            t = move_t(h,t)
            knots[knot_idx] = t
            if knot_idx == NUM_KNOTS - 1:
                locs.add(t) # Add end of robe to locs
        pass
        
print(len(locs))





