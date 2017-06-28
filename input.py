from __future__ import print_function # function print() for Python 3.x

user = raw_input('What is your name?: ') # input() - in Python 3.x
print ('Welcome', user)

lang = raw_input('Favorite language?: ')
print (lang, 'Is', 'Fun', sep = '*', end = '!\n')