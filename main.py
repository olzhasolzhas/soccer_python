import pygame
import sys
pygame.font.init()
size = (645,430)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Soccer')

map = [
    "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "g                                                               g",
    "gbbbbbbbbbbbb                                      bbbbbbbbbbbbbg",
    "gb          f                                      f           bg",
    "gb          f                                      f           bg",
    "gb       t  f                                      f   l       bg",
    "gb          f                                      f           bg",
    "gb          f                                      f           bg",
    "gb          f                                      f           bg",
    "gb       t  f                                      f   l       bg",
    "gb          f                                      f           bg",
    "gb          f                                      f           bg",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
]


class Player(object):
    def __init__(self,x,y,dx,dy,player_image):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.save_x = 0
        self.save_y = 0
        self.height = 50
        self.width = 50
        self.jump_is_allowed = False
        self.look_right = False
        self.player_left = player_image
        self.player_right = player_image
        self.player_image = player_image
        self.player_right = pygame.transform.scale(self.player_right, (self.width, self.height))
        self.player_left = pygame.transform.scale(self.player_left, (self.width, self.height))
        self.collide = False
        self.man_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.count = 0
        self.boots_x = 0
        self.boots_y = 0
        self.boots_width = int(self.width/2)
        self.boots_height = int(self.height/2)
        self.boots_right_1 = pygame.transform.scale(pygame.image.load('image/cross_right.png'),(self.boots_width, self.boots_height))
        self.boots_right_2 = pygame.transform.scale(pygame.image.load('image/cross_right_2.png'),(self.boots_width, self.boots_height))
        self.boots_right = self.boots_right_1
        self.boots_left_1 = pygame.transform.scale(pygame.image.load('image/cross_left.png'),(self.boots_width,self.boots_height))
        self.boots_left_2 = pygame.transform.scale(pygame.image.load('image/cross_left_2.png'),(self.boots_width,self.boots_height))
        self.boots_left = self.boots_left_1

        self.pinok_up = False

    def collide_f(self):

        self.save_y = self.y
        self.save_x = self.x

        self.dy = self.dy + gravity

        if self.dy > 4:
            self.dy = 4

        self.y = self.y + self.dy

        self.man_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.collide = False
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "b" or map[i][j] == "g":
                    blocks_rect = pygame.Rect(j * 10, i * 10, 10, 10)
                    if self.man_rect.colliderect(blocks_rect):
                        self.collide = True
        if self.collide or self.y <=10 or self.y >= size[1]-80:
            self.y = self.save_y
            # collide while going down?
            if self.dy > 0:
                self.jump_is_allowed = True
            self.dy = -gravity

        if self.dx >= 5:
            self.dx = 5

        self.x = self.x + self.dx

        self.man_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.collide = False
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "b" or map[i][j] == "g":
                    blocks_rect = pygame.Rect(j * 10, i * 10, 10, 10)
                    if self.man_rect.colliderect(blocks_rect):
                        self.collide = True
        if self.collide or self.x <=10 or self.x >= size[0]-40:
            self.x = self.save_x



    def boots_crd(self):
        if self == man:
            self.boots_x = int(self.x + self.width * 2 / 3)
            self.boots_y = int(self.y + self.height * 2 / 3)
        else:
            self.boots_x = int(self.x - self.width / 5)
            self.boots_y = int(self.y + self.height * 2 / 3)

    def draw(self,screen):
        self.collide_f()
        self.boots_crd()
        #dodelatttttttttttttttttttttttttttttttttt!!!!!!!!!!!!!!!!!!!!!!!!!1
        if self.look_right:
            screen.blit(self.player_right,(self.x,self.y))
        else:
            screen.blit(self.player_left,(self.x,self.y))

        if self == man:
            screen.blit(self.boots_right, (self.boots_x, self.boots_y))
        else:
            screen.blit(self.boots_left, (self.boots_x, self.boots_y))

class ball_class(object):
    def __init__(self,x,y,dx,dy,image,Player):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.save_x = 0
        self.save_y = 0
        self.height = 30
        self.width = 30
        self.image = image
        self.image = pygame.transform.scale(image,(self.width,self.height))
        self.angle = 0

    def collide_f(self):

        self.save_y = self.y
        self.save_x = self.x

        if self.dy > 15:
            self.dy = 15

        self.dy = self.dy + gravity


        self.y = self.y + self.dy
        ball_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.collide = False
        self.push = False
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "b" or map[i][j] == "g":
                    blocks_rect = pygame.Rect(j * 10, i * 10, 10, 10)
                    if ball_rect.colliderect(blocks_rect):
                        self.collide = True
        if self.collide or self.y <=10 or self.y >= size[1]-60:
            self.y = self.save_y
            self.dy = -int(self.dy/1.2)

        if self.dx >= 8:
            self.dx = 8

        self.x = self.x + self.dx

        if self.x > self.save_x:
            self.rotate_ball(90)
        if self.x < self.save_x:
            self.rotate_ball(90)

        ball_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.collide = False
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "b" or map[i][j] == "g":
                    blocks_rect = pygame.Rect(j * 10, i * 10, 10, 10)
                    if ball_rect.colliderect(blocks_rect):
                        self.collide = True

        if self.x >= size[0]-40 or self.x <= 10:
            self.x = self.save_x
            self.dx = -int(self.dx/2)

        self.x = self.x + self.dx



    def rotate_ball(self,some_angle):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.angle=self.angle + some_angle
        self.image = rotated_image

    def draw(self,screen):
        self.collide_f()
        screen.blit(self.image,(self.x,self.y))

def keys(player):
    if player == man:
        if event.type == pygame.KEYDOWN:  # Press key
            if player.jump_is_allowed:
                if event.key == pygame.K_w:
                    player.dy = -17
                    player.jump_is_allowed = False
            if event.key == pygame.K_a:
                player.dx = -4
                player.look_right = False
            if event.key == pygame.K_d:
                player.dx = 4
                player.look_right = True
            if event.key == pygame.K_SPACE:
                player.pinok_up = True
                pinok(man)
        if event.type == pygame.KEYUP:  # Release key
            if event.key == pygame.K_a:
                if player.dx < 0:
                    player.dx = 0
            if event.key == pygame.K_d:
                if player.dx > 0:
                    player.dx = 0
            if event.key == pygame.K_SPACE:
                player.pinok_up = False


    if player == enemy:
        if event.type == pygame.KEYDOWN:  # Press key
            if player.jump_is_allowed:
                if event.key == pygame.K_UP:
                    player.dy = -17
                    player.jump_is_allowed = False
            if event.key == pygame.K_LEFT:
                player.dx = -4
                player.look_right = False
            if event.key == pygame.K_RIGHT:
                player.dx = 4
                player.look_right = True
            if event.key == pygame.K_p:
                player.pinok_up = True
                pinok(enemy)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        if event.type == pygame.KEYUP:  # Release key
            if event.key == pygame.K_LEFT:
                if player.dx < 0:
                    player.dx = 0
            if event.key == pygame.K_RIGHT:
                if player.dx > 0:
                    player.dx = 0
            if event.key == pygame.K_p:
                player.pinok_up = False


def draw_blocks():
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "b":
                screen.blit(block, (j * 10, i * 10))
            if map[i][j] == 'f':
                screen.blit(net, (j * 10, i * 10))
            if map[i][j] == 'g':
                screen.blit(board, (j * 10, i * 10))




def pushing(player, ball):
    player_rect = pygame.Rect(player.x+10, player.y+10, player.width-20, player.height-15)
    ball_rect = pygame.Rect(ball.x, ball.y, ball.width, ball.height)
    if player_rect.colliderect(ball_rect):
        player.y = player.save_y
        player.x = player.save_x
        ball.x = ball.save_x
        ball.y = ball.save_y
        player.dy = player.dy + gravity
        ball.dx = -ball.dx / 2 + player.dx
        ball.dy = -ball.dy / 2 + player.dy

def pinok(player):
    boots_rect = pygame.Rect(player.boots_x, player.boots_y, player.boots_width, player.boots_height)
    ball_rect = pygame.Rect(ball.x,ball.y, ball.width,ball.height)
    if player == man:
        if boots_rect.colliderect(ball_rect):
            ball.dx = ball.dx + 10
            ball.dy = ball.dy - 20
    else:
        if boots_rect.colliderect(ball_rect):
            ball.dx = ball.dx - 10
            ball.dy = ball.dy - 20

def check_pinok(player):
    if player == man:
        if player.pinok_up:
            player.boots_right = player.boots_right_2
        else:
            player.boots_right = player.boots_right_1
    else:
        if player.pinok_up:
            player.boots_left = player.boots_left_2
        else:
            player.boots_left = player.boots_left_1

def print_goal(player):
    man.x = 200
    man.y = 200
    enemy.x = 400
    enemy.y = 200
    ball.x = 300
    ball.y = 40
    ball.dx = 0
    ball.dy = 0
    font = pygame.font.SysFont('comicsans',100,True,False)
    txt = font.render('GOAL',1,(255,0,0))
    screen.blit(txt, (200,100))
    player.count+=1
    pygame.display.update()

    i=0
    while( i < 100):
        pygame.time.delay(10)
        i+=10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 301
                pygame.quit()

def score():
    ball_rect = pygame.Rect(ball.x,ball.y,ball.width,ball.height)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "t":
                goal_rect = pygame.Rect(j * 10, i * 10, 10, 10)
                if ball_rect.colliderect(goal_rect):
                    print_goal(enemy)
            if map[i][j] == "l":
                goal_rect2 = pygame.Rect(j * 10, i * 10, 10, 10)
                if ball_rect.colliderect(goal_rect2):
                    print_goal(man)


def menu():
    running = True
    click = False
    global instruction
    while running:
        screen.blit(menu_bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        font_menu = pygame.font.SysFont('comicsans', 100)
        draw_text('Main Menu', font_menu, (255, 255, 255), screen, 100, 20)

        mx, my = pygame.mouse.get_pos()

        # first button
        button_1 = pygame.Rect(50, 100, 270, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                global game_running
                game_running = True
                game_run()
                instruction = False
                running = False

        font_2 = pygame.font.SysFont('comicsans', 65)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Start a game', font_2, (255, 255, 255), screen, 50, 100)

        # 2nd button
        button_2 = pygame.Rect(50, 200, 270, 50)
        if button_2.collidepoint((mx, my)):
            if click:
                if instruction:
                    instructions()
                    running = False
        font_2 = pygame.font.SysFont('comicsans', 65)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('Instructions', font_2, (255, 255, 255), screen, 50, 200)

        click = False


        pygame.display.update()



def instructions():
    running = True
    global instruction
    while True:
        screen.blit(menu_bg,(0,0))
        wasd = pygame.image.load('image/wasd.png')
        wasd = pygame.transform.scale(wasd,(100,100))
        space = pygame.image.load('image/space.jpg')
        space = pygame.transform.scale(space,(100,100))
        udlr = pygame.image.load('image/udlr.jpg')
        udlr = pygame.transform.scale(udlr,(120,100))
        p = pygame.image.load('image/p.png')
        p = pygame.transform.scale(p,(80,80))
        font = pygame.font.SysFont('comicsans',70)
        draw_text('1 player',font,(255,0,0),screen,80,30)
        draw_text('2 player', font, (255, 0, 0), screen, 400, 30)
        screen.blit(wasd, (100, 80))
        screen.blit(space,(100, 150))
        screen.blit(udlr, (400, 80))
        screen.blit(p, (400, 180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    instruction = False
                    menu()

        pygame.display.update()


def print_score():
    font = pygame.font.SysFont('comicsans', 100, True, False)
    txt_1 = font.render(str(man.count), 1, (0, 200, 64))
    txt_2 = font.render(str(enemy.count), 1, (0, 200, 64))
    screen.blit(txt_1, (100, 30))
    screen.blit(txt_2, (500, 30))

def game_over(player):
    running = True
    while running:
        screen.blit(menu_bg, (0, 0))
        font = pygame.font.SysFont('comicsans',100)
        draw_text('Winner',font,(255,0,0),screen,200,80)
        if player == man:
            screen.blit(pygame.transform.scale(player.player_image,(100,100)),(300,150))
        else:
            screen.blit(pygame.transform.scale(player.player_image,(100,100)), (300, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

def draw_screen():
    screen.blit(bg,(0, 0))
    draw_blocks()
    ball.draw(screen)
    man.draw(screen)
    enemy.draw(screen)
    print_score()
    pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game_run():
    pushing(man, ball)
    pushing(enemy, ball)

    check_pinok(man)
    check_pinok(enemy)
    score()
    if man.count >= 3:
        game_over(man)
        game_running = False

    if enemy.count >= 3:
        game_over(enemy)
        game_running = False

    draw_screen()

bg = pygame.image.load(r'image/back.jpg')
block = pygame.transform.scale(pygame.image.load('image/block.png'),(10,10))
net = pygame.transform.scale(pygame.image.load('image/block.png'), (10,10))
board = pygame.transform.scale(pygame.image.load(r'image/grey_board.gif'), (10,10))
player_image = pygame.image.load('image/putin.png')
enemy_image = pygame.image.load('image/boy.png')
ball_image = pygame.image.load('image/football.png')
menu_bg = pygame.image.load('image/menu.jpg')
menu_bg = pygame.transform.scale(menu_bg, bg.get_size())

clock = pygame.time.Clock()
fps = 45

gravity = 1
#player
x1 = 200
y1 = 200
dy1 = 0
dx1 = 0

#enemy
x2=400
y2=200
dx2=0
dy2=0
#ball
xb = 300
yb = 40
dx_b = 0
dy_b = 0


#Game loop
man = Player(x1,y1,dx1,dy1,player_image)
enemy = Player(x2,y2,dx2,dy2,enemy_image)
ball = ball_class(xb,yb,dx_b,dy_b,ball_image,man)
push = False
done = False
instruction = False
game_running = False
while not done:
    clock.tick(fps)
    if not game_running:
        menu()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.K_ESCAPE:
            game_running = False
            menu()

        keys(man)
        keys(enemy)

    if game_running:
        game_run()

    pygame.display.update()