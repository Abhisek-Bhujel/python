import getpass
import oracledb

# Prompt for password securely
pw = getpass.getpass("Enter password: ")

try:
    # Establish Thin-mode connection (no Oracle client required)
    connection = oracledb.connect(user="system", password=pw, dsn="localhost/xepdb1")
    print("Successfully connected to Oracle Database")
except oracledb.DatabaseError as e:
    print(f"Error connecting to Oracle: {e}")
    exit(1)

cursor = connection.cursor()

cursor.execute("DROP TABLE contacts")

cursor.execute(
    """
               CREATE TABLE contacts (
                   name VARCHAR(100),
                   phone NUMBER, 
                   email VARCHAR(100)
            )
        """
)
cursor.execute(
    "INSERT INTO contacts(name, phone, email) VALUES(:1, :2, :3)",
    ("Tim", 6545678, "tim@email.com"),
)
cursor.execute(
    "INSERT INTO contacts(name, phone, email) VALUES(:1, :2, :3)",
    ("Brian", 1254896, "brian@email.com"),
)

#Commit transaction
connection.commit()

print("Table created and data inserted Successfully")



# --- Query Data ---
cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()
print("All rows:")
print(rows)
print("*" * 50)
print("Query result:")
for row in rows:
    print(row)
    print("*" * 50)
    

#close cursor and connection
cursor.close()
connection.close()
