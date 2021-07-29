from tkinter import Tk, Frame, Menu, filedialog, Label

from Dialogs import AboutWindow, SearchWindow, FiltersWindow
from Viewer import LogViewer
from Logs import *


class LogExplorerApp(Tk):
    def __init__(self, config):
        super().__init__()

        self.cfg = config
        self.win_cfg = self.cfg['window']
        self.parse_cfg = self.cfg['parsing']

        self.reader = LogReader()
        self.title("Log Explorer")
        self.geometry(self.win_cfg['geometry'])

        self.main_frame = Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.add_menu()

        self.log_view = LogViewer(self.main_frame, '', config=self.win_cfg)
        self.log_view.pack(fill="both", expand=True)

        self.status_bar = Label(self, text="ready...", bd=0, relief="sunken", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

        self.file_lines = []
        self.threads = []
        self.entries = []

    def add_menu(self):
        menu = Menu(self)
        file_menu = Menu(menu)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Open Directory")
        file_menu.add_command(label="Settings", command=self.set_separator)
        file_menu.add_command(label="Exit", command=self.set_separator)

        logs_menu = Menu(menu)
        logs_menu.add_command(label="Search", command=lambda name="search": self.open_widow(name))
        logs_menu.add_command(label="Filters", command=lambda name="filters": self.open_widow(name))

        tools_menu = Menu(menu)
        tools_menu.add_command(label="Data Summary", command=self.get_summary)
        tools_menu.add_command(label="Colors", command=self.select_colors)
        tools_menu.add_command(label="Columns", command=self.select_columns)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Logs", menu=logs_menu)
        menu.add_cascade(label="Tools", menu=tools_menu)
        menu.add_command(label="About", command=lambda name="about": self.open_widow(name))
        self.config(menu=menu)

    def get_summary(self):
        print("get summary")

    def select_colors(self):
        print("set separator")

    def set_separator(self):
        print("set separator")

    def select_columns(self):
        print("select columns")

    def filter_data(self):
        print("filter data")

    def about(self):
        print("about")

    def open_widow(self, name):
        window = None
        if name == "about":
            window = AboutWindow(self)

        elif name == "search":
            window = SearchWindow(self)

        elif name == "filters":
            window = FiltersWindow(self, self.cfg)

        window.grab_set()

    def open_file(self):

        filename = filedialog.askopenfilename()
        self.status_bar.configure(text="Loading")
        self.update_idletasks()

        self.process_log(self.reader.read(filename))
        self.log_view.update_tree(self.entries)
        self.status_bar.configure(text="Done")

    def process_log(self, lines):
        for line in lines:
            parts = line.split(self.parse_cfg['separator'])  # generic split
            self.entries.append(LogEntry(parts[1], parts[2], parts[3], parts[0]))
