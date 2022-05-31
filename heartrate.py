#!/usr/bin python3

def solve():
    N = int(input())
    for i in range(0, N):
        b, p = input().split(" ")
        t = 60 / float(p)
        bpm = (60 * int(b)) / float(p)
        print(f"{bpm - t} {bpm} {bpm + t}")
                

if __name__ == "__main__":
    solve()