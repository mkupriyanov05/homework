from setup import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(20), nullable=False, unique=True)
    product_description = db.Column(db.String(100), nullable=False)
    count = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Product({self.product}, {self.count})'

    def get_columns(self):
        return [column.name for column in self.__table__.c]

    def get_data(self):
        return [getattr(self, data_name) for data_name in self.get_columns()]
