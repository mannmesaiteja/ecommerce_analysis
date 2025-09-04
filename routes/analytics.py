from flask import Flask, request, jsonify
import db_connection

app = Flask(__name__)

@app.route("/customers", methods=['POST', 'GET'])
def customers_analysis():
    # req_data = request.get_json()
    conn = db_connection.get_connection()
    cursor = conn.cursor()
    cursor.execute("select count(*) from customers")
    total_customers = cursor.fetchone() # gives you first matched row in the form of tuple
    # cursor.execute("select * from customers where sign_up between %s and %s", (req_data["start_date"], req_data["end_date"]))
    # new_customers = cursor.fetchall()
    cursor.execute(
        """
        select name, count( 
        from customers
        join orders
        on customers.customer_id = orders.customer_id
        """
    )
    orders = cursor.fetchall()
    print(orders)
    return jsonify({"total_customers": orders})



app.run(debug=True)