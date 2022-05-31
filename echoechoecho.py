#!/usr/bin python3

# https://open.kattis.com/problems/echoechoecho

def solve():
    word = input().strip()
    out = ""
    for i in range(0,3):
        if i != 2:
            out += f"{word} "
        else:
            out += f"{word}"

    print(out)
    
if __name__ == "__main__":
    solve()