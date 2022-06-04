from flask import render_template, request, redirect, url_for, flash
from appInitialize import app, db
from model.client import Client
from model.product import Product
from model.order import Order
import json

@app.route('/')
def index ():
    return render_template('layout.html')

#Crear cliente
@app.route('/create/client', methods=['GET', 'POST'])
def createClient ():
    if request.method == 'POST':
        name = request.form['name']
        document = request.form['document']
        client = Client(name, document)
        db.session.add(client)
        db.session.commit()
        flash('Cliente creado satisfactoriamente')
        return redirect(url_for('createClient'))    
    return render_template('create.html', route = 'client')

@app.route('/api/create/client', methods=['POST'])
def apiCreateClient ():
    if request.method == 'POST':
        data = json.loads(request.data)
        client = Client(data['name'], data['document'])
        db.session.add(client)
        db.session.commit()
        return "Registro creado", 200  

#Crear producto
@app.route('/create/product', methods=['GET', 'POST'])
def createProduct ():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        flash('Producto creado satisfactoriamente')
        return redirect(url_for('createProduct'))    
    return render_template('create.html', route = 'product')

@app.route('/api/create/product', methods=['POST'])
def apiCreateProduct ():
    if request.method == 'POST':
        data = json.loads(request.data)
        product = Product(data['name'], data['price'])
        db.session.add(product)
        db.session.commit()
        return "Registro creado", 200  

#Crear orden
@app.route('/create/order', methods=['GET', 'POST'])
def createOrder ():
    if request.method == 'POST':
        clientid = request.form['clientid']
        productid = request.form['productid']
        quantity = request.form['quantity']
        splProductid = productid.split(sep = ',')
        splQuantity = quantity.split(sep = ',')
        count = 0
        client = Client.query.filter_by(clientid = clientid, state = 'activo').all()
        if len(client) == 0:
            flash('Cliente no encontrado') 
            return render_template('create.html', route = 'order')
        for spl in splProductid:
            product = Product.query.filter(Product.productid == spl, Product.state != 'inactivo').all()
            if len(product) == 0:
                flash('Producto no encontrado') 
                return render_template('create.html', route = 'order')       
            order = Order(clientid, spl, splQuantity[count], product[0].price * int(splQuantity[count]))
            db.session.add(order)
            db.session.commit()
            count = count + 1
        flash('Orden creada satisfactoriamente')
        return redirect(url_for('createOrder'))    
    return render_template('create.html', route = 'order')

@app.route('/api/create/order', methods=['POST'])
def apiCreateOrder ():
    if request.method == 'POST':
        data = json.loads(request.data)
        splProductid = data['productid'].split(sep = ',')
        splQuantity = data['quantity'].split(sep = ',')
        count = 0
        client = Client.query.filter_by(clientid = data['clientid'], state = 'activo').all()
        if len(client) == 0:
            return "Registro no encontrado", 402 
        for spl in splProductid:
            product = Product.query.filter(Product.productid == spl, Product.state != 'inactivo').all()
            if len(product) == 0:
                return "Registro no encontrado", 402 
            order = Order(data['clientid'], spl, splQuantity[count], product[0].price * int(splQuantity[count]))
            db.session.add(order)
            db.session.commit()
            count = count + 1
        return "Registro creado", 200 

if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True)