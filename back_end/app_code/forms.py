from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField, IntegerField, 
    SelectField, DecimalField, TextAreaField, DateField
)
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional, URL, ValidationError
from wtforms.widgets import TextArea

# Custom validator for stock quantity
def validate_stock(form, field):
    if field.data < 0:
        raise ValidationError("Stock cannot be negative")

class RegistrationForm(FlaskForm):
    # User registration form with detailed validators
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    # User login form
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProductForm(FlaskForm):
    # Form to add or update product details
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=500)])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    supplier_id = SelectField('Supplier', coerce=int, validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired(), validate_stock])
    image_url = StringField('Image URL', validators=[Optional(), URL()])
    submit = SubmitField('Add Product')

class OrderForm(FlaskForm):
    # Form to place or update an order
    customer_id = SelectField('Customer', coerce=int, validators=[DataRequired()])
    status = SelectField('Status', choices=[
        ('Pending', 'Pending'), ('Shipped', 'Shipped'), 
        ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')
    ], validators=[DataRequired()])
    order_date = DateField('Order Date', format='%Y-%m-%d', validators=[DataRequired()])
    delivery_date = DateField('Delivery Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Place Order')

class CategoryForm(FlaskForm):
    # Form to add or update a category
    name = StringField('Category Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Add Category')

class SupplierForm(FlaskForm):
    # Form to add or update supplier details
    name = StringField('Supplier Name', validators=[DataRequired()])
    contact_info = TextAreaField('Contact Info', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Add Supplier')

class CustomerForm(FlaskForm):
    # Form to add or update customer details
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Optional(), Length(max=15)])
    address = TextAreaField('Address', validators=[DataRequired(), Length(max=200)], widget=TextArea())
    submit = SubmitField('Add Customer')