a = int(input('Enter First Number : '))
b = int(input('Enter Second Number : '))

print ("\n{0:b}".format(a))
print ("\n{0:b}".format(b))


c = a & b

print ("\nAND Operator {0:b}".format(c))

c = a | b

print ("\nOR Operator {0:b}".format(c))

c = a ^ b

print ("\nEXOR Operator {0:b}".format(c))

c = ~ a

print ("\nOnes Complement of a {0:b}".format(c))

c = ~ b
print ("\nOnes Complement of b {0:b}".format(c))

c = a << 3

print ("\nLeft operand value of a is shifted by 3 {0:b}".format(c))

c = a >> 3

print ("\nRight operand value of a is shifted by 3 {0:b}".format(c))

c = b << 3

print ("\nLeft operand value of a is shifted by 3 {0:b}".format(c))

c = b >> 3

print ("\nRight operand value of b is shifted by 3 {0:b}".format(c))