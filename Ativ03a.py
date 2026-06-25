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

    def is_empty(self):
        return self.singly_linked_list.is_empty()

# --- IMPLEMENTAÇÃO DA FUNÇÃO DE VERIFICAÇÃO ---

def is_balanced(expression):
    """
    Verifica se os pares de símbolos (), [], {} estão balanceados e na ordem correta.
    """
    pilha = Stack()
    
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "([{":
            pilha.push(char)
        
        elif char in ")]}":
            if pilha.is_empty():
                return False
            
            topo = pilha.pop()
            if topo != pares[char]:
                return False
                
    return pilha.is_empty()

# --- TESTES ---

if __name__ == "__main__":
    print(f"[{'CORRETO':^10}] [{is_balanced('[{}(2+2)]{}'):^7}] -> '[{}(2+2)]{}'")
    print(f"[{'ERRADO':^10}] [{is_balanced('[{}(2+2))]{}'):^7}] -> '[{}(2+2))]{}'")
    print(f"[{'ERRADO':^10}] [{is_balanced('[{}])'):^7}] -> '[{}])'")

    print("\n--- Testes Adicionais ---")
    testes = [
        ("", True),
        ("()", True),
        ("({[]})", True),
        ("{[()()]()}", True),
        ("if (a[0] > b) { return c; }", True),
        ("(", False),
        ("]", False),
        ("({[)]}", False),
        ("{[(()]}", False),
        ("((()))]", False)
    ]

    for exp, esperado in testes:
        resultado = is_balanced(exp)
        status = "✅" if resultado == esperado else "❌"
        print(f"{status} Expressão: {exp[:30]:<30} | Esperado: {esperado} | Resultado: {resultado}")
