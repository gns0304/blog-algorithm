T = int(input())
for _ in range(T):
    for i, value in enumerate(reversed(bin(int(input()))[2:])):
        if value == '1':
            print(i, end=" ")
