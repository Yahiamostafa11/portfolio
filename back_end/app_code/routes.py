from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db  # Import the Flask app instance and SQLAlchemy database object
from models import User, Product, Order, OrderProduct  # Import database models
from forms import LoginForm  # Import LoginForm from forms.py

# Index route: Displays the main page
@app.route('/')
def index():
    return render_template('index.html')

# Login route: Handles user login and authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Create an instance of LoginForm
    if form.validate_on_submit():  # If the form is submitted and valid
        user = User.query.filter_by(username=form.username.data).first()  # Query the User table for the username
        if user and user.password == form.password.data:  # If user exists and password matches
            login_user(user)  # Log in the user
            flash('Logged in successfully!', 'success')  # Flash success message
            return redirect(url_for('index'))  # Redirect to the main page
        else:
            flash('Invalid username or password', 'error')  # Flash error message
    return render_template('login.html', form=form)  # Render login template with LoginForm instance

# Logout route: Logs out the current user
@app.route('/logout')
@login_required  # Requires the user to be logged in
def logout():
    logout_user()  # Log out the user
    flash('Logged out successfully!', 'success')  # Flash success message
    return redirect(url_for('index'))  # Redirect to the main page

# Products route: Displays all products
@app.route('/products')
@login_required  # Requires the user to be logged in
def products():
    products = Product.query.all()  # Query all products from the Product table
    return render_template('products.html', products=products)  # Render products template with products data

# Order product route: Handles ordering a product
@app.route('/order/<int:product_id>', methods=['POST'])
@login_required  # Requires the user to be logged in
def order_product(product_id):
    product = Product.query.get_or_404(product_id)  # Get the product by product_id or return 404 if not found

    # Example: Create an order for the current user
    order = Order(customer_id=current_user.id)  # Create an Order instance for the current user
    db.session.add(order)  # Add the order to the session

    # Example: Add the selected product to the order
    order_product = OrderProduct(order_id=order.id, product_id=product.id)  # Create an OrderProduct instance
    db.session.add(order_product)  # Add the order product to the session

    db.session.commit()  # Commit changes to the database

    flash(f'Ordered {product.name} successfully!', 'success')  # Flash success message
    return redirect(url_for('products'))  # Redirect to the products page

# Error handler for 404: Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Render 404 error template

# Error handler for 500: Internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500  # Render 500 error template