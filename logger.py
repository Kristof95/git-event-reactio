from datetime import datetime
import csv


class Logger:

    @staticmethod
    def setup_headers():
        with open('logs/log.csv', 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=',')
            data = [['Date', 'Event type', 'Commit message']]
            a.writerows(data)

    @staticmethod
    def logging(event_type, commit_message):
        with open("logs/log.csv", "a", newline='') as logfile:
            reader = csv.reader(logfile)
            # next(reader, None)
            out = csv.writer(logfile, delimiter=',')
            out.writerow([str(datetime.now()), event_type,commit_message])


# if __name__ == '__main__':
#     # Logger.setup_headers()
#     Logger.logging("Test", "test logger class")