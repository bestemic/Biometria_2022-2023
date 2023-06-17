import os
import shutil
from tkinter import *
from tkinter import filedialog

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
        self.register_file_screen = Frame(self.root)
        self.import_images_info = None
        self.register_files = []
        self.name_entry = None
        self.entry_name_info = None

    def display(self):
        self.root.title('Eigenfaces app')
        self.root.geometry("1200x600")
        self.root.config(bg=DARK)

        screen_list = [self.start_screen, self.menu_screen, self.register_file_screen]

        for screen in screen_list:
            screen.place(relx=0, rely=0, relwidth=1, relheight=1)
            screen.configure(bg=DARK)

        self.init_start_screen()
        self.init_menu_screen()
        self.init_register_file_screen()

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

        button_container = Frame(self.menu_screen, bg=DARK)
        button_container.pack()

        button_container_left = Frame(button_container, bg=DARK)
        button_container_left.pack(side=LEFT, padx=(0, 20))

        button_container_right = Frame(button_container, bg=DARK)
        button_container_right.pack(side=RIGHT, padx=(20, 0))

        login_button1 = Button(button_container_left, text="Login by File", font=("Helvetica", 27), bg=DARK_BUTTON,
                               fg=LIGHT,
                               activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=18,
                               command=self.open_start_screen)
        login_button1.pack(pady=20)

        login_button2 = Button(button_container_right, text="Login by Camera", font=("Helvetica", 27), bg=DARK_BUTTON,
                               fg=LIGHT,
                               activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=18,
                               command=self.open_start_screen)
        login_button2.pack(pady=20)

        register_button1 = Button(button_container_left, text="Register by File", font=("Helvetica", 27),
                                  bg=DARK_BUTTON, fg=LIGHT,
                                  activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=18,
                                  command=self.open_register_file_screen)
        register_button1.pack(pady=20)

        register_button2 = Button(button_container_right, text="Register by Camera", font=("Helvetica", 27),
                                  bg=DARK_BUTTON, fg=LIGHT,
                                  activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=18,
                                  command=self.open_start_screen)
        register_button2.pack(pady=20)

        back_button = Button(self.menu_screen, text="Back", font=("Helvetica", 27), bg=DARK_BUTTON, fg=LIGHT,
                             activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=15,
                             command=self.open_start_screen)
        back_button.pack(pady=(50, 0))

    def open_register_file_screen(self):
        self.register_file_screen.tkraise()

    def init_register_file_screen(self):
        menu_label = Label(self.register_file_screen, text="Register by files", font="Helvetica 45", fg=LIGHT, bg=DARK)
        menu_label.pack(pady=(50, 25))

        # import images
        self.import_images_info = Label(self.register_file_screen, text="Select 8 image files", font="helvetica 18", fg=LIGHT, bg=DARK)
        self.import_images_info.pack(pady=(10, 5))

        select_files_button = Button(self.register_file_screen, text="Select files", font=("Helvetica", 18),
                                     bg=DARK_BUTTON, fg=LIGHT,
                                     activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=12,
                                     command=self.open_file_dialog)
        select_files_button.pack(pady=(0, 20))

        # name input
        input_info = Label(self.register_file_screen, text="Provide your name:", font="helvetica 18", fg=LIGHT, bg=DARK)
        input_info.pack(pady=(10, 0))

        self.name_entry = Entry(self.register_file_screen, width=20, font=18)
        self.name_entry.pack(pady=10)

        input_name = Button(self.register_file_screen, text="Register", font=("Helvetica", 18),
                            bg=DARK_BUTTON, fg=LIGHT,
                            activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=12,
                            command=self.set_name)
        input_name.pack()

        self.entry_name_info = Label(self.register_file_screen, text="", font="helvetica 18", fg=LIGHT, bg=DARK)
        self.entry_name_info.pack(pady=20)

        back_button = Button(self.register_file_screen, text="Back", font=("Helvetica", 27), bg=DARK_BUTTON, fg=LIGHT,
                             activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, width=15,
                             command=self.open_menu_screen)
        back_button.pack(pady=10)

    def open_file_dialog(self):
        root = Tk()
        root.withdraw()
        self.register_files.clear()

        file_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=(
            ("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")))
        root.destroy()

        if len(file_paths) != 8:
            self.import_images_info.config(text="Please select exactly 8 Image files", fg="red")
            return
        else:
            self.import_images_info.config(text="Correctly imported files", fg="green")

            for file_path in file_paths:
                self.register_files.append(file_path)
            return

    def set_name(self):
        if self.name_entry.get() == "":
            self.entry_name_info.config(text="Provide your name", fg="red")
            return
        elif len(self.register_files) != 8:
            self.import_images_info.config(text="Please select exactly 8 Image files", fg="red")
            return
        else:
            new_person_dir = os.path.join("generated_faces", self.name_entry.get())
            if os.path.exists(new_person_dir):
                self.entry_name_info.config(text="Person with this name already exist in database", fg="red")
                return

            os.mkdir(new_person_dir)

            for i, file_path in enumerate(self.register_files):
                temp = self.name_entry.get() + "_" + str(i) + ".png"
                new_file_path = os.path.join(new_person_dir, temp)
                shutil.copy2(file_path, new_file_path)

            self.entry_name_info.config(text="Successfully registered", fg="green")
