def factorial(n):
    n=int(n)
    t=1
    for i in range(1,n+1):
        t=t*i
     

    return t


def main():
    n=int(input("Enter A Number: "))
    print(factorial(n))


if __name__ == '__main__':
    main()
