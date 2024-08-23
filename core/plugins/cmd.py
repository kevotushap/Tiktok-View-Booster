from core import *

class cmd:
    def cls():
        os.system('cls')

    def thread_title():
        while True:
            current_time = time.time()
            runtime = int(current_time - start_time)
            os.system(f'title Tiktok view booster - Runtime {runtime}s')
            time.sleep(0.075)
