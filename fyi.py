#!/usr/bin python3

# https://open.kattis.com/problems/fyi

def solve():
    N = input()
    if N[0] == '5' and N[1] == '5' and N[2] == '5':
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()