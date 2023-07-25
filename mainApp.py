import os
import sys
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk

from databases_source import passwords as passdb


class MainWindow(tk.Tk):
    """Main Window That is running the Whole App"""

    def __init__(self):
        super().__init__()
        # Main GUI
        self.title('Password Manager And Generator')
        self.geometry("950x720+10+10")
        self.resizable(False, False)
        self.iconbitmap(None)
        # Color Background
        self.bg_model = tk.Label(self, bg='#2C3E50')
        self.bg_model.place(x=0, y=0, relwidth=1, relheight=1)
        self.iconbitmap('assets/logo-icover.ico')
        self.menu = SideMenus(self)


class SideMenus(tk.LabelFrame):
    """This Part is for the whole sidebar menus"""

    def __init__(self, window):
        super().__init__(window, bg="#000428", width=300, height=720)
        self.grid(row=0, column=0)
        self.interActiveFrame = tk.Frame(window)
        self.interActiveFrame.grid(row=0, column=1)
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.button_variable = 0
        # Logo and its shenanigans
        self.logo_pic = tk.PhotoImage(file='assets/main_logo.png')
        self.logo_pic_small = self.logo_pic.subsample(5, 5)

        self.picture = tk.Label(self, image=self.logo_pic_small, bg="#000428", text='KuPass',
                                font=('Arial Rounded MT Bold', 30, 'bold'),
                                foreground='white', compound='left')
        self.picture.grid(row=0, column=0, pady=10)

        self.quotationFrame = tk.Frame(self, bg="#000428")
        self.quotationFrame.grid(row=1, column=0, padx=10)

        self.quotation = tk.Label(self.quotationFrame, text='"Passwords are here, para HINDI mag KuPass sa mind!"',
                                  foreground='white',
                                  bg="#000428", font=('San Serif', 7, 'bold'))
        self.quotation.grid(row=0, column=0, padx=10)

        # Setting The frame for the Buttons
        self.frameButtons = tk.Frame(self, bg="#000428")
        self.frameButtons.grid(row=2, column=0, padx=25, pady=10)

        # All items Button
        self.app_logo = tk.PhotoImage(file="assets/All_logo.png")
        self.app_logo2 = self.app_logo.subsample(7, 7)

        self.all_button = tk.Button(self.frameButtons, image=self.app_logo2, text="All Items", compound='left', bd=0,
                                    bg="#BDC3C7", font=('Arial Rounded MT Bold', 10, 'bold'), foreground='Black',
                                    activebackground="#000428", width=250, height=50, command=self.selected_all)
        self.all_button.grid(row=0, column=0)

        # Log Ins Button
        self.log_logo = tk.PhotoImage(file="assets/Logins_logo.png")
        self.log_logo2 = self.log_logo.subsample(8, 8)

        self.log_button = tk.Button(self.frameButtons, image=self.log_logo2, text="Logins", compound='left', bd=0,
                                    bg="#000428", font=('Arial Rounded MT Bold', 10, 'bold'), foreground='White',
                                    activebackground="#000428", width=250, height=50, command=self.selected_logins)
        self.log_button.grid(row=1, column=0)

        # Personal Info Button
        self.info_logo = tk.PhotoImage(file="assets/Personal_logo.png")
        self.info_logo2 = self.info_logo.subsample(8, 8)

        self.info_button = tk.Button(self.frameButtons, image=self.info_logo2, text="Personal", compound='left', bd=0,
                                     bg="#000428", font=('Arial Rounded MT Bold', 10, 'bold'), foreground='White',
                                     activebackground="#000428", width=250, height=50, command=self.selected_personal)
        self.info_button.grid(row=2, column=0)

        # History Button
        self.history_logo = tk.PhotoImage(file="assets/History_logo.png")
        self.history_logo2 = self.history_logo.subsample(8, 8)

        self.history_button = tk.Button(self.frameButtons, image=self.history_logo2, text="History", compound='left',
                                        bd=0,
                                        bg="#000428", font=('Arial Rounded MT Bold', 10, 'bold'), foreground='White',
                                        activebackground="#000428", width=250, height=50, command=self.selected_history)
        self.history_button.grid(row=3, column=0)

        # Trash Button
        self.trash_logo = tk.PhotoImage(file="assets/Trash_logo.png")
        self.trash_logo2 = self.trash_logo.subsample(8, 8)

        self.trash_button = tk.Button(self.frameButtons, image=self.trash_logo2, text="Trash", compound='left', bd=0,
                                      bg="#000428", font=('Arial Rounded MT Bold', 10, 'bold'), foreground='White',
                                      activebackground="#000428", width=250, height=50, command=self.selected_trash)
        self.trash_button.grid(row=4, column=0)

        for widgets in self.frameButtons.winfo_children():
            widgets.grid_configure(pady=10)

        # Bottom Menu Blocks
        self.blocks = tk.LabelFrame(self, bg="#000428", text='Others', font=('Arial Rounded MT Bold', 5, 'bold'),
                                    foreground='white')
        self.blocks.grid(row=3, column=0, sticky='we', padx=10, pady=50)

        # Settings Block
        self.setting_pic = tk.PhotoImage(file="assets/block_setting.png")
        self.setting_pic2 = self.setting_pic.subsample(6, 6)

        self.setting_button1 = tk.Button(self.blocks, image=self.setting_pic2, text='Settings',
                                         compound='top', bg="#000428", bd=0, font=('Arial Rounded MT Bold', 10, 'bold'),
                                         foreground='white', command=lambda: SettingBlock(self))
        self.setting_button1.grid(row=0, column=0)

        # Tools Block
        self.tools_pic = tk.PhotoImage(file="assets/block_tools.png")
        self.tools_pic2 = self.tools_pic.subsample(6, 6)

        self.tools_button1 = tk.Button(self.blocks, image=self.tools_pic2, text='Tools',
                                       compound='top', bg="#000428", bd=0, font=('Arial Rounded MT Bold', 10, 'bold'),
                                       foreground='white', command=lambda: ToolsBlock(self))
        self.tools_button1.grid(row=0, column=1)

        # Info Block
        self.info_pic = tk.PhotoImage(file="assets/block_info.png")
        self.info_pic2 = self.info_pic.subsample(6, 6)

        self.info_button1 = tk.Button(self.blocks, image=self.info_pic2, text='Info',
                                      compound='top', bg="#000428", bd=0, font=('Arial Rounded MT Bold', 10, 'bold'),
                                      foreground='white', command=lambda: InfoBlock(self))
        self.info_button1.grid(row=0, column=2)

        for widgets in self.blocks.winfo_children():
            widgets.grid_configure(padx=2)

        # Button and Block Frame Dictionaries
        self.mainframes = {4: TrashFrame(self.interActiveFrame),
                           3: HistoryFrame(self.interActiveFrame),
                           2: PersonalFrame(self.interActiveFrame),
                           1: LoginsFrame(self.interActiveFrame),
                           0: AllItemSFrame(self.interActiveFrame)}

    """Side Button Commands and simple interaction mechanisms"""

    def selected_all(self):
        self.refresh_mechanism()
        self.all_button.config(bg="#BDC3C7", foreground='black')
        self.button_variable = 0
        self.switch_main_frames()

    def selected_logins(self):
        self.refresh_mechanism()
        self.log_button.config(bg="#BDC3C7", foreground='black')
        self.button_variable = 1
        self.switch_main_frames()

    def selected_personal(self):
        self.refresh_mechanism()
        self.info_button.config(bg="#BDC3C7", foreground='black')
        self.button_variable = 2
        self.switch_main_frames()

    def selected_history(self):
        self.refresh_mechanism()
        self.history_button.config(bg="#BDC3C7", foreground='black')
        self.button_variable = 3
        self.switch_main_frames()

    def selected_trash(self):
        self.refresh_mechanism()
        self.trash_button.config(bg="#BDC3C7", foreground='black')
        self.button_variable = 4
        self.switch_main_frames()

    def refresh_mechanism(self):
        # it refreshes any configure and the buttons, giving the feel of selection
        for widget in self.frameButtons.winfo_children():
            widget.config(foreground='white', bg='#000428')

    def switch_main_frames(self):
        open_frame = self.mainframes[self.button_variable]
        open_frame.tkraise()

    """Main Frame Classes"""


class AllItemSFrame(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.main_window = contain
        self.configure(width=650, height=720, bg='#2C3E50')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        # Database for the passwords
        self.database_passwords = passdb.PasswordDatabase()

        # Frame for Title and Add/Del Button
        self.frame_within = tk.Frame(self, bg='#2C3E50', width=600, height=50)
        self.frame_within.grid_propagate(False)
        self.frame_within.grid(row=0, column=0, padx=20, pady=15)

        self.text = tk.Label(self.frame_within, text="ALL ITEMS", font=('Arial Rounded MT Bold', 25, 'bold'),
                             bg='#2C3E50', foreground="white")
        self.text.grid(row=0, column=0)

        # Add Button
        self.add_pic = tk.PhotoImage(file="assets/add_items.png")
        self.add_pic2 = self.add_pic.subsample(15, 15)

        self.buttons = tk.Frame(self.frame_within, bg='#2C3E50')
        self.buttons.grid(row=0, column=1, padx=125)

        self.button_frame = tk.Frame(self.buttons, highlightbackground='black', highlightthickness=2, bd=0,
                                     bg='#2C3E50')
        self.button_frame.grid(row=0, column=1)
        self.add_button = tk.Button(self.button_frame, image=self.add_pic2, text='Add items', compound='left',
                                    foreground='white',
                                    font=('Arial Rounded MT Bold', 8, 'bold'), bd=0, bg='#2C3E50',
                                    command=self.spawn_new_item)
        self.add_button.grid(row=0, column=0)

        # Delete Button
        self.delete_pic = tk.PhotoImage(file="assets/delete_items.png")
        self.delete_pic2 = self.delete_pic.subsample(15, 15)

        self.button_frame = tk.Frame(self.buttons, highlightbackground='black', highlightthickness=2, bd=0,
                                     bg='#2C3E50')
        self.button_frame.grid(row=0, column=2, padx=5)
        self.del_button = tk.Button(self.button_frame, image=self.delete_pic2, text='Delete items', compound='left',
                                    foreground='white',
                                    font=('Arial Rounded MT Bold', 8, 'bold'), bd=0, bg='#2C3E50',
                                    command=self.kill_item)
        self.del_button.grid(row=0, column=0)

        # Edit Button
        self.edit = tk.PhotoImage(file="assets/edit.png")
        self.edit2 = self.edit.subsample(15, 15)

        self.button_frame = tk.Frame(self.buttons, highlightbackground='black', highlightthickness=2, bd=0,
                                     bg='#2C3E50')
        self.button_frame.grid(row=0, column=3)
        self.edit_button = tk.Button(self.button_frame, image=self.edit2, bd=0, bg='#2C3E50', command=self.edit_item)
        self.edit_button.grid(row=0, column=0)

        # Frame if No Items
        self.frame_no_item = tk.Frame(self, bg='#2C3E50', width=600, height=590)
        self.frame_no_item.grid_propagate(False)
        self.frame_no_item.pack_propagate(False)
        self.frame_no_item.grid(row=1, column=0)
        self.arrow = tk.PhotoImage(file='Assets/arrow1.png').subsample(1, 1)
        self.text_label = tk.Label(self.frame_no_item, image=self.arrow, compound='top',
                                   text="Press The Add Item to start your adventure with Us!",
                                   foreground='white', font=('Arial Rounded MT Bold', 15, 'bold'), bg='#2C3E50')
        self.text_label.place(x=10, y=-60)

        # Frame for the Items
        self.frame_within3 = tk.Frame(self, bg='#2C3E50', width=600, height=590)
        self.frame_within3.grid_propagate(False)
        self.frame_within3.pack_propagate(False)
        self.frame_within3.grid(row=1, column=0, pady=20)

        # Configure the design
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("Treeview", background='#2C3E50', foreground='white', fieldbackground='#2C3E50',
                             font=('Arial Rounded MT Bold', 10, 'bold'), rowheight=50)
        self.style.configure('Treeview.Heading', background='#2C3E50', foreground='white',
                             font=('Arial Rounded MT Bold', 12, 'bold'))
        self.style.map('Treeview', background=[('selected', "#BDC3C7")])

        # Tree View for Items
        self.table = ttk.Treeview(self.frame_within3, columns=('Name', 'Last Log', 'Serial Number'), height=11)
        self.table.grid(row=0, column=0)
        self.table.heading('0', text='Account Name', anchor='center')
        self.table.heading('1', text='Last Logged', anchor='center')
        self.table.heading('2', text='eNCryp', anchor='center')

        self.table.column('#0', anchor='center', minwidth=50, width=50, stretch=False)
        self.table.column("# 1", anchor='center', width=150, minwidth=150, stretch=False)
        self.table.column("# 2", anchor='center', width=150, minwidth=150, stretch=False)
        self.table.column("# 3", anchor='center', width=225, minwidth=225, stretch=False)

        self.facebook = tk.PhotoImage(file='Assets/facebook.png').subsample(12, 12)
        self.gmail = tk.PhotoImage(file='Assets/Google.png').subsample(12, 12)
        self.riot = tk.PhotoImage(file='Assets/Riot.png').subsample(12, 12)
        self.github = tk.PhotoImage(file='Assets/GitHub.png').subsample(12, 12)
        self.chatgpt = tk.PhotoImage(file='Assets/chat.png').subsample(12, 12)
        self.aris = tk.PhotoImage(file='Assets/TIPseal.png').subsample(12, 12)

        # Image Dictionary
        self.supported_web_dct = {"Facebook": self.facebook, "Google": self.gmail, "Riot Games Sign In": self.riot,
                                  "Github": self.github, "OpenAI - ChatGPT": self.chatgpt, "ARIS TIP": self.aris}

        # Show a message if it has no current items
        if len(self.database_passwords.show_all_pass()) == 0:
            self.frame_no_item.tkraise()
            self.del_button.config(state='disabled')
            self.edit_button.config(state='disabled')
        else:
            self.frame_within3.tkraise()
            self.del_button.config(state='normal')
            self.edit_button.config(state='normal')

        for value in self.database_passwords.show_all_pass():
            self.table.insert(parent='', index="end", image=self.supported_web_dct[value[0]],
                              values=(value[1], value[5], value[6]))

        # Treeview Scrollbar
        self.scroll = ttk.Scrollbar(self.frame_within3, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky='ns')

    def spawn_new_item(self):
        # Produce a Child Frame
        self.add = tk.Toplevel(self.main_window)
        self.add.focus()
        self.add.grab_set()
        self.add.geometry('500x325+100+100')
        self.add.title('Adding Items')
        self.add.resizable(False, False)
        self.bg_model = tk.Label(self.add, bg="#000428")
        self.bg_model.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for the Child Frame
        self.child_frame = tk.LabelFrame(self.add, bg='#2C3E50', width=460, height=295)
        self.child_frame.grid_propagate(False)
        self.child_frame.grid(row=0, column=0, padx=20, pady=20)

        # Frame:
        self.frame_holder = tk.Frame(self.child_frame, bg='#2C3E50')
        self.frame_holder.grid(row=0, column=0)

        # Info Frame
        self.informations = tk.LabelFrame(self.frame_holder, text="FILL UP ALL THE INFORMATION",
                                          bg='#2C3E50', foreground='White', font=('Arial Rounded MT Bold', 10, 'bold'),
                                          width=440, height=250)
        self.informations.grid_propagate(False)
        self.informations.grid(row=0, column=0, padx=5, pady=20)

        # info frame Holder
        self.info_frame_holder = tk.Frame(self.informations, bg='#2C3E50')
        self.info_frame_holder.grid(row=0, column=0)

        # Combo box for the supported medias
        self.supported_web = ["Facebook", "Google", "Riot Games Sign In", "Github", "OpenAI - ChatGPT", "ARIS TIP"]
        self.media = tk.Label(self.info_frame_holder, text="Web/Media: ", font=('Arial Rounded MT Bold', 8, 'bold'),
                              bg='#2C3E50', foreground='white')
        self.media.grid(row=0, column=0, padx=5, pady=20)
        self.supported_medias = ttk.Combobox(self.info_frame_holder, values=self.supported_web,
                                             font=('Arial Rounded MT Bold', 10, 'bold'), width=12)
        self.supported_medias.grid(row=0, column=1)

        # Name Entry
        self.name = tk.Label(self.info_frame_holder, text="Name: ", font=('Arial Rounded MT Bold', 8, 'bold'),
                             bg='#2C3E50', foreground='white')
        self.name.grid(row=0, column=2, padx=5, pady=20)
        self.name_entry = tk.Entry(self.info_frame_holder, bg='#BDC3C7', font=('Arial Rounded MT Bold', 10, 'bold'),
                                   width=15)
        self.name_entry.grid(row=0, column=3)

        # Email Entry
        self.email = tk.Label(self.info_frame_holder, text="Email: ", font=('Arial Rounded MT Bold', 8, 'bold'),
                              bg='#2C3E50',
                              foreground='white')
        self.email.grid(row=1, column=0, padx=5, pady=20)
        self.email_entry = tk.Entry(self.info_frame_holder, bg='#BDC3C7', font=('Arial Rounded MT Bold', 10, 'bold'),
                                    width=15)
        self.email_entry.grid(row=1, column=1)

        # ID Entry
        self.identification = tk.Label(self.info_frame_holder, text="ID #: ", font=('Arial Rounded MT Bold', 8, 'bold'),
                                       bg='#2C3E50',
                                       foreground='white')
        self.identification.grid(row=1, column=2, padx=5, pady=20)
        self.identification_entry = tk.Entry(self.info_frame_holder, bg='#BDC3C7',
                                             font=('Arial Rounded MT Bold', 10, 'bold'),
                                             width=15)
        self.identification_entry.insert(0, 'ARIS TIP ONLY')
        self.identification_entry.config(state='disabled')
        self.identification_entry.grid(row=1, column=3)

        # Password and Save Frame
        self.save_pass_frame = tk.Frame(self.informations, bg='#2C3E50')
        self.save_pass_frame.grid(row=1, column=0)

        # Password Entry
        self.password = tk.Label(self.save_pass_frame, text="Password: ", font=('Arial Rounded MT Bold', 8, 'bold'),
                                 bg='#2C3E50',
                                 foreground='white')
        self.password.grid(row=0, column=0, padx=5, pady=20)
        self.password_entry = tk.Entry(self.save_pass_frame, bg='#BDC3C7',
                                       font=('Arial Rounded MT Bold', 10, 'bold'),
                                       width=15, show="*")
        self.password_entry.grid(row=0, column=1)

        # Censored and Uncensored Button
        self.unsee = tk.PhotoImage(file='Assets/unsee.png').subsample(15, 15)
        self.see = tk.PhotoImage(file='Assets/see.png').subsample(15, 15)
        self.unsee_button = tk.Button(self.save_pass_frame, image=self.unsee, bg='#2C3E50', bd=0,
                                      command=self.show_and_unshow)
        self.unsee_button.grid(row=0, column=2, padx=10)

        # Save Button
        self.save_button = tk.Button(self.save_pass_frame, text="Save", font=('Arial Rounded MT Bold', 10, 'bold'),
                                     foreground='white', bg='#2C3E50', relief='solid',
                                     command=self.add_password_database)
        self.save_button.grid(row=1, column=1)

        self.supported_medias.bind('<<ComboboxSelected>>', self.config_tip)

    def add_password_database(self):
        try:
            if self.supported_medias.get() == '' or self.name_entry.get() == '' or self.email_entry.get() == '' or self.password_entry.get() == '':
                messagebox.showerror(title="ERROR: INPUTS",
                                     message="All Entries should have an input! {ID# is only required When Adding ARIS TIP}")
            else:
                self.database_pass_register = passdb.PasswordRegistry(self.supported_medias.get(),
                                                                      self.name_entry.get(), self.email_entry.get(),
                                                                      id_checker(self.identification_entry.get()),
                                                                      self.password_entry.get(), date_and_time())
                self.database_passwords.add_pass(self.database_pass_register)
                messagebox.showinfo(title='SUCCESS', message="Your Account is added to the system!")
                refresh()
        except:
            messagebox.showwarning(title="ERROR: SYSTEM", message="An error occurred, pls try again")

    def config_tip(self, event):
        if self.supported_medias.get() == 'ARIS TIP':
            self.identification_entry.config(state='normal')
            self.identification_entry.delete(0, tk.END)
        else:
            self.identification_entry.delete(0, tk.END)
            self.identification_entry.insert(0, "ARIS TIP ONLY")
            self.identification_entry.config(state='disabled')

    def show_and_unshow(self):
        if self.password_entry['show'] == '*':
            self.unsee_button.config(image=self.see)
            self.password_entry.config(show='')

        elif self.password_entry['show'] == '':
            self.unsee_button.config(image=self.unsee)
            self.password_entry.config(show="*")

    def show_and_unshow_edit(self):
        if self.password_entry_edit['show'] == '*':
            self.unsee_button_edit.config(image=self.see)
            self.password_entry_edit.config(show='')

        elif self.password_entry_edit['show'] == '':
            self.unsee_button_edit.config(image=self.unsee)
            self.password_entry_edit.config(show="*")

    def kill_item(self):
        self.item_del = self.table.selection()
        if len(self.item_del) == 0:
            messagebox.showinfo(title="ERROR: NO ITEM", message="Please select items first to delete")
        else:
            if messagebox.askyesno(title="ARE YOU SURE?",
                                   message="You're going to delete your selected item(s), press 'Yes' to continue"):
                for item in self.item_del:
                    self.details = self.table.item(item)
                    self.database_passwords.delete_pass(self.details['values'][2])
                    self.table.delete(item)
            else:
                for item in self.item_del:
                    self.table.selection_remove(item)
            refresh()

    def edit_item(self):
        self.item_edit = self.table.selection()
        if len(self.item_edit) == 0:
            messagebox.showinfo(title="ERROR: NO ITEM", message="Please select items first to Edit")
        elif len(self.item_edit) > 1:
            messagebox.showinfo(title="ERROR: MANY ITEM",
                                message="Multiple items to edit are not yet supported, Please try again")
            for item in self.item_edit:
                self.table.selection_remove(item)
        else:
            # Get The Values Of the selected Item
            self.selected = self.table.item(self.item_edit)
            self.encrypt = self.selected['values'][2]
            self.items_sel = self.database_passwords.get_item(self.encrypt)
            # self.serial = self.database_passwords.get_item(self.item_edit)
            # print(self.serial)
            # Produce a Child Frame
            self.edit_tab = tk.Toplevel(self.main_window)
            self.edit_tab.focus()
            self.edit_tab.grab_set()
            self.edit_tab.geometry('500x325+100+100')
            self.edit_tab.title('Edit Details')
            self.edit_tab.resizable(False, False)
            self.bg_model = tk.Label(self.edit_tab, bg="#000428")
            self.bg_model.place(x=0, y=0, relwidth=1, relheight=1)

            # Frame for the Child Frame
            self.child_frame_edit = tk.LabelFrame(self.edit_tab, bg='#2C3E50', width=460, height=295)
            self.child_frame_edit.grid_propagate(False)
            self.child_frame_edit.grid(row=0, column=0, padx=20, pady=20)

            # Frame:
            self.frame_holder_edit = tk.Frame(self.edit_tab, bg='#2C3E50')
            self.frame_holder_edit.grid(row=0, column=0)

            # Info Frame
            self.informations_edit = tk.LabelFrame(self.frame_holder_edit, text="EDIT THE ITEMS",
                                                   bg='#2C3E50', foreground='White',
                                                   font=('Arial Rounded MT Bold', 10, 'bold'),
                                                   width=440, height=250)
            self.informations_edit.grid_propagate(False)
            self.informations_edit.grid(row=0, column=0, padx=5, pady=20)

            # info frame Holder
            self.info_frame_holder_edit = tk.Frame(self.informations_edit, bg='#2C3E50')
            self.info_frame_holder_edit.grid(row=0, column=0)

            # supported medias
            self.media_edit = tk.Label(self.info_frame_holder_edit, text="Web/Media: ",
                                       font=('Arial Rounded MT Bold', 8, 'bold'),
                                       bg='#2C3E50', foreground='white')
            self.media_edit.grid(row=0, column=0, padx=5, pady=20)
            self.supported_medias_edit = tk.Entry(self.info_frame_holder_edit,
                                                  font=('Arial Rounded MT Bold', 10, 'bold'), width=15)
            self.supported_medias_edit.insert(0, self.items_sel[0])
            self.supported_medias_edit.config(state='disabled')
            self.supported_medias_edit.grid(row=0, column=1)

            # Name Entry
            self.name_edit = tk.Label(self.info_frame_holder_edit, text="Name: ",
                                      font=('Arial Rounded MT Bold', 8, 'bold'),
                                      bg='#2C3E50', foreground='white')
            self.name_edit.grid(row=0, column=2, padx=5, pady=20)
            self.name_entry_edit = tk.Entry(self.info_frame_holder_edit, bg='#BDC3C7',
                                            font=('Arial Rounded MT Bold', 10, 'bold'),
                                            width=15)
            self.name_entry_edit.insert(0, self.items_sel[1])
            self.name_entry_edit.grid(row=0, column=3)

            # Email Entry
            self.email_edit = tk.Label(self.info_frame_holder_edit, text="Email: ",
                                       font=('Arial Rounded MT Bold', 8, 'bold'),
                                       bg='#2C3E50',
                                       foreground='white')
            self.email_edit.grid(row=1, column=0, padx=5, pady=20)
            self.email_entry_edit = tk.Entry(self.info_frame_holder_edit, bg='#BDC3C7',
                                             font=('Arial Rounded MT Bold', 10, 'bold'),
                                             width=15)
            self.email_entry_edit.insert(0, self.items_sel[2])
            self.email_entry_edit.grid(row=1, column=1)

            # ID Entry
            self.identification_edit = tk.Label(self.info_frame_holder_edit, text="ID #: ",
                                                font=('Arial Rounded MT Bold', 8, 'bold'),
                                                bg='#2C3E50',
                                                foreground='white')
            self.identification_edit.grid(row=1, column=2, padx=5, pady=20)
            self.identification_entry_edit = tk.Entry(self.info_frame_holder_edit, bg='#BDC3C7',
                                                      font=('Arial Rounded MT Bold', 10, 'bold'),
                                                      width=15)
            self.identification_entry_edit.insert(0, self.items_sel[3])
            if self.items_sel[0] == "ARIS TIP":
                self.identification_entry_edit.config(state='normal')
            else:
                self.identification_entry_edit.insert(0, "ARIS TIP ONLY")
                self.identification_entry_edit.config(state='disabled')
            self.identification_entry_edit.grid(row=1, column=3)

            # Password and Save Frame
            self.save_pass_frame_edit = tk.Frame(self.informations_edit, bg='#2C3E50')
            self.save_pass_frame_edit.grid(row=1, column=0)

            # Password Entry
            self.password_edit = tk.Label(self.save_pass_frame_edit, text="Password: ",
                                          font=('Arial Rounded MT Bold', 8, 'bold'),
                                          bg='#2C3E50',
                                          foreground='white')
            self.password_edit.grid(row=0, column=0, padx=5, pady=20)
            self.password_entry_edit = tk.Entry(self.save_pass_frame_edit, bg='#BDC3C7',
                                                font=('Arial Rounded MT Bold', 10, 'bold'),
                                                width=15, show="*")
            self.password_entry_edit.insert(0, self.items_sel[4])
            self.password_entry_edit.grid(row=0, column=1)

            # Censored and Uncensored Button
            self.unsee = tk.PhotoImage(file='Assets/unsee.png').subsample(15, 15)
            self.see = tk.PhotoImage(file='Assets/see.png').subsample(15, 15)
            self.unsee_button_edit = tk.Button(self.save_pass_frame_edit, image=self.unsee, bg='#2C3E50', bd=0,
                                               command=self.show_and_unshow_edit)
            self.unsee_button_edit.grid(row=0, column=2, padx=10)

            # Save Button
            self.save_button_edit = tk.Button(self.save_pass_frame_edit, text="UPDATE",
                                              font=('Arial Rounded MT Bold', 10, 'bold'),
                                              foreground='white', bg='#2C3E50', relief='solid',
                                              command=self.edit_things)
            self.save_button_edit.grid(row=1, column=1)

    def edit_things(self):
        try:
            if self.supported_medias_edit.get() == '' or self.name_entry_edit.get() == '' or self.email_entry_edit.get() == '' or self.password_entry_edit.get() == '':
                messagebox.showerror(title="ERROR: INPUTS",
                                     message="All Entries should have an input! {ID# is only required When Adding ARIS TIP}")
            else:
                self.database_passwords.update(self.items_sel[6], self.name_entry_edit.get(),
                                               self.email_entry_edit.get(),
                                               id_checker(self.identification_entry_edit.get()),
                                               self.password_entry_edit.get(), date_and_time())
                messagebox.showinfo(title='SUCCESS', message="Your Account is Updated")
                refresh()
        except:
            messagebox.showwarning(title="ERROR: SYSTEM", message="An error occurred, pls try again")


class LoginsFrame(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.configure(width=650, height=720, bg='#2C3E50')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.text = tk.Label(self, text="Logins Sample Test")
        self.text.grid(row=0, column=0)


class PersonalFrame(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.configure(width=650, height=720, bg='#2C3E50')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.text = tk.Label(self, text="Personal Sample Test")
        self.text.grid(row=0, column=0)


class HistoryFrame(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.configure(width=650, height=720, bg='#2C3E50')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.text = tk.Label(self, text="History Sample Test")
        self.text.grid(row=0, column=0)


class TrashFrame(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.configure(width=650, height=720, bg='#2C3E50')
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        self.text = tk.Label(self, text="Trash Sample Test")
        self.text.grid(row=0, column=0)


"""Block Button Frames"""


class SettingBlock(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.configure(width=300, height=720, bg='#000428')
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        self.button = BackButton(self)


class ToolsBlock(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.configure(width=300, height=720, bg='#000428')
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        self.button = BackButton(self)


class InfoBlock(tk.Frame):
    def __init__(self, contain):
        super().__init__(contain, highlightbackground='black', highlightthickness=2)
        self.configure(width=300, height=720, bg='#000428')
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        self.button = BackButton(self)


class BackButton(tk.Button):
    def __init__(self, contain):
        super().__init__(contain, command=contain.grid_forget, bd=0, text="Back", bg='#000428', compound='left',
                         font=('Arial Rounded MT Bold', 10, 'bold'), foreground='white')
        self.back_pic = tk.PhotoImage(file="assets/back_logo.png")
        self.back_pic2 = self.back_pic.subsample(15, 15)
        self.configure(image=self.back_pic2)
        self.grid(row=0, column=0)


# Un classed Commands to all class to share
def refresh():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def date_and_time():
    now = datetime.now()
    date_string = now.strftime("%m/%d/%Y %H:%M")
    return date_string


def id_checker(value):
    if value == 'ARIS TIP ONLY':
        return ''
    else:
        return value


main = MainWindow()
main.mainloop()
