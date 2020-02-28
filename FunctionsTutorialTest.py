number = int(input("number "))
def fact(number):
    count=1
    factorial = 1
    while count <= number:
        factorial = factorial * count
        count += 1
    return factorial
print (fact(number))

num = 5
def fact(num):
    count=1
    factorial = 1
    while count <= num:
        factorial = factorial * count
        count += 1
    return factorial
print (fact(num))



