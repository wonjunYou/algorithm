from itertools import combinations as c
import sys

while True:
    S = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    
    if S == [0]:
        break
        
    k = S[0]
    S.pop(0)

    lotto_numbers = list(c(S, 6))

    for numbers in lotto_numbers:
        print(*numbers)
    print()