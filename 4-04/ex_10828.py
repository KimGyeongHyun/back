from sys import stdin


class Stack:

    def __init__(self):
        self.l = []

    def push(self, data: int):
        self.l.append(data)

    def pop(self) -> int:
        if len(self.l) == 0:
            return -1
        else:
            return_int = self.l[-1]
            self.l = self.l[:-1]
            return return_int

    def size(self) -> int:
        return len(self.l)

    def empty(self) -> int:
        if len(self.l) == 0:
            return 1
        else:
            return 0

    def top(self) -> int:
        if len(self.l) == 0:
            return -1
        else:
            return self.l[-1]


if __name__ == "__main__":
    stack = Stack()

    n = int(stdin.readline())
    for _ in range(n):

        s = stdin.readline().strip()

        if len(s) >= 4 and s.split()[0] == "push":
            stack.push(int(s.split()[1]))

        if s == "pop":
            print(stack.pop())

        if s == "size":
            print(stack.size())

        if s == "empty":
            print(stack.empty())

        if s == "top":
            print(stack.top())
