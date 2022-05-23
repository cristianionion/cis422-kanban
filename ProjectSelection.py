from tkinter import *
from tkinter import ttk

from Board import *
from Bucket import *

class ProjectSelection:
    def __init__(self, root):
        self.root = root
        self.boards = []
        self.board_name = StringVar()
        self.name = None

    def gen(self):
        mainframe = ttk.Frame(self.root)

        if self.name is None:
            login_btn = ttk.Button(mainframe, text="Login", command=self.create_login_window)
            login_btn.grid(column=0, row=0)

        else:
            user_greeting = ttk.Label(mainframe, text=f"Hello, {self.name}!")
            user_greeting.grid(column=0, row=0)

            name_entry = ttk.Entry(mainframe, text="Name", textvariable=self.board_name)
            name_entry.grid(column=0, row=1)

            add_board_btn = ttk.Button(mainframe, text="Add Board", command=self.add_board)
            add_board_btn.grid(column=1, row=1)

            for i in range(len(self.boards)):
                b = ttk.Button(mainframe, text=self.boards[i], command=lambda index=i: self.enter_board(index))
                b.grid(column=0, row=i+2) 

        return mainframe

    def add_board(self):
        name = self.board_name.get()

        if len(name) > 0:
            self.board_name.set("")
            self.boards.append(name)

            for widget in self.root.grid_slaves():
                widget.grid_forget()

            self.gen().grid(column=0, row=0)

    def enter_board(self, index):
        for widget in self.root.grid_slaves():
            widget.grid_forget()

        buckets = [Bucket("Not Started", []),
                   Bucket("In Progress", []),
                   Bucket("Completed", [])
                   ]

        b = Board(self.root, self.boards[index], buckets)

        for bucket in buckets:
            bucket.change_parent_to(b)

        b.gen().grid(row=0, column=0)

    def create_login_window(self):
        new_window = Tk()
        new_window.title("Kanban")

        window_frame = ttk.Frame(new_window, padding="4 10 4 10")

        name_text = ttk.Label(window_frame, text="Enter Name:")
        name_text.grid(column=0, row=0)

        name = StringVar() 
        name_input = ttk.Entry(window_frame, textvariable=name)
        name_input.grid(column=1, row=0)

        password_text = ttk.Label(window_frame, text="Enter Password:")
        password_text.grid(column=0, row=1)

        password = StringVar() 
        password_input = ttk.Entry(window_frame, textvariable=password)
        password_input.grid(column=1, row=1)

        login_button = ttk.Button(window_frame,
                                  text="Sign in",
                                  command=lambda: self._login(name_input.get(), password_input.get(), new_window)
                                  )
        login_button.grid(column=0, row=2)

        window_frame.grid(column=0, row=0)

        new_window.mainloop()

    def _login(self, name: str, password: str, new_window):
        self.name = name
        # Need to login here
        new_window.destroy()
        for widget in self.root.grid_slaves():
            widget.grid_forget()

        self.gen().grid(column=0, row=0)
