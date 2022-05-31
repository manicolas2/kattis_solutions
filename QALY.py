#!/usr/bin python3

# https://open.kattis.com/problems/qaly

def solve():
    N = int(input())
    sum = 0
    for i in range(0, N):
        inp = input()
        q, y = inp.split(" ")
        sum += float(q) * float(y)

    print(sum)

if __name__ == "__main__":
    solve()