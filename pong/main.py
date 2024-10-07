import pygame
from sys import exit
import random

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 140)
computer = pygame.Rect(10, screen_height/2 -70, 10, 140)
ball = pygame.Rect(screen_width/2 -15, screen_height/2 -15, 30, 30)

light_grey = (200, 200, 200)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
computer_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    if computer.centery > ball.centery:
        computer.y -= computer_speed
    if computer.centery < ball.centery:
        computer.y += computer_speed



    if ball.colliderect(player):
        ball_speed_x *= -1
    if ball.colliderect(computer):
        ball_speed_x *= -1
        






    if ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    
    if ball.right >= screen_width:
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_x *= random.choice([-1, 1])
        ball_speed_y *= random.choice([-1, 1])

    if ball.left <= 0:
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_x *= random.choice([-1, 1])
        ball_speed_y *= random.choice([-1, 1])


    ball.y += ball_speed_y
    ball.x += ball_speed_x
    
    
    
    
    
    
    
    screen.fill(pygame.Color('grey12'))

    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, computer)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))


    


    pygame.display.update()
    clock.tick(60)












