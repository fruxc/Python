def Add(a, b):
   r = a + b
   return r
 
def Sub(a, b):
   r = a - b
   return r
 
def Mul(a, b):
   r = a * b
   return r
 
def Div(a, b):
   if (a != 0 and b != 0):
  	r = a // b
  	return r
   else:
  	return ("Divion is not possible , its not defined ")
 
def Mod(a, b):
   r = a % b
   return r
