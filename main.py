from tkinter import Tk, Toplevel
from WordCountGUI import WordCountApp
import psutil
import os
import argparse

# Get all .txt and .rtf files from a directory recursively.
def get_txt_and_rtf_files(directory):
    return [
        os.path.join(root, filename)
        for root, _, filenames in os.walk(directory)
        for filename in filenames
        if filename.endswith((".txt", ".rtf"))
    ]

# Check if a file is currently open by any process.
def is_file_open(file_path):
    for proc in psutil.process_iter(attrs=['pid', 'open_files']):
        try:
            if proc.info['open_files']:
                if any(f.path == file_path for f in proc.info['open_files']):
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Get the open status for each file in the list.
def get_open_file_status(files):
    return {file: is_file_open(file) for file in files}

# Update the UI to show open files.
def update_ui(root, directory, open_windows):
    
    files = get_txt_and_rtf_files(directory)
    file_status = get_open_file_status(files)

    for file, is_open in file_status.items():
        if is_open:
            if file not in open_windows:
                open_windows[file] = WordCountApp(file, root)
        else:
            if file in open_windows:
                open_windows[file].close_window()
                del open_windows[file]
    
    # Schedule the next UI update
    root.after(100, lambda: update_ui(root, directory, open_windows))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help="The directory to monitor", default="path/to/directory")

    args = parser.parse_args()
   
    root = Tk()

    # Create a dummy window to hide the root window
    dummy = Toplevel(root)
    root.withdraw()
    dummy.destroy()

    open_windows = {}
    root.after(100, lambda: update_ui(root, args.directory, open_windows))
    root.mainloop()

