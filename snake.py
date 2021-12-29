from turtle import Turtle

STARTING_POSITION = [(0, 0),  (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # constructor
    def __init__(self):
        self.snakes_obj_list = []
        self.create_snake()
        self.head = self.snakes_obj_list[0]

    def create_snake(self):
        for positon in STARTING_POSITION:
            self.add_snake_obj_tolist(positon)

    #adds snake body segment in the list  as eat food
    def add_snake_obj_tolist(self, position):
            new_body = Turtle("square")  # create new objects each time
            new_body.color("white")
            new_body.penup()
            new_body.goto(position) #get position of this new body
            self.snakes_obj_list.append(new_body) #add to the list, list size grows as snake body

    def reset(self):
        for seg in self.snakes_obj_list:
            seg.goto(1000, 1000)
        self.snakes_obj_list.clear()
        self.create_snake()
        self.head = self.snakes_obj_list[0]
    #extends snake body by adding to the last index > add_snake_obj_tolist(self, -1)
    def extend(self):
        self.add_snake_obj_tolist(self.snakes_obj_list[-1].position()) #get position of that added tail body

    def move(self):
        # to make tails move first and then move/turn head to make sure the snake body moves together
        for seg in range(len(self.snakes_obj_list)-1, 0, -1):
            new_x = self.snakes_obj_list[seg-1].xcor()
            new_y = self.snakes_obj_list[seg-1].ycor()
            self.snakes_obj_list[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        #can't go back to opposite direction up > down, down > up or l > r, r > l
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


