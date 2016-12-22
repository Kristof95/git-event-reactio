from watcher import Watcher
from logger import Logger

if __name__ == '__main__':
    w = Watcher()
    Logger.setup_headers()
    w.run()
