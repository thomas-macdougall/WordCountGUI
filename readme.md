
# Word Count GUI for Text Files

## Overview

A quick project where I messed around with JavaScript (JXA) and used Python's Tkinter for a simple GUI. One cool thing I ran into was how text gets buffered in a file, making it tricky to read the file in real-time. That's why I used JavaScript for Automation (JXA) on my Mac, so I could grab the text before it gets saved. Outputs, the word count in text files you've got open. Only on macOS for now, but I'll add support for other operating systems soon.


## Features

- Real-time word count for each open `.txt` and `.rtf` file.
- The GUI window is placed near the text editor for easy visibility.
- Platform-independent, though some features require macOS.
  
## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/thomas-macdougall/WordCountGUI.git
cd WordCountGUI
```

#### Create and activate the Virtual Environment

- On macOS:

  ```bash
  pipenv shell
  ```

### 2. Install Dependencies

Once the virtual environment is activated, install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

Run the program using Python:

- Needs elevated privileges to monitor the directory.

```bash
sudo python main.py --dir "/path/to/your/directory"
```

Replace `"/path/to/your/directory"` with the directory you want to monitor.

## To Do

- [ ] Add support for other text editors.
- [ ] Add support for other operating systems.
- [ ] Pin the GUI to the text editor to prevent it from being shown on top of other windows.

