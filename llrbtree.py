class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.color = True  


class LLRBTREE:
    def __init__(self):
        self.root = None

    def rotate_left(self, my_node):
        print("поворот влево!!")
        child = my_node.right
        child_left = child.left

        child.left = my_node
        my_node.right = child_left

        return child

    def rotate_right(self, my_node):
        print("вращение вправо")
        child = my_node.left
        child_right = child.right

        child.right = my_node
        my_node.left = child_right

        return child

    def is_red(self, my_node):
        if my_node is None:
            return False
        return my_node.color

    def swap_colors(self, node1, node2):
        node1.color, node2.color = node2.color, node1.color

    def insert(self, my_node, data):
        if my_node is None:
            return Node(data)

        if data < my_node.data:
            my_node.left = self.insert(my_node.left, data)
        elif data > my_node.data:
            my_node.right = self.insert(my_node.right, data)
        else:
            return my_node

        if self.is_red(my_node.right) and not self.is_red(my_node.left):
            my_node = self.rotate_left(my_node)
            self.swap_colors(my_node, my_node.left)

        if self.is_red(my_node.left) and self.is_red(my_node.left.left):
            my_node = self.rotate_right(my_node)
            self.swap_colors(my_node, my_node.right)

        if self.is_red(my_node.left) and self.is_red(my_node.right):
            my_node.color = not my_node.color
            my_node.left.color = False
            my_node.right.color = False

        return my_node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            c = '●' if node.color is False else '◯'
            print(str(node.data) + c + " ", end='')
            self.inorder(node.right)


if __name__ == "__main__":
    tree = LLRBTREE()

    while True:
        num = int(input("Введите целое число: "))
        tree.root = tree.insert(tree.root, num)

        tree.inorder(tree.root)
        print()
        
        choice = input("Вы хотите продолжить? (введите y или n): ")
        if choice.lower() != 'y':
            break
