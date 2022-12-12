#!/usr/bin python3

#https://open.kattis.com/problems/fizzbuzz
def solve():
    X, Y, N = [int(q) for q in input().split()]
    for i in range(1, N+1):
        if i%X == 0 and i%Y != 0:
            print("Fizz")
        elif i%Y == 0 and i%X != 0:
            print("Buzz")
        elif i%X == 0 and i%Y == 0:
            print("FizzBuzz")
        else:
            print(i)

if __name__ == "__main__":
    solve()