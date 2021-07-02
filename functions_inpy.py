from random import *
from functools import *
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
#b=shuffle(a)
#print(b)
#type(b)

num = randint(0,100)
print(num)
name = input('What is ur name ?')
print('Hello {}'.format(name))

def greet(name):
    print('Good Morning '+name)
greet(name)

def add(a,b):
    return a+b
b = add(20,50)
print(b)

def even_num(a):
    """
    This function return even numbers!
    input = a list
    output = a list
    """
enum = []
for numbers in a:
    if numbers%2==0:
        enum.append(numbers)
print(enum)
#even_num(int(input("enter a list ="))

def new_func(*args):
    print(args)
    for item in args:
        print(item)
new_func(12,34,56,78,99)

def nu (**kwargs):
    print(kwargs)
    if 'flower' in kwargs:
        print('we have {} for you!' .format(kwargs['flower']))
    else:
        print('No flower for you')

nu(flower='rose')
# Map function
def cal_sq(n):
    return n*n
#cal_sq(5)
print(cal_sq(5))

l = [1,2,3,4,5]
map(cal_sq, l)
for items in map(cal_sq, l):
    print(items)

y = list(map(cal_sq, l))
print(y)

#Filter function
def check_even(n):
    return n%2==0
print(check_even(10))

filter(check_even, l)
for p in filter(check_even, l):
    print(p)

#lambda function
cal_sq = lambda n:n*n
print(cal_sq(25))

z = list(map(lambda n:n*n, l))
print(z)

q = list(filter(lambda n:n%2==0, l))
print(q)

new = [1,2,3,4,5]
new.pop(0)
print(new)


