class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return(f'Rectangle(width={self.width}, height={self.height})')

    def set_width(self, newWidth):
        self.width = newWidth

    def set_height(self, newHeight):
        self.height = newHeight

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = []
        for i in range(self.height):
            for j in range(self.width):
                pic.append('*')
            pic.append('\n')
        return ''.join(pic)

    def get_amount_inside(self, shape):
        return (self.width//shape.width) * (self.height//shape.height)

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_width(self, newWidth):
        self.width = newWidth
        self.height = newWidth

    def set_height(self, newHeight):
        self.height = newHeight
        self.width = newHeight

    def set_side(self, newSide):
        self.height = newSide
        self.width = newSide

    def __str__(self):
        return(f'Square(side={self.width})')



