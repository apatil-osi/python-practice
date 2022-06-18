## -- Problem URL: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

def comp():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = []

    ## Traditional solution

    for i in a:
        if i % 2 == 0:
            b.append(i)

    ## One line solution (LIST COMPREHENSION)

    c = [i for i in a if i % 2 == 0]

    print(b)

    print("One line solution demonstrating List Comprehension:", c)
def main():
    comp()

if __name__ == "__main__":
    main()


