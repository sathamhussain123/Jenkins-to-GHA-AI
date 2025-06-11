from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests, time, os

WATCH_DIR = "/app/data/projects"

class JenkinsfileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if os.path.basename(event.src_path) == "Jenkinsfile":
            print(f"Detected change: {event.src_path}")
            try:
                requests.post("http://localhost:8000/convert/", json={"path": event.src_path})
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(JenkinsfileHandler(), path=WATCH_DIR, recursive=True)
    observer.start()
    print(f"Watching for Jenkinsfiles in {WATCH_DIR}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
