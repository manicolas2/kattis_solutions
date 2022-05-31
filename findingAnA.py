#!/usr/bin python3

def solve():
    strn = input()
    ind = strn.index('a')
    tmp = ""
    for i in range(ind, len(strn)):
        tmp += strn[i]
    print(tmp)
            

if __name__ == "__main__":
    solve()