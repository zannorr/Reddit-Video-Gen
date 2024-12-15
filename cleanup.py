import os
import shutil
import psutil
import time
def find_and_kill_processes_using_file(file_path):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for item in proc.open_files():
                if item.path == file_path:
                    proc.terminate()
                    proc.wait()
                    print(f"Terminated process {proc.pid} ({proc.name()}) using file {file_path}")
                    return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return False

def delete_specific_folders_in_current_directory(folders_to_delete, retries=3, delay=1):
    current_directory = os.getcwd()
    
    for item in os.listdir(current_directory):
        item_path = os.path.join(current_directory, item)
        if os.path.isdir(item_path) and item in folders_to_delete:
            for attempt in range(retries):
                try:
                    shutil.rmtree(item_path)
                    print(f"Deleted: {item_path}")
                    break
                except Exception as e:
                    if "being used by another process" in str(e):
                        # Attempt to close handles
                        for root, dirs, files in os.walk(item_path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                if find_and_kill_processes_using_file(file_path):
                                    time.sleep(delay)
                                    break
                    if attempt < retries - 1:
                        print(f"Retrying deletion of {item_path} due to error: {e}")
                        time.sleep(delay)
                    else:
                        print(f"Failed to delete {item_path} after {retries} attempts: {e}")
    print('Restarting application. Please Reopen and continue.')