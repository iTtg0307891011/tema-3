# Venta de Hamburguesas – Cola y Pila

**Nombre del alumno:** Sergio Alexander Antonio Gracida
**Grupo/Materia:** Estructuras de Datos / Pilas y Colas para sistemas de apoyo

---

## Descripción del sistema

Esta aplicación web está desarrollada en Python con Flask y permite gestionar la **venta de hamburguesas** mediante:

- **Cola de pedidos (FIFO):** los clientes agregan su pedido y esperan su turno.
- **Pila de historial de ventas (LIFO):** cada vez que se atiende un pedido, se registra en el historial; se puede “deshacer” la última venta.

El sistema ofrece botones para:
- **Encolar** un nuevo pedido.
- **Atender** (desencolar) el siguiente pedido y pasarlo al historial.
- **Registrar** manualmente una venta.
- **Deshacer** (desempilar) la última venta.

Se utiliza Bootstrap para una interfaz sencilla y clara.

---

## Instalación

1. **Clona o descarga** este repositorio en tu máquina local.  
2. Abre una terminal y sitúate en la carpeta raíz del proyecto (donde está `requirements.txt`):  
   ```bash
   cd /ruta/a/tu/proyecto

3. (Opcional) Crea un entorno virtual e instálalo:
python -m venv venv
source venv/bin/activate      # macOS/Linux
.\venv\Scripts\activate       # VisualStudio

4.Instala las dependencias:
pip install -r requirements.txt

Ejecución
Para arrancar el servidor Flask, ejecuta:

bash
Copiar
Editar
python app.py
Luego abre tu navegador en:

cpp
Copiar
Editar
http://127.0.0.1:5000/

Ejemplo de uso
Ver menú principal:
– /

Agregar un pedido a la cola:

Escribe “Combo Clásico” y haz clic en Agregar Pedido.

Verás tu pedido listado como número 1.

Atender siguiente pedido:

Haz clic en Atender Siguiente Pedido.

El pedido desaparece de la cola y se añade al historial de ventas.

Registrar/Deshacer ventas manuales:

Ve a /pila, añade una venta manual o haz clic en Deshacer Última Venta para quitar la más reciente.
