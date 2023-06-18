from tkinter import *

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

    def display(self):
        self.root.title('Eigenfaces app')
        self.root.geometry("1200x600")
        self.root.config(bg=DARK)

        screen_list = [self.start_screen, self.menu_screen]

        for screen in screen_list:
            screen.place(relx=0, rely=0, relwidth=1, relheight=1)
            screen.configure(bg=DARK)

        self.init_start_screen()
        self.init_menu_screen()

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
                                  command=self.open_start_screen)
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
