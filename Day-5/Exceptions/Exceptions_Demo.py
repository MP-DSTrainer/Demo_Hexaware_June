
# Python program to handle simple exception
'''
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))

    print ("Fourth element = %d" %(a[3]))
except :
    print ("An error occurred")


# Program to depict else clause with try-except
# Function which returns a/b
def divide(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
# Driver program to test above function
divide(2.0, 3.0)
divide(3.0, 3.0)

# Python program to demonstrate finally
try:
    k = 5//1 # raises divide by zero exception.
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("No exception raised")

finally:
# this block is always executed
# regardless of exception generation.
    print('This is always executed')

# Program to depict Raising Exception
try:
    raise NameError("Hi there") # Raise Error
except NameError as e:
    print ("An exception",e)

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("argument is not numbers\n", Argument)
temp_convert("xyz")
'''
class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

