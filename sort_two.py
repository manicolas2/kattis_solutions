#!/usr/bin python3

# https://open.kattis.com/problems/sorttwonumbers

def solve():
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)

    print(f"{b} {a}") if a > b else print(f"{a} {b}")


if __name__ == "__main__":
    solve()