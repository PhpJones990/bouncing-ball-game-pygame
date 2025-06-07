import pygame
import math

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(64)

WINDOW_SIZE = [500, 500]

screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("Bouncing Ball!")
clock = pygame.time.Clock()

font = pygame.font.Font(None, size=30)

sound = pygame.mixer.Sound("paddle_hit.wav")

x = 50
y = 50
r = 10.0
x_speed = 50
y_speed = 45

score = 0

delta_time = 0.1

running = True
moving = True

ball_color = (255, 255, 255)
pressed_time = True

def m_ball_collision(b_x, b_y, m_x, m_y, radius):
    distance = math.sqrt((b_x-m_x)**2 + (b_y-m_y)**2)
    if distance <= radius:
        return True
    else:
        return False

while running:

    screen.fill((0, 0, 0))

    m_pos = pygame.mouse.get_pos()
    m_pressed = pygame.mouse.get_pressed()

    if m_ball_collision(x, y, m_pos[0], m_pos[1], r) and m_pressed[0] and pressed_time:
        ball_color = (255, 0, 0)
        pressed_time = False
        r *= 1.1
        x_speed *= 1.2
        y_speed *= 1.2
        score += 1
        sound.play()
    elif not m_ball_collision(x, y, m_pos[0], m_pos[1], r):
        ball_color = (255, 255, 255)
        pressed_time = True

    pygame.draw.circle(screen, ball_color, (x, y), r)
    if moving:
        x += x_speed * delta_time
        y += y_speed * delta_time

    text = font.render(f"{score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if x < r:
        x = r+1
        x_speed *= -1
        x_speed *= 1.1
        r *= 1.05
        sound.play()
    elif x > WINDOW_SIZE[0] - r:
        x = WINDOW_SIZE[0] - r - 1
        x_speed *= -1
        x_speed *= 1.1
        r *= 1.05
        sound.play()
    if y < r:
        y = r+1
        y_speed *= -1
        y_speed *= 1.1
        r *= 1.05
        sound.play()
    elif y > WINDOW_SIZE[1] - r:
        y = WINDOW_SIZE[1] - r - 1
        y_speed *= -1
        y_speed *= 1.1
        r *= 1.05
        sound.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                x_speed *= 1.1
            if event.key == pygame.K_c:
                x_speed *= 0.9
            if event.key == pygame.K_y:
                y_speed *= 1.1
            if event.key == pygame.K_u:
                y_speed *= 0.9
            if event.key == pygame.K_SPACE:
                if moving:
                    moving = False
                else:
                    moving = True
        

    delta_time = clock.tick(120) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
    pygame.display.flip()

pygame.quit()