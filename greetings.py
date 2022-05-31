#!/usr/bin python3

def solve():
    hey = input()
    cnt = 0
    for i in hey:
        if i == 'e':
            cnt += 1

    greet = 'h'
    for i in range(0, cnt*2):
        greet += 'e'    

    greet += 'y'

    print(greet)


if __name__ == "__main__":
    solve()