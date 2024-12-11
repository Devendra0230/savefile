import os
import shutil
from tkinter import Tk, filedialog

import eel

# Initialize Eel app
eel.init('web')

# Fixed destination folder: User's "Documents" folder
DESTINATION_FOLDER = os.path.join(os.path.expanduser("~"), "Documents")

# Ensure the destination folder exists
os.makedirs(DESTINATION_FOLDER, exist_ok=True)


@eel.expose
def save_file(file_path, new_file_name):
    """
    Save the selected file to the fixed destination folder with the given new name.
    """
    if not file_path or not new_file_name:
        return {"error": "File path or new file name is missing!"}

    try:
        # Ensure the file exists
        if not os.path.exists(file_path):
            return {"error": "The selected file does not exist!"}

        # Get destination path
        destination_path = os.path.join(DESTINATION_FOLDER, new_file_name)

        # Check if file with the same name already exists in the destination folder
        if os.path.exists(destination_path):
            os.remove(destination_path)

        # Copy the file to the destination folder with the new name
        shutil.copy(file_path, destination_path)
        return {"success": f"File saved successfully to {destination_path}!"}
    except Exception as e:
        return {"error": str(e)}


@eel.expose
def select_file():
    """
    Open file dialog to select an .exe file.
    """
    try:
        root = Tk()
        root.withdraw()  # Hide the tkinter root window
        root.attributes("-topmost", True)  # Keep the dialog on top
        file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
        return {"file_path": file_path} if file_path else {"error": "No file selected!"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == '__main__':
    eel.start('index.html', size=(600, 400))
