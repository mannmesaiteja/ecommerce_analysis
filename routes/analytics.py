from flask import Flask, request, jsonify
import db_connection

app = Flask(__name__)

conn = db_connection.get_connection()
cursor = conn.cursor()

@app.route("/customers", methods=['POST', 'GET'])
def customers_analysis():
    req_data = request.get_json()
    cursor.execute("select count(*) from customers")
    total_customers = cursor.fetchone() # gives you first matched row in the form of tuple
    cursor.execute("select * from customers where sign_up between %s and %s", (req_data["start_date"], req_data["end_date"]))
    new_customers = cursor.fetchall()
    cursor.execute(
        """
        select  customers.name, count(order_items.order_id) as no_of_order_items
        from customers
        join orders
        on customers.customer_id = orders.customer_id
        join order_items
        on orders.order_id = order_items.order_id
        group by customers.customer_id, customers.name
        order by no_of_orders
        
        """
    ) # number of order items per customer
    no_of_oitemspc = cursor.fetchall()
    cursor.execute(
        """
        select  customers.name, count(distinct order_items.order_id) as no_of_orders, sum(order_items.total_price)
        from customers
        join orders
        on customers.customer_id = orders.customer_id
        join order_items
        on orders.order_id = order_items.order_id
        group by customers.customer_id
        """
    )  # number of orders per customer
    no_orders = cursor.fetchall()

    # top customers by revenue.
    cursor.execute(
        """
        select customers.name, sum(order_items.total_price) as price
        from customers
        join orders 
        on customers.customer_id = orders.customer_id
        join order_items
        on orders.order_id = order_items.order_id
        group by customers.customer_id
        order by price desc
        """
    )
    return jsonify({"total_customers": no_of_oitemspc})

@app.route("/product", methods=["POST", "GET"])
def product_analysis():
    req_data = request.get_json()
    cursor.execute(
        """
        select product_name, category
        from products
        """
    )
    # here we used formula for total_revenue = total_price * quantity
    # Top Products by Revenue
    if req_data["top_selling_products"]:
        cursor.execute(
            """
            select product_name, category, sum(order_items.total_price * order_items.quantity) as total_revenue
            from products
            join order_items
            on order_items.product_id = products.product_id
            group by products.product_id, products.product_name
            order by total_revenue desc
            limit 10
            """
        )
        top_revenue_products = cursor.fetchall()
    # top products by quantity
    if req_data["top_products_by_quantity"]:
        cursor.execute(
            """
            select product_name, category, products.product_id, sum(order_items.quantity) as total_quantity
            from products
            join order_items
            on order_items.product_id = products.product_id
            group by products.product_id, products.product_name
            order by total_quantity desc
            limit 10
            """
        )
        top_sold_items = cursor.fetchall()
    # category-wise sales breakdown

@app.route("/order_analysis", methods = ["POST", "GET"])
def order_analysis():
    req_data = request.get_json()
    cursor.execute(
        """
        select count(*)
        from orders
        """
    )
    total_orders = cursor.fetchone()
    cursor.execute(
        """
        select count(*)
        from orders
        where status = "completed"
        """
    )
    completed_orders = cursor.fetchone()
    cursor.execute(
        """
        select count(*)
        from orders
        where status = "pending"
        """
    )
    pending = cursor.fetchone()
    cursor.execute(
        """
        select count(*)
        from orders
        where status = "cancelled"
        """
    )
    cancelled = cursor.fetchone()
    # gives all orders in a given date range
    cursor.execute(
        """
        select *
        from orders
        where order_date between %s and %s
        """,
        (req_data["start_date"], req_data["end_date"])
    )
    date_range_orders = cursor.fetchall()
    # monthly orders
    cursor.execute(
        """
        select year(order_date), month(order_date), count(order_id) as total_orders
        from orders
        group by year(order_date), month(order_date)
        order by year(order_date), month(order_date)
        """
    )
    monthly_orders = cursor.fetchall()
    return {"total_orders": total_orders[0], "completed_orders": completed_orders[0], "pending": pending[0],
            "cancelled": cancelled[0], "date_range_orders": date_range_orders, "monthly_orders": monthly_orders}


app.run(debug=True)