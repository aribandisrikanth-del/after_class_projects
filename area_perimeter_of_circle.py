class circle:
    def __init__(self):
        self.radius=()
    def get_radius(self):
        self.radius=int(input("pick a radius to find the perimineter and area of the circle "))
    def perimeter(self):
        x=2*(self.radius*3.1415926539)
        print("the perimeter of the circle is",x)
    def area(self):
        y=3.1415926539*(self.radius**2)
        print("the area of the circle is",y)
small=circle()
small.get_radius()
small.perimeter()
small.area()