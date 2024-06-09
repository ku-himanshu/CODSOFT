import random
import string

def generate_password(l, complexity):
    if complexity in ("low","l"):
        ch= string.ascii_letters
    elif complexity in ("medium","m"):
        ch= string.ascii_letters + string.digits
    elif complexity in ('high',"h"):
        ch = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level !!!! ")
    
    password=""
    for i in range(l):
        password+=random.choice(ch)

    return password


while True:
    try:
        l = int(input("Enter the Required length of the password: "))
        if l <= 0:
            print("Please enter a positive integer(1,2,3,4...)\n")
        else:
            break
    except ValueError:
        print("ERROR!!")
        print("Please enter a valid integer.\n")
    
while True:
    print("Complexity levels:\nLow: Contains Only upper and lower case Alphabets\nMedium:Contains both digits and alphabets\nHard: Contains Alphabets, digits and Special characters too\n")
    complexity = input("Enter the desired complexity level (low, medium, high): ")
    print()
    complexity.lower()
    if complexity in ['low', 'medium', 'high',"l","h","m"]:
        break
    else:
        print("Please enter a valid complexity level: low, medium, or high...")

password = generate_password(l, complexity)
print("Generated Password:",password)



