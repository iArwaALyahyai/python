# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:06:45 2020

@author: Arwa
@section: 20
@id: 129130

Program Design:
1- Purpose:
    Write a program that represent analog clock with different bachground and the time allowing the user to input time in hours
    and minutes.
2- Input and output:
    Inputs:
    - time is hours and minutes
    - background design
    Outputs:
    - analog clock with the time and appropriate background
3- Algorithm:
    - Create turtle instance
    - Set the speed of turtle to 0
    - Prompt user to choose the background style
    - Read background style from user
    - checking input:
        if background is s or c or n or x
        
            if background = x
                exit
                
            Read hours from user
            Read minutes from user
            
            while hour or minutes are not digit
                Read hours from user
                Read minutes from user
                
            if hours and minutes is digit
                convert hours and minutes to integer
                while hours greater than 12 or minuted not multiple of 5
                Read hours from user
                Read minutes from user
                convert hours and minutes to integer
                
            Draw the outer square:
            setup turtle windows by 600pix in wedth and length
            set pensize to 3
            set pen up
            goto(-290,290)
            set pen down
            loop for 4 times
                set turtle color to blue
                move turtle forward by 580 pix
                turn right by 90 angle
            set pen up  
            goto(0,0)
            set pen down
        
            if background = s
                set list of of colors, pen size and angles
                choose colors, pen size and angles randomly
        
                draw nested squares:
                loop for 15 squares
                    start filling
                    if iterate number is even
                        set turtle color to color1
                        set filling color to color1      
                    else
                        set turtle color to color2
                        set filling color to color2
                
                    loop for each sequare 4 times
                        move turtle forward by (50+10*itrate number) pix
                        turn left by 90 angle
                
                    stop filling 
                    set pen up
                    turn right by angle
                    set pen down
            
                set pen up  
                goto(0,0)
                set pen size to size1
                Set turtle direction to 90
        
                draw clock
                set pen size to 4
                loop for i from 1 to 13
                    turnright by 30 angle
                    set pen up
                    set turtle color to black 
                    goto(0,0)
                    set pen down
                    move forward by 200 pix
                    set pen up
                    move forward by 30 pix
                    write numbers with format
                        
                Draw the hour hand
                set pensize to 7    
                set pen up
                goto(0,0)
                set turtle color to red
                Set turtle direction to 90
                compute angle of hours by this formula (hour/12)*360
                turn right by angle of hours
                set pen down
                move forward by 100 pix
                set pen size to 2
                set shape to arrow 
                put arrow stamp
                    
                Draw the minutes hand
                set pen up
                goto(0,0)
                set turtle color to blue
                Set turtle direction to 90
                compute angle of minutes by this formula (minutes/60)*360
                turn right by angle of minutes
                set pen down
                move forward by 180 pix
                set pen size to 2
                set shape to arrow 
                put arrow stamp
        
                stop turtle

            elif background = n
                set pen size to 4
                Draw clock
                loop for i from 1 to 13
                    turnright by 30 angle
                    set pen up
                    set turtle color to black 
                    goto(0,0)
                    set pen down
                    move forward by 200 pix
                    set pen up
                    move forward by 30 pix
                    write numbers with format
                        
                Draw the hour hand
                set pensize to 7    
                set pen up
                goto(0,0)
                set turtle color to red
                Set turtle direction to 90
                compute angle of hours by this formula (hour/12)*360
                turn right by angle of hours
                set pen down
                move forward by 100 pix
                set pen size to 2
                set shape to arrow 
                put arrow stamp
                    
                Draw the minutes hand
                set pen up
                goto(0,0)
                set turtle color to blue
                Set turtle direction to 90
                compute angle of minutes by this formula (minutes/60)*360
                turn right by angle of minutes
                set pen down
                move forward by 180 pix
                set pen size to 2
                set shape to arrow 
                put arrow stamp
        
                stop turtle
        
            elif background = c
                set list of of colors, pen size and angles
                choose colors, pen size and angles randomly
         
                loop for this angles[30,120,210,300]
                    Set turtle direction to that angle
                    loop 8 times
                        draw circle with diameter (10*itrate number)+8 
                        set pen up
                        move forward by (itrate number+20)
                        set pen down
                        if itrate number is even 
                            set turtle color to color1
                            set pen size to size1
                        else
                            set turtle color to color2
                            set pen size to size2
                            
                    set pen up
                    goto(0,0)
                    Set turtle direction to 0
                    set pen down
            
                Draw clock
                set pen size to 4
                loop for i from 1 to 13
                turnright by 30 angle
                set pen up
                set turtle color to black 
                goto(0,0)
                set pen down
                move forward by 200 pix
                set pen up
                move forward by 30 pix
                write numbers with format
                        
                Draw the hour hand
                set pensize to 7    
                set pen up
                goto(0,0)
                set turtle color to red
                Set turtle direction to 90
                compute angle of hours by this formula (hour/12)*360
                turn right by angle of hours
                set pen down
                move forward by 100 pix
                set pen size to 2
                set shape to arrow 
                put arrow stamp
                    
                Draw the minutes hand
                set pen up
                goto(0,0)
                set turtle color to blue
                Set turtle direction to 90
                compute angle of minutes by this formula (minutes/60)*360
                turn right by angle of minutes
                set pen down
                move forward by 180 pix
                set pen size to 2
                set shape to arrow 
                put arrow stamp
        
                stop turtle
                
        else:
            invalid background design
            
            
            
4. Test Case:
====================================================================================================================================================
backgroundDesign    hour    minutes    Expected                               result                                 Comment
===============================================================================================================================================
x                    none    none       exit                                   exit                                  correct
                                            
c                     3       30        clock with nested circles               clock with nested circles            correct
                                        background, hour hand direct to 3,     background, hour hand direct to 3, 
                                        minuted hand direct to 30              minuted hand direct to 30
                                        
s                     1        55       clock with nested squares              clock with nested squares              correct
                                        background, hour hand direct to 1,     background, hour hand direct to 1, 
                                        minuted hand direct to 55              minuted hand direct to 55    

n                     4         10      clock without background ,             clock without background,              correct
                                        hour hand direct to 4,                 hour hand direct to 4, 
                                        minuted hand direct to 10              minuted hand direct to 10
                                        
w                   none      none      Wrong input: try again                 Wrong input: try again                  correct   

c                    ee        17       read hours and minutes again           read hours and minutes again            correct

n                    16        -6       read hours and minutes again           read hours and minutes again            correct

                                                                                
                                                                                                             
                                                                                             
















            
"""
#Import libraries
from sys import exit
from random import random,randint
import turtle

#Create turtle instance
t = turtle.Turtle()

#speed of turtle
t.speed(0)

#Prompt user to choose the background style
print("Choosing baclground design")
print("Enter c or C for background design with pattern of NESTED CIRCLES design")
print("Enter s or S for background design with pattern of NESTED SQUARES design")
print("Enter n or N for clock without background ")
print("Enter x or X to exit ")

#Read background style 
backgroundDesign  = input("Enter type of background shapes: ")
backgroundDesign= backgroundDesign.lower()

#Checking input

if backgroundDesign== "c" or backgroundDesign== "s" or backgroundDesign== "n"\
    or backgroundDesign== "x":
    
    #Exit from the program
    if  backgroundDesign== "x":
            exit("Exit")
        
    #Read the time
    print("Input time")
    hour = input("Hour: ")
    minutes = input("Minutes multiput of 5: ")
    
    #checking if the inputs are not digits
    while not hour.isdigit() or not minutes.isdigit():
        print("Input time")
        hour = input("Hour: ")
        minutes = input("Minutes multiput of 5: ")
        
    #checking if the inputs are digits
    if hour.isdigit() and minutes.isdigit():
        hour = int(hour)
        minutes = int(minutes)
        #read time again if the first input was wrong
        while hour > 12 or minutes % 5 != 0:
            print("Input time")
            hour = input("Hour: ")
            minutes = input("Minutes multiput of 5: ")
            
            #convert hours and minutes to integer
            hour = int(hour)
            minutes = int(minutes)

        
            

    #Draw outer square 
    if hour <= 12 and minutes % 5 == 0:
        turtle.setup(600,600)
        t.pensize(3)
        t.penup()
        t.goto(-290,290)
        t.pendown()
        for i in range (4):
            t.pencolor("blue")
            t.forward(580)
            t.right(90) 
        t.penup()  
        t.goto(0,0)
        t.pendown()
            
        #Squares background
        
        if backgroundDesign == "s":
        
            #setting list of colors, pen size and angles
            colors1 = ["rosybrown","darkred","lightsteelblue","slategrey","darkseagreen","gold"]
            colors2 = ["lightcyan","tan","pink","lavender","thistle","limegreen"]
            angles = list(range(25,35))
            
            #choose random colors, pensize,angles and side length
            #color
            color1 = colors1[randint(0,5)]
            color2 = colors2[randint(0,5)]
            #pen size
            size1 = randint(1,4)
            #angle
            angle = angles[randint(0,4)]
            #side length:
            sideLength = randint(50,60)
            
            
            #draw nested sequares
            for i in range (15):
                t.begin_fill()
                if i % 2 == 0:
                    t.color(color1)
                    t.fillcolor(color1)       
                else:
                    t.color(color2)
                    t.fillcolor(color2)
                    
                for j in range(4):
                    t.forward(sideLength+10*i)
                    t.left(90)
                    
                t.end_fill()
                t.penup()
                t.right(angle)
                t.pendown()
                
            t.penup()  
            t.goto(0,0)
            t.pensize(size1)
            t.setheading(90)
            
            #Draw clock
            t.pensize(4)
            for i in range(1,13):
                t.right(30)
                t.penup()
                t.color("black")
                t.goto(0,0)
                t.pendown()
                t.forward(200)
                t.penup()
                t.forward(30)
                t.write(i, align="center", font=("Arial", 8, "normal"))
                
            #Draw the hour hand
            t.pensize(7)    
            t.penup()
            t.goto(0,0)
            t.color("red")
            t.setheading(90)
            angleHour = (hour/12)*360
            t.right(angleHour)
            t.pendown()
            t.forward(100)
            t.turtlesize(2)
            t.shape("arrow")
            t.stamp()
            
            
            #Draw the minutes hand
            t.penup()
            t.goto(0,0)
            t.color("blue")
            t.setheading(90)
            angleMinutes = (minutes/60)*360
            t.right(angleMinutes)
            t.pendown()
            t.forward(180)
            t.turtlesize(2)
            t.shape("arrow")
            t.stamp()
            
            turtle.done()
                
        #without background
            
        elif backgroundDesign == "n":
            
            #draw clock
            t.seth(90)
            t.pensize(4)
            for i in range(1,13):
                t.right(30)
                t.penup()
                t.color("black")
                t.goto(0,0)
                t.pendown()
                t.forward(200)
                t.penup()
                t.forward(30)
                t.write(i, align="center", font=("Arial", 8, "normal"))
                
            #Draw the hour hand:
            t.pensize(7)    
            t.penup()
            t.goto(0,0)
            t.color("red")
            t.setheading(90)
            angleHour = (hour/12)*360
            t.right(angleHour)
            t.pendown()
            t.forward(100)
            t.turtlesize(2)
            t.shape("arrow")
            t.stamp()
            
            #Draw the minutes hand:
            t.penup()
            t.goto(0,0)
            t.color("blue")
            t.setheading(90)
            angleMinutes = (minutes/60)*360
            t.right(angleMinutes)
            t.pendown()
            t.forward(180)
            t.turtlesize(2)
            t.shape("arrow")
            t.stamp()
            turtle.done()
                
        #Circles background
            
        elif backgroundDesign == "c":
            
            #setting list of colors, pen size and angles
            colors1 = ["rosybrown","darkred","lightsteelblue","slategrey","darkseagreen","gold"]
            colors2 = ["purple","tan","pink","ovlive","thistle","limegreen"]
            angles = list(range(45,95))
            
            #choose random colors, pensize and angles
            #color
            color1 = colors1[randint(0,5)]
            color2 = colors2[randint(0,5)]
            #pen size
            size1 = randint(1,4)
            size2 = randint(1,4)
            #angle
            angle = angles[randint(0,49)]
            
            #Draw nested circles
            for i in[30,120,210,300]:
                t.seth(i)
                for j in range(8):
                    t.circle((10*j)+8)
                    t.penup()
                    t.forward(j+20)
                    t.pendown()
                    if j%2 == 0 :
                        t.color(color1)
                        t.pensize(size1)
                    else:
                        t.color(color2)
                        t.pensize(size2)
                t.penup()
                t.goto(0,0)
                t.seth(0)
                t.pendown()
                
            #Draw clock
            t.pensize(4)    
            t.seth(90)
            for i in range(1,13):
                t.right(30)
                t.penup()
                t.color("black")
                t.goto(0,0)
                t.pendown()
                t.forward(200)
                t.penup()
                t.forward(30)
                t.write(i, align="center", font=("Arial", 8, "normal"))
                
            #Draw the hour hand:
            t.pensize(7)    
            t.penup()
            t.goto(0,0)
            t.color("red")
            t.setheading(90)
            angle = (hour/12)*360
            t.right(angle)
            t.pendown()
            t.forward(100)
            t.turtlesize(2)
            t.shape("arrow")
            t.stamp()
            
            #Draw the minutes hand:
            t.penup()
            t.goto(0,0)
            t.color("blue")
            t.setheading(90)
            angle = (minutes/60)*360
            t.right(angle)
            t.pendown()
            t.forward(180)
            t.turtlesize(2)
            t.shape("arrow")
            t.stamp()
            turtle.done() 
                          
else:
    exit("Wrong input: try again")
    