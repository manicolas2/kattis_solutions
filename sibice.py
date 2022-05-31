#!/usr/bin python3

# https://open.kattis.com/problems/sibice

import math

def solve():
    N, W, H = input().split(" ")
    diagonal = math.sqrt(math.pow(int(W), 2) + math.pow(int(H), 2))
    for i in range(0, int(N)):
        L = int(input())
        print("DA") if L <= diagonal else print("NE")


if __name__ == "__main__":
    solve()