from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests, time, os

WATCH_DIR = "/app/data/projects"

class JenkinsfileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and os.path.basename(event.src_path) == "Jenkinsfile":
            print(f"[🔍] Detected change: {event.src_path}")
            time.sleep(0.5)  # Ensure file write is complete
            try:
                response = requests.post(
                    "http://localhost:8000/convert/",
                    json={"path": event.src_path}
                )
                if response.status_code == 200:
                    result = response.json()
                    print(f"[✅] Conversion done! Workflow at: {result['workflow_path']}")
                else:
                    print(f"[❌] Conversion failed: {response.text}")
            except Exception as e:
                print(f"[⚠️] Error during API call: {e}")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(JenkinsfileHandler(), path=WATCH_DIR, recursive=True)
    observer.start()
    print(f"[👀] Watching for Jenkinsfile changes in {WATCH_DIR}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
