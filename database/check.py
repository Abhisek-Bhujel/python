import getpass
import oracledb

# pw = getpass.getpass("Enter password: ")

connection = oracledb.connect(user="system", password="system", dsn="localhost/xepdb1")
cursor = connection.cursor()

new_email = "anotherupdate@update.com"
phone = input("Please enter the phone number to update: ")  # 1254896

update_cursor = connection.cursor()


update_cursor.execute(
    """
                UPDATE contacts 
                SET email = :email
                WHERE phone = :phone
               """,
    {"email": new_email, "phone": phone},
)

print("{} rows updated".format(update_cursor.rowcount))

# commit changes
connection.commit

cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()
