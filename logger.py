from datetime import datetime
import csv


class Logger:
    
    log_file = open("logs/log.csv", "a")
    fieldnames = ('Date', 'Event type', 'Commit message')
    writer = csv.DictWriter(log_file, fieldnames)
    headers = dict((n, n) for n in fieldnames)

    @staticmethod
    def setup_headers():
        Logger.writer.writerow(Logger.headers)

    @staticmethod
    def logging(event_type, commit_message):
            Logger.writer.writerow({'Date': str(datetime.now()), 'Event type': event_type,
                                    'Commit message': commit_message})
