from stack import Stack

def is_balanced(expression):

    pilha = Stack()
    
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '({[':
            pilha.push(char)
        
        elif char in ')}]':
            if pilha.is_empty():
                return False
            
            topo = pilha.pop()
            if topo != pares[char]:
                return False
    
    return pilha.is_empty()


# ==================== TESTES ====================
if __name__ == "__main__":
    testes = [
        "[{}(2+2)]{}",
        "[{}(2+2))]{}",
        "[{}])",
        "",
        "()",
        "({[]})",
        "{[()()]()}",
        "if (a[0] > b) { return c; }",
        "(",
        "]",
        "({[)]}",
        "{[(()]}",
        "((()))]"
    ]
    
    for exp in testes:
        resultado = is_balanced(exp)
        print(f"{exp:<35} → {resultado}")
