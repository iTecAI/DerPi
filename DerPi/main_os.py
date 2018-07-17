import time, pygame

pygame.init()
screen = pygame.display.set_mode([480,320], pygame.NOFRAME)
pygame.display.flip()

pygame.mouse.set_cursor(*pygame.cursors.broken_x)
pygame.mouse.set_visible(False)

#run intro
dpos = 0
dlogo = pygame.image.load('derplogo.png')
for i in range(50):
    screen.fill([230,230,230])
    pygame.draw.rect(screen, pygame.Color(0,0,0,0), pygame.Rect(200, 220, 40, 100))
    pygame.display.flip()
    screen.blit(dlogo, (220, dpos))
    pygame.display.flip()
    dpos += 4
    time.sleep(0.05)
    pygame.event.get()

start = pygame.mixer.Sound('start.wav')
start.play()
time.sleep(6)
for i in range(70):
    screen.fill([230,230,230])
    pygame.draw.rect(screen, pygame.Color(0,0,0,0), pygame.Rect(200, 220, 40, 100))
    pygame.display.flip()
    dlogo = pygame.transform.rotate(dlogo, -2)
    screen.blit(dlogo, (220, dpos))
    pygame.display.flip()
    time.sleep(0.05)
    pygame.event.get()

opacity = 255
box = pygame.Surface((40, 100), pygame.SRCALPHA)
for i in range(52):
    screen.fill([230,230,230])
    box.fill([0,0,0,opacity])
    screen.blit(box, (200,220))
    pygame.display.flip()
    opacity -= 5
    time.sleep(0.02)
    pygame.event.get()

screen.fill([230,230,230])
pygame.display.flip()
#intro complete

pR = pygame.image.load('pointerR.png')
pL = pygame.image.load('pointerL.png')
pygame.mouse.set_visible(True)

screen.blit(pR, (400, 110))
screen.blit(pL, (30, 110))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] >= 400 and event.pos[0] <= 450 and event.pos[1] >= 110 and event.pos[1] <= 210:
                print('pr')
            if event.pos[0] >= 30 and event.pos[0] <= 80 and event.pos[1] >= 110 and event.pos[1] <= 210:
                print('pl')
