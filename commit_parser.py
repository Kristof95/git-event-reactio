import os
import re


class CommitParser:

    file_ext = ""
    SPACE = " "

    def __init__(self, file_path):
        self.file_path = file_path

    def file_exist(self):
        try:
            if os.path.lexists(self.file_path):
                return True
        except FileNotFoundError as error:
            print(error)
        return False

    def file_extension(self):
        splitted_path = self.file_path.split("/")
        return splitted_path[len(splitted_path)-1]

    def read_comment_from_file(self):
        commit_msg = ""
        pattern = ""
        file_content = self.read_file_content()
        for item in file_content:
            match_line = re.match(r"#commit/.*/end", item, re.M | re.I)
            if match_line:
                commit_msg = match_line.group().split("/")[1]
                pattern = match_line.group()
                file_content.remove(pattern)
                break
        with open(self.file_path, "w") as rewrite:
            for mod in file_content:
                rewrite.write(mod+"\n")
        return commit_msg

    def read_file_content(self):
        content = []
        if self.file_exist():
            with open(self.file_path, "r") as file:
                for line in file.readlines():
                    content.append(line.strip())
        return content

    def make_commit_message(self, event_type):
        if self.read_comment_from_file():
            return self.read_comment_from_file()
        return event_type + self.SPACE + self.file_extension()

# if __name__ == '__main__':
#     cp = CommitParser("log")
#     print(cp.make_commit_message("test"))