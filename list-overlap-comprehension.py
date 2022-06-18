
## -- Problem URL: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

def overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    c = []

    c = [i for i in set(a) if i in b]

    print(c)

if __name__ == "__main__":
    overlap()