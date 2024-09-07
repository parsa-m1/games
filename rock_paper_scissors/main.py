import pygame
import sys
from random import choice

pygame.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Rock Paper Scissors')

clock = pygame.time.Clock()

running = True

#icons 

paper = pygame.image.load('files/paper.png')
paper_rect = paper.get_rect(center=(170, 150))

rock = pygame.image.load('files/rock.png')
rock_rect = rock.get_rect(center=(530, 150))

scissors = pygame.image.load('files/scissors.png')
scissors_rect = scissors.get_rect(center=(350, 300))

# messages

dujitsu_font = pygame.font.Font('files/DujitsuFont-Demo.otf', 50)
sylfaen_font = pygame.font.Font('files/sylfaen.ttf', 20)

title_message = dujitsu_font.render('Rock Paper Scissors', False, (255, 255, 255))
title_message_rect = title_message.get_rect(center=(350, 40))


scores = {
    'wins': 0,
    'ties': 0,
    'losses': 0
}

# second page

restart_message = dujitsu_font.render('press space to play again', False, (22, 31, 61))
restart_message = pygame.transform.rotozoom(restart_message, 0, 1.2)
restart_message_rect = restart_message.get_rect(center=(350, 340))

player_picked_rect = paper.get_rect(center=(150, 180))
computer_picked_rect = paper.get_rect(center=(550, 180))

player_picked_message = sylfaen_font.render('You picked: ', False, (255, 255, 255))
player_picked_message_rect = player_picked_message.get_rect(center=(150, 70))

computer_picked_message = sylfaen_font.render('Computer picked: ', False, (255, 255, 255))
computer_picked_message_rect = computer_picked_message.get_rect(center=(550, 70))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if running:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if paper_rect.collidepoint(pygame.mouse.get_pos()):
                    player_move = 'paper'
                    computer_move = choice(['rock', 'paper', 'scissors'])
                    running = False

                    if computer_move == 'paper':
                        result = 'tie'
                        scores['ties'] += 1
                    elif computer_move == 'rock':
                        result = 'win'
                        scores['wins'] += 1
                    else:
                        result = 'lose'
                        scores['losses'] += 1
                
                elif rock_rect.collidepoint(pygame.mouse.get_pos()):
                    player_move = 'rock'
                    computer_move = choice(['rock', 'paper', 'scissors'])
                    running = False

                    if computer_move == 'rock':
                        result = 'tie'
                        scores['ties'] += 1
                    elif computer_move == 'scissors':
                        result = 'win'
                        scores['wins'] += 1
                    else:
                        result = 'lose'
                        scores['losses'] += 1
                
                elif scissors_rect.collidepoint(pygame.mouse.get_pos()):
                    player_move = 'scissors'
                    computer_move = choice(['rock', 'paper', 'scissors'])
                    running = False

                    if computer_move == 'scissors':
                        result = 'tie'
                        scores['ties'] += 1
                    elif computer_move == 'paper':
                        result = 'win'
                        scores['wins'] += 1
                    else:
                        result = 'lose'
                        scores['losses'] += 1
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True


    if running:

        screen.fill((15, 22, 43))

        # messages

        screen.blit(title_message, title_message_rect)

        score_text = [f'wins: {scores["wins"]}',
            f'ties: {scores["ties"]}',
            f'losses: {scores["losses"]}'              
        ]
        for i in range(len(score_text)):
            score_message = sylfaen_font.render(score_text[i], False, (255, 255, 255))
            screen.blit(score_message, (50, 300 + (i * 30)))

        # iconc
        pygame.draw.circle(screen, (255, 255, 255), center=(170, 150), radius=70)
        screen.blit(paper, paper_rect)

        pygame.draw.circle(screen, (255, 255, 255), center=(530, 150), radius=70)
        screen.blit(rock, rock_rect)
                
        pygame.draw.circle(screen, (255, 255, 255), center=(350, 300), radius=70)
        screen.blit(scissors, scissors_rect)

    else:
        screen.fill((15, 22, 43))

        # messages

        screen.blit(restart_message, restart_message_rect)

        screen.blit(player_picked_message, player_picked_message_rect)
        screen.blit(computer_picked_message, computer_picked_message_rect)

        if result == 'win':
            result_message = dujitsu_font.render('You won', False, (22, 31, 61))
        elif result == 'lose':
            result_message = dujitsu_font.render('You lost', False, (22, 31, 61))
        else:
            result_message = dujitsu_font.render('Tie', False, (22, 31, 61))

        result_message_rect = result_message.get_rect(center = (350, 200))
        screen.blit(result_message, result_message_rect)

        # icons

        pygame.draw.circle(screen, (255, 255, 255), center=(150, 180), radius=70)
        if player_move == 'paper':
            screen.blit(paper, player_picked_rect)
        elif player_move == 'rock':
            screen.blit(rock, player_picked_rect)
        else:
            screen.blit(scissors, player_picked_rect)


        pygame.draw.circle(screen, (255, 255, 255), center=(550, 180), radius=70)
        if computer_move == 'paper':
            screen.blit(paper, computer_picked_rect)
        elif computer_move == 'rock':
            screen.blit(rock, computer_picked_rect)
        else:
            screen.blit(scissors, computer_picked_rect)

        



    pygame.display.update()
    clock.tick(60)




