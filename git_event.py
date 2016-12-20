import time
import os
from commit_parser import CommitParser


class GitEvent:

    @staticmethod
    def git_event(path, git_branch, event_type):
        try:
            git_commit = CommitParser(path).make_commit_message(event_type)
            time.sleep(2)
            os.system('git pull')
            os.system('git checkout '+git_branch)
            os.system('git add .')
            os.system('git commit -m \"'+git_commit+'\"')
            os.system('git push origin '+git_branch)
        except Exception as error:
            print(error)
            exit(0)
