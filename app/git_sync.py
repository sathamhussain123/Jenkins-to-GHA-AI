import subprocess
import time
import os

REPO_DIR = "/app/data/projects"

def pull_changes():
    while True:
        print("[git_sync] Pulling latest changes...")
        try:
            subprocess.run(["git", "-C", REPO_DIR, "pull"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"[git_sync] Git pull failed: {e}")
        time.sleep(60)

if __name__ == "__main__":
    print("[git_sync] Starting Git sync loop...")
    pull_changes()