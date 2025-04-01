file_name = input("Enter the file that you want to read.:")
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"The file you are looking for is not found:")
