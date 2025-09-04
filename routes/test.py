import requests

x = requests.post(" http://127.0.0.1:5000/customers").json()
print(x['total_customers'])