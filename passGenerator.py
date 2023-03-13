import random

def generatePassword(chars, numbers, symbols):
    # defining the string of choices of characters, numbers, and symbols.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "123456789"
    syms = "!@#$%^&*()"

  

    chosenLetters = random.sample(characters, chars)
    chosenNumbers = random.sample(nums, numbers)
    chosenSymbols = random.sample(syms, symbols)

    passwordList = chosenLetters + chosenNumbers + chosenSymbols
    
    random.shuffle(passwordList)

    password = "".join(passwordList)

    return password


if __name__ == "__main__":

    chars = int(input("Enter the number of the character that you want in your password: "))
    numbers = int(input("Enter the number of the numbers that you want in your password: "))
    symbols = int(input("Enter the number of the symbols that you want in your password: "))

    password = generatePassword(chars, numbers, symbols)
    print("A randomly selected password is:", password)
