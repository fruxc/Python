
p = float(input('Enter Principle Amount : '))
t = int(input('Enter Time in years : '))
r = float(input('Enter Rate of Interest : '))

si=(p*t*r)/100

print("\nThe simple interest is:",si)

a = p*(1+(r/100))**t

ci = a-p

print("\nThe annual compound interest is:",ci)

