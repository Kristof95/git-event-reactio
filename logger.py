from datetime import datetime
import csv


class Logger:

    @staticmethod
    def logging(event_type, commit_message):
        log_file = open("logs/log.csv", "a")
        try:
            fieldnames = ('Date', 'Event type', 'Commit message')
            writer = csv.DictWriter(log_file, fieldnames)
            headers = dict((n, n) for n in fieldnames)
            writer.writerow(headers)
            writer.writerow({'Date': str(datetime.now()),
                             'Event type': event_type,
                             'Commit message': commit_message})
        finally:
            log_file.close()
