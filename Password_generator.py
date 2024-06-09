import random
import string

def generate_pd(l, level):
    if level in ("low","l"):
        ch= string.ascii_letters
    elif level in ("medium","m"):
        ch= string.ascii_letters + string.digits
    elif level in ('high',"h"):
        ch = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid level level !!!! ")
    
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
        print("Please enter a valid integer... \n")
    
while True:
    print("Complexity levels:\nLow: Contains Only upper and lower case Alphabets\nMedium:Contains both digits and alphabets\nHard: Contains Alphabets, digits and Special characters too\n")
    level = input("Enter the desired Complexity level (low, medium, high): ")
    print()
    level.lower()
    if level in ['low', 'medium', 'high',"l","h","m"]:
        break
    else:
        print("Please enter a valid Complexity level: low, medium, or high...")

password = generate_pd(l, level)
print("Generated Password:",password)



