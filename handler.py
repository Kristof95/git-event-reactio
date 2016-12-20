from watchdog.events import FileSystemEventHandler
from git_event import GitEvent


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event, **kwargs):
        if event.is_directory:
            pass
        elif event.event_type:
            GitEvent.git_event(event.src_path, "master", str(event.event_type))
