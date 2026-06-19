from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        node = Node(data)
        self.root = node

    # Percurso em ordem simétrica (In-order)
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.simetric_traversal(node.right)

    # Percurso em PÓS-ORDEM (left, right, root)
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=' ')

    # Percurso em PRÉ-ORDEM (root, left, right)
    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        print(node, end=' ')
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    # Percurso em nível (Level-order / Breadth-first)
    def levelorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
            
        q = Queue()
        q.put(node)                    # enqueue

        while not q.empty():
            current = q.get()          # dequeue
            print(current, end=' ')

            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)


def example_tree():
    tree = BinaryTree()
    n1 = Node('B')
    n2 = Node('A')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')

    n5.right = n6
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    return tree


if __name__ == '__main__':
    tree = example_tree()
    print("Simétrico - InOrder")
    tree.simetric_traversal()
    print("\n")

    tree2 = example_tree()
    print("Pós Ordem - PostOrder")
    tree2.postorder_traversal()
    print("\n")

    tree3 = example_tree()
    print("Pré Ordem - PreOrder")
    tree3.preorder_traversal()
    print("\n")

    tree4 = example_tree()
    print("Em nível - Breadth-first")
    tree4.levelorder_traversal()
    print()
