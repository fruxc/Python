import re

count = 3

while count>0:
        print("Number of attemps : ",count)
        pw = input("Enter password \n")
        flag = 0
        while True:

                if(len(pw)<6):
                        flag = 1
                        break
                if(len(pw)>16):
                        flag = 1
                        break
                elif not re.search("[a-z]", pw):
                        flag = 1
                        break
                elif not re.search("[A-Z]", pw):
                        flag = 1
                        break
                elif not re.search("[0-9]", pw):
                        flag = 1
                        break
                elif not re.search("[#$@]", pw):
                        flag = 1
                        break
                else :
                        flag = 0
                        count = 0
                        print("Valid password")
                        break

        if( flag == 1):
                print("Invalid password")
                print(flag)
                count-=1
	
