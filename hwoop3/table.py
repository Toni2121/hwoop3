import sqlite3
from FoodProduct import FoodProduct  # Assuming you have your FoodProduct class defined


def select_all_products(my_cursor):
    # Execute the SELECT query to fetch all rows
    my_cursor.execute("SELECT * FROM FoodProducts")
    rows = my_cursor.fetchall()

    # Create a list of FoodProduct objects from the query results
    product_list = []
    for row in rows:
        product = FoodProduct(
            name=row["name"],
            price=row["price"],
            category=row["category"],
            production_date=row["production_date"],
            expiration_date=row["expiration_date"]
        )
        product_list.append(product)

    return product_list


# Usage example
conn = sqlite3.connect("hwoop3.db")
conn.row_factory = sqlite3.Row  # Allows using column names
cursor = conn.cursor()

# Fetch all products
products = select_all_products(cursor)

# Print the list of products
for product in products:
    print(product)

conn.close()
