input = int(input())
[print(f"{'*' * i}".rjust(input, ' ')) for i in range(1, input + 1)]
