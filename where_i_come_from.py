#this is a simple way of drawning moroccan flag
#visit https://docs.python.org/3/library/turtle.html#turtle.exitonclick to know more about turtle library
import turtle
def draw_flag(taille, couleur):
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color(couleur)
    brad.speed(3)
    brad.width(15)
    brad.goto(-165,0)

    count_er = 0
    while count_er < 5:
        brad.forward(300)
        brad.right(144)
        count_er += 1
    brad.hideturtle()

my_window = turtle.Screen()
my_window.bgcolor("red")
my_window.title("Morocco Maroc Marokko ⵍⵎⵖⵔⵉⴱ المغرب") #Morocco in differnt languges including Amazigh and arabic
draw_flag(2, "green")
my_window.exitonclick()
