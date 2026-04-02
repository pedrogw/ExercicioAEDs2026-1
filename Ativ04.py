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
            raise IndexError("Estrutura Vazia - Impossível remover elemento")
        
        removed_data = self.top.data
        self.top = self.top.next
        self.size -= 1                  
        return removed_data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise IndexError("Estrutura Vazia - Impossível espiar")
        return self.top.data

class Stack:
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def push(self, data):
        self.singly_linked_list.insert_at_top(data)

    def pop(self):
        data = self.singly_linked_list.delete_from_top()
        return data

    def peek(self):
        data = self.singly_linked_list.peek()
        return data

    def is_empty(self):
        return self.singly_linked_list.is_empty()
    
    def size(self):
        return self.singly_linked_list.size
    
    def __str__(self):
        if self.singly_linked_list.top is None:
            return "Pilha vazia"

        linhas = []
        atual = self.singly_linked_list.top  
        index = 0  

        while atual is not None:
            if index == 0:
                linhas.append(f"{atual.data} (Topo)")
            else:
                linhas.append(f"{atual.data}")

            atual = atual.next
            if atual is not None:
                linhas.append("↓") 
            index += 1

        if "↓" in linhas[-1]:
            linhas.pop()

        if index > 1:
            for i in range(len(linhas) - 1, -1, -1):
                if linhas[i] != "↓":
                    linhas[i] += " (base)"
                    break

        return "\n".join(linhas)

class QueueUsingStacks:
    def __init__(self):
        self.pilha_principal = Stack()
        self.pilha_aux = Stack()

    def enqueue(self, data):
        self.pilha_principal.push(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila Vazia - Impossível remover elemento")
            
        if self.pilha_aux.is_empty():
            while not self.pilha_principal.is_empty():
                elemento = self.pilha_principal.pop()
                self.pilha_aux.push(elemento)
                
        return self.pilha_aux.pop()

    def is_empty(self):
        return self.pilha_principal.is_empty() and self.pilha_aux.is_empty()

    def __str__(self):
        temp_principal = Stack()
        temp_aux = Stack()
        result = []

        while not self.pilha_aux.is_empty():
            val = self.pilha_aux.pop()
            result.append(val)
            temp_aux.push(val)

        while not self.pilha_principal.is_empty():
            val = self.pilha_principal.pop()
            temp_principal.push(val)

        while not temp_principal.is_empty():
            val = temp_principal.pop()
            result.append(val)
            self.pilha_principal.push(val)

        while not temp_aux.is_empty():
            self.pilha_aux.push(temp_aux.pop())

        if not result:
            return "Fila vazia"

        result[0] = f"{result[0]} (Início)"
        result[-1] = f"{result[-1]} (Fim)"
        return "\n↓\n".join(str(x) for x in result)


if __name__ == "__main__":
    fila = QueueUsingStacks()

    print("\nInserindo: 10, 20, 30")
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    print(fila)

    print("\nRemovendo dois elementos:")
    print(fila.dequeue())
    print(fila.dequeue())
    fila.enqueue(40)

    print("\nEstado atual da fila:")
    print(fila)

    print("\nA fila está vazia?", fila.is_empty())

    print("\nRemovendo mais um elemento:")
    print(fila.dequeue())

    print("\nA fila está vazia?", fila.is_empty())

    print("\nEstado atual da fila:")
    print(fila)
