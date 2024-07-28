import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, font

# Function to show message in GUI status widget
def show_operations(message):
    status_text.insert(tk.END, message + '\n')
    status_text.see(tk.END)
    root.update_idletasks

# Function to get options selected by the user in the check box 
def get_selected_items():
    selected_items = [option for option, var in zip(options, variables) if var.get()]
    messagebox.showinfo("Select the folders you want to create","\n".join(selected_items))

# Function to create folders selected by the user
def create_folders(path, selected_folders):
    for folder in selected_folders:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            show_operations(f"{folder} folder created") #prints the message in GUI
            print(f"{folder} folder created") #prints the message in terminal

# Function to move files in the created folder
def move_files(path, files, selected_folders):
    for file in files:
        if 'Images' in selected_folders and file.endswith(('.jpg', '.png', '.jpeg')) and not os.path.exists(os.path.join(path, 'Images', file)):
            shutil.move(os.path.join(path, file), os.path.join(path, 'Images', file))
            show_operations(f"{file} was moved to Images folder")
            print(f"{file} was moved to Images folder")

        elif 'Compressed' in selected_folders and file.endswith('.zip') and not os.path.exists(os.path.join(path, 'Compressed', file)):
            shutil.move(os.path.join(path, file), os.path.join(path, 'Compressed', file))
            show_operations(f"{file} was moved to compressed folder")
            print(f"{file} was moved to Compressed folder")
        
        else:
            show_operations(f"No matching folder for {file}")
            print(f"No matching folder for {file}")

# Function to select the path directory and organize the files by calling create_folders() & move_files()
def organize_files():
    selected_folders = [option for option, var in zip(options, variables) if var.get()]
    path = filedialog.askdirectory()
    
    if not path:
        messagebox.showwarning("No Folder Selected", "Please select a folder.")
        return

    files = os.listdir(path)
    create_folders(path, selected_folders)
    move_files(path, files, selected_folders)
    messagebox.showinfo("Task Completed", "Files have been organized successfully.")

# Create the main window for GUI
root = tk.Tk()
root.title("File Master")

# Display Heading
heading_font = font.Font(family='Helvetica', size=16, weight='bold')
heading_label = tk.Label(root, text="Select the files you want to organize", font=heading_font)
heading_label.pack(pady=10)

options = ['Images', 'Compressed', 'Video']
variables = []

for option in options:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=option, variable=var)
    chk.pack(anchor=tk.W)
    variables.append(var)

# Create and place the button
organize_button = tk.Button(root, text="Organize", command=organize_files)
organize_button.pack(pady=50)

# Status text widget
status_text = tk.Text(root, height=10, width=50)
status_text.pack(pady=20)

# Run the application
root.mainloop()
