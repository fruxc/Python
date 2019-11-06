file = open("Books.txt","w+")

l = ["This file is for books. \n","Books are good source of knowlegde.\n"]

file.write("Writing something in file.\n")

file.writelines(l)

file.close()

file = open("Books.txt","r+")

print(file.read())

file.seek(0)

print(file.readline())

file.seek(0)

print(file.read(9))

file.seek(0)

print(file.readline(9))

file.seek(0)

print(file.readlines())

print(file.readable())

print(file.writable())

file.close()
