def set_from_range_str(range_str):
    mini, maxi = tuple(map(int, range_str.split("-")))
    return set(range(mini, maxi+1))

pairs = open("day04.txt").read().split('\n')
duplicates_parta = 0
duplicates_partb = 0
for pair in pairs:
    elf1, elf2 = tuple(map(set_from_range_str, pair.split(",")))
    if elf1 <= elf2 or elf2 <= elf1:
        duplicates_parta += 1
    if (elf1 & elf2):
        duplicates_partb += 1
        
print(duplicates_parta)
print(duplicates_partb)