#!/usr/bin python3

# https://open.kattis.com/problems/tarifa

def solve():
    X = int(input())
    N = int(input())
    sum = X
    for i in range(0, N):
        P = int(input())
        sum += X-P
    print(sum)

if __name__ == "__main__":
    solve()