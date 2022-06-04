from flask import render_template, request, redirect, url_for, flash
from appInitialize import app, db
from model.client import Client
from model.product import Product
from model.order import Order
import json

@app.route('/')
def index ():
    return render_template('layout.html')

#Eliminar cliente
@app.route('/delete/client', methods=['GET', 'POST'])
def deleteClient ():
    if request.method == 'POST':
        clientid = request.form['clientid']
        client = Client.query.filter_by(clientid = clientid, state = 'activo').all()
        if len(client) == 0:
            flash('Cliente no encontrado') 
            return render_template('delete.html', route = 'client')
        else:          
            client = Client.query.get(clientid)  
            client.state = 'inactivo'
            db.session.add(client)
            db.session.commit()
            flash('Cliente eliminado satisfactoriamente')
            return render_template('delete.html', route = 'client') 
    return render_template('delete.html', route = 'client')

@app.route('/api/delete/client/<string:id>', methods=['POST'])
def apiDeleteClient (id):
    if request.method == 'POST':
        client = Client.query.get(id)
        if len(client) == 0:
            return "Registro no encontrado", 402  
        else:
            client.state = 'inactivo'
            db.session.add(client)
            db.session.commit()
            return "Registro modificado", 200 
            
#Eliminar producto
@app.route('/delete/product', methods=['GET', 'POST'])
def deleteProduct ():
    if request.method == 'POST':
        productid = request.form['productid']
        product = Product.query.filter(Product.productid == productid, Product.state != 'inactivo').all()
        if len(product) == 0:
            flash('Producto no encontrado') 
            return render_template('delete.html', route = 'product')
        else:          
            product = Product.query.get(productid)  
            product.state = 'inactivo'
            db.session.add(product)
            db.session.commit()
            flash('Producto eliminado satisfactoriamente')
            return render_template('delete.html', route = 'product') 
    return render_template('delete.html', route = 'product')

@app.route('/api/delete/product/<string:id>', methods=['POST'])
def apiDeleteProduct (id):
    if request.method == 'POST':
        product = Product.query.get(id)
        if len(product) == 0:
            return "Registro no encontrado", 402  
        else:
            product.state = 'inactivo'
            db.session.add(product)
            db.session.commit()
            return "Registro modificado", 200             

#Eliminar orden
@app.route('/delete/order', methods=['GET', 'POST'])
def deleteOrder ():
    if request.method == 'POST':
        clientid = request.form['clientid']
        client = Client.query.filter_by(clientid = clientid, state = 'activo').all()
        if len(client) == 0:
            flash('Cliente no encontrado') 
            return render_template('delete.html', route = 'order')
        else:          
            orders = Order.query.filter_by(clientid = clientid, state = 'pendiente').all()
            if len(orders) == 0:
                flash('Orden no encontrada') 
                return render_template('delete.html', route = 'order')
            for order in orders:
                db.session.delete(order)
                db.session.commit()
            flash('Orden eliminada satisfactoriamente')
            return render_template('delete.html', route = 'order') 
    return render_template('delete.html', route = 'order')

@app.route('/api/delete/order/<string:id>', methods=['POST'])
def apiDeleteOrder (id):
    if request.method == 'POST':
        client = Client.query.get(id)
        if len(client) == 0:
            return "Registro no encontrado", 402  
        else:
            orders = Order.query.filter_by(clientid = id, state = 'pendiente').all()
            if len(orders) == 0:
                return "Registro no encontrado", 402 
            for order in orders:
                db.session.delete(order)
                db.session.commit()
            return "Registro eliminado", 200   

if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True)