dirs = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1),
}

def calc_next_pos(h,t):
    tx, ty = t
    hx, hy = h
    # Get distance
    dx = hx-tx
    dy = hy-ty
    if abs(dx) <= 1 and abs(dy) <= 1:
        return t# No need to move
    tx += (dx > 0) - (dx < 0)
    ty += (dy > 0) - (dy < 0)
    return tx, ty

def get_coverage_of_tail(num_knots):
    knots = {n: (0,0) for n in range(num_knots)}
    locs = set([(0,0)])
    for dir, distance in map(str.split,open("day09.txt").read().split('\n')):
        x,y = dirs[dir]
        for _ in range(int(distance)):
            hx, hy = knots[0] # move 'real' head in the set direction
            knots[0] = (hx+x, hy+y)

            for knot_idx in range(1, num_knots): # Let the other knots follow
                h = knots[knot_idx-1]
                t = knots[knot_idx]

                t = calc_next_pos(h,t)
                knots[knot_idx] = t
                if knot_idx == num_knots - 1:
                    locs.add(t) # Add end of robe to locs
            pass

    return len(locs)

print(get_coverage_of_tail(2))
print(get_coverage_of_tail(10))




