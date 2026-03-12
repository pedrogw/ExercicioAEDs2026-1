class DynamicIntArray:
    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity  # Tamanho real do array interno
        self.size = 0             # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity  # Cria Array estático interno

    def is_empty(self):
        return self.size == 0

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora do intervalo")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fora do intervalo")
        self.data[index] = value

    def append(self, value):
        if self.size == self.capacity:
            # Dobra a capacidade (estratégia comum)
            new_capacity = self.capacity * 2
            self._resize(new_capacity)
        
        self.data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        if new_capacity > self.capacity:
            print(f"⏫ Redimensionando de {self.capacity} para {new_capacity}")
        else:
            print(f"⬇️ Redimensionando de {self.capacity} para {new_capacity}")
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __str__(self):
        return str(self.data[:self.size])
