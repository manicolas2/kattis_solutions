#!/usr/bin python3

# https://open.kattis.com/problems/jumbojavelin

def solve():
    N = int(input())
    sum = 0
    for i in range(0, N):
        l = int(input())
        if i != 0:
            sum += l
            sum -= 1
        else:
            sum += l
    
    print(sum)
if __name__ == "__main__":
    solve()