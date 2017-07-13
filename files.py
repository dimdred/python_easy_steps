def display(s):
    '''Print value of argument'''
    print s

display(display.__doc__) # __doc__ - info about function
display(r'C:\Program Files') # r - for \ symbol
display('\nHello'+'Python!')
display('Python in Easy Step\n' [7:])
display('p' in 'Python')
display('P' in 'Python')

import dog
for i in dir(dog):
    print i


snack = '{} and {}'.format('Burger', 'Fries')
print '\nReplaced:', snack
snack = '{1} and {0}'.format('Burger', 'Fries')
print '\nReplaced:', snack
snack = '%s and %s' % ('Milk', 'Cookies') # %s - string, %c - char, %d - number, %f - float
print '\nReplaced:', snack


# modify
string = 'python in easy step'
print '\nCapitalized:', string.capitalize()
print 'Titled:', string.title()
print 'Centered:', string.center(50,'*')
print 'Uppercase:', string.upper()
print 'Joined:', string.join('***')
print 'Justified:', string.rjust(30, '*')
print 'Replaced:', string.replace('s', '*')

# unicode
import unicodedata
s = 'test'
print '\nString:', s
print 'Type:', type(s), 'Length:', len(s)
s = s.encode('utf-8')
print 'Encoded string:', s
print 'Type:', type(s), 'Length:', len(s)
s = s.decode('utf-8')
print 'Decoded string:', s
print 'Type:', type(s), 'Length:', len(s)
print s
for i in range(len(s)):
    print s[i], unicodedata.name(s[i])

s = b'Gr\xc3\xb6n'
print '\nGreen string:', s.decode('utf-8')
s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print '\nGreen string:', s

# access
file = open('example.txt', 'w')
print '\nFile name:', file.name
print 'File open mode:', file.mode
# for Python 3 print 'Readable:', file.readable()
# for Python 3 print 'Writable:', file.writable()

def get_status(f):
    if(f.closed != False):
        return 'Closed'
    else:
        return 'Open'

print 'File status:', get_status(file)
file.close()
print 'File status:', get_status(file)

# write in file (w - re-write data into the file)
poem = 'I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

file = open('poem.txt', 'w')
file.write(poem)
file.close()

file = open('poem.txt', 'r')
for line in file:
    print line
file.close()

file = open('poem.txt', 'a') # add string
file.write('(Oscar Wilde)')
file.close()

