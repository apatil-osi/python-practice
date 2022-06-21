## -- Problem URL: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def strRev(string):
    rslt = ' '.join(string.split()[::-1])
    return rslt

if __name__ == "__main__":
    string = "My name is Michele"
    #strRev(string)
    print("OG String was:", string, "\nReversed String is:",strRev(string))