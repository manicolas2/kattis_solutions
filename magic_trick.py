#!/usr/bin python3

def solve():
    N = input()
    tmp = ""
    for letter in N:
        if letter not in tmp:
            tmp += letter
        else:
            return(0)
    return(1)

if __name__ == "__main__":
    print(solve())