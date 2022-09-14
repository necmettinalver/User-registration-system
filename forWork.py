import tkinter
from tkinter import *
from tkinter import ttk
#The code was written using python and the tkinter library. If you don't have the tkinter library, please type in cmd: 'pip install tkinter'
#If you get an error while running, close and reopen the ide to run the code again.

user_counter=2
hiding=True

#The function that will happen when you press the NewUser Button.
def NewUser(): 
    check_enabled_button.deselect()
    name_text_field.delete('1.0','end')
    email_text_field.delete('1.0','end')
    phone_text_field.delete('1.0','end')
    displayname_text_field.delete('1.0','end')

#When the SaveUser button is pressed, it deletes the values entered in the TextFields.
def SaveUser():
    global user_counter #number of users registered in the system
    
    if var_check_enabled_button.get()==1:
        _bool='True'
    else:
        _bool='False'
    data_table.insert(parent='', index='end', iid=user_counter, text='', tags=('ttk'),
                   values=(user_counter+1, name_text_field.get('1.0','end'), email_text_field.get('1.0','end'), _bool))
    user_counter+=1

#Hide the display of users with false value when HideDisabledButton button is pressed
def HideDisabledUser():

    for count in range(0,user_counter):##As many cycles as the number of users are created.
        global hiding
        item=data_table.item(count)##Each user in the table is kept as an item.
        
        record = item['values']##A temporary variable is created to access the value variables of the items.
        data_table.selection_set()

        if(record[3]=='False'):##The variable that holds whether the record[3] enabled button is checked or not.
            if hiding:
                data_table.detach(count)
            else:
                data_table.move(count , parent='', index=count)

    if hiding:
        hiding=False
    else:
        hiding=True

#Creating an interface using thinker

#The main canvas has been created to place my widgets.
master = Tk()
canvas = Canvas(master, height=450, width=750)
canvas.pack()

#Its home screen is divided into three to make it easier to place widgets.
frame_top = Frame(master, bg='#f5f5f5')
frame_top.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.12)

frame_left = Frame(master, bg='#ffffff')
frame_left.place(relx=0.01, rely=0.13, relwidth=0.50, relheight=0.85)

frame_right = Frame(master, bg='#ffffff')
frame_right.place(relx=0.52, rely=0.13, relwidth=0.61, relheight=0.85)

#widgets have been placed in the top frame.
##The new user button has been placed in the upper frame. The function is written for the operation to be performed when clicked with the command command.(NewUser())
new_user_button = Button(frame_top, text='+ New User', height=2, width=12, command=NewUser, bg='#007cba', fg='#ffffff',
                         font='Verdana 9 bold')
new_user_button.pack(padx=10, pady=10, side=LEFT)

##The save user button has been placed in the upper frame. The function is written for the operation to be performed when clicked with the command command.(SaveUser())
save_user_button = Button(frame_top, text='Save User', height=2, width=12, command=SaveUser, bg='#56a7cf', fg='#ffffff',
                          font='Verdana 7 bold')
save_user_button.pack(padx=10, pady=10, side=RIGHT)

##The check button is positioned on the left side. 
##The padx command was used to create a space with the new user button. The command command was used to call a function that you clicked.
var_check_hide_button = IntVar()
check_hide_button = Checkbutton(frame_top, text='Hide Disabled User', variable=var_check_hide_button,
                                command=HideDisabledUser, onvalue=1, offvalue=0, bg='#f5f5f5', selectcolor='#0075ff',
                                highlightcolor='#0075ff', font='Verdana 8 ')
check_hide_button.pack(padx=10, pady=10, side=LEFT)

#widgets have been placed in the right frame.

##Grid positioning was used for placements.
##row controls the horizontal ordering, and the column controls the vertical order within the horizontal order. 
##Thus, texts and textField widgets to receive values ​​were placed in front of them.

###New user text and this background 
newUser_label = Label(frame_right, bg='#f5f5f5', text='New User', font='Verdana 10', width=40, height=2,
                      anchor=tkinter.W)
newUser_label.grid(row=1, column=1, columnspan=18, padx=10, pady=10)

###username part
name_Label = Label(frame_right, bg='#ffffff', text='Username :', font='Verdana 7').grid(row=2, column=1, pady=15, padx=10)
###username text field part
name_text_field = Text(frame_right, height=1, width=25)
name_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
name_text_field.grid(row=2, column=2, pady=15, padx=10)

###displayname part
displayname_Label = Label(frame_right, bg='#ffffff', text='Displayname :', font='Verdana 7').grid(row=3, column=1, pady=15, padx=10)
###displayname text field part
displayname_text_field = Text(frame_right, height=1, width=25)
displayname_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
displayname_text_field.grid(row=3, column=2, pady=15, padx=10)

###phonename label part
phone_Label = Label(frame_right, bg='#ffffff', text='Phone :', font='Verdana 7').grid(row=4, column=1, pady=15, padx=10)
###phone text field part 
phone_text_field = Text(frame_right, height=1, width=25)
phone_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
phone_text_field.grid(row=4, column=2, pady=15, padx=10)

###email label part
email_Label = Label(frame_right, bg='#ffffff', text='Email :', font='Verdana 7').grid(row=5, column=1, pady=15, padx=10)
###email text field part
email_text_field = Text(frame_right, height=1, width=25)
email_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
email_text_field.grid(row=5, column=2, pady=15, padx=10)

###this is UserRole label
Label(frame_right, bg='#ffffff', text='User Role :', font='Verdana 7').grid(row=6, column=1, pady=15, padx=10)

###The stringvar widget has been placed. This is our popup.
user_role_option = StringVar(frame_right)
###Assignment was made when nothing is selected (default).
user_role_option.set("Select User")

###We have assigned the elements of our option menu. You can assign it with an array if you want.
user_role_dropdown_menu = OptionMenu(frame_right, user_role_option, 'Guest', 'Admin', 'SuperAdmin')
user_role_dropdown_menu.configure(width=28, bg='#ffffff')
user_role_dropdown_menu.grid(row=6, column=2, pady=15, padx=10)
### more info : https://pythonguides.com/python-tkinter-optionmenu/

###enabled label
Label(frame_right, bg='#ffffff', text='Enabled :', font='Verdana 7').grid(row=7, column=1, pady=15, padx=10)

###Our variable keeps the value 1 when the enabled button is checked. keeps 0 when unchecked.
var_check_enabled_button = IntVar()
check_enabled_button = Checkbutton(frame_right, variable=var_check_enabled_button, onvalue=1, offvalue=0, bg='#ffffff', font='Verdana 10 ')
check_enabled_button.grid(row=7, column=2, pady=15, padx=1)

#widgets have been placed in the left frame.
##used ttk to create table
### https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Treeview.html
data_table = ttk.Treeview(frame_left, show='headings')
data_table['columns'] = ('user_id', 'user_name', 'user_email', 'user_enabled')

##for our table we add columns for
data_table.column("user_id", anchor=N, width=60)
data_table.column("user_name", anchor=N, width=90)
data_table.column("user_email", anchor=N, width=140)
data_table.column("user_enabled", anchor=N, width=80)

##We add the titles of the tables we created.we use column name as reference (user_id,user_name...)
data_table.heading("user_id", text="Id", anchor=tkinter.W)
data_table.heading("user_name", text="User Name", anchor=tkinter.W)
data_table.heading("user_email", text="Email", anchor=tkinter.W)
data_table.heading("user_enabled", text="Enabled", anchor=tkinter.W)

##I pre-added it as an example of adding elements to the table
###The function of adding user automatically with the save user button is written above.
data_table.insert(parent='', index='end', iid=0, text='', tags=('ttk'),
               values=('1', 'AdminUser', 'admin@piworks.net', 'False'))
data_table.insert(parent='', index='end', iid=1, text='', tags=('ttk'),
               values=('2', 'TestUser', 'testuser@piworks.net', 'True'))

##to change the style of the table and to get the image you want

style = ttk.Style(data_table)
style.theme_use("default")
style.configure("Treeview.Heading", background="#007cba", foreground="white")

data_table.pack()

#For the interface to work continuousl
master.mainloop()
