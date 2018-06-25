def summation(n):
    n = int(n)
    t = 0
    for i in range(1, n + 1):
        if(i%2 != 0):
         t = t + i

    return t


def main():
    n = int(input("Enter A Number: "))
    print(summation(n))


if __name__ == '__main__':
    main()
