import getpass
import oracledb
import datetime

# Prompt for user name
username = input("Enter username: ")

# Prompt for password securely
pw = getpass.getpass("Enter password: ")

#prompt for filepath
filePath = input("Enter filepath:  ")

try:
    # Connect to GMU Oracle Database (Thin mode)
    connection = oracledb.connect(
        user= username,
        password= pw,
        dsn="artemis.vsnet.gmu.edu:1521/vse18c.vsnet.gmu.edu",
    )
    print("Successfully connected to GMU Oracle Database")
except oracledb.DatabaseError as e:
    print(f"Error connecting to Oracle: {e}")
    exit(1)

cursor = connection.cursor()

# Drop table if it exists (optional, for fresh start)
try:
    cursor.execute("DROP TABLE Workshops")
    cursor.execute("DROP TABLE Registrations")
except oracledb.DatabaseError:
    # Ignore if table does not exist
    pass

# Create table

with open(filePath, "r") as f:
    sql_commands = f.read()


# Split commands by semicolon
commands = sql_commands.split(";")


# Execute each command separately
for command in commands:
    # Strip whitespace, newlines 
    cmd = command.strip()
    # Only execute if cmd is non-empty
    if cmd:
        try:
            cursor.execute(cmd)
        except oracledb.DatabaseError:
            pass


# Commit connection
connection.commit()

# Helper functions
def display_menu():
    print("Menu:")
    print("1. View table contents")
    print("2. Search workshops")
    print("3. Show registered students")
    print("4. Register a new student")
    print("5. Delete a registration")
    print("6. Exit")


def display_table_menu():
    print("Which Table content do you want to view:")
    print("1. Workshops")
    print("2. Registrations")


def display_search_workshops_menu():
    print("Search Workshops by: ")
    print("1. Workshop-ID")
    print("2. Title")
    print("3. Category")


def display_show_registered_students_menu():
    print("Search Registered Students by: ")
    print("1. Workshop-ID")
    print("2. Title")


while True:
    display_menu()
    choice = input("Choose the option from the menu: ")
    if choice == "6":
        print("You exited the Program")
        break

    if choice == "1":
        display_table_menu()
        table_choice = input()
        if table_choice == "1":
            cursor.execute("SELECT * FROM Workshops")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        elif table_choice == "2":
            cursor.execute("SELECT * FROM Registrations")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        else:
            print("Invalid Choice")

    elif choice == "2":
        display_search_workshops_menu()
        search_workshops_choice = input()
        if search_workshops_choice == "1":
            workshop_id = int(input("Provide Workshop-ID: "))
            cursor.execute(
                "SELECT * FROM Workshops WHERE WorkshopID = :1", (workshop_id,)
            )
            rows = cursor.fetchall()
            if not rows:
                print("No workshops found matching that Workshop-ID.")
            else:
                for row in rows:
                    print(row)
            print()

        elif search_workshops_choice == "2":
            title = input("Provide Title: ")
            cursor.execute(
                "SELECT * FROM Workshops WHERE LOWER(Title) LIKE :1",
                ("%" + title.lower() + "%",),
            )
            rows = cursor.fetchall()
            if not rows:
                print("No workshops found matching that title.")
            else:
                for row in rows:
                    print(row)
            print()

        elif search_workshops_choice == "3":
            category = input("Provide Category: ")
            cursor.execute(
                "SELECT * FROM Workshops WHERE LOWER(Category) LIKE :1",
                ("%" + category.lower() + "%",),
            )
            rows = cursor.fetchall()
            if not rows:
                print("No workshops found matching that Category.")
            else:
                for row in rows:
                    print(row)
            print()

        else:
            print("Invalid choice")

    elif choice == "3":
        display_show_registered_students_menu()
        show_registered_students_choice = input()
        if show_registered_students_choice == "1":
            workshop_id = int(input("Provide Workshop-ID: "))
            cursor.execute(
                "SELECT StudentID FROM Registrations WHERE WorkshopID = :1",
                (workshop_id,),
            )
            rows = cursor.fetchall()
            number_of_rows = cursor.rowcount
            if not rows:
                print("No StudentID found matching that WorkshopID.")
            else:
                for row in rows:
                    print(row)
            print(
                f"Total number of student registered for this workshop are {number_of_rows}"
            )
            print()

        elif show_registered_students_choice == "2":
            title = input("Provide Workshop Title: ")
            cursor.execute(
                """
                SELECT StudentID
                FROM Registrations r
                INNER JOIN Workshops w
                    ON r.WorkshopID = w.WorkshopID
                WHERE LOWER(Title) LIKE :1
                
                """,
                ("%" + title.lower() + "%",),
            )
            rows = cursor.fetchall()
            number_of_rows = cursor.rowcount
            if not rows:
                print("No StudentID found matching this Title.")
            else:
                for row in rows:
                    print(row)
            print(
                f"Total number of student registered for this workshop are {number_of_rows}"
            )
            print()

        else:
            print("Invalid choice")

    elif choice == "4":
        workshop_id = int(input("Provide Workshop-ID: "))
        student_id = input("Provide StudentID: ")
        cursor.execute(
            """ 
                    SELECT WorkshopID
                    FROM Workshops
                """
        )

        available_workshop_ids = []
        for row in cursor.fetchall():
            available_workshop_ids.append(row[0])

        if workshop_id not in available_workshop_ids:
            print(f"Error: WorkshopID {workshop_id} not available")
            continue

        cursor.execute(
            """ 
                SELECT Capacity
                FROM Workshops
                WHERE WorkshopID = :1
            """,
            (workshop_id,),
        )
        result = cursor.fetchone()
        capacity = result[0]

        cursor.execute(
            """ 
                    SELECT COUNT(*)
                    FROM Registrations
                    WHERE WorkshopID = :1
                """,
            (workshop_id,),
        )

        result = cursor.fetchone()
        total_students_in_workshop = result[0]

        if capacity <= total_students_in_workshop:
            print("Error: Capacity Full, Cannot register more students")
            continue

        cursor.execute(
            """ 
                    SELECT StudentID
                    FROM Registrations
                    WHERE WorkshopID = :1
                """,
            (workshop_id,),
        )

        available_student_ids = []
        for row in cursor.fetchall():
            available_student_ids.append(row[0])

        if student_id in available_student_ids:
            print("Error")
            print(
                f"Student with StudentID {student_id} already exist in this workshop {workshop_id}"
            )
            continue

        else:
            cursor.execute(
                "INSERT INTO Registrations (WorkshopID, StudentID, RegisteredOn) VALUES (:1, :2, :3)",
                (workshop_id, student_id, datetime.date.today()),
            )
            connection.commit()
            print("Student registered successfully")

    elif choice == "5":
        workshop_id = int(input("Provide Workshop-ID: "))
        student_id = input("Provide StudentID: ")
        cursor.execute(
            """ 
                    SELECT WorkshopID
                    FROM Workshops
                """
        )

        available_workshop_ids = []
        for row in cursor.fetchall():
            available_workshop_ids.append(row[0])

        if workshop_id not in available_workshop_ids:
            print(f"Error: WorkshopID {workshop_id} not available")
            continue

        cursor.execute(
            """ 
                    SELECT StudentID
                    FROM Registrations
                    WHERE WorkshopID = :1
                """,
            (workshop_id,),
        )

        available_student_ids = []
        for row in cursor.fetchall():
            available_student_ids.append(row[0])

        if student_id not in available_student_ids:
            print("Error")
            print(
                f"Student with StudentID {student_id} does not exist in this workshop {workshop_id}"
            )
            continue

        cursor.execute(
            """
                DELETE FROM Registrations
                WHERE WorkshopID = :1 AND StudentID = :2
                """,
            (workshop_id, student_id),
        )

        if cursor.rowcount == 0:
            print("No registration found for this WorkshopID and StudentID.")
        else:
            connection.commit()
            print("Registration deleted successfully!")
            
    else:
        print("Invalid Choice.")


# Close cursor and connection
cursor.close()
connection.close()
