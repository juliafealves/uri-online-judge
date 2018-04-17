# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Multiples - Beginner

numbers = map(int, raw_input().split())

big = max(numbers)
little = min(numbers)

if big % little == 0:
    print 'Sao Multiplos'
else:
    print 'Nao sao Multiplos'
