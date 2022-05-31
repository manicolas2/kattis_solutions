#!/usr/bin python3

# https://open.kattis.com/problems/reversebinary

def solve():
    N = int(input())
    binary = ""
    while N != 1:
        binary += str(N%2)
        N = N//2
    binary += str(N%2)
    power = len(binary)-1
    value = 0
    for i in range(0, power+1):
        if binary[i] == "1":
            value += 2**power
        power -= 1
    
    print(value)        


if __name__ == "__main__":
    solve()