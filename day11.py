from dataclasses import dataclass
from typing import Callable
import re
m = re.compile(r"Monkey (\d+):\n  Starting items: (.+)\n  Operation: new = (.+)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)", re.MULTILINE)

N = 1

@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], int]
    inspected_items: int = 0

def parse_monkey(data):
    global N
    groups = m.match(data).groups()
    num = int(groups[0])
    items = [int(x) for x in groups[1].split(", ")]
    operation = lambda old: eval(groups[2])
    test = lambda num: int(groups[4]) if num % int(groups[3]) == 0 else int(groups[5])
    N *= int(groups[3])
    return {num:  Monkey(items, operation, test)}

monkeys = {}
for desc in open("day11.txt").read().split("\n\n"):
    monkeys |= parse_monkey(desc)

ROUNDS = 10000

for round in range(1,ROUNDS+1):
    for num, monkey in monkeys.items():
        for item in monkey.items:
            monkey.inspected_items += 1
            worry_level = monkey.operation(item)
            # worry_level = worry_level // 3 PARTA
            worry_level %=N # PARTB
            monkeys[monkey.test(worry_level)].items.append(worry_level)
        monkey.items.clear()

    if round == ROUNDS:
        print(f"Round {round}")
        for num, monkey in monkeys.items():
            print(f"{num} {monkey.inspected_items}")


count = [m.inspected_items for m in monkeys.values()]
count = list(reversed(sorted(count)))
print(count[0] * count[1])