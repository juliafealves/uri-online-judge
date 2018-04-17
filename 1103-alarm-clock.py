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

    current = (time[0], time[1])
    alarm = (time[2], time[3])

    hours = abs(alarm[0] - current[0])
    minutes = abs(alarm[1] - current[1])
    time_sleep = 0

    if alarm[0] > current[0] or alarm[1] > current[1]:
        time_sleep = MINUTE_HOUR * hours + minutes
    else:
        time_sleep = MINUTE_DAY - (MINUTE_HOUR * hours + minutes)

    print time_sleep


