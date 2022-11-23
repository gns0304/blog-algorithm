from string import ascii_lowercase
S = input()
[print(S.index(c), end=" ") if c in S else print(-1, end=" ") for c in list(ascii_lowercase)]