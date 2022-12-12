#!/usr/bin python3

def solve():
    W = int(input())
    N = int(input())
    #A, B = [int(q) for q in input().split()]
    total = 0
    for i in range (0, N):
        w, l = [int(q) for q in input().split()]
        total += w*l

    print(total//W)


    
if __name__ == "__main__":
    solve()