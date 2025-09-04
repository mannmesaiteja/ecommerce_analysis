-- Insert Customers
INSERT INTO customers (name, email, signup_date, country) VALUES
('John Doe', 'john@example.com', '2023-01-15', 'USA'),
('Jane Smith', 'jane@example.com', '2023-02-10', 'India'),
('Michael Lee', 'michael@example.com', '2023-03-05', 'UK'),
('Sara Connor', 'sara@example.com', '2023-04-12', 'Canada'),
('David Miller', 'david@example.com', '2023-05-18', 'Australia');

-- Insert Products
INSERT INTO products (product_name, category, price) VALUES
('Wireless Mouse', 'Electronics', 15.99),
('Mechanical Keyboard', 'Electronics', 79.99),
('Water Bottle', 'Home', 12.50),
('Yoga Mat', 'Fitness', 25.00),
('LED Monitor', 'Electronics', 199.99);

-- Insert Orders
INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2023-07-01', 'Completed'),
(2, '2023-07-05', 'Completed'),
(3, '2023-07-10', 'Cancelled'),
(4, '2023-07-15', 'Completed'),
(5, '2023-07-18', 'Pending');

-- Insert Order Items
INSERT INTO order_items (order_id, product_id, quantity, total_price) VALUES
(1, 1, 2, 31.98),
(1, 2, 1, 79.99),
(2, 3, 3, 37.50),
(3, 4, 1, 25.00),
(4, 5, 2, 399.98),
(5, 1, 1, 15.99);

-- Insert Transactions
INSERT INTO transactions (order_id, payment_method, payment_status, amount) VALUES
(1, 'Credit Card', 'Paid', 111.97),
(2, 'UPI', 'Paid', 37.50),
(3, 'Debit Card', 'Failed', 25.00),
(4, 'PayPal', 'Paid', 399.98),
(5, 'Credit Card', 'Pending', 15.99);
