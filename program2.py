filename = 'user_input.txt'

user_input = input("Enter something that you want to write:")

with open(filename,'w') as file:
    file.write(user_input)

print(f"Your input has been written to {filename}")
