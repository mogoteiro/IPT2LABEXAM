import mysql.connector 
from mysql.connector import Error

def create_connection():
    
    try:
      connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='IPT_Resume_Builder'
        
      )
      if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected {db_info}")
      return connection
    except Error as e:
      print(f"Error while connecting to mysql: {e}")
      return None
    
def create_table(connection):
    """
    create a simple table in the database
    """
    
    try:
      cursor = connection.cursor()
      
      #SQL query to create a table
      
      create_table_query = """
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        age INT,
        adress VARCHAR(40) NOT NULL,
        phone VARCAHR(11) NOT NULL,
        email VARCHAR(20) NOT NULL,
        job_title VARCHAR(15) NOT NULL,
        prof_sum VARCHAR(255) NOT NULL,
        expe VARCHAR(255) NOT NULL,
        educ VARCHAR(255) NOT NULL,
        skills VARCHAR(255) NOT NULL
      )
      """
      
      #  CREATE TABLE IF NOT EXISTS users create a table named users only if it doesnt
      #already exist, prevents error if the the table is already there.
      
      cursor.execute(create_table_query)
      connection.commit()
      print("table users created successfully")
      cursor.close()
    except Error as e:
      print(f"Error creating table: {e}")

def get_user_input():
    print("=" * 40)
    print("Enter User Information")
    print("=" * 40)

name = input("Enter name: ").strip()

while True:
    try:
        age = int (18 <= 70) (input("Enter age: "))
        break
    except ValueError:
          print("Please enter a valid number for age")

    address = input("Enter address: ").strip()
    phone = input("Enter Phone num: ").strip()
    email = input("Enter Email: ").strip()
    job_title = input("Enter Job Title: ").strip()
    prof_sum = input("Enter Professional Summary: ").strip()
    expe = input("Enter Experince: ").strip()
    educ = input("Enter Education: ").strip()
    skills = input("Enter Skills: ").strip()

    return name, age, address, phone, email, job_title, prof_sum, expe, educ, skills

def insert_user_data(connection, name, age, address, phone, email, job_title, prof_sum, expe, educ, skills):
# ... (This is almost identical to our old insert_data function) ...
  try:
    cursor = connection.cursor()
    
    insert_query = "INSERT INTO users (name, age, address, phone, email, job_title, prof_sum, expe, educ, skills) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    user_data = (name, age, address, phone, email, job_title, prof_sum, expe, educ, skills)
    
    cursor.execute(insert_query, user_data)
    connection.commit()
    print(f"\n✓ Record inserted successfully for {name}\n")
    cursor.close()

  except Error as e:
    print(f"Error inserting data: {e}")

def main_menu(connection):
  while True:
    print("\n" + "=" * 40)
    print("User Management System")
    # ... (more print statements for menu) ...
    print("3. Exit")
    print("=" * 40)
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        name, age, address, phone, email, job_title, prof_sum, expe, educ, skills = get_user_input()
        insert_user_data(connection, name, age, address, phone, email, job_title, prof_sum, expe, educ, skills)
    
    elif choice == "2":
        retrieve_data(connection)
    
    elif choice == "3":
        print("\nThank you for using the system!")
        break
    
    else:
        print("\nInvalid choice! Please enter 1, 2, or 3")

def retrieve_data(connection):
    """
    Retrieve and display all data from the users table
    """
    try:
      cursor = connection.cursor()
      
      select_query = "SELECT * FROM users"
      cursor.execute(select_query)
      
      #Fetch all records
      
      records = cursor.fetchall() #get all the results and store them in a variable called records
      
      if records:
        print("\n" + "=" * 60)
        print("All Users in Database")
        print("=" * 60)
        for record in records: #loop through each row one by one
            print(f"ID: {record[0]}") 
            print(f"  Name: {record[1]}")
            print(f"  Age: {record[2]})") 
            print(f"  Address: {record[3]}") 
            print(f"  Phone: {record[4]}")
            print(f"  Email: {record[5]}")
            print(f"  Job Title: {record[6]}") 
            print(f"  Professional Summary: {record[7]}") 
            print(f"  Experince: {record[8]}") 
            print(f"  Education: {record[9]}")
            print(f"  Skills: {record[10]}")
        cursor.close()
    except Error as e:
      print(f"Error retrieving data: {e}")   
  
  #cursor it is like a pointer or pen that executes SQL Commands.
  
def close_connection(connection):
  if connection.is_connected():
    connection.close()
    print("\n MYSQL connection is closed")
if __name__ == "__main__": # means " only run this code if this file is run directly"

#step 1: create a connection
  conn = create_connection()

if conn:
    create_table(conn)

    get_user_input(conn)

    insert_user_data(conn)

    main_menu(conn)
    
    retrieve_data(conn)
    
    close_connection(conn)