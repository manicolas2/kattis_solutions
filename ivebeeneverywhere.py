#!/usr/bin python3

def solve():
    T = int(input())
    for i in range(0, T):
        n = int(input())
        cities = []
        for j in range(0, n):
            city = input()
            if city not in cities:
                cities.append(city)
        print(len(cities))

if __name__ == "__main__":
    solve()