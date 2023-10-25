from sys import stdin

# temp_string 에 += "+\n" 하는 대신
# 오퍼레이터를 리스트에 담아 "\n".join(list) 하는 것이 시간초과가 안 남

class Stack:

    def __init__(self):
        self.stack_list = []

    def push(self, data : int):
        self.stack_list.append(data)

    def see(self) -> int:
        if len(self.stack_list) == 0:
            return 0
        else:
            return self.stack_list[-1]

    def pop(self) -> int:
        output_data = self.stack_list[-1]
        self.stack_list = self.stack_list[:-1]
        return output_data


def push_n_pop(number_list, n):
    stacking_number = 1
    stack = Stack()
    oper_list = []

    for number in number_list:
        while stack.see() < number:
            stack.push(stacking_number)
            oper_list.append('+')
            stacking_number += 1
        if number < stack.see():
            return "NO"
        else:
            stack.pop()
            oper_list.append('-')

    return "\n".join(oper_list)


if __name__ == "__main__":

    n = int(stdin.readline())
    number_list = []
    for i in range(n):
        number_list.append(int(stdin.readline()))

    stacking_number = 1
    stack = Stack()

    print(push_n_pop(number_list, n))
