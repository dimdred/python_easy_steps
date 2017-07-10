# kitty
import cat

cat.purr()
cat.lick()
cat.nap()

cat.purr('Kitty')
cat.lick('Kitty')
cat.nap('Kitty')

pet = input('Enter a pet Name:')
cat.purr(pet)
cat.lick(pet)
cat.nap(pet)

# pooch
from dog import bark, lick, nap
# from dog import * # import all functions

bark()
lick()
nap()

bark('Pooch')
lick('Pooch')
nap('Pooch')

# system
import sys, keyword
print 'Python version:', sys.version
print 'Python Interpreter Location:', sys.executable
print 'My module search path:'
for dir in sys.path:
    print dir
print 'Python Keywords:'
for word in keyword.kwlist:
    print word