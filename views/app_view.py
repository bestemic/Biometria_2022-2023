from tkinter import *

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
        start_label = Label(self.start_screen, text="Eigenfaces recognition app", font="Helvetica 50 bold", fg=LIGHT, bg=DARK)
        start_label.pack(pady=(120, 10))

        button = Button(self.start_screen, text="Start", font=("Helvetica", 40), bg=DARK_BUTTON, fg=LIGHT,
                        activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=10, command=self.open_menu_screen)
        button.pack(pady=(150, 0))

    def open_menu_screen(self):
        self.menu_screen.tkraise()

    def init_menu_screen(self):
        start_label = Label(self.menu_screen, text="Chooce option", font="Helvetica 50", fg=LIGHT, bg=DARK)
        start_label.pack(pady=(70, 10))

        # TODO name and function
        login = Button(self.menu_screen, text="LOGIN", font=("Helvetica", 40), bg=DARK_BUTTON, fg=LIGHT,
                        activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, command=self.open_start_screen)
        login.pack(pady=(100, 10))

        # TODO name and function
        register = Button(self.menu_screen, text="REGISTER", font=("Helvetica", 40), bg=DARK_BUTTON, fg=LIGHT,
                        activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, command=self.open_start_screen)
        register.pack()

        back = Button(self.menu_screen, text="Back", font=("Helvetica", 40), bg=DARK_BUTTON, fg=LIGHT,
                        activebackground=DARK_BUTTON_FOCUS, activeforeground=LIGHT, bd=5, command=self.open_start_screen)
        back.pack(pady=(10, 0))

