import sys
input = sys.stdin.readline


def print(src):
    sys.stdout.write(str(src) + '\n')


class Stack:

    def __init__(self):
        self.__stack = list()

    def empty(self):
        if self.__stack:
            return 0
        return 1

    def push(self, X):
        self.__stack.append(X)

    def pop(self):
        if self.empty():
            return -1
        return self.__stack.pop()

    def top(self):
        if self.empty():
            return -1
        return self.__stack[-1]

    def size(self):
        return len(self.__stack)


if __name__ == '__main__':
    N = int(input())
    stack = Stack()
    for _ in range(N):
        n = input().strip().split(' ')
        if n[0] == "push":
            stack.push(int(n[1]))
        elif n[0] == "pop":
            print(stack.pop())
        elif n[0] == "size":
            print(stack.size())
        elif n[0] == "empty":
            print(stack.empty())
        elif n[0] == "top":
            print(stack.top())
