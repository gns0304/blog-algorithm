import sys
input = sys.stdin.readline


def print(src):
    sys.stdout.write(str(src) + '\n')


class Queue:

    def __init__(self):
        self.__queue = list()

    def empty(self):
        if self.__queue:
            return 0
        return 1

    def push(self, X):
        self.__queue.append(X)

    def pop(self):
        if self.empty():
            return -1
        return self.__queue.pop(0)

    def front(self):
        if self.empty():
            return -1
        return self.__queue[0]

    def back(self):
        if self.empty():
            return -1
        return self.__queue[-1]

    def size(self):
        return len(self.__queue)


if __name__ == '__main__':
    N = int(input())
    stack = Queue()
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
        elif n[0] == "front":
            print(stack.front())
        elif n[0] == "back":
            print(stack.back())