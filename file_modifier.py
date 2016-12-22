import re


class FileModifier:

    commit_message = ""

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        content = []
        with open(self.filepath, "r") as read_file:
            for line in read_file.readlines():
                content.append(line.replace("\n", "").strip())
        return content

    def remove_commit_pattern(self):
        content = self.read()
        commit_message = ""
        pattern = ""
        is_match = False
        for item in content:
            match_line = re.match(r"#commit/.*/end", item, re.M | re.I)
            if match_line:
                pattern = match_line.group()
                commit_message = str(match_line.group()).split("/")[1]
                is_match = True
                break
        if is_match:
            content.remove(pattern)
        return content, commit_message

    def overwrite_file_content(self):
        new_content, self.commit_message = self.remove_commit_pattern()
        with open(self.filepath, "w") as write_file:
            for new in new_content:
                write_file.write(new + "\n")


# if __name__ == '__main__':
#     fm = FileModifier("log")
#     fm.overwrite_file_content()
#     print(fm.commit_message)