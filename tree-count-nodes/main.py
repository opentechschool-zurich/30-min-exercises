class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def count_nodes(self):
        count = 1
        if self.left is not None:
            count += self.left.count_nodes()
        if self.right is not None:
            count += self.right.count_nodes()
        return count

    def count_nodes_no_recursion(self):
        count = 0
        stack = [self]
        while stack:
            current = stack.pop()
            count += 1
            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)
        return count

def main():
    tree = Tree(1, Tree(2), Tree(3, None, Tree(4, Tree(5, None, Tree(6)))))

    print(tree.right.left)
    print(tree.count_nodes())
    print(tree.count_nodes_no_recursion())

if __name__ == '__main__':
    main()
