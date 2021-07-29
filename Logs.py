import sys
import os


class LogEntry:
    def __init__(self, level, thread, message, date):
        self.level = level
        self.thread = thread
        self.message = message
        self.date = date


class LogReader:
    def __init__(self):
        pass

    def read(self, filepath):
        if not os.path.exists(filepath):
            print("%s not found" & filepath)
            return

        f = open(filepath)  # load entire file into memory
        file_lines = f.readlines()
        f.close()
        return file_lines
