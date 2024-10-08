# core/plugins/log.py

import datetime

class ConsoleFormat:
    def __init__(self):
        self.black = '\033[30m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.yellow = '\033[33m'
        self.blue = '\033[34m'
        self.magenta = '\033[35m'
        self.cyan = '\033[36m'
        self.white = '\033[37m'
        self.reset = '\033[0m'

class Style:
    def __init__(self):
        self.RESET_ALL = '\033[0m'

class Log:
    def __init__(self):
        self.formatter = ConsoleFormat()
        self.style = Style()

    def get_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self, module, message):
        f = self.formatter
        S = self.style
        print(f'{f.black}{self.get_time()} {f.cyan}INF{S.RESET_ALL} {f.black}[{module}] {f.reset}>{f.black} [{message}]')

    def error(self, module, message):
        f = self.formatter
        S = self.style
        print(f'{f.black}{self.get_time()} {f.red}ERR{S.RESET_ALL} {f.black}[{module}] {f.reset}>{f.black} [{message}]')

# Create a single instance of Log
log = Log()
