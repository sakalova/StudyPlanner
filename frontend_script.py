from tkinter import *
from backend_script import Database

database = Database("database.db")

window = Tk()
window.title("Study planner")
window.resizable(width=FALSE, height=FALSE)


class LabelEnter:
    """ Class for creation Label and Entry widgets."""

    def __init__(self):
        self.lbl_enter = Label(window, text="Enter what do you plan to learn:",
                               font=("Times", "14", "bold italic"), )
        self.lbl_enter.grid(row=0, column=0, columnspan=3,)

        self.enter_text = StringVar()
        self.enter_text.trace('w', self.character_limit)

        self.entry_enter = Entry(window, textvariable=self.enter_text, width=50, cursor='arrow', fg='dark blue',
                                 font=("Times", "12", "italic"),)
        self.entry_enter.grid(row=1, column=0, columnspan=3, ipady=4)

    def character_limit(self, *args):
        value = self.enter_text.get()
        if len(value) > 70:
            self.enter_text.set(value[:70])


class Buttons:
    """ Class for creation Button widgets and command modules for buttons.
        Create button 'Add'.
        Create button 'My plan'.
        Create button 'In progress'.
        Create button 'Finished'.
        Create button 'Update'.
        Create button 'Delete'.
        Create button 'Push to  In progress'.
        Create button 'Push to Finished'.
        Create button 'Close'.

    """

    def __init__(self):
        self.button_add = self.press_button_add()
        self.button_plan = self.passive_button_plan()
        self.button_progr = self.passive_button_progr()
        self.button_finish = self.passive_button_finish()

        self.button_update = Button(window, text='Update', width=12, activebackground='white', relief=RIDGE,
                                    font=("Times", "12", "italic"), cursor='hand2', command=self.preupdate_command)
        self.button_update.grid(row=6, column=1, padx=5, pady=5)

        self.button_delete = Button(window, text='Delete', width=12, activebackground='white', relief=RIDGE,
                                    font=("Times", "12", "italic"), cursor='hand2', command=self.delete_command)
        self.button_delete.grid(row=6, column=2, padx=5, pady=5)

        self.button_push_prog = Button(window, text='Push to   In progress', width=12, height=3, wraplength=75,
                                       justify=CENTER, activebackground='white', relief=RIDGE,
                                       font=("Times", "12", "italic"), cursor='hand2', command=self.push_to_progress)
        self.button_push_prog.grid(row=3, column=4, padx=5, pady=5)

        self.button_push_fin = Button(window, text='Push to Finished', width=12, height=3, wraplength=75,
                                      justify=CENTER,
                                      activebackground='white', relief=RIDGE, font=("Times", "12", "italic"),
                                      cursor='hand2', command=self.push_to_fin)
        self.button_push_fin.grid(row=4, column=4, padx=5, pady=5)

        self.button_close = Button(window, text='Close', width=12, activebackground='white', relief=RIDGE,
                                   font=("Times", "12", "italic"), cursor='hand2', command=window.destroy)
        self.button_close.grid(row=6, column=4, padx=5, pady=5)

    def press_button_add(self):
        self.button_add = Button(window, text='Add', width=11, activebackground='white', relief=RIDGE,
                                 font=("Times", "14", "italic"), cursor='hand2', command=self.add_command)
        self.button_add.grid(row=1, column=4, padx=5, pady=5)
        return self.button_add

    def press_button_save(self):
        self.button_add = Button(window, text='Save', width=11, activebackground='white', relief=RIDGE,
                                 font=("Times", "14", "italic"), cursor='hand2', command=self.update_selected)
        self.button_add.grid(row=1, column=4, padx=5, pady=5)
        return self.button_add

    def passive_button_plan(self):
        self.button_plan = Button(window, text='My plan', width=12, relief=GROOVE,
                                  font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_command)
        self.button_plan.grid(row=2, column=0, padx=3, pady=5)
        return self.button_plan

    def active_button_plan(self):
        self.button_plan = Button(window, text='My plan', width=12, relief=SUNKEN,
                                  font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_command)
        self.button_plan.grid(row=2, column=0, padx=3, pady=5)
        return self.button_plan

    def passive_button_progr(self):
        self.button_progr = Button(window, text='In progress', width=12,relief=GROOVE,
                                   font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_p_command)
        self.button_progr.grid(row=2, column=1, padx=3, pady=5)
        return self.button_progr

    def active_button_progr(self):
        self.button_progr = Button(window, text='In progress', width=12, relief=SUNKEN,
                                   font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_p_command)
        self.button_progr.grid(row=2, column=1, padx=3, pady=5)
        return self.button_progr

    def passive_button_finish(self):
        self.button_finish = Button(window, text='Finished', width=12, relief=GROOVE,
                                    font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_f_command)
        self.button_finish.grid(row=2, column=2, padx=5, pady=5)
        return self.button_finish

    def active_button_finish(self):
        self.button_finish = Button(window, text='Finished', width=12, relief=SUNKEN,
                                    font=("Times", "14", "bold italic"), cursor='hand2', command=self.view_f_command)
        self.button_finish.grid(row=2, column=2, padx=5, pady=5)
        return self.button_finish

    def push_to_progress(self):

        database.push_p((getPrimaryKey(selected_string)))
        self.view_p_command()

    def push_to_fin(self):
        database.push_f((getPrimaryKey(selected_string)))
        self.view_f_command()

    def add_command(self):
        database.insert(label_enter.enter_text.get())
        list_scrollbar.list.delete(0, END)
        list_scrollbar.list.insert(END, label_enter.enter_text.get())
        list_scrollbar.list.delete(0, END)
        self.clear_text()
        self.view_command()

    def clear_text(self):
        label_enter.entry_enter.delete(0, END)

    # When push button 'My plan' in the listbox are shown entered text with status==0 (status 0 - means status 'my plan').
    def view_command(self):
        self.button_add = self.press_button_add()
        self.button_progr = self.passive_button_progr()
        self.button_finish = self.passive_button_finish()
        list_scrollbar.list.delete(0, END)

        for row in database.view():
            row = str(row[0]) + '. ' + ''.join(row[1:])
            list_scrollbar.list.insert(END, row)
        self.button_plan = self.active_button_plan()

    # When push button 'In progress' in the listbox are shown entered text with status==1 (status 1 - means status 'in progress').
    def view_p_command(self):
        self.button_plan = self.passive_button_plan()
        self.button_finish = self.passive_button_finish()
        list_scrollbar.list.delete(0, END)
        for row in database.view_p():
            row = str(row[0]) + '. ' + ''.join(row[1:])
            list_scrollbar.list.insert(END, row)
        self.button_progr = self.active_button_progr()

    # When push button 'Finished' in the listbox are shown entered text with status==2 (status 2 - means status 'finished').
    def view_f_command(self):
        self.button_plan = self.passive_button_plan()
        self.button_progr = self.passive_button_progr()
        list_scrollbar.list.delete(0, END)
        for row in database.view_f():
            row = str(row[0]) + '. ' + ''.join(row[1:])
            list_scrollbar.list.insert(END, row)
        self.active_button_finish()

    def delete_command(self):
        try:
            database.delete(getPrimaryKey(selected_string))
            self.view_command()
        except NameError:
            pass

    def preupdate_command(self):
        label_enter.entry_enter.insert(END, stripPrimaryKey(selected_string))
        self.button_add = self.press_button_save()


    def update_selected(self):
        try:
            database.update(getPrimaryKey(selected_string), label_enter.enter_text.get(), )

        except NameError:
            pass
        self.view_command()
        self.clear_text()


def getPrimaryKey(string):
    dotPos = string.find('. ')
    primaryKey = string[0:dotPos]
    return primaryKey

def stripPrimaryKey(string):
    separation_token = '. '
    dotPos = string.find(separation_token)
    return string[dotPos + len(separation_token):]


class ListScrollbar:
    """Class for creation Listbox and Scrollbar widget and  connection of vertical scrollbar to listbox. """

    def __init__(self):
        self.list = Listbox(window, width=60, fg='dark green', font=("Times", "12", "italic"), selectmode=SINGLE, )
        self.list.grid(row=3, column=0, rowspan=2, columnspan=3, padx=5, )

        self.scrollbar_list = Scrollbar(window, cursor='double_arrow', )
        self.scrollbar_list.grid(row=3, column=3, rowspan=3, ipady=45, padx=3, pady=3)
        # scrollbar_list.bind("<MouseWheel>", callback)

        self.list.bind('<<ListboxSelect>>', self.get_selected_row)
        self.list.configure(yscrollcommand=self.scrollbar_list.set)
        self.scrollbar_list.configure(command=self.list.yview)

    def get_selected_row(self, event):
        try:
            global selected_string

            index = list_scrollbar.list.curselection()
            if index:
                selected_string = list_scrollbar.list.get(index)
                label_enter.entry_enter.delete(0, END)

        except IndexError:
            pass


label_enter = LabelEnter()
buttons = Buttons()
list_scrollbar = ListScrollbar()

window.mainloop()
