import os
from file_modifier import FileModifier


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
            exit(0)

    def file_extension(self):
        splitted_path = self.file_path.split("\\")
        return splitted_path[len(splitted_path)-1]

    def make_commit_message(self, event_type):
        file_modifier = FileModifier(self.file_path)
        file_modifier.overwrite_file_content()
        if file_modifier.commit_message:
            return file_modifier.commit_message
        return event_type + self.SPACE + self.file_extension()
