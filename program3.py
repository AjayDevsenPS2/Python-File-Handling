new_txt = input("Enter something that you want to append to the text file:")

filename = 'user_input.txt'

with open(filename, 'a') as file:
    file.write('\n' + new_txt)
print(f"Your new input has been added to the file {filename}")
