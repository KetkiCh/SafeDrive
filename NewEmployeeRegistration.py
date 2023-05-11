from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkinter import messagebox

import io
import EmployeesDB as edb
import base64

filename = ''
data_packet = []
font_setting = ('Times', 14)

def register_window(register_screen):  
    global var
    var = StringVar()
    var.set('Driver') 
    global employee_details_form
    employee_details_form = Frame(
        register_screen, 
        border=2, 
        background='#5075a6',
        relief=SOLID, 
        padx=10, 
        pady=10
        )

    Label(
        employee_details_form, 
        text="Name", 
        background='#5075a6',
        font=font_setting
        ).grid(row=0, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Email ID", 
        background='#5075a6',
        font=font_setting
        ).grid(row=1, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Contact Number", 
        background='#5075a6',
        font=font_setting
        ).grid(row=2, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Select Employee Type", 
        background='#5075a6',
        font=font_setting
        ).grid(row=3, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Employee ID", 
        background='#5075a6',
        font=font_setting
        ).grid(row=4, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Enter Password", 
        background='#5075a6',
        font=font_setting
        ).grid(row=5, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Re-Enter Password", 
        background='#5075a6',
        font=font_setting
        ).grid(row=6, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Vehicle ID (Enter NA if admin)", 
        background='#5075a6',
        font=font_setting
        ).grid(row=7, column=0, sticky=W, pady=10)

    Label(
        employee_details_form, 
        text="Profile Picture", 
        background='#5075a6',
        font=font_setting
        ).grid(row=8, column=0, sticky=W, pady=10)

    employee_type_frame = LabelFrame(
        employee_details_form,
        background='#5075a6',
        padx=10, 
        pady=10,
        )
    
    global register_name
    register_name = Entry(
        employee_details_form, 
        font=font_setting
        )

    global register_email
    register_email = Entry(
        employee_details_form, 
        font=font_setting
        )

    global register_mobile
    register_mobile = Entry(
        employee_details_form, 
        font=font_setting
        )

    driver_rb = Radiobutton(
        employee_type_frame, 
        text='Driver',
        background='#5075a6',
        variable=var,
        value='driver',
        font=('Times', 10),
        )

    admin_rb = Radiobutton(
        employee_type_frame,
        text='Admin',
        background='#5075a6',
        variable=var,
        value='admin',
        font=('Times', 10),
        )
    
    global register_employeeID
    register_employeeID = Entry(
        employee_details_form, 
        font=font_setting
        )

    global register_pwd
    register_pwd = Entry(
        employee_details_form, 
        font=font_setting,
        show='*'
        )

    global pwd_again
    pwd_again = Entry(
        employee_details_form, 
        font=font_setting,
        show='*'
        )

    global register_vehicleID
    register_vehicleID = Entry(
        employee_details_form, 
        font=font_setting,    
        )

    register_upload_btn = Button(
        employee_details_form,
        width=15,
        text='Upload',
        font=font_setting, 
        relief=SOLID,
        cursor='hand2',
        command=lambda:upload_file()
        )

    register_btn = Button(
        employee_details_form, 
        width=15, 
        text='Register', 
        font=font_setting, 
        relief=SOLID,
        cursor='hand2',
        command=lambda:register_btn_callback()
        )

    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_mobile.grid(row=2, column=1, pady=10, padx=20)
    register_employeeID.grid(row=4, column=1, pady=10, padx=20)
    register_pwd.grid(row=5, column=1, pady=10, padx=20)
    pwd_again.grid(row=6, column=1, pady=10, padx=20)
    register_vehicleID.grid(row=7, column=1, pady=10, padx=20)
    register_upload_btn.grid(row=8, column=1, pady=10, padx=20)
    register_btn.grid(row=10, column=1, pady=10, padx=20)
    employee_details_form.pack()

    employee_type_frame.grid(row=3, column=1, pady=10, padx=20)
    driver_rb.pack(expand=True, side=LEFT)
    admin_rb.pack(expand=True, side=LEFT)

def jpg_to_blob(file_path):
    # Open the image file
    with open(file_path, 'rb') as f:
        image = Image.open(f)
        # Convert the image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='JPEG')
        # Get the binary data from the BytesIO object
        img_blob = img_bytes.getvalue()
        return img_blob
    
def png_to_blob(file_path):
    # Open the image file
    with open(file_path, 'rb') as f:        
        data = f.read()        
        img_blob = base64.b64encode(data)
        return img_blob

def upload_file():
    global img  
    global filename  
    f_types = [('png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((400,200))   
    img=ImageTk.PhotoImage(img_resized)
    b2 =Button(employee_details_form,image=img) 
    b2.grid(row=9,column=1)

# Implementing event on register button
def register_btn_callback():
    check_counter=0
    warn = []
    
    if register_name.get() == "":
         warn.append("Name can't be empty")
    else:
        check_counter += 1
    
    if register_name.get().isalpha() == False:
        warn.append("Name can't be numeric")
    else:
        check_counter += 1
    
    if register_email.get() == "":
        warn.append("Email can't be empty")
    else:
        check_counter += 1

    if register_mobile.get() == "":
        warn.append("Contact can't be empty")
    else:
        check_counter += 1
    
    if register_mobile.get().isalnum() == True:
        warn.append("Contact No. can't be alphanumeric")
    else:
        check_counter += 1
        
    if  var.get() == "":
        warn.append("Select Employee Type")
    else:
        check_counter += 1

    if register_employeeID.get() == "":
        warn.append("Employee ID can't be empty")
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn.append("Password can't be empty")
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn.append("Re-enter password can't be empty")
    else:
        check_counter += 1
        
    if register_pwd.get() != pwd_again.get():
        warn.append("Passwords didn't match!")
    else:
        check_counter += 1
    
    if register_vehicleID.get() == "":
        warn.append("Vehicle ID can't be empty")
    else:
        check_counter += 1
    
    if warn:
        messagebox.showerror('Error',warn)       
    else:
        edb.add_data(pack_registration_data())
        messagebox.showinfo('Info','Registraion was successful')  

def pack_registration_data():
    global data_packet
    data_packet.append(register_name.get())
    data_packet.append(register_employeeID.get())
    data_packet.append(register_mobile.get())
    data_packet.append(png_to_blob(filename))
    data_packet.append(register_email.get())
    data_packet.append(register_pwd.get())
    data_packet.append(var.get())
    data_packet.append(register_vehicleID.get())
    return data_packet