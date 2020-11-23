from flask import url_for,redirect,render_template,flash
from flaskblog import app,db
from flaskblog.models import item


@app.route("/")
@app.route("/home")
def home():
    items = item.query.all()
    length = len(items)
    return render_template('home.html',length=length)

@app.route("/cart")
def cart():
    items = item.query.all()
    total = 0
    for i in items:
       total = total + i.cart_price
    return render_template('cart.html',items = items,length = len(items),total_price =total)

@app.route("/addtocart/<item_name>/<item_price>/<price_cart>")
def addtocart(item_name,item_price,price_cart):
    ite = item.query.filter_by(name=item_name).first()
    image = item_name +".png"
    image_file = url_for('static',filename = 'images/' + image)
    if(ite is None):
          items = item(name=item_name,price=item_price,cart_price=price_cart,images = image_file)
          db.session.add(items)
          db.session.commit()
    
    else:
          flash('Already added this Item in the cart')
          return redirect(url_for('home'))
    
    return redirect(url_for('home'))


@app.route("/plus/<item_name>")
def sayPlus(item_name):
    cart_no =  item.query.filter_by(name=item_name).first()
    cart_no.cart = cart_no.cart +1
    cart_no.cart_price = cart_no.price * cart_no.cart
    db.session.commit()
    return redirect(url_for('cart'))

@app.route("/minus/<item_name>")
def sayMinus(item_name):
    items = item()
    cart_no =  items.query.filter_by(name=item_name).first()
    cart_no.cart = cart_no.cart -1
    cart_no.cart_price = cart_no.price * cart_no.cart
    if(cart_no.cart == 0 ):
        db.session.delete(cart_no)
    db.session.commit()
    return redirect(url_for('cart'))

