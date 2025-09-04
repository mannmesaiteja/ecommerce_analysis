create database ecommerce_analytics;
use ecommerce_analytics;

CREATE table customers(
customer_id int auto_increment primary key,
name varchar(40),
email varchar(40) unique,
sign_up date,
country varchar(20)
);

create table products(
product_id int primary key auto_increment,
product_name varchar(100),
category varchar(100),
price decimal
);

create table orders(
order_id int auto_increment primary key,
customer_id int,
order_date date,
status enum("completed", "cancelled", "pending"),
foreign key(customer_id) references customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    total_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    payment_method ENUM('Credit Card','Debit Card','PayPal','UPI'),
    payment_status ENUM('Paid','Failed','Pending'),
    amount DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

