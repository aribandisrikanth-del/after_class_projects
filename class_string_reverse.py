class reverse():
    def __init__(self,word):
        self.word=word
    def reverse1(self):
        self.word1=""
        for i in self.word[::-1]:
            self.word1+=i
        return self.word1
obj=reverse(input("pick a word to reverse using a class "))
print(obj.reverse1())