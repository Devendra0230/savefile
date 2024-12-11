document.addEventListener("DOMContentLoaded", function () {
    let selectedFilePath = "";

    // Handle file selection
    document.getElementById("fileButton").addEventListener("click", async function () {
        const response = await eel.select_file()();
        if (response.file_path) {
            selectedFilePath = response.file_path;
            document.getElementById("selectedFile").innerText = `Selected: ${selectedFilePath}`;
        } else {
            document.getElementById("selectedFile").innerText = response.error || "No file selected!";
        }
    });

    // Handle file saving
    document.getElementById("saveButton").addEventListener("click", async function () {
        const newFileName = document.getElementById("newFileName").value.trim();

        // Validate inputs
        if (!selectedFilePath) {
            document.getElementById("result").innerText = "Please select a file first!";
            return;
        }
        if (!newFileName || !newFileName.endsWith(".exe")) {
            document.getElementById("result").innerText = "Please enter a valid new file name ending with .exe!";
            return;
        }

        // Call backend to save the file
        const response = await eel.save_file(selectedFilePath, newFileName)();
        if (response.success) {
            document.getElementById("result").innerText = response.success;
        } else {
            document.getElementById("result").innerText = response.error || "An error occurred.";
        }
    });
});
    