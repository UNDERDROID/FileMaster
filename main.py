import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def create_folders(path, folder_names):
    for folder in folder_names:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"{folder} folder created")

def move_files(path, files, folder_names):
    for file in files:
        if file.endswith(('.jpg', '.png', '.jpeg')) and not os.path.exists(os.path.join(path, 'Images', file)):
            shutil.move(os.path.join(path, file), os.path.join(path, 'Images', file))
            print(f"{file} was moved to Images folder")
        elif file.endswith('.zip') and not os.path.exists(os.path.join(path, 'Compressed', file)):
            shutil.move(os.path.join(path, file), os.path.join(path, 'Compressed', file))
            print(f"{file} was moved to Compressed folder")
        else:
            print(f"No matching folder for {file}")

def organize_files():
    folder_names = ['Images', 'Compressed', 'Video']
    path = filedialog.askdirectory()
    
    if not path:
        messagebox.showwarning("No Folder Selected", "Please select a folder.")
        return
    
    files = os.listdir(path)
    create_folders(path, folder_names)
    move_files(path, files, folder_names)
    messagebox.showinfo("Task Completed", "Files have been organized successfully.")

# Create the main window
root = tk.Tk()
root.title("File Organizer")

# Create and place the button
organize_button = tk.Button(root, text="Select Folder and Organize Files", command=organize_files)
organize_button.pack(pady=50)

# Run the application
root.mainloop()
