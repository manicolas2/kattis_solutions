#!/usr/bin python3

def solve():
    S = input()
    l = input()
    chat = ""
    for i in range(0, len(l), 3):
        index = l[i]+l[i+1]+l[i+2]
        index = int(index.lstrip('0'))
        chat += S[index-1]
    print(chat)
            
if __name__ == "__main__":
    solve()