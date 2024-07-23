class Figure:
    sides_count = 0

    def __init__(self, color):
        self.__sides = [1] * self.sides_count
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)
        self.__radius = circumference / (2 * 3.14159)

    def get_square(self):
        return 3.14159 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.__height = self.__calculate_height(side1, side2, side3)

    def __calculate_height(self, side1, side2, side3):
        # Calculate the height of the triangle using Heron's formula
        semi_perimeter = (side1 + side2 + side3) / 2
        return (2 / side1) * (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5

    def get_square(self):
        return 0.5 * self.__height * self.__get_base()

    def __get_base(self):
        # Assuming the triangle is isosceles, the base is the longest side
        return max(self.get_sides())


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color)
        self.__sides = [side_length] * self.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())