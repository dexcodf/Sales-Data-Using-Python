import sqlite3

# Step 1: Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create the sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')

# Step 4: (Optional) Insert sample data into the sales table
sample_data = [
    ('Product A', 10, 15.50),
    ('Product B', 5, 20.00),
    ('Product C', 8, 7.25)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully with sample data.")
