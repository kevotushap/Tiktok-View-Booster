from core import *

class f:
    black = Fore.LIGHTBLACK_EX
    res = Fore.RESET
    cyan = Fore.CYAN
    red = Fore.RED
    green = Fore.GREEN

class log:
    def get_time(self) -> str:
        return datetime.datetime.now().strftime('%H:%M:%S')
    
    def info(module: str, message: str):
        print(f'{f.black}{log.get_time()} {f.cyan}INF{S.RESET_ALL} {f.black}[{module}] {f.res}>{f.black} [{message}]')

    def error(module: str, message: str):
        print(f'{f.black}{log.get_time()} {f.red}ERR{S.RESET_ALL} {f.black}[{module}] {f.res}>{f.black} [{message}]')