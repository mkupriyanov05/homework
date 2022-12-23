from flask import render_template, request
from setup import app, db
from tables import Products


@app.route('/')
def home_page():
    return render_template('index.html', is_home=True)

@app.route('/table')
def table():
    products = db.session.execute(db.select(Products)).scalars().all()
    return render_template('table.html', columns=Products().get_columns(), products=products)

@app.route('/edit', methods=['GET', 'POST'])
def edit_page():
    id = request.form.get('id')
    new_val = request.form.get('new_val')
    if id and new_val:
        db.engine.execute(f'UPDATE products SET count = {new_val} WHERE id = {id}')
        db.session.commit()
    return render_template('edit.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_page():
    id = request.form.get('id')
    if id:
        db.engine.execute(f'DELETE FROM products WHERE id = {id}')
    return render_template('delete.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        products = db.session.execute(db.select(Products)).scalars().all()
        if len(products) == 0:
            db.session.add(Products(product='potato', product_description='epic potato very tasty', count=10))
            db.session.add(Products(product='milk', product_description='miiiiiiiiiilk tasty', count=22))
            db.session.add(Products(product='eggs', product_description='eggs from chicken very tasty buy', count=1000))
            db.session.add(Products(product='water', product_description='Delicious water from the mountain rivers', count=3))

            db.session.commit()

    app.run()
