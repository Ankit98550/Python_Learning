from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry 
import datetime
import sqlite3
import re

connector=sqlite3.connect("EmployeeManagement.db")
cursor=connector.cursor()
connector.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE_MANAGEMENT(EMPLOYEE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT , CONTACT_NUMBER INTEGER ,E_MAIL TEXT UNIQUE, JOINING_DATE TEXT, SALARY INTEGER)")

def is_valid_name(name):
    return name.isalpha() and len(name) >=3

def is_valid_contact(contact):
    return contact.isdigit() and len(contact) == 10

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_valid_salary(salary):
    return salary.isdigit() and len(salary) >= 4

def reset_fields():
    global id_strvar, name_strvar, contact_intvar, email_strvar, joining_date, salary_intvar
    for i in ['id_strvar', 'name_strvar',  'contact_intvar','email_strvar', 'salary_intvar']:
       exec(f"{i}.set('')")
    joining_date.set_date(datetime.datetime.now().date())

def reset_form():
    global tree
    tree.delete(*tree.get_children())
    reset_fields()

def display_records():
   tree.delete(*tree.get_children())
   curr = connector.execute('SELECT * FROM EMPLOYEE_MANAGEMENT')
   data = curr.fetchall()
   for records in data:
       tree.insert('', END, values=records)


def add_record():
    global id_strvar, name_strvar, contact_intvar, email_strvar, joining_date, salary_intvar
    name = name_strvar.get()
    contact = contact_intvar.get()
    email = email_strvar.get()
    join_date = joining_date.get_date()
    salary = salary_intvar.get()

    if not name and not contact and not email and not join_date and not salary:
        mb.showerror('Error!', "Please fill all the missing fields!!")
        return
    
    if not is_valid_name(str(name)):
        mb.showerror("Invalid Name", 'Please enter a valid Name')
        return

    # Validate contact number
    if not is_valid_contact(str(contact)):
        mb.showerror('Invalid Contact', 'Please enter a valid 10-digit contact number.')
        return
    
        # Validate email
    if not is_valid_email(email):
        mb.showerror('Invalid Email', 'Please enter a valid email address.') 
        return 
    
    if not is_valid_salary(str(salary)):
        mb.showerror("Invalid Salary","Please enter a valid salary")
        return
     
    else:
        try:
           connector.execute(
           'INSERT INTO EMPLOYEE_MANAGEMENT(NAME,  CONTACT_NUMBER, E_MAIL, JOINING_DATE, SALARY) VALUES (?,?,?,?,?)', (name, contact, email, join_date, salary)
           )
           connector.commit()
           mb.showinfo('Record added', f"Record of {name} was successfully added")
           reset_fields()
           display_records()
        except:    
            mb.showerror('DB Error', 'The type of the values entered is not accurate.')


def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]
        tree.delete(current_item)
        connector.execute('DELETE FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID=%d' % selection[0])
        connector.commit()
        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
        display_records()

def view_record():
    global id_strvar, name_strvar, contact_intvar, email_strvar, joining_date, salary_intvar
    if not tree.selection():
        mb.showerror('Error!', 'Please select a record to view')
    else:
         current_item = tree.focus()
         values = tree.item(current_item)
         selection = values["values"]

         id_strvar.set(selection[0]); name_strvar.set(selection[1])
         contact_intvar.set(selection[2]); email_strvar.set(selection[3])
         date = datetime.date(int(selection[4][:4]), int(selection[4][5:7]), int(selection[4][8:]))
         joining_date.set_date(date); salary_intvar.set(selection[5])


def search_data_by_id(id):
    global id_strvar
    id=id_strvar.get()
    search=connector.execute("SELECT * FROM EMPLOYEE_MANAGEMENT WHERE EMPLOYEE_ID=?", (id))
    rows = search.fetchall()
    return rows

# Update the Treeview with search results
def update_treeview(rows):
    for row in tree.get_children():
        tree.delete(row)

    for row in rows:
        tree.insert('', 'end', values=row)


def search():
    id=id_strvar
    try:
        emp_id = (id.get())  
        results = search_data_by_id(emp_id)
        update_treeview(results)
    except ValueError:
        print("Please enter a valid Employee ID.")

def update_record():
    global id_strvar, name_strvar, contact_intvar, email_strvar, joining_date, salary_intvar
    id=id_strvar.get()
    name = name_strvar.get()
    contact = contact_intvar.get()
    email = email_strvar.get()
    join_date = joining_date.get_date()
    salary = salary_intvar.get()

    if not id and not name and not contact and not email and not join_date and not salary:
        mb.showerror('Error!', "Please fill all the missing fields!!")
        return
    
    if not is_valid_name(str(name)):
        mb.showerror("Invalid Name", 'Please enter a valid Name')
        return
    # Validate contact number
    if not is_valid_contact(str(contact)):
        mb.showerror('Invalid Contact', 'Please enter a valid 10-digit contact number.')
        return
    # Validate email
    if not is_valid_email(email):
        mb.showerror('Invalid Email', 'Please enter a valid email address.')
        return
    if not is_valid_salary(str(salary)):
        mb.showerror("Invalid Salary","Please enter a valid salary")
        return

    else:
        try:
            connector.execute(
    "UPDATE EMPLOYEE_MANAGEMENT SET NAME=?, CONTACT_NUMBER=?, E_MAIL=?, JOINING_DATE=?, SALARY=? WHERE EMPLOYEE_ID=?",
    (name, contact, email, join_date, salary, id)
)
            connector.commit()
            mb.showinfo("Record Updated Successfully")
            reset_fields()
            display_records()
        except:    
            mb.showerror('Wrong type', 'The type of the values entered is not accurate.')



headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)



main = Tk()
main.title('Employe Management System')
main.geometry('1000x1000')
# main.resizable(0, 0)

lf_bg = 'skyblue' 
cf_bg = 'orange' 

id_strvar=StringVar()
name_strvar=StringVar()
contact_intvar=StringVar()
email_strvar=StringVar()
salary_intvar=StringVar()


Label(main, text="EMPLOYEE MANAGEMENT SYSTEM", font=headlabelfont, bg='lightgreen').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
center_frame = Frame(main, bg="aquamarine")
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
right_frame = Frame(main, bg="Gray")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

Label(left_frame, text="Employee Id For Searching", font=labelfont, bg=lf_bg).place(relx=0.05, rely=0.05)
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.18)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.31)
Label(left_frame, text="EMAIL", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.44)
Label(left_frame, text="joining Date", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.57)
Label(left_frame, text="Salary", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.67)

Entry(left_frame, width=19, textvariable=id_strvar,  font=entryfont).place(x=20, rely=0.1)
Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.23)
Entry(left_frame, width=19, textvariable=contact_intvar, font=entryfont).place(x=20, rely=0.36)

Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=20, rely=0.49)
Entry(left_frame, width=19, textvariable=salary_intvar, font=entryfont).place(x=20, rely=0.75)


joining_date = DateEntry(left_frame, font=("Arial", 12), width=15)
joining_date.place(x=20, rely=0.62)
Button(left_frame, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(relx=0.025, rely=0.85)

Button(center_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(relx=0.1, rely=0.25)
Button(center_frame, text='View Record', font=labelfont, command=view_record, width=15).place(relx=0.1, rely=0.35)
Button(center_frame, text='Search  Record', font=labelfont, command=search, width=15).place(relx=0.1, rely=0.45)
Button(center_frame, text='Update Record', font=labelfont, command=update_record, width=15).place(relx=0.1, rely=0.55)
Button(center_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(relx=0.1, rely=0.65)
Button(center_frame, text='Delete database', font=labelfont, command=reset_form, width=15).place(relx=0.1, rely=0.75)


Label(right_frame, text='Employee Records', font=headlabelfont, bg='powderblue', fg='black').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                   columns=('Employee Id', "Name", "Contact Number", "Email Address", "Joining Date", "Salary"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('Employee Id', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Joining Date', text='Joining Date', anchor=CENTER)
tree.heading('Salary', text='Salary', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.column('#6', width=80, stretch=NO)

tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()

main.update()
main.mainloop()
