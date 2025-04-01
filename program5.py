old_file = input("Enter the file that you want to copy:")
new_file = 'new_file'

with open(old_file, 'r') as source_file:
    with open(new_file, 'w') as destination_file:
        content = source_file.read()
        destination_file.write(content)

print(f"Your {old_file} has been copied to {new_file}")
