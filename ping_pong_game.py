from pygame import *
from random import randint
score1 = 0
score2 = 0
window = display.set_mode((700, 500))
display.set_caption("Ping Pong Game")
background = transform.scale(image.load("background.png"), (700, 500))
font.init()
font1 = font.SysFont("Arial", 80)
font2 = font.SysFont("Arial", 36)
missed = 0
hit = 0
max_missed = 3
win = font1.render("You win!", True, (0, 255, 0))
lose = font1.render("You lose!", True, (255, 0, 0))
game = 1
finish = 0
clock = time.Clock()
fps = 60
font.init()
font1 = font.SysFont("Arial", 80)
font2 = font.SysFont("Arial", 30)
win1 = font1.render("Player 1 Wins!", True, (0, 255, 0))
win2 = font1.render("Player 2 Wins!", True, (0, 255, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, img_w, img_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (img_w, img_h))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < 415:
            self.rect.y += self.speed_y
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed_y
class Object(GameSprite):
    def update(self):
        global missed, score1, score2
        if self.rect.y > 465:
            self.speed_y = -1 * self.speed_y
        if self.rect.y < -20:
            self.speed_y = -1 * self.speed_y
        if self.rect.x > 665:
            self.speed_x = -1 * self.speed_x
            score1 += 1
            self.rect.x = 300
            self.rect.y = 200
        if self.rect.x < -20:
            self.speed_x = -1 * self.speed_x
            score2 += 1
            self.rect.x = 300
            self.rect.y = 200
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
paddle1 = Player("paddle.jpg", 0, 400, 0, 5, 50, 90)
paddle2 = Player("paddle.jpg", 650, 400, 0, 5, 50, 90)
ball = Object("ball.png", 300, 300, 5, 2, 65, 65)
while game:
    for events in event.get():
        if events.type == QUIT:
            game = 0
    if not finish:
        window.blit(background, (0, 0))
        text1 = font2.render("Player 1: " + str(score1), 1, (255,255,255))
        window.blit(text1,(10,20))
        text2 = font2.render("Player 2: " + str(score2), 1, (255,255,255))
        window.blit(text2,(550,20))
        keys_pressed = key.get_pressed()
        paddle1.reset()
        paddle2.reset()
        ball.reset()
        paddle1.update1()
        paddle2.update2()
        ball.update()
        if sprite.collide_rect(paddle1, ball) or sprite.collide_rect(paddle2, ball):
            ball.speed_x *= -1
            ball.speed_y *= -1
        if score1 >= 10:
            finish = 1
            window.blit(win1, (200, 200))
        if score2 >= 10:
            finish = 1
            window.blit(win2, (200, 200))
        display.update()
        clock.tick(fps)