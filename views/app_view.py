import os
import shutil
from tkinter import *
from tkinter import filedialog

from logic.kernel import Kernel

DARK = '#26242f'
LIGHT = 'white'
DARK_BUTTON = '#16151c'
DARK_BUTTON_FOCUS = 'black'


class AppView:

    def __init__(self):
        self.root = Tk()
        self.screen = Frame(self.root)
        self.start_screen = Frame(self.root)
        self.menu_screen = Frame(self.root)
        self.kernel = Kernel()
        self.kernel.compute_eigenfaces()
        self.register_file_screen = Frame(self.root)
        self.login_file_screen = Frame(self.root)
        self.register_images_info = None
        self.login_images_info = None
        self.register_files = []
        self.login_file = None
        self.name_entry = None
        self.entry_name_info = None
        self.login_name_info = None

    def display(self):
        self.root.title('Eigenfaces app')
        self.root.geometry("1200x600")
        self.root.config(bg=DARK)

        screen_list = [self.start_screen, self.menu_screen, self.register_file_screen, self.login_file_screen]

        for screen in screen_list:
            screen.place(relx=0, rely=0, relwidth=1, relheight=1)
            screen.configure(bg=DARK)

        self.init_start_screen()
        self.init_menu_screen()
        self.init_register_file_screen()
        self.init_login_file_screen()

        self.open_start_screen()
        self.root.resizable(False, False)
        self.root.mainloop()

    def open_start_screen(self):
        self.start_screen.tkraise()

    def init_start_screen(self):
        start_label = Label(self.start_screen, text="Eigenfaces recognition app", font="Helvetica 50 bold", fg=LIGHT,
                            bg=DARK)
        start_label.pack(pady=(120, 10))

        button = Button(self.start_screen, text="Start", font=("Helvetica", 30), bg=DARK_BUTTON, fg=LIGHT,
                        activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=10, width=10,
                        command=self.open_menu_screen)
        button.pack(pady=(150, 0))

    def open_menu_screen(self):
        self.menu_screen.tkraise()

    def init_menu_screen(self):
        menu_label = Label(self.menu_screen, text="Select option", font="Helvetica 45", fg=LIGHT, bg=DARK)
        menu_label.pack(pady=(50, 75))

        login_button = Button(self.menu_screen, text="Login", font=("Helvetica", 27), bg=DARK_BUTTON,
                              fg=LIGHT,
                              activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=18,
                              command=self.open_login_file_screen)
        login_button.pack(pady=20)

        register_button = Button(self.menu_screen, text="Register", font=("Helvetica", 27),
                                 bg=DARK_BUTTON, fg=LIGHT,
                                 activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=18,
                                 command=self.open_register_file_screen)
        register_button.pack(pady=20)

        back_button = Button(self.menu_screen, text="Back", font=("Helvetica", 27), bg=DARK_BUTTON, fg=LIGHT,
                             activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=18,
                             command=self.open_start_screen)
        back_button.pack(pady=(50, 0))

    def open_register_file_screen(self):
        self.register_file_screen.tkraise()

    def init_register_file_screen(self):
        menu_label = Label(self.register_file_screen, text="Register by files", font="Helvetica 45", fg=LIGHT, bg=DARK)
        menu_label.pack(pady=(50, 25))

        # import images
        self.register_images_info = Label(self.register_file_screen, text="Select 8 image files", font="helvetica 18",
                                          fg=LIGHT, bg=DARK)
        self.register_images_info.pack(pady=(10, 5))

        select_files_button = Button(self.register_file_screen, text="Select files", font=("Helvetica", 18),
                                     bg=DARK_BUTTON, fg=LIGHT,
                                     activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=12,
                                     command=self.open_register_file_dialog)
        select_files_button.pack(pady=(0, 20))

        # name input
        input_info = Label(self.register_file_screen, text="Provide your name:", font="helvetica 18", fg=LIGHT, bg=DARK)
        input_info.pack(pady=(10, 0))

        self.name_entry = Entry(self.register_file_screen, width=20, font=18)
        self.name_entry.pack(pady=10)

        input_name = Button(self.register_file_screen, text="Register", font=("Helvetica", 18),
                            bg=DARK_BUTTON, fg=LIGHT,
                            activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=12,
                            command=self.register_with_files)
        input_name.pack()

        self.entry_name_info = Label(self.register_file_screen, text="", font="helvetica 18", fg=LIGHT, bg=DARK)
        self.entry_name_info.pack(pady=20)

        back_button = Button(self.register_file_screen, text="Back", font=("Helvetica", 27), bg=DARK_BUTTON, fg=LIGHT,
                             activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=15,
                             command=self.register_clear_and_back)
        back_button.pack(pady=10)

    def open_register_file_dialog(self):
        root = Tk()
        root.withdraw()
        self.register_files.clear()

        file_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=(
            ("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")))
        root.destroy()

        if len(file_paths) != 8:
            self.register_images_info.config(text="Please select exactly 8 Image files", fg="red")
            return
        else:
            self.register_images_info.config(text="Correctly imported files", fg="green")

            for file_path in file_paths:
                self.register_files.append(file_path)
            return

    def register_with_files(self):
        if self.name_entry.get() == "":
            self.entry_name_info.config(text="Please provide your name", fg="red")
            return
        else:
            self.entry_name_info.config(text="")

        if len(self.register_files) != 8:
            self.register_images_info.config(text="Please select exactly 8 Image files", fg="red")
            return

        if not os.path.exists('database'):
            os.mkdir('database')

        name_parts = self.name_entry.get().split()
        person_name = ""

        for part in name_parts:
            person_name += part + "_"

        person_name = person_name[:-1]

        if os.path.exists("database/" + person_name + "_0.png"):
            self.entry_name_info.config(text="Person with this name already exist in database", fg="red")
            return

        for i, file_path in enumerate(self.register_files):
            temp = person_name + "_" + str(i) + ".png"
            new_file_path = os.path.join("database", temp)
            shutil.copy2(file_path, new_file_path)

        self.entry_name_info.config(text="Successfully registered", fg="green")
        self.kernel.compute_eigenfaces()

    def register_clear_and_back(self):
        self.register_images_info.config(text="Select 8 image files", fg="white")
        self.entry_name_info.config(text="")
        self.name_entry.delete(0, END)
        self.register_files.clear()
        self.open_menu_screen()

    def open_login_file_screen(self):
        self.login_file_screen.tkraise()

    def init_login_file_screen(self):
        menu_label = Label(self.login_file_screen, text="Login by files", font="Helvetica 45", fg=LIGHT, bg=DARK)
        menu_label.pack(pady=(50, 25))

        # import images
        self.login_images_info = Label(self.login_file_screen, text="Select one image file", font="helvetica 18",
                                       fg=LIGHT, bg=DARK)
        self.login_images_info.pack(pady=(10, 5))

        select_files_button = Button(self.login_file_screen, text="Select file", font=("Helvetica", 18),
                                     bg=DARK_BUTTON, fg=LIGHT,
                                     activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=12,
                                     command=self.open_login_file_dialog)
        select_files_button.pack(pady=(0, 20))

        login_button = Button(self.login_file_screen, text="Login", font=("Helvetica", 18),
                              bg=DARK_BUTTON, fg=LIGHT,
                              activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=12,
                              command=self.login_by_file)
        login_button.pack()

        self.login_name_info = Label(self.login_file_screen, text="", font="helvetica 18", fg=LIGHT, bg=DARK)
        self.login_name_info.pack(pady=20)

        back_button = Button(self.login_file_screen, text="Back", font=("Helvetica", 27), bg=DARK_BUTTON, fg=LIGHT,
                             activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=15,
                             command=self.login_clear_and_back)
        back_button.pack(pady=10)

    def open_login_file_dialog(self):
        root = Tk()
        root.withdraw()
        self.login_file = None

        file_path = filedialog.askopenfilenames(title="Select Image File", filetypes=(
            ("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")))
        root.destroy()

        if not file_path or len(file_path) != 1:
            self.login_images_info.config(text="Please select exactly one file", fg="red")
            return
        else:
            self.login_images_info.config(text="Correctly imported file", fg="green")
            self.login_file = file_path[0]

    def login_by_file(self):
        if not self.login_file:
            self.login_images_info.config(text="Please select exactly one file", fg="red")
            return

        self.kernel.login(self.login_file)

        self.login_name_info.config(text="Not autorized user", fg="red")
        return

    def login_clear_and_back(self):
        self.login_images_info.config(text="Select one image File", fg="white")
        self.login_file = None
        self.login_name_info.config(text="")
        self.open_menu_screen()
