value = input("Welcome to the menu. Options are listed below:")

print("The value you input is:", value)
print(f'It is of type {type(value)}.')

while True:
    if value.isdigit() ==True:
        value = int(value)
        break #exit the loop when right datatype used
    else:
        value=input("Invalid input, please provide an integer:") #ask for a new value

print("The converted is:", value)
print(f'It is of type {type(value)}.')

        
