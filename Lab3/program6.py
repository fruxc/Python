print("Items of my books:")
MyBooks = {'Absalom, Absalom!': 1, 'Ah, Wilderness!': 2, 'An Acceptable Time': 3}
print(MyBooks)
print("sum of all values of my books:")
print(sum(MyBooks.values()))

print("Items of your books:")
YourBooks = {'Antic Hay': 2, 'Death Be Not Proud': 4, 'A Fanatic Heart': 5}
print(YourBooks)
print("sum of all values of your books:")
print(sum(YourBooks.values()))

print("merging of My Books and Your Books:")
MyBooks.update(YourBooks)
print (MyBooks)
