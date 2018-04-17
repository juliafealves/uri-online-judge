# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Queen - AD-HOC - https://bit.ly/2HqAtxI


# Target is in column or row of source.
def one_move(origin, target):
    if origin[0] == target[0] or origin[1] == target[1]:
        return True
    elif abs(origin[0] - target[0]) == abs(origin[1] - target[1]):
        return True

    return False


while True:
    positions = map(int, raw_input().split())

    if 0 in positions:
        break

    origin = (positions[0], positions[1])
    target = (positions[2], positions[3])

    if origin == target:
        print "0"
    elif one_move(origin, target):
        print "1"
    else:
        print "2"
