# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Alarm Clock - AD-HOC - https://bit.ly/2EUNEBy

MINUTE_HOUR = 60
MINUTE_DAY = MINUTE_HOUR * 24

while True:
    time = map(int, raw_input().split())

    if max(time) == 0:
        break

    current = time[0] * MINUTE_HOUR + time[1]
    alarm = time[2] * MINUTE_HOUR + time[3]

    if alarm > current:
        print '%i' % (alarm - current)
    else:
        print '%i' % (MINUTE_DAY - abs(alarm - current))
