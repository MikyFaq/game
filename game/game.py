#Попытка не пытка
import pygame

pygame.init()
#Дисплей
win = pygame.display.set_mode((500,500))
#Имя
pygame.display.set_caption("ХАХАХАХААХХА ТРАМП")
#Спрайты
walkRight = [pygame.image.load('pygame_right_1.png'),
pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'),
pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'),
pygame.image.load('pygame_right_6.png')]

walkLeft = [pygame.image.load('pygame_left_1.png'),
pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'),
pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'),
pygame.image.load('pygame_left_6.png')]
#Фон
bg = pygame.image.load('pygame_bg.jpg')
playerStand = pygame.image.load('pygame_idle.png')

clock = pygame.time.Clock()
#Персонаж
x = 50
y = 425
widht = 60
height = 71
speed = 5
#Прыжок
isJump = False
jumpCount = 10
#Анимки
left = False
right = False
animCount = 0
#Ходьба
def drawWindow():
    global animCount
    win.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0

    if left == True:
        win.blit(walkLeft[animCount // 5], (x,y))
        animCount += 1
    elif right == True:
        win.blit(walkRight[animCount // 5], (x,y))
        animCount += 1
    else:
        win.blit(playerStand, (x,y))


    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Кнопки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    if keys[pygame.K_RIGHT] and x < 500 - widht - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    #Прыжок
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    drawWindow()
pygame.quit()
