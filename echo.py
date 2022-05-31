#!/usr/bin python3

# https://open.kattis.com/problems/oddecho

def solve():
    N = int(input())
    for i in range(0, N):
        text = input()
        if i % 2 == 0:
            print(text)
    

if __name__ == "__main__":
    solve()