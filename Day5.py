import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print('Welcome to the PyPassword Generator')
numletters = int(input('How many letters would you like in your password?\n'))
numnumbers = int(input('How many numbers would you like in your password?\n'))
numsymbols = int(input('How many symbols would you like in your password?\n'))
password = []
for char in range(1, numletters + 1):
    randomCharacter = random.choice(letters)
    password.append(randomCharacter)
for num in range(1, numnumbers + 1):
    randomnumber = random.choice(numbers)
    password.append(randomnumber)
for sym in range(1, numsymbols + 1):
    randomsymbol = random.choice(symbols)
    password.append(randomsymbol)
random.shuffle(password)

# once we created a list with the appropriate characters the next step was migrating that into a string using a for loop
passwordString = ''
for item in password:
    passwordString += item
print(passwordString)