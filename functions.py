# scope
global_var = 1
def my_vars():
    print 'Global var:', global_var
    local_var = 2
    print 'Local var:', local_var
    global inner_var
    inner_var = 3

my_vars()
print 'Coerced var:', inner_var

# args
def echo(user):
    print 'User:', user
echo('Mike')

def echo(user, lang, sys):
    print 'User:', user, 'Language:', lang, 'System:', sys
echo('Mike', 'Python', 'Windows')
echo(lang='C++', sys='Linux', user='Alex')

def mirror(user = 'Ann', lang = 'Python'):
    print '\nUser:', user, 'Language:', lang
mirror()
mirror(lang = 'Java')
mirror(user = 'Tony')
mirror('Susan', 'Ruby')

# return
num = input('\nEnter An Integer:')
def square(num):
    if not type(num) is int: # isdigit not work
        return 'Invalid Entry!'
    num = int(num)
    return num * num

print num, 'Squared is:', square(num)

# lambda
def fun_1(x): return x**2
def fun_2(x): return x**3
def fun_3(x): return x**4

callbacks = [fun_1, fun_2, fun_3]
print '\nNamed functions:'
for function in callbacks : print 'Result:', function(3)

callbacks = \
    [lambda x : x**2, lambda x : x**3, lambda x : x**4] # continue code in new line
print '\nAnonymous functions:'
for function in callbacks : print 'Result:', function(3)

# skip (pas)
title = '\nPython in easy steps\n'
for char in title: print char

for char in title:
    if char == 'y':
        print '*'
        continue
    print char # replace y on *

for char in title:
    if char == 'y':
        print '*'
        pass
    print char # put * before y

# yield
def fibonacci_generator():
    a = b = 1
    while True:
        yield a
        a, b = b, a+b

fib = fibonacci_generator()
for i in fib:
    if i > 100: break
    else: print 'Generated:', i

# exceptions (raise)
day = 32
try:
    if day > 31:
        raise ValueError('Invalid day number')
except ValueError as msg:
    print '\nThe Program Found An', msg
finally:
    print 'But Today is Beautiful Day Anyway!'

# assert
chars = ['Alpha', 'Beta', 'Gama', 'Delta', 'Epsilon']
def display(elem):
    assert type(elem) is int, 'Argument must be Integer!'
    print 'List element', elem, '=', chars[elem]

elem = 4
display(elem)

elem = elem / 1.5 # when elem is not int will work assert
display(elem)