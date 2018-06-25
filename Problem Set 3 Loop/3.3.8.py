def average(n):
    n = int(n)
    t = 0
    for i in range(1, n + 1):
        t = t + i

    return t/n


def main():
    n = int(input("Enter A Number: "))
    print(average(n))


if __name__ == '__main__':
    main()
