flag = 0
high = 100
low = 0

print("All Prime Numbers Between {0} to {1}".format(low,high))

for n in range(low, high+1):
        if n > 1:
                flag = 0
                for i in range(2,(n//2+1)):
                        if(n%i) == 0:
                               	flag = flag + 1
                                break
                if flag == 0:
                        print("%d"%n)
