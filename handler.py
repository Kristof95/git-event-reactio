from watchdog.events import FileSystemEventHandler
from git_event import GitEvent


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event, **kwargs):
        if event.event_type == 'created' or event.event_type == 'modified':
            GitEvent.git_event(event.src_path, "master", str(event.event_type))
