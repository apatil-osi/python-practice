'''Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.'''

def main():

    s_list = []
    
    values = input("Enter sequence of comma separated values:\n")
    s_list = values.split(',')

    tup = tuple(s_list)

    print("List: ", s_list, "\nTuple: ", tup)

if __name__ == "__main__":
    main()

    