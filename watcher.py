import time
from watchdog.observers import Observer
from handler import Handler
import subprocess


class Watcher:

    DIRECTORY_TO_WATCH = input("Directory:")
    # BRANCH = input("Git branch:")

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            whoami = subprocess.check_output("whoami", shell=True)
            error_msg = str(whoami, encoding='utf-8').replace("\n", "")+" interrupt the script with CTRL + C"
            print(error_msg)
        except Exception as e:
            self.observer.stop()
            print(e)
        self.observer.join()
