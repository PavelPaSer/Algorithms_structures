# Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def rev_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
# Создание связного списка: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Разворот списка
new_head = rev_linked_list(head)

# Вывод развернутого списка: 5 -> 4 -> 3 -> 2 -> 1
current = new_head
while current:
    print(current.value)
    current = current.next
