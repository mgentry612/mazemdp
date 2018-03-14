# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:11:27 2018
@author: yhao
"""
#Adampted from; https://www.youtube.com/watch?v=-0q_miviUDs&list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP&index=2

import turtle
import maze

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)
wn.exitonclick()

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0) #Animation speed

def policy_iteration_animate(grid, gamma):
    is_policy_changed = True
    
    setup_maze(grid)
    
    actions = ['up', 'down', 'left', 'right']
    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]

    
    # Policy iteration
    while is_policy_changed:
        is_policy_changed = False
        #print(policy)
        # Policy evaluation
        # Transition probabilities not shown due to deterministic setting
        is_value_changed = True
        while is_value_changed:
            is_value_changed = False
            # Run value iteration for each state
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '#':
                        policy[i][j] = '#'
                    else:
                        neighbor = getattr(grid[i][j], policy[i][j])
                        v = grid[i][j].reward + gamma * grid[neighbor[0]][neighbor[1]].value
                        # Compare to previous iteration
                        if v != grid[i][j].value:
                            is_value_changed = True
                            grid[i][j].value = v
                                
        # Once values have converged for the policy, update policy with greedy actions
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '#':
                    # Dictionary comprehension to get value associated with each action
                    action_values = {a: grid[getattr(grid[i][j], a)[0]][getattr(grid[i][j], a)[1]].value for a in actions}
                    best_action = max(action_values, key=action_values.get)
                    # Compare to previous policy
                    if best_action != policy[i][j]:
                        is_policy_changed = True
                        policy[i][j] = best_action
                        
        animate_policy(policy)
        
    turtle.done()
    return(policy)
        

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x, y coordinate
            #Note the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #Check if it is an X (representing a wall)
            if character == "#":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                
    pen.color('red')
    pen.goto(-264, 264)
    pen.stamp()
                
    #turtle.done()

    
def animate_policy(policy):
    
    pen.shape('arrow')
    wn.tracer(0,0)
    
    for y in range(len(policy)):
        for x in range(len(policy[y])):
            
            character = policy[y][x]
            
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            
            if character != '#':
                pen.goto(screen_x, screen_y)
                pen.color('black')
                pen.shape('square')
                pen.stamp()
                pen.color('white')
                pen.shape('arrow')
                
                
            if character == 'up':
                pen.setheading(90)
                pen.stamp()
                
            if character == 'down':
                pen.setheading(270)
                pen.stamp()
                
            if character == 'left':
                pen.setheading(180)
                pen.stamp()
                
            if character == 'right':
                pen.setheading(0)
                pen.stamp()
                
    pen.color('red')
    pen.shape('square')
    pen.goto(-264, 264)
    pen.stamp()
                
    wn.update()

                
#Create class instances
pen = Pen()

#Set up the maze
if __name__ == '__main__':
    test_maze = maze.Maze(w=10, h=10)
    test_grid = maze.maze_to_mdp(test_maze)
    #test_policy = policyiteration.policy_iteration(test_grid, .9)
    policy_iteration_animate(test_grid, .9)
    #setup_maze(test_grid)


         
        
        
        
        
        
        
        
        
        
        
        
        
        