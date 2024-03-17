import os

# Get the current working directory
current_dir = os.getcwd()
print("Current directory:", current_dir)

# List files and directories in the current directory
print("Contents of the current directory:")
for item in os.listdir(current_dir):
    print(item)

# Create a new directory
new_dir = os.path.join(current_dir, 'new_directory')
os.makedirs(new_dir, exist_ok=True)
print("Created directory:", new_dir)

# Check if a file exists
file_path = os.path.join(current_dir, 'example.txt')
file_exists = os.path.exists(file_path)
print("File exists:", file_exists)

# Write some content to a file
if not file_exists:
    with open(file_path, 'w') as file:
        file.write("Hello, world!")

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()
    print("File content:", file_content)

# Delete the file and directory
os.remove(file_path)
print("Deleted file:", file_path)

os.rmdir(new_dir)
print("Deleted directory:", new_dir)