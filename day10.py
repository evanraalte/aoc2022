from collections import deque

class CPU:

    def __init__(self):
        self.x = 1
        self.pipeline = deque()
        self.crt = []
        self.crt_cnt = 0

    def decode(self, cmd):
        match cmd.split():
            case ["addx", num]:
                self.pipeline.appendleft("noop")
                self.pipeline.appendleft(cmd)
            case _:
                self.pipeline.appendleft("noop")
                pass
        
    def draw(self):
        if self.x -1 <= self.crt_cnt <= self.x + 1:
            self.crt.append('#')
        else:
            self.crt.append(' ')
        self.crt_cnt = (self.crt_cnt+1)%40
    def execute(self):
        cmd = self.pipeline.pop()
        match cmd.split():
            case ["addx", num]:
                self.x += int(num)
            case _:
                pass

signal_strengths = 0
program = deque(open("day10.txt").read().split("\n"))
cpu = CPU()
cycle = 0
while len(cpu.pipeline) or len(program):
    if len(program):
        cmd = program.popleft()
        cpu.decode(cmd)
    cpu.draw()
    if (cycle+1) in range(20,220+1,40): 
        signal_strengths += (cycle+1)*cpu.x
        # Part A
        if cycle+1 == 220:
            print(signal_strengths)
    cpu.execute()
    cycle +=1

# Part B
for row in range(0,6):
    print("".join(cpu.crt[row*40:row*40+40]))
pass