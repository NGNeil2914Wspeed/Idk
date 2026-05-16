import pygame
import sys
import random as rd

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Bouncing Circle")
clock = pygame.time.Clock()

def main():
    colours = [(255, 1, 1), (1, 1, 255), (255, 255, 255)]
    current_color = rd.choice(colours)
    bg_colours = ((100, 200, 1), (20, 255, 3), (255, 255, 1))
    bg_colour = rd.choice(bg_colours)
    

    x, y = 300, 300
    radius = 50
    # Use separate speeds for X and Y for better bouncing
    dx, dy = 5, 5 
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 1. Update Position
        x += dx
        y += dy

        screen.fill((255, 0, 0))

        # 2. Collision Detection (Bounce)
        if x + radius >= WIDTH or x - radius <= 0:
            dx *= -1
            current_color = rd.choice(colours)
            bg_colour =rd.choice(bg_colours)
            
        if y + radius >= HEIGHT or y - radius <= 0:
            dy *= -1
            current_color = rd.choice(colours)
            bg_colour = rd.choice(bg_colours)

        # 3. Draw
        screen.fill((0, 0, 0)) # Clear screen with black
        pygame.draw.circle(screen, current_color, (x, y), radius, 3)
        
        pygame.display.flip()
        clock.tick(60) # Constant 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
