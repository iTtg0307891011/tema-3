from flask import Flask, render_template, request, redirect, url_for
from models.cola import ColaPedidos
from models.pila import HistorialVentas

app = Flask(__name__)
cola = ColaPedidos()
historial = HistorialVentas()

@app.route('/', methods=['GET'])
def menu():
    return render_template('menu.html')

@app.route('/cola', methods=['GET', 'POST'])
def gestionar_cola():
    if request.method == 'POST':
        # Si viene un nuevo pedido
        nuevo = request.form.get('pedido')
        if nuevo:
            cola.encolar(nuevo)
        # Si se atiende el siguiente pedido
        if request.form.get('accion') == 'atender' and not cola.esta_vacia():
            pedido = cola.desencolar()
            historial.empilar(pedido)
        return redirect(url_for('gestionar_cola'))

    return render_template('cola.html', pedidos=cola.obtener())

@app.route('/pila', methods=['GET', 'POST'])
def gestionar_historial():
    if request.method == 'POST':
        # Añadir manualmente una venta al historial
        venta = request.form.get('venta')
        if venta:
            historial.empilar(venta)
        # Deshacer (eliminar) la última venta
        if request.form.get('accion') == 'deshacer' and not historial.esta_vacia():
            historial.desempilar()
        return redirect(url_for('gestionar_historial'))

    return render_template('pila.html', ventas=historial.obtener())

if __name__ == '__main__':
    app.run(debug=True)
