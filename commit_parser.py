import os
import re


class CommitParser:

    file_ext = ""
    DEFAULT_MSG = " "

    def __init__(self, file_path):
        self.file_path = file_path

    def file_exist(self):
        if os.path.lexists(self.file_path):
            return True
        return False

    def file_extension(self):
        if self.file_path and self.file_exist():
            extension = self.file_path.split("/")
            if len(extension) > 1 and "." in extension[len(extension)-1]:
                self.file_ext = str(extension[len(extension)-1]).split(".")[1]
                return self.file_ext if self.file_path else "file"
            return extension[len(extension)-1]

    def read_comment_from_file(self):
        commit_msg = ""
        if self.file_exist():
            with open(self.file_path, "r") as file:
                for line in file.readlines():
                    match_line = re.match(r"#commit/.*/end", line, re.M | re.I)
                    if match_line:
                        commit_msg = match_line.group().split("/")[1]
                        break
            return commit_msg

    def make_commit_message(self, event_type):
        if self.read_comment_from_file():
            return self.read_comment_from_file()
        return event_type + self.DEFAULT_MSG + self.file_extension()


# if __name__ == '__main__':
#     cp = CommitParser("test.sh")
#     print(cp.make_commit_message())
