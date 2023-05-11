#import modules
 
from tkinter import *
import os
import NewEmployeeRegistration as reg
import EmployeesDB as edb
 
# Designing window for registration
 
def register():
    global register_screen
    # an instance of secondary window on top of the main login screen
    register_screen = Toplevel(main_screen)
    register_screen.title("SafeDrive: New Employee Registration")    
    register_screen.config(background='#0B5A81')  
    # call the function which designs the window  
    reg.register_window(register_screen) 
 
# Designing window for login 
 
def login():
    global login_screen
    # an instance of secondary window on top of the main login screen
    login_screen = Toplevel(main_screen)
    login_screen.title("SafeDrive: Login")
    login_screen.geometry("300x250")
    
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global employeeID_verify
    global password_verify
 
    employeeID_verify = StringVar()
    password_verify = StringVar()
 
    global employeeID_login_entry
    global password_login_entry
 
    Label(login_screen, text="Employee ID").pack()
    employeeID_login_entry = Entry(login_screen, textvariable=employeeID_verify)
    employeeID_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Forgot Password", width=15, height=1, command = reset_password).pack()

# Implementing event on Forgot Password button 
def reset_password():
    global reset_password_screen
    # an instance of secondary window on top of the main login screen
    reset_password_screen = Toplevel(main_screen)
    reset_password_screen.title("SafeDrive: Reset Password")     
    reset_password_screen.geometry("300x250")
    
    Label(reset_password_screen, text="Please enter details below to reset password").pack()
    Label(reset_password_screen, text="").pack()

    global employeeID_for_reset
    global new_password

    employeeID_for_reset = StringVar()
    new_password = StringVar()

    Label(reset_password_screen, text="Employee ID").pack()
    employeeID_for_reset_entry = Entry(reset_password_screen, textvariable=employeeID_for_reset)
    employeeID_for_reset_entry.pack()
    Label(reset_password_screen, text="").pack()
    Label(reset_password_screen, text="New Password").pack()
    new_password_entry = Entry(reset_password_screen, textvariable=new_password, show='*')
    new_password_entry.pack()
    Label(reset_password_screen, text="").pack()
    Button(reset_password_screen, text="Reset Password", width=15, height=1, command = update_new_password).pack()


def update_new_password():
    edb.update_password(employeeID_for_reset.get(),new_password.get())
    reset_password_screen.destroy()

# Implementing event on login button 

def login_verify():
    employeeID1 = employeeID_verify.get()
    password1 = password_verify.get()
    employeeID_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    edb.login_verify(employeeID1,password1)
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Invalid Password")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Password not recognized.Try Again!").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Record Not Found")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Employee Not Found. Please register first!").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("SafeDrive: Account Login")    
    Label(text="Select Your Choice", bg="#0B5A81", width="300", height="2", font=("Calibri", 14)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
main_account_screen()