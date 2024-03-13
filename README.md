# Technical-Evaluation-Python-File-System-Simulator-
This is a Python program with an interface that simulates a file system without using any built-in data structure and is only held in memory.

It simulates a basic file system operations such as listing directory contents, creating directories, changing directories, and creating files. 
The program supports ls, mkdir, cd, and touch, and is designed to demonstrate how a file system works in a controlled and simulated environment.

Getting started:

1. Firstly, you must have Python 3 installed on your PC, which can be downloaded from the official Python website.
2. Download the repository to your local machine.
3. Go to the directory where the project has been saved.
4. Run the main script using your Python interpreter. PyCharm can be used for this, or you can run it through your terminal with "python filesystem_simulator.py".
5. How to use: The interface consists of a text area where the output of commands is displayed and an input field where you can type your commands.

commands - 
'ls' : Lists the contents of the current directory. 
'mkdir [directory_name]' : Creates a new directory in the current directory. 
'cd ..' : Use to move to the parent directory. 
'touch [file_name]' : Creates a new file in the current directory. 
'exit' : Exits the application 
(DO NOT INCLUDE THE APOSTROPHES)

Example Usage:

1. Start the program in your Python interpreter.
2. In the input field, type 'mkdir docs' and press Enter to create a new directory named "docs".
3. Type 'ls' and press Enter to view the list of contents in the current directory, including any added files. You should see "docs" listed.
4. Type 'cd docs' and press Enter to change into the "docs" directory.
5. Type 'touch readme.txt' and press Enter to create a new file called "readme.txt" inside the "docs" directory.
6. Type 'ls' again to see the newly created file listed inside the "docs" directory.
7. If you wish to exit, type 'exit' in the input field to quit the program.
