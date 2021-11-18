# A program to calculate attributes for functions and shapes
# Abigail Knapp 2021

class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.area = self.height * self.length

    def tell_attributes(self):
        print("\n",
              "For this rectangle--"
              "\nThe height is:", self.height,
              "\nThe length is:", self.length,
              "\nThe area is:", self.area,
              "\n")

    @classmethod
    def create_default(cls):
        return Rectangle(100, 100)


class Square(Rectangle):
    pass


class Parabola:
    def __init__(self, a, b, c):
        # A parabola is written in the form f(x) = ax^2 + bx + c
        self.a = a
        self.b = b
        self.c = c

    def eval_parabola(x):
        pass

    # A python function to calculate the vertex of a parabola using quadratics
    def find_vertex_quad(self):
        # the parabola vertex is defined as (h, k)
        h = -(self.b / (2 * self.a))
        k = (self.a * (h ** 2)) + (self.b * h) + self.c
        vertex = f"{h}, {k}"
        print("\n",
              "For this parabola--",
              "\nThe vertex of the parabola is: (", vertex, ")",
              "\n")

    # A python function to calculate the vertex of a parabola using my own method
    def find_vertex_mine(self):
        pass

    # A python function to calculate the vertex of a parabola using calculus
    def find_vertex_calc(self):
        pass


# Return values for a specific Rectangle
r_example = Rectangle(2, 3)
Rectangle.tell_attributes(r_example)

# Return values for a specific parabola
p_example = Parabola(2, -6, 7)
Parabola.find_vertex_quad(p_example)
