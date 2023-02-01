class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):

        temp_string = ""
        iterator = self.head
        case_number = 1

        while iterator is not None:
            temp_string += "Case #{}: {} + {} = {}\n".format(case_number, iterator.data[0], iterator.data[1],
                                                             iterator.data[0] + iterator.data[1])
            iterator = iterator.next
            case_number += 1

        return temp_string


if __name__ == "__main__":

    linked_list = LinkedList()

    repeat = int(input())

    for i in range(repeat):
        a, b = map(int, input().split())
        linked_list.append((a, b))

    print(linked_list)