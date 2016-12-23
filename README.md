# Cloned git repository folder file event listener
- The script react to file events (e.g file creation, modify).
- When a file modified in a directory which listening this script,
then the script is going to push the file to the remote repository.
- Made a commit pattern: #commit/This is a commit message/end.
- The script search commit pattern in file content which modified or created,
if the file is contains this commit pattern the script read the text among slashes
and push to the remote repository with this commit message.
If file is not contains commit pattern the file is going to push
to remote repository according to file event type + file name.
(e.g commit message: modified README.md)

- Logger is a clear-cut, this class is going to save date of event, event type and the commit message
to logs/log.csv.
#commit/Logger class is under testing./end