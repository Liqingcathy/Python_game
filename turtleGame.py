from turtle import Turtle, Screen
import tkinter
import random 

tim = Turtle();
screen = Screen()
"""
def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(50)

def turn_right():
    new_heading =  tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
#listen to event of pressing space then trigger the move_forward function
#screen.onkey(key="space", fun=move_forwards)
screen.onkey(move_forwards, "w")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.exitonclick()
""" 

continue_race = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which color turtule will win the race? Enter color: ")
y_position = [-70, -40, -10, 20, 50,80]
colors = ["green", "red", "orange", "blue", "purple", 'brown']
all_turtle = []

for t_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    new_turtle.goto(x=-200, y=y_position[t_index])
    all_turtle.append(new_turtle)

if user_bet:
    continue_race = True

while continue_race:
    for turtle in all_turtle:
        if turtle.xcor() > 180:
            continue_race = False
            if turtle.pencolor() == user_bet:
                print(f"You won the guess! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You lost! The {turtle.pencolor()} turtle is the winner!")  
        
        random_distance =  random.randint(0,10)
        turtle.forward(random_distance)
        
screen.exitonclick()