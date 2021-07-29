from tkinter import Toplevel, Label, Button, Text, Listbox


class AboutWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("About LogExplorer")
        self.geometry("200x200")

        Label(self, text="A simple log exploration app").pack(fill="both", expand=True)
        Button(self, text="Close", command=self.destroy).pack(expand=True)
        Label(self, text="Aaron Clark Diaz").pack(fill="x", side="bottom", expand=True)


class SearchWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Search")
        self.geometry("300x100")

        Label(self, text="look for:").pack(fill="x", side="top", expand=True)
        Text(self, height=1, padx=5).pack(fill="x", expand=True)
        Button(self, text="Close", command=self.destroy).pack(side="bottom", expand=True)


class FiltersWindow(Toplevel):
    def __init__(self, parent, config):
        super().__init__(parent)

        self.title("Filters")
        self.geometry("300x100")

        Label(self, text="look for:").pack(fill="x", side="top", expand=True)

        self.listbox = Listbox(self)
        self.listbox.pack(fill="both", side="left", expand=True)


        for item in config['filters']:

            self.listbox.insert("end", item['name'])

        Text(self, height=1, padx=5).pack(fill="x", expand=True)
        Button(self, text="Close", command=self.destroy).pack(side="bottom", expand=True)


class SettingsWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Settings")
        self.geometry("300x100")

        Label(self, text="look for:").pack(fill="x", side="top", expand=True)
        Text(self, height=1, padx=5).pack(fill="x", expand=True)
        Button(self, text="Close", command=self.destroy).pack(side="bottom", expand=True)
