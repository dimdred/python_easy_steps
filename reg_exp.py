from re import *

pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9_.])+[a-z]{2,6}(\s|$)')

def get_address():
    addr = raw_input('Enter Email Address:' )
    is_valid = pattern.match(addr)
    if is_valid:
        print 'Valid Address:', is_valid.group()
    else:
        print 'Invalid Address! Please retry...\n'

get_address()