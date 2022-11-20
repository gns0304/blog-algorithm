input = int(input())
[print(" " * (input - i) +  '*' * i) for i in range(1, input + 1)]
