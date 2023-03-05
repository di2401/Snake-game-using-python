from tkinter import *
from tkinter.font import Font
import tkinter as tk
import pygame
import time
import random
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (227, 13, 30)
green = (13, 227, 29)
blue = (50, 153, 213)
pink=(230, 30, 163)
p=(227, 123, 192)
 
dis_width = 600
dis_height = 400

def rules():
	r = Tk() #creates a window
	r.title('RULES:')
	r.geometry("800x400")
	r['bg']='#74edc9'
	Ta = tk.Text(r, height=2, width=60,font=bigf,bg='#5ceded')
	intro="  WELCOME TO SNAKE AND APPLE GAME  RULES!!"
	Ta.insert(tk.END, intro)
	Ta.pack()
	T2= tk.Text(r, height=10,width=70,font=("Hevetica",12))
	rule="-->The player starts out controlling a snake that is constantly moving around the screen.\n-->The player cannot stop or slow down it , but they can control which direction it turns.\n-->A red apple appears randomly on the screen, and the player must move the snake so that it eats the apple.\n-->Each time the snake eats an apple, the snake grows longer by one segment and a new apple randomly appears on the screen.\n--> The game is over if the snake crashes into itself or the edges of the screen."
	T2.insert(tk.END, rule)
	T2.pack()
	r.mainloop()
	
def snake_play_low():
         
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game ')
 
        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 10
 
        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("bahnschrift", 25)
 
 
        def Your_score(score):
            value = score_font.render("Your Score: " + str(score), True, black)
            dis.blit(value, [0, 0])
  
 
        def our_snake(snake_block, snake_list):
            for x in snake_list:
                 pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
 
        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
        def gameLoop():
            game_over = False
            game_close = False
 
            x1 = dis_width / 2
            y1 = dis_height / 2
 
            x1_change = 0
            y1_change = 0
 
            snake_List = []
            Length_of_snake = 1
 
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
            while not game_over:
 
                while game_close == True:
                    dis.fill(blue)
                    message("You Lost! Press C-Play Again or Q-Quit", red)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()
 
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()
 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
               
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                       
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0
 
                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(blue)
                pygame.draw.rect(dis, red , [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]
 
                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True
 
                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)
 
                pygame.display.update()
 
                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1
 
                clock.tick(snake_speed)
 
            pygame.quit()
            quit()

        gameLoop()


def snake_play_med():
         
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game ')
 
        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 15
 
        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("bahnschrift", 25)
 
 
        def Your_score(score):
            value = score_font.render("Your Score: " + str(score), True, black)
            dis.blit(value, [0, 0])
  
 
        def our_snake(snake_block, snake_list):
            for x in snake_list:
                 pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
 
        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
        def gameLoop():
            game_over = False
            game_close = False
 
            x1 = dis_width / 2
            y1 = dis_height / 2
 
            x1_change = 0
            y1_change = 0
 
            snake_List = []
            Length_of_snake = 1
 
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
            while not game_over:
 
                while game_close == True:
                    dis.fill(blue)
                    message("You Lost! Press C-Play Again or Q-Quit", red)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()
 
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()
 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
               
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                       
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0
 
                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(blue)
                pygame.draw.rect(dis, red , [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]
 
                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True
 
                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)
 
                pygame.display.update()
 
                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1
 
                clock.tick(snake_speed)
 
            pygame.quit()
            quit()

        gameLoop()

def snake_play_fast():
         
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game ')
 
        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 20
 
        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("bahnschrift", 25)
 
 
        def Your_score(score):
            value = score_font.render("Your Score: " + str(score), True, black)
            dis.blit(value, [0, 0])
  
 
        def our_snake(snake_block, snake_list):
            for x in snake_list:
                 pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
 
        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
        def gameLoop():
            game_over = False
            game_close = False
 
            x1 = dis_width / 2
            y1 = dis_height / 2
 
            x1_change = 0
            y1_change = 0
 
            snake_List = []
            Length_of_snake = 1
 
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
            while not game_over:
 
                while game_close == True:
                    dis.fill(blue)
                    message("You Lost! Press C-Play Again or Q-Quit", red)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()
 
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()
 
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
               
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                       
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0
 
                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(blue)
                pygame.draw.rect(dis, red , [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]
 
                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True
 
                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)
 
                pygame.display.update()
 
                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1
 
                clock.tick(snake_speed)
 
            pygame.quit()
            quit()

        gameLoop()
	

root = Tk() 
root.title('SNAKE AND APPLE GAME:')
root.geometry("800x600")
root['bg']='#e6e6ff'

bigf=Font(
	family="Helvetica",
	size=20,
	weight="bold")

norf=Font(
	family="Helvetica",
	size=16,
	weight="bold")

nf=Font(
	family="Helvetica",
	size=12,
	weight="bold")

T1 = tk.Text(root, height=2, width=60,font=bigf,bg="pink")
intro="               WELCOME TO SNAKE AND APPLE GAME!!"
T1.insert(tk.END, intro)
T1.pack()

label = tk.Label(text="\nENTER YOUR NAME:\n",height=2,font=norf)
entry = tk.Entry()
label.pack()
entry.pack()

def myClick():
     message = "HELLO "+entry.get()
     lb4 = Label(root, text = message,font=nf)
     lb4.pack()
     ln = Label(root, text = "ALL THE BEST!!",font=nf)
     ln.pack()

bt2 = Button(root, text = "next", command = myClick,bg = "blue",fg = "white",font=nf)
bt2.pack()


label5=tk.Label(text="\nTO KNOW MORE ABOUT THE GAME:\n",font=norf)
label5.pack()

bt_rule = Button(root, text = "RULES", command = rules,bg = "blue",fg = "white",font=nf)
bt_rule.pack()

label2=tk.Label(text="\nARE U READY TO PLAY!!   CHOOSE YOUR LEVEL...\n",font=norf)
label2.pack()

btlow = Button(root, text = "SLOW!", command = snake_play_low,bg = "blue",fg = "white",font=nf)
btlow.pack()

'''label3=tk.Label(text="\nARE U READY TO PLAY(med)",font=norf)
label3.pack()'''

btmed = Button(root, text = "INTERMEDIATE!", command = snake_play_med,bg = "blue",fg = "white",font=nf)
btmed.pack()

btfast = Button(root, text = "FAST!", command = snake_play_fast,bg = "blue",fg = "white",font=nf)
btfast.pack()

root.mainloop()