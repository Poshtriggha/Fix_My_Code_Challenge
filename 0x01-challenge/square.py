#!/usr/bin/python3

class Square:
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return self.width * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=12)  # Making sure width and height are equal for a square
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())

