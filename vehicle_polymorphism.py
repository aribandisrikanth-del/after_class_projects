class BMW():
    def speed(self):
        print("The BMW can go 195 miles an hour")
    def millage(self):
        print("The BMW's millage is 1,000,000 miles")
class Ferrari():
    def speed(self):
        print("The Ferrari can go 249 miles an hour")
    def millage(self):
        print("The Ferrari's millage is 260,000 miles")

obj_BMW=BMW()
obj_Ferrari=Ferrari()

for info in (obj_BMW,obj_Ferrari):
    info.speed()
    info.millage()