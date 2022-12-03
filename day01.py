import heapq
data = [sum(int(d) for d in elf.split()) for elf in open("day01.txt").read().split("\n\n")]
part1 = heapq.nlargest(1,data)
part2 = sum(heapq.nlargest(3,data))
print(part1)
print(part2)
pass