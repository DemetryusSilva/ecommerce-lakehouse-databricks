import pandas as pd
import random
import uuid
from datetime import datetime, timedelta
import os

# Gatantir diretório
os.makedirs("data/raw", exist_ok=True)

# ---------------
# 1. Customers
# ---------------

customers = []
for i in range(1000):
    customers.append({
        "customer_id": str(uuid.uuid4()),
        "name": f"Customer_{i}",
        "email": f"customer_{i}@email.com",
        "country": random.choice(["Brazil", "USA", "Portugal", None]),
        "created_at": datetime.now() - timedelta(days=random.randint(1, 1000))
    })

df_customers = pd.DataFrame(customers)
df_customers.to_csv("data/raw/customers.csv", index=False)

# ---------------
# 2. Products
# ---------------

products = []
categories = ["Electronics", "Clothing", "Books", "Home"]

for i in range(200):
    products.append({
        "product_id": str(uuid.uuid4()),
        "name": f"Product_{i}",
        "category": random.choice(categories),
        "price": round(random.uniform(10, 500), 2)
    })

df_products = pd.DataFrame(products)
df_products.to_csv("data/raw/products.csv", index=False)

# ---------------
# 3. Orders
# ---------------

orders = []
for i in range(3000):
    orders.append({
        "order_id": str(uuid.uuid4()),
        "customer_id": random.choice(df_customers["customer_id"].tolist()),
        "order_date": datetime.now() - timedelta(days=random.randint(1, 365)),
        "status": random.choice(["created", "shipped", "delivered", "cancelled", None])
    })

    df_orders = pd.DataFrame(orders)
    df_orders.to_csv("data/raw/orders.csv", index=False)

# ---------------
# 4. Order Items
# ---------------

order_items = []

for order_id in df_orders["order_id"]:
    for _ in range(random.randint(1, 5)):
        product = df_products.sample(1).iloc[0]
        quantity = random.randint(1, 3)
        order_items.append({
            "order_id": order_id,
            "product_id": product["product_id"],
            "quantity": quantity,
            "unit_price": product["price"]
        })

df_order_items = pd.DataFrame(order_items)
df_order_items.to_csv("data/raw/order_items.csv", index=False)

print("Dados gerados com sucesso!")