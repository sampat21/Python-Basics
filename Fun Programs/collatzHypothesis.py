def printCollatz(num):
    steps = 0
    while num != 1:
        print(num, end = '\n')

        # If n is even
        if num % 2 == 0:
            num = int(num / 2)

        # If odd
        else:
            num = int(3 * num + 1)
        steps = steps+1

    # Print 1 at the end
    print(num)

    return steps

# Driver code
num = int(input("Enter number: "))
count = printCollatz(num)
print("Steps: ", count)