class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1

    def insert(self, index, data):
        new_node = Node(data)

        if index == 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            self.size += 1
            return

        if index > self.size:
            index = self.size

        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        if new_node.next is None:
            self.tail = new_node

        self.size += 1

    def __str__(self):
        elements = []
        trav = self.head
        while trav:
            elements.append(str(trav.data))
            trav = trav.next
        return " -> ".join(elements) if elements else "Lista vazia"


# TESTE
print("=" * 60)
print("TESTE DA LISTA ENCADEADA - INICIANDO...")
print("=" * 60)

linked_list = SingleLinkedList()
linked_list.append(5)
linked_list.append(23)
linked_list.append(7)
linked_list.append(13)

print("\nLista original:")
print(linked_list)
print(f"Tamanho atual: {linked_list.size} | Head: {linked_list.head.data} | Tail: {linked_list.tail.data}")

linked_list.insert(2, 11)

print("\nLista após insert(2, 11):")
print(linked_list)
print(f"Tamanho atual: {linked_list.size} | Head: {linked_list.head.data} | Tail: {linked_list.tail.data}")

print("\n" + "=" * 60)
print("TESTE CONCLUÍDO COM SUCESSO!")
print("=" * 60)
