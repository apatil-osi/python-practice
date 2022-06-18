## -- Problem URL: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

def palin():
    print("Please enter a string of your choice")
    char = str(input())

    
    print("Regular:",char[0:], "\nReversed:", char[::-1])
    
    if char[0:] == char[::-1]:
        print("String is a Palindrome")
    else:
        print("String is Not a palindrome")

if __name__ == "__main__":
    palin()