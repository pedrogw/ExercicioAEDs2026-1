class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def insert_at_top(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1 

    def delete_from_top(self):
        if self.top is None:
            raise IndexError("Estrutura Vazia")
        removed_data = self.top.data
        self.top = self.top.next
        self.size -= 1                  
        return removed_data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise IndexError("Estrutura Vazia")
        return self.top.data

class Stack:
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def push(self, data):
        self.singly_linked_list.insert_at_top(data)

    def pop(self):
        return self.singly_linked_list.delete_from_top()

    def peek(self):
        return self.singly_linked_list.peek()

    def is_empty(self):
        return self.singly_linked_list.is_empty()


if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        main_stack.push(data)
        if min_stack.is_empty() or data <= min_stack.peek():
            min_stack.push(data)

    def pop_aux():
        data = main_stack.pop()
        if data == min_stack.peek():
            min_stack.pop()
        return data

    def get_min():
        return min_stack.peek()

    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")
