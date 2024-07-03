create database project_db;

CREATE TABLE Categories (
	    category_id INT AUTO_INCREMENT PRIMARY KEY,
	    name VARCHAR(50) NOT NULL,
	    description TEXT
);

CREATE TABLE Products (
	    product_id INT AUTO_INCREMENT PRIMARY KEY,
	    name VARCHAR(50) NOT NULL,
	    description TEXT,
	    price DECIMAL(10, 2) NOT NULL,
	    stock_quantity INT NOT NULL,
	    category_id INT,
	    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Customers (
	    customer_id INT AUTO_INCREMENT PRIMARY KEY,
	    first_name VARCHAR(50) NOT NULL,
	    last_name VARCHAR(50) NOT NULL,
	    email VARCHAR(100) NOT NULL,
	    phone VARCHAR(50),
	    address TEXT
);

CREATE TABLE Orders (
	    order_id INT AUTO_INCREMENT PRIMARY KEY,
	    customer_id INT,
	    order_date DATETIME NOT NULL,
	    status VARCHAR(50) NOT NULL,
	    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE OrderDetails (
	    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
	    order_id INT,
	    product_id INT,
	    quantity INT NOT NULL,
	    price DECIMAL(10, 2) NOT NULL,
	    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
	    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Suppliers (
	    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
	    name VARCHAR(255) NOT NULL,
	    contact_person VARCHAR(255) NOT NULL,
	    phone VARCHAR(50),
	    email VARCHAR(255),
	    address TEXT
);

CREATE TABLE Inventory (
	    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
	    product_id INT,
	    supplier_id INT,
	    quantity INT NOT NULL,
	    received_date DATETIME NOT NULL,
	    FOREIGN KEY (product_id) REFERENCES Products(product_id),
	    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);
