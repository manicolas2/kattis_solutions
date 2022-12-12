#!/usr/bin python3

#https://open.kattis.com/problems/filip

def reverse(string):
    string = string[::-1]
    return string

def solve():
    A, B = input().split()
    if A[2] != B[2]:
        if A[2] > B[2]:
            print(reverse(A))
        else:
            print(reverse(B))
    else:
        if A[1] > B[1]:
            print(reverse(A))
        else:
            print(reverse(B))

if __name__ == "__main__":
    solve()