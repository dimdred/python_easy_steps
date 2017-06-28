a = 8
b = 2
print 'Addition:\t', a, '+', b, '=', a+b
print 'Subtraction:\t', a, '-', b, '=', a-b
print 'Multiplication:\t', a, '*', b, '=', a*b
print 'Division:\t', a, '/', b, '=', a/b
print 'Floor Division:\t', a, '/', b, '=', a//b
print 'Modulus:\t', a, '%', b, '=', a%b
print 'Exponent:\t', a, '**', b, '=', a**b

# assign
a += b
print 'Add & Assign:\t', 'a =', a
a -= b
print 'Subtract & Assign:\t', 'a =', a
a *= b
print 'Multiply & Assign:\t', 'a =', a
a /= b
print 'Divide & Assign:\t', 'a =', a
a %= b
print 'Modulus & Assign:\t', 'a =', a

# comparison
nil = 0
num = 0
max = 1
cap = 'A'
low = 'a'
print 'Equality: \t', nil, '==', num, nil == num
print 'Equality: \t', cap, '==', low, cap == low
print 'Inequality: \t', nil, '!=', max, nil != max
print 'Greater: \t', nil, '>', max, nil > max
print 'Lesser: \t', nil, '<', max, nil < max
print 'More or Equal: \t', nil, '>=', num, nil >= num
print 'Less or Equal: \t', max, '<=', num, max <= num

# logical
a = True
b = False
print 'AND Logic: \t', 'a AND a =', a and a, ' a AND b =', a and b, ' b AND b =', b and b
print 'OR Logic: \t', 'a AND a =', a or a, ' a AND b =', a or b, ' b AND b =', b or b
print 'NOT Logic: \t', 'a =', a, ' not a =', not a, ' b =', b, ' not b =', not b

# condition
a = 1
b = 2
print 'Variable a Is: ', 'One' if (a == 1) else 'Not One'
print 'Variable a Is: ', 'Even' if (a % 2 == 0) else 'Odd'
print 'Variable b Is: ', 'One' if (b == 1) else 'Not One'
print 'Variable b Is: ', 'Even' if (b % 2 == 0) else 'Odd'
max = a if (a > b) else b
print 'Greater value: ', max
