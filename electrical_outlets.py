#!/usr/bin python3

# https://open.kattis.com/problems/electricaloutlets

def solve():
    N = int(input())
    for i in range(0, N):
        inp = input().split(" ")
        K = int(inp[0])
        sum = 0
        for test in range(1, K+1):
            if test != 1:
                sum += int(inp[test]) - 1
            else:
                sum += int(inp[1])
        print(sum)

if __name__ == "__main__":
    solve()