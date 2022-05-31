#!/usr/bin python3

def solve():
    N = int(input())
    nums = input().split(" ")
    sum = 0
    for i in range(0, N):
        sum += int(nums[i])

    print(sum)

        
if __name__ == "__main__":
    solve()