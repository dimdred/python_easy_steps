# Tuple - unchanged list t=(1,2,1,3). Could use specific element t[1]
# Set - unchanged list with unique items s = {1,2,3}. Could not apply to specific element. Use methods for it.

# lists
a, b, c = 1, 2, 3
nums = [0, 1 , 2, 3, 4, 5]
print nums
quarter = ['Jan', 'Feb', 'Mar']
print 'First month:\t', quarter[0]
print 'Second month:\t', quarter[1]
print 'Third month:\t', quarter[2]
coords = [[1,2,3],[4,5,6]]
print '\nTop left 0,0 :\t', coords[0][0]
print '\nBottom right 1,2 :\t', coords[1][2]
print '\nSecond month first letter:\t', quarter[1][0]
print '\nSecond month last letter:\t', quarter[1][-1] #last symbol (from right)

# pop
basket = ['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']
print '\nBasket List: ', basket
print 'Basket Elements: ', len(basket)
basket.append('Damson') #add element to the end
print 'Appended: ', basket
print 'Last Item removed: ', basket.pop()
print 'Basket List: ', basket
basket.extend(crate) # add second list
print 'Extended: ', basket
basket.reverse()
print 'Reversed: ', basket
del basket[1]
print 'Item removed: ', basket
del basket[1:3]
print 'Slice removed: ', basket

# tuple, set
zoo = ('Kangaroo', 'Leopard', 'Mouse')
print '\nTuple: ', zoo, '\tLength:', len(zoo)
print type(zoo)

bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print '\nSet:', bag, '\tLength:', len(bag)
print type(bag)
print '\nIs Green in Bag', 'Green' in bag# search in set
print 'Is Orange in Bag', 'Orange' in bag
box = {'Red', 'Purple', 'Yellow'}
print '\nSet:', box, '\tLength:', len(box)
print 'Common to both sets:', bag.intersection(box)

# dict
dict = {'name':'Bob', 'ref':'Python', 'sys':'Win'}
print '\nDictionary: ', dict
print 'Reference:', dict['ref']
print 'Keys:', dict.keys()
del dict['name']
dict['user'] = 'Tom'
print 'Dictionary: ', dict
print 'Is there a name key?: ', 'name' in dict

# if
num = int(input('Please Enter a Number:'))
if num > 5:
    print 'Number Exceeds 5'
elif num <5:
    print 'Number is Less than 5'
else:
    print 'Number is 5'
if num > 7 and num < 9:
    print 'Number is 8'
if num == 1 or num == 3:
    print 'Number is 1 or 3'

# while
i = 1
while i < 4:
    print '\nOuter Loop Iteration:', i
    i += 1
    j = 1
    while j < 4:
        print '\tInner Loop Iteration:', j
        j += 1

# for
chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
dict = {'name':'Mike', 'ref':'Python', 'sys':'Win'}
print '\nElements:'
for item in chars:
    print item

print '\nEnumerated:'
for item in enumerate(chars):
    print item

print '\nZipped:'
for item in zip(chars, fruit):
    print item

print '\nPaired:'
for key, value in dict.items():
    print key, '=', value

# nest
for i in range(1,4):
    for j in range(1,4):
        if i == 1 and j == 1:
            print 'Continue inner loop at i=1 and j=1'
            continue
        if i == 2 and j == 1:
            print 'Break inner loop at i=2 and j=1'
            break
        print 'Running i =', i, 'j =', j