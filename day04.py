def set_from_range(range_str):
    mini, maxi = range_str.split("-")
    return set(range(int(mini), int(maxi)+1))

pairs = open("day04.txt").read().split('\n')
duplicates_parta = 0
duplicates_partb = 0
for pair in pairs:
    elf1, elf2 = tuple(map(set_from_range, pair.split(",")))
    if (elf1 & elf2 ) in [elf1, elf2]:
        duplicates_parta += 1

    if (elf1 & elf2):
        duplicates_partb += 1
        
print(duplicates_parta)
print(duplicates_partb)