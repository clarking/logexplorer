from tkinter import Frame, Scrollbar, ttk
from tkinter.ttk import Treeview
from typing import List
from Logs import LogEntry


class LogViewer(Frame):
    def __init__(self, *args, config):
        Frame.__init__(self, *args)
        self.cfg = config['grid']
        self.current_font = (config['font']['family'], int(config['font']['size']))

        self.style = ttk.Style()
        self.load_style()

        self.tree = Treeview(self, selectmode="browse", columns=('level', 'message', 'date'))

        self.tree.tag_configure('bg', background='#000000')
        self.tree.tag_configure('fg', foreground='#E8E8E8')

        for col in self.cfg['columns']:
            if not col['parent']:
                self.tree.heading('#0', text=col['header'])
                self.tree.column('#0', width=col['width'], stretch=col['stretch'])
            else:
                self.tree.heading(col['name'], text=col['header'])
                if 'width' in col:
                    self.tree.column(col['name'], width=col['width'], stretch=col['stretch'])
                else:
                    self.tree.column(col['name'], stretch=col['stretch'])

        self.vsb = Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.xsb = Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side='right', fill="y")
        self.tree.pack(fill="both", expand=True)

    def load_style(self):
        self.style.map('Treeview',
                       foreground=self.fixed_map('foreground'),
                       background=self.fixed_map('background'))
        self.style.configure('Treeview', highlightthickness=0, bd=0, font=self.current_font)
        self.style.configure('Treeview.Heading', highlightthickness=0, bd=0, font=self.current_font)
        self.style.configure('Treeview.Item', highlightthickness=0, bd=0, font=self.current_font)
        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

    def clear_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def update_tree(self, entries: List[LogEntry]):
        threads = []

        entry_id = 0
        for entry in entries:
            entry_id = entry_id + 1
            if entry.thread not in threads:
                threads.append(entry.thread)
                iid = self.tree.insert('', int(entry.thread), entry.thread, text=entry.thread)
                self.tree.item(iid, tags=('fg', 'bg'))
            else:
                self.tree.insert(
                    entry.thread,
                    entry_id, entry_id,
                    values=(entry.level, entry.message, entry.date),
                    tags=('fg', 'bg'))

    def fixed_map(self, option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in self.style.map('Treeview', query_opt=option) if
                elm[:2] != ('!disabled', '!selected')]
