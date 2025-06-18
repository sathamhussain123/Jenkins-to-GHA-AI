import multiprocessing
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_api():
    subprocess.run(["uvicorn", "convert_api:app", "--host", "0.0.0.0", "--port", "8000"])

def run_file_watcher():
    subprocess.run(["python", os.path.join(BASE_DIR, "file_watcher.py")])

def run_git_sync():
    subprocess.run(["python", os.path.join(BASE_DIR, "git_sync.py")])

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_api)
    p2 = multiprocessing.Process(target=run_file_watcher)
    p3 = multiprocessing.Process(target=run_git_sync)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()