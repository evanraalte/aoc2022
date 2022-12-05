import re
import copy

def parse_input():
    init, program = open("day05.txt").read().split("\n\n")
    init = init.split('\n')
    program = program.split('\n')

    state = {}
    for idx, val in enumerate(init[-1]):
        if val !=' ':
            state[val] = []
            for row in reversed(init[:-1]):
                if row[idx] != ' ':
                    state[val].append(row[idx])
            pass
    return state, program

def parta(init_state, program):
    state = copy.deepcopy(init_state)
    m = re.compile(r"move (\d+) from (\d+) to (\d+)")
    for command in program:
        amount, fr, to = m.match(command).groups()
        for _ in range(int(amount)):
            state[to].append(state[fr].pop())
    return "".join(l[-1] for l in state.values())

def partb(init_state, program):
    state = copy.deepcopy(init_state)
    m = re.compile(r"move (\d+) from (\d+) to (\d+)")
    for command in program:
        amount, fr, to = m.match(command).groups()
        buf = []
        for _ in range(int(amount)):
            buf.append(state[fr].pop())
        state[to] += reversed(buf)
    return "".join(l[-1] for l in state.values())

state, program = parse_input()
print(parta(state, program))
print(partb(state, program))

