'''
l=[1,2,3,4,5]
#print(l[6])#IndexError
#a=1+'2'#TypeError
#a=int('abc') # ValueError
n=10/0#ZeroDivisionError


try:
    a=10
    b=0
    c=a/b#throw the exception
    print(c)
except TypeError:
    print('division by zero')
except ZeroDivisionError as e :
    print('error-',e)
except Exception:
    print('exception')
else:
    print('no exception')
finally:
    print('finally bye...')


Student('Rajni')

try:
    raise NameError('This is name error')#forcefully we are throwing the exception
except NameError as e :
    print(e)

def divide(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
# Driver program to test above function
#divide(2.0, 3.0)
divide(3.0, 3.0)
'''
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("argument is not numbers\n", Argument)
temp_convert("xyz")





