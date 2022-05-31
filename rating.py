#!/usr/bin python3

# https://open.kattis.com/problems/ratingproblems

def solve():
    inp = input()
    n = int(inp.split(" ")[0])
    k = int(inp.split(" ")[1])
    max = 0
    min = 0
    for i in range(0, k):
        r = int(input())
        max += r
        min += r

    left = n - k
    for j in range(0, left):
        max += 3
        min += -3

    print(f"{min/n} {max/n}")

if __name__ == "__main__":
    solve()