#!/usr/bin python3

# https://open.kattis.com/problems/stopwatch

def solve():
    N = int(input())
    pressed1 = 0
    pressed2 = 0
    sum = 0
    for i in range(0, N):
        if i%2 == 0:
            pressed1 = int(input())
        else:
            pressed2 = int(input())
            sum += pressed2 - pressed1 
    if N%2 == 0:
        print(sum)
    else:
        print("still running")

if __name__ == "__main__":
    solve()