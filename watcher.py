import time
from watchdog.observers import Observer
from handler import Handler


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
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()
