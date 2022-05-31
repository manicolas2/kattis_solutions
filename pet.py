#!/usr/bin python3

# https://open.kattis.com/problems/pet

def solve():
    total = []
    for i in range(0, 5):
        N = input().split(" ")
        total.append(int(N[0]) + int(N[1]) + int(N[2]) + int(N[3]))
    maxVal = max(total)
    maxInd = total.index(maxVal) + 1
    print(f"{maxInd} {maxVal}")

if __name__ == "__main__":
    solve()