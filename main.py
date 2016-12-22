from watcher import Watcher
from logger import Logger

if __name__ == '__main__':
    w = Watcher()
    l = Logger()
    l.setup_hearders()
    w.run()
