#!/usr/bin python3

def solve():
    G, T, N = map(int, input().split(" "))
    tmp = (G - T) * .90
    items = list(map(int, input().split(" ")))
    sum = 0
    for i in range(0, N):
        sum += items[i]
    res = tmp - sum
    print(int(res))



if __name__ == "__main__":
    solve()