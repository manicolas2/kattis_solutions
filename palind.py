#!/usr/bin python3

# NOT A KATTIS QUESTION

#######
# A string is said to be a palindrome if it reads the same forwards and backwards. e.g. KAYAK, RACECAR
# BAYABAS is not a palindrome, but if we delete the last 2 letters, we will get BAYAB, which is a palindrome.
# Define a function DELPALINDROME that accepts a string argument S and prints out the minimum number of characters that can be deleted to make the string a palindrome.
#######


def solve():
    text = input("Enter a word: ")
    palin = ""
    rev = ''.join(list(reversed(text)))
    q, cnt = 0, 0
    for i in range(0, len(text)):
        for j in range(q, len(rev)):
            if text[i] == rev[j]:
                palin = palin + text[i]
                cnt += 1
                q = j + 1
                break
    res = len(text) - cnt
    print(f"Resulting Palindrome: {palin}")
    print(f"Number of Letters to Remove: {res}")


if __name__ == "__main__":
    solve()