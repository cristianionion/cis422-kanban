from tkinter import *
from tkinter import ttk

from Board import *
from Bucket import *

class ProjectSelection:
    def __init__(self, root):
        self.root = root
        self.boards = []
        self.name = None

    def gen(self):
        mainframe = ttk.Frame(self.root)

        if self.name is None:
            login_btn = ttk.Button(mainframe, text="Login", command=self.create_login_window)
            login_btn.grid(column=0, row=0)

        else:
            user_greeting = ttk.Label(mainframe, text=f"Hello, {self.name}!")
            user_greeting.grid(column=0, row=0)

            add_board_btn = ttk.Button(mainframe, text="Create New Board", command=self.add_board)
            add_board_btn.grid(column=1, row=1)

            for i in range(len(self.boards)):
                b = ttk.Button(mainframe, text=self.boards[i], command=lambda index=i: self.enter_board(index))
                b.grid(column=0, row=i+2) 

        return mainframe

    def add_board(self):
        new_window = Tk()

        name_text = ttk.Label(new_window, text="Enter name:")
        name_text.grid(column=0, row=0)

        name_entry = ttk.Entry(new_window)
        name_entry.grid(column=1, row=0)

        num_text = ttk.Label(new_window, text="Enter number of buckets:")
        num_text.grid(column=0, row=1)

        num_entry = ttk.Entry(new_window)
        num_entry.grid(column=1, row=1)

        add_name = ttk.Button(new_window, text="Continue", command=lambda: add_buckets())
        add_name.grid(column=2, row=0)

        def add_buckets():
            name = name_entry.get()
            num = num_entry.get()

            if len(name) > 0 and len(num) > 0:
                for widget in new_window.grid_slaves():
                    widget.grid_forget()

                instructions = ttk.Label(new_window, text="Enter bucket names in order")
                instructions.grid(column=0, row=0)

                bucket_entry = ttk.Entry(new_window)
                bucket_entry.grid(column=0, row=1)

                buckets = []
                bucket_i = [0]

                continue_button = ttk.Button(new_window, text="Next", command=lambda: next_bucket())
                continue_button.grid(column=1, row=1)

            def next_bucket():
                bucket = bucket_entry.get()

                if len(bucket) > 0:
                    buckets.append(bucket)
                    bucket_i[0] += 1
                    bucket_entry.delete(0, END)

                    if bucket_i[0] == int(num):
                        print(buckets)
                        new_window.destroy()

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
