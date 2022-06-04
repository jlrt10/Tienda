from flask import render_template, request, redirect, url_for, flash
from appInitialize import app, db
from model.client import Client
from model.product import Product
from model.order import Order
import json

@app.route('/')
def index ():
    return render_template('layout.html')

#Modificar cliente
@app.route('/update/client', methods=['GET', 'POST'])
def updateClient ():
    if request.method == 'POST':
        id = request.form['id']
        if id == "true":
            clientid = request.form['clientid']
            client = Client.query.filter_by(clientid = clientid, state = 'activo').all()
            if len(client) == 0:
                flash('Cliente no encontrado') 
                return render_template('update.html', id = True, route = 'client')
            else:
                return render_template('update.html', id = False, records = client, route = 'client')
        else:
            clientid = request.form['client']
            name = request.form['name']
            document = request.form['document']
            client = Client.query.get(clientid)
            client.name = name
            client.document = document
            db.session.add(client)
            db.session.commit()
            flash('Cliente actualizado satisfactoriamente')
            return redirect(url_for('updateClient'))   
    return render_template('update.html', id = True, route = 'client')

@app.route('/api/update/client/<string:id>', methods=['POST'])
def apiUpdateClient (id):
    if request.method == 'POST':
        client = Client.query.get(id)
        data = json.loads(request.data)
        if len(client) == 0:
            return "Registro no encontrado", 402  
        else:
            client.name = data['name']
            client.document = data['document']
            db.session.add(client)
            db.session.commit()
            return "Registro modificado", 200  

#Modificar producto
@app.route('/update/product', methods=['GET', 'POST'])
def updateProduct ():
    if request.method == 'POST':
        id = request.form['id']
        if id == "true":
            productid = request.form['productid']
            product = Product.query.filter_by(productid = productid, state = 'activo').all()
            if len(product) == 0:
                flash('Producto no encontrado') 
                return render_template('update.html', id = True, route = 'product')
            else:
                return render_template('update.html', id = False, records = product, route = 'product')
        else:
            productid = request.form['product']
            name = request.form['name']
            price = request.form['price']
            product = Product.query.get(productid)
            product.name = name
            product.price = price
            db.session.add(product)
            db.session.commit()
            flash('Producto actualizado satisfactoriamente')
            return redirect(url_for('updateProduct'))   
    return render_template('update.html', id = True, route = 'product')

@app.route('/api/update/product/<string:id>', methods=['POST'])
def apiUpdateProduct (id):
    if request.method == 'POST':
        product = Product.query.get(id)
        data = json.loads(request.data)
        if len(product) == 0:
            return "Registro no encontrado", 402  
        else:
            product.name = data['name']
            product.price = data['price']
            db.session.add(product)
            db.session.commit()
            return "Registro modificado", 200  

#Modificar orden
@app.route('/update/order', methods=['GET', 'POST'])
def updateOrder ():
    if request.method == 'POST':
        id = request.form['id']
        if id == "true":
            orderid = request.form['orderid']
            order = Order.query.filter_by(orderid = orderid, state = 'pendiente').all()
            if len(order) == 0:
                flash('Orden no encontrada') 
                return render_template('update.html', id = True, route = 'order')
            else:
                return render_template('update.html', id = False, records = order, route = 'order')
        else:
            orderid = request.form['order']
            clientid = request.form['clientid']
            productid = request.form['productid']
            quantity = request.form['quantity']
            splProductid = productid.split(sep = ',')
            splQuantity = quantity.split(sep = ',')            
            count = 0
            client = Client.query.filter_by(clientid = clientid, state = 'activo').all()
            if len(client) == 0:
                flash('Cliente no encontrado') 
                return render_template('create.html', id = True, route = 'order')
            for spl in splProductid:
                product = Product.query.filter_by(productid = spl, state = 'activo').all()
                if len(product) == 0:
                    flash('Producto no encontrado') 
                    return render_template('create.html', id = True, route = 'order')       
                order = Order.query.get(orderid)
                order.clientid = clientid
                order.productid = spl
                order.quantity = splQuantity[count]
                order.total = product[0].price * int(splQuantity[count])
                db.session.add(order)
                db.session.commit()
                count = count + 1
            flash('Orden actualizada satisfactoriamente')
            return redirect(url_for('updateOrder'))   
    return render_template('update.html', id = True, route = 'order')

@app.route('/api/update/order/<string:id>', methods=['POST'])
def apiUpdateOrder (id):
    if request.method == 'POST':
        order = Order.query.get(id)
        data = json.loads(request.data)
        if len(order) == 0:
            return "Registro no encontrado", 402  
        else:
            order.clientid = data['clientid']
            order.productid = data['productid']
            order.quantity = data['quantity']
            order.total = data['total']
            db.session.add(order)
            db.session.commit()
            return "Registro modificado", 200  

#Pagar compra
@app.route('/update/purchase', methods=['GET', 'POST'])
def updatePurchase ():
    if request.method == 'POST':
        id = request.form['id']
        if id == "true":
            clientid = request.form['clientid']
            client = Client.query.filter_by(clientid = clientid, state = 'activo').all()
            if len(client) == 0:
                flash('Cliente no encontrado') 
                return render_template('update.html', id = True, route = 'purchase')
            else:
                order = Order.query.filter_by(clientid = clientid, state = 'pendiente').all()
                if len(order) == 0:
                    flash('Orden no encontrada')
                    return render_template('update.html', id = True, route = 'purchase')
                return render_template('update.html', id = False, records = order, route = 'purchase')
        else:
            clientid = request.form['client']  
            orders = Order.query.filter_by(clientid = clientid).all()
            for order in orders:
                order.state = 'pagada'
                db.session.add(order)
                db.session.commit()
            flash('Orden pagada satisfactoriamente')
            return redirect(url_for('updatePurchase'))   
    return render_template('update.html', id = True, route = 'purchase')

@app.route('/api/update/purchase/<string:id>', methods=['POST'])
def apiUpdatePurchse (id):
    if request.method == 'POST':
        client = Client.query.get(id)
        data = json.loads(request.data)
        if len(client) == 0:
            return "Registro no encontrado", 402  
        else:
            orders = Order.query.filter_by(clientid = id).all()
            for order in orders:
                order.state = 'pagada'
                db.session.add(order)
                db.session.commit()
            return "Registro modificado", 200  

if __name__ == '__main__':    
    app.run(host='0.0.0.0', debug=True)