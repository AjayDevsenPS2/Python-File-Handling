filename = input('Enter the file you want to open: ')
with open(filename, 'r') as file:
    count = 0
    for line in file:
        count += 1
print(f"The line count in {filename} is {count}")
