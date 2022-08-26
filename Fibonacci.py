
# WK8Lab2 – Recursive Function
# Course no: CIS 261
# Name: Terrence Miller

# function to print 16 first fibonacci numbers using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    print("The fibonacci series for 16 ")
    for i in range(16):
        print(fibonacci(i), end=", ")
    print("...")   


if __name__ == "__main__":
    main()

