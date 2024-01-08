import sqlite3

# Connect to SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 28))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 34))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 22))

# Commit the changes to the database
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the retrieved data
print("Users:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Close the connection
conn.close()
