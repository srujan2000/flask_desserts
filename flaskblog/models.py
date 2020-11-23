from flaskblog import db

class item(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    name = db.Column(db.String(30),nullable = False)
    price = db.Column(db.Integer, nullable = False)
    cart = db.Column(db.Integer,nullable=False,default = 1)
    cart_price = db.Column(db.Integer,nullable=False,default = price)
    images = db.Column(db.String(30),nullable = False)

    def __repr__(self):
        return f"items('{self.id}','{self.name}','{self.price}','{self.cart}','{self.cart_price}','{self.images}')"