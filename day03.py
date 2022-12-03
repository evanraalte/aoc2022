
def get_score(char):
    if char.islower():
        prio=ord(char) - ord('a') + 1
    else:
        prio=ord(char) - ord('A') + 27
    return prio

rucksacks = open("day03.txt").read().split('\n')
priorities = 0
for rucksack in rucksacks:
    p1 = rucksack[:len(rucksack)//2]
    p2 = rucksack[len(rucksack)//2:]
    set(p1).intersection(set(p2))
    char = set(p1).intersection(set(p2)).pop()
    priorities += get_score(char)
print(priorities)
priorities=0
for i in range(0, len(rucksacks),3):
    p0 = set(rucksacks[i])
    p1 = set(rucksacks[i+1])
    p2 = set(rucksacks[i+2])
    char = p0.intersection(p1).intersection(p2).pop()
    priorities += get_score(char)
print(priorities)