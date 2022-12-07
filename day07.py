lines = [x.split() for x in open("day07.txt").read().split('\n')]
path = []
sizes = {}
for line in lines:
    if line[0] == '$':
        if line[1] == "cd":
            if line[2] == "..":
                path.pop()
            else:
                path.append(line[2])
    else:
        if line[0] != "dir":
            print(f"Found {line[1]} with size {line[0]} at {path}")
            # add size to every sub path
            for i in range(len(path)):
                p = "".join(path[0:i+1])
                if p not in sizes:
                    sizes[p] = 0
                sizes[p] += int(line[0])

free_space = 70_000_000 - sizes['/']
space_extra_needed = 30_000_000 - free_space
print(sum(s for s in sizes.values() if s < 100000))
print(next(s for s in sorted(sizes.values()) if s >= space_extra_needed))