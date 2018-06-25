def grade(n):
    if(n=="A+" or n=="A"):
        t=4.0
    elif (n=="A-"):
        t=3.7
    elif (n == "B+"):
        t = 3.3
    elif (n == "B"):
        t = 3.0
    elif (n == "B-"):
        t = 2.7
    elif (n == "C+"):
        t = 2.3
    elif (n == "C"):
        t = 2.0
    elif (n == "C-"):
        t = 1.7
    elif (n == "D+"):
        t = 1.3
    elif (n == "D"):
        t = 1.0
    elif (n == "F"):
        t = 0.0
    else:
        t = -1.0

    return t


def cgpa(course,pcgpa,pcredit):
    credit=[5]
    tcredit=0
    gpa=0.0
    for i in range (0,course):
        p= int(input("Enter Course Credit: "))
        credit.append(p)
        n=input("Earned Grade: ")
        t = grade(n)
        if(t==-1.0):
            print("Invalid Grade Entered. Try Again.")
            i=i-1
        else:
            gpa=gpa + credit[i]*t
            tcredit=tcredit+credit[i]

    tcgpa = gpa + (pcgpa*pcredit)
    tcredit = tcredit + pcredit

    new= tcgpa/tcredit

    return round(new,2)


def main():
    course = int(input("Number Of Course Enrolled Into: "))
    pcgpa = float(input("CGPA Earned Until Now: "))
    pcredit = int(input("Credit Earned Until Now: "))
    result = cgpa(course,pcgpa,pcredit)
    print("New CGPA: ",result)



if __name__ == '__main__':
    main()
