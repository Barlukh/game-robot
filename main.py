"""
Project Title: Robot
Filename: main.py

Description:
    2D game written with Pygame. Player controls a Robot and collects coins trying to avoid the monster.
    Collision is detected with rectangles, no Sprite classes were used in this project. Use arrow keys to move.
    Requirements: Python and Pygame.
"""

import pygame
import random

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Robot!")
clock = pygame.time.Clock()

class Coins:
    """ Class for coins collected. """
    def __init__(self, amount: int):
        self.amount = amount

class Entity:
    """ Class for entities (player, monsters, collectibles). """
    def __init__(self, image: callable, rect: callable):
        self.image = image
        self.rect = rect

coins = Coins(0)    
robot = Entity(pygame.image.load("graphics/robot.png"), pygame.image.load("graphics/robot.png").get_rect(center = (640 / 2, 440 / 2)))
coin = Entity(pygame.image.load("graphics/coin.png"), pygame.image.load("graphics/coin.png").get_rect(center = (random.randint(25, 615), random.randint(25, 415))))
monster_spawns = [(25, 35), (615, 35), (25, 405), (615, 405)]
monster = Entity(pygame.image.load("graphics/monster.png"), pygame.image.load("graphics/monster.png").get_rect(center = monster_spawns[random.randint(0, 3)]))

def main():
    game_start()

def game_start():
    """ Draw 'welcome' window with info for the player. """
    window.fill((50, 50, 50))
    pygame.draw.rect(window, (0, 0, 0), (0, 440, 640, 480))
    info = f"Coins collected: {coins.amount}{" " * 6}Arrow keys: move{" " * 6}Space: continue"
    game_font = pygame.font.SysFont("Arial", 23)
    text = game_font.render(info, True, (255, 255, 0))
    window.blit(text, (20, 446))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    check_events()

def check_events():
    """ Core loop. Check for events, set clock, control game state. """
    to_up = False
    to_down = False
    to_right = False
    to_left = False
    game_state = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if game_state == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        to_up = True
                    if event.key == pygame.K_DOWN:
                        to_down = True
                    if event.key == pygame.K_RIGHT:
                        to_right = True
                    if event.key == pygame.K_LEFT:
                        to_left = True    	        

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        to_up = False
                    if event.key == pygame.K_DOWN:
                        to_down = False
                    if event.key == pygame.K_RIGHT:
                        to_right = False
                    if event.key == pygame.K_LEFT:
                        to_left = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = True
                        monster.rect.center = monster_spawns[random.randint(0, 3)]
                        coins.amount = 0

        if game_state == True:
            if to_up:
                if robot.rect.top >= 3:
                    robot.rect.top -= 3
            if to_down:
                if robot.rect.bottom <= 440 - 3:    
                    robot.rect.bottom += 3    
            if to_right:
                if robot.rect.right <= 640 - 3:    
                    robot.rect.right += 3
            if to_left:
                if robot.rect.left >= 3:    
                    robot.rect.left -= 3

        coin_collision()
        monster_chase()
        game_state = monster_collision()
        if game_state == True:
            draw_window()
        else:
            game_over()
            to_up = False
            to_down = False
            to_right = False
            to_left = False

        clock.tick(60)
        pygame.display.flip()

def coin_collision():
    """ Check for coin collision, add amount if deteced. """
    if robot.rect.colliderect(coin.rect):
        coin.rect.center = (random.randint(25, 615), random.randint(25, 415))
        coins.amount += 1

def monster_chase():
    """ Set monster chasing behaviour. """
    if monster.rect.center[0] > robot.rect.center[0]:
        monster.rect.center = (monster.rect.center[0] - 1, monster.rect.center[1])
    if monster.rect.center[0] < robot.rect.center[0]:
        monster.rect.center = (monster.rect.center[0] + 1, monster.rect.center[1])
    if monster.rect.center[1] > robot.rect.center[1]:
        monster.rect.center = (monster.rect.center[0], monster.rect.center[1] - 1)
    if monster.rect.center[1] < robot.rect.center[1]:
        monster.rect.center = (monster.rect.center[0], monster.rect.center[1] + 1)

def monster_collision():
    """ Check for monster collision, return True if detected. """
    if robot.rect.colliderect(monster.rect):
        return False
    else:
        return True

def draw_window():
    """ Draw the window of the game. """
    window.fill((50, 50, 50))
    draw_score()
    draw_entities()

def draw_score():
    """ Draw collected coins score. """
    pygame.draw.rect(window, (0, 0, 0), (0, 440, 640, 480))
    game_font = pygame.font.SysFont("Arial", 23)
    text = f"Coins collected: {coins.amount}"
    text = game_font.render(text, True, (255, 255, 0))
    window.blit(text, (20, 446))

def draw_entities():
    """ Draw all entities. """
    window.blit(robot.image, robot.rect)
    window.blit(coin.image, coin.rect)
    window.blit(monster.image, monster.rect)

def game_over():
    """ Draw 'game over' window when monster_collision True. """
    window.fill((50, 50, 50))
    pygame.draw.rect(window, (0, 0, 0), (0, 440, 640, 480))
    info = f'Coins collected: {coins.amount}{" " * 22}Press Space to play again'
    game_font = pygame.font.SysFont("Arial", 23)
    text = game_font.render(info, True, (255, 255, 0))
    window.blit(text, (20, 446))

if __name__ == "__main__":
    main()