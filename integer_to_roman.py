import random

class integer():
    def __init__(self):
        self.fruits={"1":"|","2":"||","3":"|||","4":"||||",}
    def convert(self):
        num= input("pick a number to convert to roman numeral from 1 to 4 ")
        return self.fruits.get(num,"invalid input")

print("welcome to integer coverter")
fq=integer()
print(fq.convert())