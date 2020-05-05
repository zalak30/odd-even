# different output for odd/even integers
print("Enter number between 1 to 100")
n = int(input().strip())


def is_even(num):
    if (num % 2 == 0) & (num in range(6, 21)):
        print('Weird')
    elif num % 2 == 0:
        print("Not Weird")
    else:
        print('Weird')


is_even(n)