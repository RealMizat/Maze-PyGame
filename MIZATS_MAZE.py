#! /usr/bin/env python

import os
import random
import pygame

# Class for the orange dude
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(20, 20, 7, 16)

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 14)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((900, 740))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                      WW               WWWW    WWWWWWW",
"W         WWWWWW      WWWWWW    WW            WWWWWWWWW",
"W   WWWW       W   W     WW     WW   W                W",
"W   W        WWWW  WW          WW   WW          WW    W",
"W  WW              WWWW       WWW  WWWWWWW   WWWWW    W",
"W   W     W        WWWWWWW          WW        WWWW    W",
"W   W     W   WWW  W   wWWWWW  WW  WW        WWWW     W",
"W   WWW WWW   W W  W           WW  WWWWW     WWWW     W",
"W     W   W   W W  W           WW  WWWWW    WWWWW     W",
"WWW       WWWWW W  W  WWWWW     WWWWWWWW    WWWWW     W",
"W        WW        W   WWWWW   W   WWW      WWWWW   W W",
"WW     WWWW            wWwwW   W        WWWW   W   W W",
"W      W              WWWWW    WW               W   W W",
"WW    WWWWWWWWWWWWWWWWWWWWW    WWWWWWWWWW       W   W W",
"WW        WWWWW      WWWWWWw       WWWWWW       W   W W",
"W   WW    WWWWW      WWWW                  W    W   W W", 
"WW WWW                 WWWWWWWWWWWWWW      W WWWW   W W",
"WW WWWWWWWWWWWWWW             WWWW WW      WWWWW  WW  WWWWWWW",
"WW WW  WWWWWWWWWW WWWW W WWWWWWWWW WW   WWWW  WWW   W W W  W",
"W      WWWWWWWWW           WW      W     WWW  WWW   W WW  EWW",
"WWWWWWWWWWWWWWWW     WW    WW      WWWW       WWW   W W   WW",
"W                                  WWWW        WW   W    WW",
"W                                        WW    WW     WWWW",
"WW                       WWW                WW   WW   W",
"WW                     WW   WW       WWWW      WW  WW W",
"WWW                   W       W     W    WWW    WW WW W",
"WWWW                 W         WWWWW        W     WWW W",
"WWW                 W   WWW              W W W  WWWW  W",
"WW         WWWW     W WWWWWWW   WWWWWW  WWWWW W WWWW  W",
"WW        WWWWW W  W  WW W WW   W WW W  W W W  W  W   W",
"W        WWWWWW W W  WWWWWWWWW  WWWWWW  WWWWW  W  W   W", 
"W      WWWW   WWWWW  W WW WW W  W WW W  W W WW  WW    W",
"W      WWW W W W W   WWWWWWWWW WWWWWWWWWWWWWWWWW W    W",
"W      WWW W W WW    WWW   WWWWWW  W  WWWWW WWWW W    W",
"W                                                     W",
"WW    WWWWWWWWWWWWWWWWWWWWWWWW WWWWWWWWWWWWWWWWWW     W",
"WW    W WW  WW  WW  WWW   WW  W  WW   WW  WW  WWW     W",
"WW    WWWWWWWWWWWWWWWWWWWW   W W   WWWWWWWWWWWWW      W",
"W                       WWWWWWWWWWWWWW                W",
"W                        WWWWWWWWWWWW      WW         W",
"WWW                        WW    WW        WW        WW",
"WWW                                                  WW",
"W                                                   WWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 6, 18)
        x += 16
    y += 16
    x = 0

running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    
    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        raise SystemExit ("You win!")
    
    # Draw the scene
    screen.fill((5, 17, 9))
    for wall in walls:
        pygame.draw.rect(screen, (156, 44, 152), wall.rect)
    pygame.draw.rect(screen, (44, 192, 213), end_rect)
    pygame.draw.rect(screen, (15, 124, 73), player.rect)
    pygame.display.flip()

