class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def oblicz(node):
    if isinstance(node.value, str):
        left_value = oblicz(node.left)
        right_value = oblicz(node.right)

        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            if right_value == 0:
                raise ValueError("Dzielenie przez zero")
            return left_value / right_value
    else:
        return node.value


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')


def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        if isinstance(node.value, str):
            print("(", end='')
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)
        if isinstance(node.value, str):
            print(")", end='')


def main():
    root = Node('+')
    root.left = Node('*')
    root.right = Node('-')
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(8)
    root.right.right = Node(2)
    print("Wartość wyrażenia:", oblicz(root))
    print("Postorder:", end=' ')
    postorder(root)
    print("\nPreorder:", end=' ')
    preorder(root)
    print("\nInorder z nawiasami:", end=' ')
    inorder(root)


if __name__ == "__main__":
    main()
