# A program to calculate attributes for functions and shapes
# Abigail Knapp 2021


class Parabola:
    def __init__(self, a, b, c):
        # A parabola is written in the form f(x) = ax^2 + bx + c
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def eval_parabola(x):
        pass

    # A python function to calculate the vertex of a parabola using quadratics
    def find_vertex_quad(self):
        # the parabola vertex is defined as (h, k)
        h = -(self.b / (2 * self.a))
        k = (self.a * (h ** 2)) + (self.b * h) + self.c
        vertex = f"{h}, {k}"
        print("\n",
              f"For this parabola {self.a}x^2 + {self.b}x + {self.c}",
              "\nUsing the formula h = -b/2a,",
              "\nThen evaluate f(h) to find k",
              "\nthe vertex (h, k) of the parabola is: (", vertex, ")",
              "\n")

    # A python function to calculate the vertex of a parabola using my own method
    def find_vertex_mine(self, x_int_1, x_int_2):
        x_width = abs(x_int_1) + abs(x_int_2)
        if x_int_1 > x_int_2:
            big_x_int = x_int_1
        else:
            big_x_int = x_int_2
        h = big_x_int - (x_width/2)
        k = (self.a * (h ** 2)) + (self.b * h) + self.c
        vertex = f"{h}, {k}"
        print("\n",
              f"For this parabola {self.a}x^2 + {self.b}x + {self.c}",
              "\nThe x intercepts of the parabola are: (", x_int_1, x_int_2, ")",
              "\nThe distance between x intercepts of the parabola is: (", x_width, ")",
              "\nThe largest x intercept of the parabola is: (", big_x_int, ")",
              "\nThen h is halfway between the x intercepts",
              "\nThen evaluate f(h) to find k",
              "\nThe vertex (h, k) of the parabola is: (", vertex, ")",
              "\n")

    # A python function to calculate the vertex of a parabola using calculus
    def find_vertex_calc(self):
        pass

    @classmethod
    def create_default(cls):
        return Parabola(1, 1, 0)



# Test values for a specific parabola
print("The parabola's form must be f(x) = ax^2 + bx + c")

def check_input(user_input):#Need to add this type checking to the entry below
    if type(user_input) == int:
        return TRUE
    else:
        print("Error: Not an integer. Please enter an integer.") #Return the user to the entry again

a = input("Enter an integer value for a: ")
b = input("Enter an integer value for b: ")
c = input("Enter an integer value for c: ")

p = Parabola(a=a, b=b, c=c)
Parabola.find_vertex_quad(p)
Parabola.find_vertex_mine(p, x_int_1=-2, x_int_2=6)