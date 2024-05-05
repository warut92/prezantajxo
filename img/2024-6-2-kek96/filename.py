import os

# Get the current directory
current_directory = os.getcwd()

# Get all file names in the current directory
file_names = os.listdir(current_directory)

# Write file names to a text file
with open('file_names.txt', 'w') as file:
    for name in file_names:
        file.write('<img src="img/2024-6-2-kek96/' + name + '" alt="200">\n')