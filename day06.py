# bvwbj
import collections

def find_unique_sequence(seq_len):
    d = collections.deque(maxlen=seq_len)
    for idx, c in enumerate(open("day06.txt").read()):
        d.append(c)
        if len(set(d)) == seq_len:
            return idx + 1

print(find_unique_sequence(4))
print(find_unique_sequence(14))
