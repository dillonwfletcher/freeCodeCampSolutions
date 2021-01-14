class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        shape = ""
        for i in range(self.height):
            shape += "*" * self.width + "\n"
        return shape

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side={})".format(self.width)
    
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    
