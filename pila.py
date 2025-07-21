class HistorialVentas:
    def __init__(self):
        self._datos = []

    def empilar(self, venta):
        """Añade una venta al tope del historial."""
        self._datos.append(venta)

    def desempilar(self):
        """Quita y devuelve la última venta registrada."""
        if not self.esta_vacia():
            return self._datos.pop()
        raise IndexError("El historial está vacío.")

    def esta_vacia(self):
        return len(self._datos) == 0

    def obtener(self):
        """Devuelve el historial completo en orden LIFO."""
        return list(self._datos)
