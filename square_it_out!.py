import math
L=[int(input("pick the lower end to take square numbers from ")),int(input("pick the higher end to take square numbers from "))]
print("the perfect squares are ")
for i in range(L[0],L[-1]+1):
    if math.isqrt(i)==math.sqrt(i):
        if i%2==0:
            print(i,"is even")
        else:
            print(i,"is odd")