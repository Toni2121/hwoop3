import sqlite3
from pprint import pprint
from FoodProduct import FoodProduct

# Connect to the SQLite database
conn = sqlite3.connect("hwoop3.db")
conn.row_factory = sqlite3.Row  # Allows using column names
cursor = conn.cursor()  # Create cursor

# Create the FoodProducts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS FoodProducts (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL,
    production_date TEXT NOT NULL,
    expiration_date TEXT NOT NULL
);
''')
conn.commit()


def insert_product(my_cursor, product_insert: FoodProduct):
    query = '''
    INSERT INTO FoodProducts (name, price, category, production_date, expiration_date)
    VALUES (?, ?, ?, ?, ?)
    '''
    my_cursor.execute(query, (
        product_insert.name,
        product_insert.price,
        product_insert.category,
        product_insert.production_date,
        product_insert.expiration_date
    ))
    my_cursor.connection.commit()


# Create a FoodProduct object
product1 = FoodProduct('cheese', 9.99,
                       "Dairy",
                       "2024-12-17",  # Format in YYYY-MM-DD
                       "2025-02-02")

# Insert product into the database
insert_product(cursor, product1)

# Optional: Print the inserted data to verify
cursor.execute("SELECT * FROM FoodProducts")
rows = cursor.fetchall()
for row in rows:
    pprint(dict(row))

# Close the connection
conn.close()
