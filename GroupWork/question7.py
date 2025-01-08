import sqlite3


def insert_sample_data():
    try:
        conn = sqlite3.connect('employees.db')
        cursor = conn.cursor()

        
        cursor.execute("DROP TABLE IF EXISTS employees")

        
        cursor.execute('''
            CREATE TABLE employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
        ''')

        
        sample_data = [
            ('Alice', 'HR', 50000),
            ('Bob', 'IT', 75000),
            ('Charlie', 'Finance', 60000),
            ('Diana', 'Marketing', 65000),
            ('Eve', 'IT', 80000)
        ]

        cursor.executemany("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", sample_data)
        conn.commit()
        print("Sample data inserted successfully.\n")
        conn.close()
    except sqlite3.Error as e:
        print(f"An error occurred while inserting data: {e}")


def search_employee(name):
    try:
        conn = sqlite3.connect('employees.db')
        cursor = conn.cursor()

    
        cursor.execute("SELECT * FROM employees WHERE name = ?", (name,))
        results = cursor.fetchall()

        if results:
            print("\nEmployee Details:")
            for row in results:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Department: {row[2]}")
                print(f"Salary: {row[3]}")
                print("-" * 20)
        else:
            print(f"\nNo employee found with the name '{name}'.")

        conn.close()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def main():
    
    insert_sample_data()

    
    employee_name = input("Enter the employee's name to search: ")
    search_employee(employee_name)


if __name__ == "__main__":
    main()
