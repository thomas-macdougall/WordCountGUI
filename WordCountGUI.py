from tkinter import Tk, Label, Toplevel
import threading
import time
import queue
import subprocess

# Function to get document text using JXA script
def get_data_from_jxa(filename, script_path):
    with open(script_path, 'r') as file:
        jxa_script_template = file.read()
    
    jxa_script = jxa_script_template.replace("__FILENAME__", filename)
    result = subprocess.run(['osascript', '-l', 'JavaScript', '-e', jxa_script], capture_output=True, text=True)
    
    return result.stdout.strip()

# Function to get window information
def window_info(filename):
    result = get_data_from_jxa(filename, 'get_window_info.js')
    coords = result.split(', ')
    
    new_coords = {}
    for coord in coords:
        key_value = coord.split(':')
        if len(key_value) == 2:
            key, value = key_value
            new_coords[key] = value
    
    return new_coords


# Main Class for Word Count App
class WordCountApp:
    def __init__(self, file_path, root=None):
        self.file_path = file_path
        self.file_name = self.file_path.split("/")[-1].split(".")[0]
        self.word_count_queue = queue.Queue()

        self.updateFreq = 1000
        self.closed = False
        
        # Initialize Tkinter window
        self.root = Tk() if root is None else Toplevel(root)
        self.root.title(f"Word Count for {file_path}" if root else "Word Count Application")
        
        # Set window position
        self.update_position(window_info(self.file_name))
        
        # Initialize label and pack it
        self.label = Label(self.root, text="Word Count: 0")
        self.label.pack()
        self.root.wm_attributes("-topmost", True)

        # Create and start update thread
        self.update_thread = threading.Thread(target=self.updates)
        self.update_thread.daemon = True
        self.update_thread.start()
        
        # Set window close protocol and UI update
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.after(self.updateFreq, self.update_ui)
                        
        if root is None:
            self.root.mainloop()

    # Function to close the window
    def close_window(self):
        self.closed = True
        self.root.destroy()

    # Function to continuously update window position and word count
    def updates(self):
        while self.closed is False:
            self.update_position(window_info(self.file_name))
            self.update_word_count(get_data_from_jxa(self.file_name, 'docText.js'))
            time.sleep(1)

    # Function to update word count
    def update_word_count(self, text):
        word_count = len(text.split())
        self.word_count_queue.put(word_count)

    # Function to update window position
    def update_position(self, coords):
        if coords == {}:
            return
        x, y, width, height = map(int, [coords['x'], coords['y'], coords['width'], coords['height']])
        self.root.geometry(f"+{x+width-105}+{height+y-50}")
        self.root.update()

    # Function to update UI elements
    def update_ui(self):
        try:
            word_count = self.word_count_queue.get_nowait()
            self.label.config(text=f"Word Count: {word_count}")
        except queue.Empty:
            pass
        self.root.after(1000, self.update_ui)
