from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey, Index, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class for declarative class definitions
Base = declarative_base()

# Dictionary to hold table names for consistency
TABLE_NAMES = {
    'categories': 'Categories',
    'products': 'Products',
    'customers': 'Customers',
    'orders': 'Orders',
    'order_details': 'OrderDetails',
    'suppliers': 'Suppliers',
    'inventory': 'Inventory'
}

class Category(Base):
    """Category model"""
    _tablename_ = TABLE_NAMES['categories']
    category_id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String(50), nullable=False)  # Category name
    description = Column(Text)  # Description of the category

class Product(Base):
    """Product model"""
    _tablename_ = TABLE_NAMES['products']
    product_id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String(50), nullable=False)  # Product name
    description = Column(Text)  # Product description
    price = Column(Numeric(10, 2), nullable=False)  # Price of the product
    stock_quantity = Column(Integer, nullable=False)  # Stock quantity available
    category_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["categories"]}.category_id'))  # Foreign key to categories
    category = relationship('Category', backref='products', lazy='dynamic')  # Relationship to Category

class Customer(Base):
    """Customer model"""
    _tablename_ = TABLE_NAMES['customers']
    customer_id = Column(Integer, primary_key=True)  # Primary key
    first_name = Column(String(50), nullable=False)  # First name
    last_name = Column(String(50), nullable=False)  # Last name
    email = Column(String(100), nullable=False)  # Email address
    phone = Column(String(50))  # Phone number
    address = Column(Text)  # Address
    _table_args_ = (Index('idx_customer_email', 'email'),)  # Index on email for faster queries

class OrderStatus(Enum):
    """Enum for order status"""
    PENDING = 'pending'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'

class Order(Base):
    """Order model"""
    _tablename_ = TABLE_NAMES['orders']
    order_id = Column(Integer, primary_key=True)  # Primary key
    customer_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["customers"]}.customer_id', ondelete='CASCADE'))  # Foreign key to customers
    customer = relationship('Customer', backref='orders', lazy='dynamic')  # Relationship to Customer
    order_date = Column(DateTime, nullable=False)  # Date of the order
    status = Column(Enum(OrderStatus), nullable=False)  # Status of the order

class OrderDetail(Base):
    """OrderDetail model"""
    _tablename_ = TABLE_NAMES['order_details']
    order_detail_id = Column(Integer, primary_key=True)  # Primary key
    order_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["orders"]}.order_id', ondelete='CASCADE'))  # Foreign key to orders
    order = relationship('Order', backref='order_details', lazy='dynamic')  # Relationship to Order
    product_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["products"]}.product_id'))  # Foreign key to products
    product = relationship('Product', backref='order_details', lazy='dynamic')  # Relationship to Product
    quantity = Column(Integer, nullable=False)  # Quantity of the product ordered
    price = Column(Numeric(10, 2), nullable=False)  # Price of the product

class Supplier(Base):
    """Supplier model"""
    _tablename_ = TABLE_NAMES['suppliers']
    supplier_id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String(255), nullable=False)  # Supplier name
    contact_person = Column(String(255), nullable=False)  # Contact person at the supplier
    phone = Column(String(50))  # Phone number
    email = Column(String(255))  # Email address
    address = Column(Text)  # Address

class Inventory(Base):
    """Inventory model"""
    _tablename_ = TABLE_NAMES['inventory']
    inventory_id = Column(Integer, primary_key=True)  # Primary key
    product_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["products"]}.product_id'))  # Foreign key to products
    product = relationship('Product', backref='inventory', lazy='dynamic')  # Relationship to Product
    supplier_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["suppliers"]}.supplier_id'))  # Foreign key to suppliers
    supplier = relationship('Supplier', backref='inventory', lazy='dynamic')  # Relationship to Supplier
    quantity = Column(Integer, nullable=False)  # Quantity in inventory
    received_date = Column(DateTime, nullable=False)  # Date the inventory was received