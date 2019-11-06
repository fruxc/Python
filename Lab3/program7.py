A = {0, 2, 4, 6, 8}; 
B = {1, 2, 3, 4, 5};
print(A)
print(B)
A.add(11)
print ("Updated set:",A)
B.remove(5)
print ("Updated set:",B) 
print("Union :", A | B) 
print("Intersection :", A & B) 
print("Difference :", B - A)  
print("Symmetric difference :", A ^ B)
