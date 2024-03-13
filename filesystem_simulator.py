# This is a coding assessment test for a file system simulator by Paul Farri
# Program also includes an interface for the end user to send commands like a prompt

import tkinter as tk
from tkinter import scrolledtext


# Defines a class for nodes in the file system (both directories and files)
class Node:
    def __init__(self, name, is_directory=False):
        self.name = name  # Name of the file or directory
        self.is_directory = is_directory  # Flag indicating if this is a directory
        self.children = []  # List of child nodes (for directories)
        self.parent = None  # Parent directory node


# Define the core file system class
class FileSystem:
    def __init__(self):
        self.root = Node("/", True)  # Root directory
        self.current = self.root  # Current working directory

    # Lists the contents of the current directory
    def ls(self):
        if self.current.is_directory:
            return "\n".join([child.name for child in self.current.children])
        else:
            return "Current location is not a directory. "

    # Creates a new directory in the current directory
    def mkdir(self, name):
        new_dir = Node(name, True)
        new_dir.parent = self.current
        self.current.children.append(new_dir)
        return f"Directory '{name}' created."

    # Changes the current directory
    def cd(self, dir_name):
        if dir_name == "..":  # Moves up to the parent directory
            if self.current.parent is not None:
                self.current = self.current.parent
                return "Moved up to the parent directory."
        else:  # Move into a child directory
            for child in self.current.children:
                if child.name == dir_name and child.is_directory:
                    self.current = child
                    return f"Changed directory to '{dir_name}'."
            return f"No such directory: '{dir_name}'"

    # Creates a new file in the current directory
    def touch(self, name):
        new_file = Node(name)
        self.current.children.append(new_file)
        return f"File '{name}' created."


# Defines the GUI class, inheriting from FileSystem for functionality
class FileSystemGUI(FileSystem):
    def __init__(self, master):
        super().__init__()
        self.master = master  # The main Tk window
        self.create_widgets()

    # Create GUI widgets
    def create_widgets(self):
        # Text area for output
        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(padx=10, pady=5)
        self.text_area.insert(tk.INSERT, "Simple File System GUI. Type 'exit' to quit.\n")
        self.text_area.configure(state='disabled')

        # Input field for commands
        self.input = tk.Entry(self.master, width=80)
        self.input.pack(padx=10, pady=5)
        self.input.bind("<Return>", self.process_command)  # Bind Enter key to command processing
        self.input.focus()

    # Processes commands entered by the user
    def process_command(self, event):
        command = self.input.get().strip().split(" ")
        cmd = command[0]
        arg = command[1] if len(command) > 1 else None

        # Determine the action based on the command
        if cmd == "exit":
            self.master.destroy()  # Closes the Interface
            return

        # Executes the command and get the output
        output = ""
        if cmd == "ls":
            output = self.ls()
        elif cmd == "mkdir" and arg:
            output = self.mkdir(arg)
        elif cmd == "cd" and arg:
            output = self.cd(arg)
        elif cmd == "touch" and arg:
            output = self.touch(arg)
        else:
            output = "Unknown command or missing argument"

        # Display the output in the text area
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.INSERT, f"$ {cmd} {arg if arg else ''}\n{output}\n")
        self.text_area.configure(state='disabled')
        self.text_area.see(tk.END)  # Scroll to the end of the text area
        self.input.delete(0, tk.END)  # Clears the input field


# Main function to run the Interface application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("File System Simulator")  # Sets the window title
    app = FileSystemGUI(root)  # Creates an instance of the Interface application
    root.mainloop()  # Starts the Interface event loop
