#!/usr/bin python3

# https://open.kattis.com/problems/pieceofcake2

def solve():
    inps = input().split(" ")
    n = int(inps[0])
    h = int(inps[1])
    v = int(inps[2])

    vol = max(h, n-h) * max(v, n-v) * 4

    print(vol)

if __name__ == "__main__":
    solve()