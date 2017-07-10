import math, random

print 'Rounded Up 9.5:', math.ceil(9.5)
print 'Rounded Down 9.5:', math.floor(9.5)

num = 4
print num, 'squared:', math.pow(num, 2)
print num, 'squared root:', math.sqrt(num)

# 6 random numbers from list
nums = random.sample(range(1, 49), 6)
print 'Lucky numbers are:', nums

# inaccurate
item = 0.70
rate = 1.05
tax = item * rate
total = item + rate
print 'Item: \t', '%.2f' %item
print 'Tax: \t', '%.2f' %tax
print 'Total: \t', '%.2f' %total
print '\nItem: \t', '%.20f' %item
print 'Tax: \t', '%.20f' %tax
print 'Total: \t', '%.20f' %total

#  list of Python modules installed in computer
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print installed_packages_list

# decimal use when accuracy is very important
from decimal import *
item = Decimal(0.7)
rate = Decimal(1.05)
print '\nItem: \t', '%.20f' %item
print 'Tax: \t', '%.20f' %tax
print 'Total: \t', '%.20f' %total