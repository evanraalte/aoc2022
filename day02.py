from enum import Enum

class Shape(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Verdict(Enum):
    X = 0
    Y = 3
    Z = 6


def compute_round_score(me: Shape, opp: Shape):
    if me == opp:
        return 3
    elif (me.value+1)%3 == (opp.value%3):
        return 0
    else:
        return 6
        
def get_shape_from_letter(letter):
    if letter in "AX":
        return Shape.ROCK
    elif letter in "BY":
        return Shape.PAPER
    elif letter in "CZ":
        return Shape.SCISSORS

def get_shape_from_verdict(v: Verdict, opp: Shape):
    ret_val = 0
    if v == Verdict.Z:
        ret_val = Shape((opp.value+1)%3)
    elif v == Verdict.Y:
        ret_val = opp
    else:
        ret_val = Shape((opp.value+2)%3)
    return ret_val


rounds = open("day02.txt").read().split('\n')
score_parta = 0
score_partb = 0
for round in rounds:
    l_opp, l_me = round.split(" ")
    opp = get_shape_from_letter(l_opp)
    me_parta = get_shape_from_letter(l_me)
    me_partb = get_shape_from_verdict(Verdict[l_me], opp)
    score_parta += 1 + me_parta.value + compute_round_score(me_parta, opp)
    score_partb += Verdict[l_me].value + me_partb.value + 1
print(score_parta)
print(score_partb)