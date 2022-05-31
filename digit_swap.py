#!/usr/bin python3

# https://open.kattis.com/problems/digitswap

def solve(digit):
    ans = digit[1] + digit[0]
    return ans

if __name__ == "__main__":
    ans = solve(input())
    print(ans)