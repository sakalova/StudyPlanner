from tkinter import *
from backend_script import Database

database = Database("database.db")

window = Tk()
window.title("Study planner")
window.resizable(width=FALSE, height=FALSE)


class LabelEnter:
    """ """
    def __init__(self):
        self.lbl_enter = Label(window, text="Enter what do you plan to learn:", font=("Times", "14", "bold italic"),) # Enter what you plan to learn LABEL
        self.lbl_enter.grid(row=0, column=0, columnspan=3,)
        self.enter_text = StringVar()

        self.entry_enter = Entry(window, textvariable=self.enter_text, width=50, cursor='arrow', fg='dark blue', font=("Times", "12", "italic"), )
        self.entry_enter.grid(row=1, column=0, columnspan=3, ipady=4)


class Buttons:
    """ """
    def __init__(self):
        # Create buttons for GUI and grid
        # Create button 'Add'
        self.button_add = Button(window, text='Add', width=11, activebackground='white', relief=RIDGE,
                            font=("Times", "14", "italic"), cursor='hand2', command=self.add_command)
        self.button_add.grid(row=1, column=4, padx=5, pady=5)

        # Create button 'My plan'
        self.button_plan = Button(window, text='My plan', width=12, activebackground='white', relief=GROOVE,
                             font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_command)
        self.button_plan.grid(row=2, column=0, padx=3, pady=5)

        # Create button 'In progress'
        self.button_progr = Button(window, text='In progress', width=12, activebackground='white', relief=GROOVE,
                              font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_p_command)
        self.button_progr.grid(row=2, column=1, padx=3, pady=5)

        # Create button 'Finished'
        self.button_finish = Button(window, text='Finished', width=12, activebackground='white', relief=GROOVE,
                               font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_f_command)
        self.button_finish.grid(row=2, column=2, padx=5, pady=5)


        # Create button 'Update'
        self.button_update = Button(window, text='Update', width=12, activebackground='white', relief=RIDGE,
                               font=("Times", "12", "italic"), cursor='hand2', command=self.update_command)
        self.button_update.grid(row=6, column=1, padx=5, pady=5)

        # Create button 'Delete'
        self.button_delete = Button(window, text='Delete', width=12, activebackground='white', relief=RIDGE,
                               font=("Times", "12", "italic"), cursor='hand2', command=self.delete_command)
        self.button_delete.grid(row=6, column=2, padx=5, pady=5)

        # Create button 'Push to  In progress'
        self.button_push_prog = Button(window, text='Push to   In progress', width=12, height=3, wraplength=75,
                                       justify=CENTER, activebackground='white', relief=RIDGE,
                                       font=("Times", "12", "italic"), cursor='hand2', command = self.push_to_progress)
        self.button_push_prog.grid(row=3, column=4, padx=5, pady=5)

        # Create button 'Push to Finished'
        self.button_push_fin = Button(window, text='Push to Finished', width=12, height=3, wraplength=75, justify=CENTER,
                                      activebackground='white', relief=RIDGE, font=("Times", "12", "italic"),
                                      cursor='hand2', command=self.push_to_fin)
        self.button_push_fin.grid(row=4, column=4, padx=5, pady=5)

        # Create button 'Close'
        self.button_close = Button(window, text='Close', width=12, activebackground='white', relief=RIDGE,
                                   font=("Times", "12", "italic"), cursor='hand2', command=window.destroy)
        self.button_close.grid(row=6, column=4, padx=5, pady=5)

    def push_to_progress(self):
        database.push_p((selected_tuple[0]))
        self.view_p_command()

    def push_to_fin(self):
        database.push_f((selected_tuple[0]))
        self.view_f_command()

    def add_command(self):
        database.insert(label_enter.enter_text.get())
        list_scrollbar.list.delete(0, END)
        print(type(label_enter.enter_text.get()))
        list_scrollbar.list.insert(END, label_enter.enter_text.get())

    def view_command(self):
        list_scrollbar.list.delete(0, END)
        for row in database.view():
            list_scrollbar.list.insert(END, row)

    def view_p_command(self):
        list_scrollbar.list.delete(0, END)
        for row in database.view_p():
            list_scrollbar.list.insert(END, row)

    def view_f_command(self):
        list_scrollbar.list.delete(0, END)
        for row in database.view_f():
            list_scrollbar.list.insert(END, row)
            
    def delete_command(self):
        try:
            database.delete(selected_tuple[0])
            self.view_command()
        except NameError:
            pass

    def update_command(self):
        try:
            database.update(selected_tuple[0], label_enter.enter_text.get(), )
        except NameError:
            pass
        self.view_command()

class ListScrollbar:
    """ """
    def __init__(self):
        self.list = Listbox(window, width=60, fg='dark green', font=("Times", "12", "italic"), selectmode=SINGLE, )
        self.list.grid(row=3, column=0, rowspan=2, columnspan=3, padx=5,)

        self.scrollbar_list = Scrollbar(window, cursor='double_arrow', )
        self.scrollbar_list.grid(row=3, column=3, rowspan=3, ipady=45, padx=3, pady=3)
        # scrollbar_list.bind("<MouseWheel>", callback)

        self.list.bind('<<ListboxSelect>>', self.get_selected_row)
        self.list.configure(yscrollcommand=self.scrollbar_list.set)
        self.scrollbar_list.configure(command=self.list.yview)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = list_scrollbar.list.curselection()[0]
            selected_tuple = list_scrollbar.list.get(index)
            label_enter.entry_enter.delete(0, END)
            label_enter.entry_enter.insert(END, selected_tuple[1])

        except IndexError:
            pass


label_enter = LabelEnter()
buttons = Buttons()
list_scrollbar = ListScrollbar()

window.mainloop()
