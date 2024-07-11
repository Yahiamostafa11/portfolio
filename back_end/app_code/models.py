from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

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
    __tablename__ = TABLE_NAMES['categories']
    category_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)

class Product(Base):
    """Product model"""
    __tablename__ = TABLE_NAMES['products']
    product_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["categories"]}.category_id'))
    category = relationship('Category', backref='products')

class Customer(Base):
    """Customer model"""
    __tablename__ = TABLE_NAMES['customers']
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(50))
    address = Column(Text)

class Order(Base):
    """Order model"""
    __tablename__ = TABLE_NAMES['orders']
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["customers"]}.customer_id'))
    customer = relationship('Customer', backref='orders')
    order_date = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)

class OrderDetail(Base):
    """OrderDetail model"""
    __tablename__ = TABLE_NAMES['order_details']
    order_detail_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["orders"]}.order_id'))
    order = relationship('Order', backref='order_details')
    product_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["products"]}.product_id'))
    product = relationship('Product', backref='order_details')
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

class Supplier(Base):
    """Supplier model"""
    __tablename__ = TABLE_NAMES['suppliers']
    supplier_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    contact_person = Column(String(255), nullable=False)
    phone = Column(String(50))
    email = Column(String(255))
    address = Column(Text)

class Inventory(Base):
    """Inventory model"""
    __tablename__ = TABLE_NAMES['inventory']
    inventory_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["products"]}.product_id'))
    product = relationship('Product', backref='inventory')
    supplier_id = Column(Integer, ForeignKey(f'{TABLE_NAMES["suppliers"]}.supplier_id'))
    supplier = relationship('Supplier', backref='inventory')
    quantity = Column(Integer, nullable=False)
    received_date = Column(DateTime, nullable=False)