class ColaPedidos:
    def __init__(self):
        self._datos = []

    def encolar(self, pedido):
        """Agrega un pedido al final de la cola."""
        self._datos.append(pedido)

    def desencolar(self):
        """Sirve (retira) el primer pedido de la cola."""
        if not self.esta_vacia():
            return self._datos.pop(0)
        raise IndexError("La cola está vacía.")

    def esta_vacia(self):
        return len(self._datos) == 0

    def obtener(self):
        """Devuelve la lista de pedidos actuales."""
        return list(self._datos)
