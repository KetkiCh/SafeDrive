import pymysql
from tkinter import messagebox

# Open a connection to the database
db = pymysql.connect(
    host="localhost",
    user="enter your username here",
    password="enter yor password here",
    db="employees"
)
print("Successfully connected")
# Prepare a cursor object for executing SQL queries
cursor = db.cursor()

def update_password(employee_id_reset,new_password):
    sql = "UPDATE login_details SET password = %s WHERE employee_id = %s"
    cursor.execute(sql,(new_password,employee_id_reset))
    messagebox.showinfo('Info', 'Password reset successfully. Try to login again')

def login_verify(employee_id_verify,password_verify):
    # Retrieve an employee's login details by ID    
    sql = "SELECT * FROM login_details WHERE employee_id = %s"
    cursor.execute(sql, (employee_id_verify,))
    result = cursor.fetchone()
    if result:
        id, name, employee_id, contact_number, profile_picture, email_id, password, employee_type, vehicle_id = result
        if password == password_verify:
            messagebox.showinfo('Info','Login success')
        else:
            messagebox.showerror('Error',"Password didn't match")
        # Do something with the login details
    else:
        messagebox.showerror('Error',"Employee not found. Please register the employee.")

def add_data(values):
    # Insert a new employee's login details    
    sql = "INSERT INTO login_details (name, employee_id, contact_number, profile_picture, email_id, password, employee_type, vehicle_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7]))
    db.commit()
    messagebox.showinfo('Info','Employee Data added in Database')    

# Close the database connection
db.close()