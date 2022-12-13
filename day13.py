from enum import Enum
import functools
sets = open("day13.txt").read().split("\n\n")

# class Verdict(Enum):
RIGHT_ORDER = -1
WRONG_ORDER = 1
CONTINUE = 0


def compare(left, right) -> int:
    if type(left) == list and type(right) == list:
        fallback_order = compare(len(left), len(right))
        for i in range(min(len(left), len(right))):
            order = compare(left[i], right[i])
            if order != CONTINUE:
                return order
        return fallback_order
    elif type(left) == int and type(right) == int:
        if left < right:
            return RIGHT_ORDER
        elif left == right:
            return CONTINUE
        else:
            return WRONG_ORDER
    else: # One must be an integer
        if type(left) == int:
            left = [left]
        else:
            right = [right]
        return compare(left, right)

total = 0
for idx, set in enumerate(sets):
    left, right = tuple(map(eval,set.split("\n")))
    if compare(left,right) == RIGHT_ORDER:
        total += idx + 1
print(total)


total = 0
packets = []
packets.append([[2]])
packets.append([[6]])
for idx, set in enumerate(sets):
    left, right = tuple(map(eval,set.split("\n")))
    packets.append(left)
    packets.append(right)
packets.sort(key=functools.cmp_to_key(compare))

index1 = packets.index([[6]]) + 1
index2 = packets.index([[2]]) + 1
print(index1*index2)