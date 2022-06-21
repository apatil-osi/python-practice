## -- Problem URL: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

from random import random
import random
import string
def password(strength, length):
    paswd = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    if strength == 'strong':
        temp = random.sample(paswd, length)
        usrPassword = ''.join(temp)
    else:
        ranLst = ["Hello", "password", "birthday", "world", "charizma"]
        temp = random.sample(ranLst, len(ranLst))
        usrPassword = ''.join(temp)

    return usrPassword

if __name__ == "__main__":
    print("Enter length of password:")
    length = int(input())
    print("Enter strength of password (strong/weak):")
    strength = str(input())
    print("Your password was seleceted to be:", password(strength, length))

