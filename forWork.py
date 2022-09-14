import tkinter
from tkinter import *
from tkinter import ttk


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
    global user_counter
    if var_check_enabled_button.get()==1:
        _bool='True'
    else:
        _bool='False'
    my_game.insert(parent='', index='end', iid=user_counter, text='', tags=('ttk'),
                   values=(user_counter+1, name_text_field.get('1.0','end'), email_text_field.get('1.0','end'), _bool))
    user_counter+=1

#Hide the display of users with false value when HideDisabledButton button is pressed
def HideDisabledUser():

    for count in range(0,user_counter):
        global hiding
        item=my_game.item(count)
        
        record = item['values']
        my_game.selection_set()

        if(record[3]=='False'):
            if hiding:
                my_game.detach(count)
            else:
                my_game.move(count , parent='', index=count)

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
new_user_button = Button(frame_top, text='+ New User', height=2, width=12, command=NewUser, bg='#007cba', fg='#ffffff',
                         font='Verdana 9 bold')
new_user_button.pack(padx=10, pady=10, side=LEFT)

save_user_button = Button(frame_top, text='Save User', height=2, width=12, command=SaveUser, bg='#56a7cf', fg='#ffffff',
                          font='Verdana 7 bold')
save_user_button.pack(padx=10, pady=10, side=RIGHT)

var_check_hide_button = IntVar()
check_hide_button = Checkbutton(frame_top, text='Hide Disabled User', variable=var_check_hide_button,
                                command=HideDisabledUser, onvalue=1, offvalue=0, bg='#f5f5f5', selectcolor='#0075ff',
                                highlightcolor='#0075ff', font='Verdana 8 ')
check_hide_button.pack(padx=10, pady=10, side=LEFT)

#widgets have been placed in the right frame.
newUser_label = Label(frame_right, bg='#f5f5f5', text='New User', font='Verdana 10', width=40, height=2,
                      anchor=tkinter.W)
newUser_label.grid(row=1, column=1, columnspan=18, padx=10, pady=10)

name_Label = Label(frame_right, bg='#ffffff', text='Username :', font='Verdana 7').grid(row=2, column=1, pady=15, padx=10)
name_text_field = Text(frame_right, height=1, width=25)
name_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
name_text_field.grid(row=2, column=2, pady=15, padx=10)

displayname_Label = Label(frame_right, bg='#ffffff', text='Displayname :', font='Verdana 7').grid(row=3, column=1, pady=15, padx=10)
displayname_text_field = Text(frame_right, height=1, width=25)
displayname_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
displayname_text_field.grid(row=3, column=2, pady=15, padx=10)

phone_Label = Label(frame_right, bg='#ffffff', text='Phone :', font='Verdana 7').grid(row=4, column=1, pady=15, padx=10)
phone_text_field = Text(frame_right, height=1, width=25)
phone_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
phone_text_field.grid(row=4, column=2, pady=15, padx=10)

email_Label = Label(frame_right, bg='#ffffff', text='Email :', font='Verdana 7').grid(row=5, column=1, pady=15, padx=10)
email_text_field = Text(frame_right, height=1, width=25)
email_text_field.tag_configure('style', foreground='#2a333c', font=('Verdana', 7, 'bold'))
email_text_field.grid(row=5, column=2, pady=15, padx=10)

Label(frame_right, bg='#ffffff', text='User Role :', font='Verdana 7').grid(row=6, column=1, pady=15, padx=10)
user_role_option = StringVar(frame_right)
user_role_option.set("Select User")
user_role_dropdown_menu = OptionMenu(frame_right, user_role_option, 'Guest', 'Admin', 'SuperAdmin')
user_role_dropdown_menu.configure(width=28, bg='#ffffff')
user_role_dropdown_menu.grid(row=6, column=2, pady=15, padx=10)

Label(frame_right, bg='#ffffff', text='Enabled :', font='Verdana 7').grid(row=7, column=1, pady=15, padx=10)
var_check_enabled_button = IntVar()
check_enabled_button = Checkbutton(frame_right, variable=var_check_enabled_button, onvalue=1, offvalue=0, bg='#ffffff', font='Verdana 10 ')
check_enabled_button.grid(row=7, column=2, pady=15, padx=1)

#widgets have been placed in the left frame.
#used ttk to create table
my_game = ttk.Treeview(frame_left, show='headings')
my_game['columns'] = ('user_id', 'user_name', 'user_email', 'user_enabled')

my_game.column("user_id", anchor=N, width=60)
my_game.column("user_name", anchor=N, width=90)
my_game.column("user_email", anchor=N, width=140)
my_game.column("user_enabled", anchor=N, width=80)

my_game.heading("user_id", text="Id", anchor=tkinter.W)
my_game.heading("user_name", text="User Name", anchor=tkinter.W)
my_game.heading("user_email", text="Email", anchor=tkinter.W)
my_game.heading("user_enabled", text="Enabled", anchor=tkinter.W)

my_game.insert(parent='', index='end', iid=0, text='', tags=('ttk'),
               values=('1', 'AdminUser', 'admin@piworks.net', 'False'))
my_game.insert(parent='', index='end', iid=1, text='', tags=('ttk'),
               values=('2', 'TestUser', 'testuser@piworks.net', 'True'))

style = ttk.Style(my_game)
style.theme_use("default")
style.configure("Treeview.Heading", background="#007cba", foreground="white")

my_game.pack()

#For the interface to work continuousl
master.mainloop()
