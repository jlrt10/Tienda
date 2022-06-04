from flask import render_template, request, flash, jsonify
from appInitialize import app, db
from model.client import Client
from model.product import Product
from model.order import Order
import json

@app.route('/')
def index ():
    return render_template('layout.html')

#Consultar clientes
@app.route('/read/clients', methods=['GET'])
def readClients ():
    clients = Client.query.filter_by(state = 'activo').all()
    return render_template('read.html', id = False, records = clients, route = 'client')

@app.route('/api/read/clients', methods=['GET'])
def apiReadClients ():
    clients = Client.query.filter_by(state = 'activo').all()
    return jsonify([{'name': client.name, 'document': client.document, 'state': client.state, 'created_at': client.created_at} for client in clients])

#Consultar productos
@app.route('/read/products', methods=['GET'])
def readProducts ():
    products = Product.query.filter(Product.state != 'inactivo').all()
    return render_template('read.html', id = False, records = products, route = 'product')

@app.route('/api/read/products', methods=['GET'])
def apiReadProducts ():
    products = Product.query.filter(Product.state != 'inactivo').all()
    return jsonify([{'name': product.name, 'document': product.price, 'state': product.state, 'created_at': product.created_at} for product in products])

#Consultar ordenes
@app.route('/read/orders', methods=['GET', 'POST'])
def readOrders ():
    if request.method == 'POST':
        id = request.form['id']
        if id == "true":
            clientid = request.form['clientid']
            client = Client.query.filter_by(clientid = clientid, state = 'activo').all()            
            if len(client) == 0:
                flash('Cliente no encontrado') 
                return render_template('read.html', id = True, route = 'order')
            else:
                orders = Order.query.filter_by(clientid = clientid, state = 'pendiente').join(Client, Order.clientid == Client.clientid and Client.state == 'activo').join(Product, Order.clientid == Product.productid and Product.state != 'inactivo').all()
                return render_template('read.html', id = False, records = orders, route = 'order')
    return render_template('read.html', id = True, route = 'order')

@app.route('/api/read/orders', methods=['POST'])
def apiReadOrders ():
    if request.method == 'POST':
        data = json.loads(request.data)
        client = Client.query.filter_by(clientid = data['clientid'], state = 'activo').all()  
        if len(client) == 0:
            return "Registro no encontrado", 402  
        orders = Order.query.filter_by(clientid = data['clientid'], state = 'pendiente').join(Client, Order.clientid == Client.clientid and Client.state == 'activo').join(Product, Order.clientid == Product.productid and Product.state != 'inactivo').all()
        return jsonify([{'clientid': order.clientid, 'productid': order.productid, 'quantity': order.quantity, 'total': order.total, 'state': order.state, 'created_at': order.created_at} for order in orders])

#Consultar compras
@app.route('/read/purchases', methods=['GET', 'POST'])
def readPurchases ():
    if request.method == 'POST':
        id = request.form['id']
        if id == "true":
            clientid = request.form['clientid']
            client = Client.query.filter_by(clientid = clientid, state = 'activo').all()            
            if len(client) == 0:
                flash('Cliente no encontrado') 
                return render_template('read.html', id = True, route = 'purchase')
            else:
                orders = Order.query.filter_by(clientid = clientid, state = 'pagada').join(Client, Order.clientid == Client.clientid and Client.state == 'activo').join(Product, Order.clientid == Product.productid and Product.state != 'inactivo').all()
                return render_template('read.html', id = False, records = orders, route = 'purchase')
    return render_template('read.html', id = True, route = 'purchase')

@app.route('/api/read/purchases', methods=['POST'])
def apiReadPurchases ():
    if request.method == 'POST':
        data = json.loads(request.data)
        client = Client.query.filter_by(clientid = data['clientid'], state = 'activo').all()  
        if len(client) == 0:
            return "Registro no encontrado", 402  
        orders = Order.query.filter_by(clientid = data['clientid'], state = 'pagada').join(Client, Order.clientid == Client.clientid and Client.state == 'activo').join(Product, Order.clientid == Product.productid and Product.state != 'inactivo').all()
        return jsonify([{'clientid': order.clientid, 'productid': order.productid, 'quantity': order.quantity, 'total': order.total, 'state': order.state, 'created_at': order.created_at} for order in orders])

if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True)