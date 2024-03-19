import pygame
import sys
import random

# Initialize Pygame....
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300  # Adjusted window size....
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ARRAY_SIZE = 25  # Adjusted array size....
ARRAY_ELEMENT_WIDTH = WIDTH // ARRAY_SIZE

# Generate a random array of heights
# array = random.sample(range(10, 91), ARRAY_SIZE)
array = [90, 20, 40, 60, 10, 80, 30, 50, 70]

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")
font = pygame.font.Font(None, 15)  # Adjusted font size
clock = pygame.time.Clock()

# Remaining code remains the same...

def draw_array():
    for i, height in enumerate(array):
        # Display the value above the bar
        text = font.render(str(height), True, BLACK)
        text_rect = text.get_rect(center=(i * ARRAY_ELEMENT_WIDTH + ARRAY_ELEMENT_WIDTH // 2, HEIGHT - height - 20))
        screen.blit(text, text_rect)

        # Draw the bar
        pygame.draw.rect(screen, BLACK, (i * ARRAY_ELEMENT_WIDTH, HEIGHT - height, ARRAY_ELEMENT_WIDTH, height))

    pygame.display.flip()


def bubble_sort():
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            # Highlight the elements being compared
            screen.fill(WHITE)
            for k, height in enumerate(array):
                color = RED if k == j or k == j + 1 else BLACK

                # Display the value above the bar
                text = font.render(str(height), True, color)
                text_rect = text.get_rect(
                    center=(k * ARRAY_ELEMENT_WIDTH + ARRAY_ELEMENT_WIDTH // 2, HEIGHT - height - 20))
                screen.blit(text, text_rect)

                # Draw the bar graph
                pygame.draw.rect(screen, color, (k * ARRAY_ELEMENT_WIDTH, HEIGHT - height, ARRAY_ELEMENT_WIDTH, height))

            pygame.display.flip()
            pygame.time.delay(400)

            # Swap if needed
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    # Final display
    screen.fill(WHITE)
    for i, height in enumerate(array):
        # Display the value above the bar
        text = font.render(str(height), True, BLACK)
        text_rect = text.get_rect(center=(i * ARRAY_ELEMENT_WIDTH + ARRAY_ELEMENT_WIDTH // 2, HEIGHT - height - 20))
        screen.blit(text, text_rect)

        # Draw the bar
        pygame.draw.rect(screen, BLACK, (i * ARRAY_ELEMENT_WIDTH, HEIGHT - height, ARRAY_ELEMENT_WIDTH, height))

    pygame.display.flip()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Run the bubble sort algorithm
    if not any(array[i] > array[i + 1] for i in range(len(array) - 1)):
        # If the array is sorted, stop the loop
        running = False
    else:
        bubble_sort()

    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()