#!/usr/bin python3

# https://open.kattis.com/problems/heimavinna

def solve(inp):
    inps = []
    probs = ""
    for i in range(0, len(inp)):
        if inp[i] == ";":
            inps.append(probs)
            probs = ""
        else:
            probs += inp[i]
            if i == len(inp) - 1:
                inps.append(probs)
                
    sum = 0
    for prob in inps:
        if "-" in prob:
            min = int(prob.split("-")[0])
            max = int(prob.split("-")[1])
            for j in range(min, max+1):
                sum += 1
        else:
            sum += 1
    ans = sum
    return ans

if __name__ == "__main__":
    ans = solve(input())
    print(ans)