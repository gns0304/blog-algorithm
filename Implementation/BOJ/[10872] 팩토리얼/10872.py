def factorial(N):
    if N > 0:
        return N * factorial(N-1)
    elif N == 0:
        return 1

if __name__ == '__main__':
    print(factorial(int(input())))