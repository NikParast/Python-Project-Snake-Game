import sys
import pygame
import random
import time
from math import dist

pygame.init()
screen = pygame.display.set_mode((800,600))

def draw_line(sx,sy,ex,ey):
    pygame.draw.line(screen, (0,0,0), (sx, sy), (ex, ey), 5)


class Snake:
    def __init__(self, color, x, y, direction, k_right, k_left, k_up, k_down):
        self.color = color
        self.direction = direction
        self.x = x
        self.y = y
        self.right = getattr(pygame, k_right)
        self.left = getattr(pygame, k_left)
        self.up = getattr(pygame, k_up)
        self.down = getattr(pygame, k_down)
        self.body = [[self.x, self.y]]
        self.immortal = False
        self.immortal_time = 8.0
        self.dont_pop = False
        self.speed = 0


    def _move_right(self):
        self.direction = "right"
        self.x += 40
        self.body.insert(0, [self.x, self.y])
        if not self.dont_pop:
            self.body.pop()

    def _move_left(self):
        self.direction = "left"
        self.x -= 40
        self.body.insert(0, [self.x, self.y])
        if not self.dont_pop:
            self.body.pop()

    def _move_up(self):
        self.direction = "up"
        self.y -= 40
        self.body.insert(0, [self.x, self.y])
        if not self.dont_pop:
            self.body.pop()

    def _move_down(self):
        self.direction = "down"
        self.y += 40
        self.body.insert(0, [self.x, self.y])
        if not self.dont_pop:
            self.body.pop()


    def change_direction(self):
        opposites = {"right": "left", "left": "right", "up": "down", "down": "up"}
        if event.key == self.right:
            if opposites[self.direction] != "right":
                self.direction = "right"
        elif event.key == self.left:
            if opposites[self.direction] != "left":
                self.direction = "left"
        elif event.key == self.up:
            if opposites[self.direction] != "up":
                self.direction = "up"
        elif event.key == self.down:
            if opposites[self.direction] != "down":
                self.direction = "down"


    def move(self):
        if self.direction == "right":
            self._move_right()
        elif self.direction == "left":
            self._move_left()
        elif self.direction == "up":
            self._move_up()
        elif self.direction == "down":
            self._move_down()



    def draw_snake(self):
        for directions in self.body:
            pygame.draw.rect(screen, self.color, (directions[0], directions[1], 30, 30))







snakes_amount = 1
clock = pygame.Clock()
sx, sy = 0, 0
ex, ey = 0, 0
snakes = [
    Snake((255,0,0), 5, 5, "right", "K_RIGHT", "K_LEFT", "K_UP", "K_DOWN"),
    Snake((255,180,0),765,5, "down", "K_d", "K_a", "K_w", "K_s"),
    Snake((7, 255, 58), 5, 565, "up", "K_h", "K_f", "K_t", "K_g"),
    Snake((0, 158, 255), 765, 565, "left", "K_KP6", "K_KP4", "K_KP8", "K_KP5")
    ]


wait = 5
wall_time = 10
fx, fy = -1000, -1000
walls = []
speed = 3
first_time = True
period = 5
period_addition = 5
make_wall = True
black_time = 0

##############
sticky_fruit = False
immortal = False
all_black = False
##############
special_fruit = (random.randint(1, 2), random.randint(10, 12))
special_fruit_reach_counter = 0
can_be_immortal = False

start = time.time()

music_started = False
run = False
done = False
go_to_main_menu = False
intro_image = pygame.image.load(r"C:\Users\asre_rayane\Downloads\Mobile Devices\8o5cuW4XWHvDNDLVX2tDiiGdVDM-AjRud8P_QPil_k_Qlk5cPA.png")
intro_image = pygame.transform.scale(intro_image, (800, 600))
font = pygame.font.Font(r"C:\Users\asre_rayane\Downloads\Press_Start_2P\PressStart2P-Regular.ttf", 36)
smfont = pygame.font.Font(r"C:\Users\asre_rayane\Downloads\Press_Start_2P\PressStart2P-Regular.ttf", 20)
STtext = font.render("Start", True, (0, 0, 0))
STRect = pygame.Rect(300, 270, 200, 60)
How_Many_Players_Text = smfont.render("How Many Players ?", True, (0, 0, 0))
ONE_PlayerRect = pygame.Rect(235, 235, 30, 30)
TWO_PlayerRect = pygame.Rect(335, 235, 30, 30)
THREE_PlayerRect = pygame.Rect(435, 235, 30, 30)
FOUR_PlayerRECT = pygame.Rect(535, 235, 30, 30)
Exit_C_pos = (400, 400)##
Exit_C_R = 40##
white = (255, 255, 255)
black = (0, 0, 0)
one_text_color=black
two_text_color=black
three_text_color=black
four_text_color=black
immortal_text = smfont.render("Immortal", True, (255, 203, 229))
MultiFruit_text = smfont.render("MultiFruit", True, (255, 0, 0))
exit_text = smfont.render("Exit", True, (0,0,0))


one_rect_color = white
two_rect_color = white
three_rect_color = white
four_rect_color = white

info_image = pygame.image.load(r"C:\Users\asre_rayane\Downloads\Mobile Devices\file_0000000086a8824684e63b977c04d377.png")
info_image = pygame.transform.scale(info_image, (800, 600))

# music & sound
###############
pygame.mixer.init()
musics = {
    "intro": r"C:\Users\asre_rayane\Downloads\Run-Amok(chosic.com).mp3",
    "end": r"C:\Users\asre_rayane\Downloads\tuomas_data-game-over-39-199830.mp3",
    "Sneaky": r"C:\Users\asre_rayane\Downloads\Elevator-music(chosic.com).mp3",
    "Elevator": r"C:\Users\asre_rayane\Downloads\Sneaky-Snitch(chosic.com).mp3",
    "Ultra bag": r"C:\Users\asre_rayane\Downloads\Ultra-Lag-chosic.com_.mp3",
    "Sakura": r"C:\Users\asre_rayane\Downloads\Sakura-Girl-Yay-chosic.com_.mp3",
    "Forest walk": r"C:\Users\asre_rayane\Downloads\ForestWalk-320bit(chosic.com).mp3"
}
sounds = {
    "bubble": r"C:\Users\asre_rayane\Downloads\universfield-bubble-pop-06-351337.mp3",
    "double bubble": r"C:\Users\asre_rayane\Downloads\universfield-bubble-pop-08-351339.mp3",
    "intense bubble pop": r"C:\Users\asre_rayane\Downloads\soundreality-bubble-pop-424583 (1).mp3",
    "hit": r"C:\Users\asre_rayane\Downloads\mrstokes302-omega-perc-the-light-kit-mrstokes302-441066.mp3"
}
bubble = pygame.mixer.Sound(sounds["bubble"])
double_bubble = pygame.mixer.Sound(sounds["double bubble"])
hit = pygame.mixer.Sound(sounds["hit"])
intense_bubble = pygame.mixer.Sound(sounds["intense bubble pop"])
###############
if not run:
    pygame.mixer.music.load(musics["intro"])
    pygame.mixer.music.play(-1)



while True:
    if not run:

        One = smfont.render("1", True, one_text_color)
        Two = smfont.render("2", True, two_text_color)
        Three = smfont.render("3", True, three_text_color)
        Four = smfont.render("4", True, four_text_color)
        screen.blit(intro_image, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), STRect)
        screen.blit(STtext, (315, 280))
        pygame.draw.rect(screen, (255, 255, 255), (235, 195, 330, 30))
        pygame.draw.rect(screen, (255, 255, 255), (575, 195, 30, 30))
        screen.blit(How_Many_Players_Text, (240, 200))
        pygame.draw.rect(screen, one_rect_color, ONE_PlayerRect)
        pygame.draw.rect(screen, two_rect_color, TWO_PlayerRect)
        pygame.draw.rect(screen, three_rect_color, THREE_PlayerRect)
        pygame.draw.rect(screen, four_rect_color, FOUR_PlayerRECT)
        screen.blit(One, (240, 240))
        screen.blit(Two, (340, 240))
        screen.blit(Three, (440, 240))
        screen.blit(Four, (540, 240))
        pygame.draw.rect(screen, (255, 203, 229), (50,500, 30,30))
        screen.blit(immortal_text, (3, 538))
        pygame.draw.rect(screen, (255, 0, 0), (700,50, 30,30))
        screen.blit(MultiFruit_text, (600, 10))
        pygame.draw.circle(screen, (255, 255, 255), Exit_C_pos, Exit_C_R)
        screen.blit(exit_text, (362, 390))
        pygame.display.update()

    elif run and not done:
        screen.blit(info_image, (0, 0))
        pygame.display.flip()

    elif done:
        if not music_started:
            pygame.mixer.music.stop()
            music_started = True
            selected_music = random.choice(list(musics.keys())[2:])
            pygame.mixer.music.load(musics[selected_music])
            pygame.mixer.music.play(-1)


        clock.tick(speed)
        not_allowed_wall = False
        screen.fill((255, 255, 255))





        for index, snake in enumerate(snakes):
            snake.dont_pop = False
            if not snake.immortal:
                if snake.x >= 800 or snake.x <= 0 or snake.y >= 600 or snake.y <= 0:
                    hit.play()
                    snake.body.clear()
                    snakes.remove(snake)
                for i in range(len(walls)):
                    if snake.x == walls[i][0] and snake.y == walls[i][1]:
                        hit.play()
                        snake.body.clear()
                        snakes.remove(snake)
                for index2, snake2 in enumerate(snakes):
                    if index2 != index:
                        for direction2 in snake2.body:
                            if snake.body and snake.body[0] == direction2:
                                hit.play()
                                snake.body.clear()
                                snakes.remove(snake)
                                break
                    elif index2 == index:
                        for direction2 in snake2.body[4:]:
                            if snake.body and snake.body[0] == direction2:
                                hit.play()
                                snake.body.clear()
                                snakes.remove(snake)
                                break
            else:
                teleported = False
                if snake.x >= 800:
                    snake.x = -35
                    teleported = True
                elif snake.x < 0:
                    snake.x = 805
                    teleported = True
                elif snake.y >= 600:
                    snake.y = -35
                    teleported = True
                elif snake.y < 0:
                    snake.y = 605
                    teleported = True

                if teleported and snake.body:
                    snake.body[0] = [snake.x, snake.y]



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for snake in snakes:
                    snake.change_direction()



        if wait == 0:
            wait = 20
            if sticky_fruit:
                sticky_fruit = False
            if can_be_immortal:
                can_be_immortal = False


            special_fruit_reach_counter += 1
            if special_fruit_reach_counter == special_fruit[1]:

                if special_fruit[0] == 1:
                    wait = 30
                    sticky_fruit = True
                elif special_fruit[0] == 2:
                    can_be_immortal = True

                special_fruit = (random.randint(1, 2), random.randint(6, 8))

                special_fruit_reach_counter = 0

            fx, fy = random.randrange(5, 796, 40), random.randrange(5, 595, 40)
        if sticky_fruit:
            pygame.draw.rect(screen, (255, 0, 0), (fx, fy, 30, 30))
        elif can_be_immortal:
            pygame.draw.rect(screen, (207, 188, 204), (fx, fy, 30, 30))
        elif all_black:
            pygame.draw.rect(screen, (0, 0, 0), (fx, fy, 30, 30))
        else:
            pygame.draw.rect(screen, (255, 21, 154), (fx, fy, 30, 30))
        if wall_time == 0 and make_wall:
            wall_time = 25
            wx, wy = random.randrange(5, 796, 40), random.randrange(5, 595, 40)
            for snake in snakes:
                if wx == snake.body[0][0] and wy == snake.body[0][1]:
                    not_allowed_wall = True
                    break
            if not not_allowed_wall:
                walls.append([wx, wy, 30, 30])

        for wall in walls:
                    pygame.draw.rect(screen, (60,60,60), wall)


        for snake in snakes:
            snake.speed = speed
            if snake.x == fx and snake.y == fy:


                if sticky_fruit:
                    double_bubble.play()
                    pygame.draw.rect(screen, (255, 0, 0), (fx, fy, 30, 30))
                elif can_be_immortal:
                    intense_bubble.play()
                    snake.copy_color = snake.color
                    snake.color = (207, 188, 204)
                    snake.immortal = True
                    snake.immortal_time = 8.0
                    fx, fy = -1000, -1000

                else:
                    bubble.play()
                    fx, fy = -1000, -1000
                snake.dont_pop = True

        if len(walls) == 40:
            make_wall = False

        for snake in snakes:
            if snake.immortal:
                snake.immortal_time -= 1 / speed
                if snake.immortal_time <= 0:
                    snake.color = snake.copy_color
                    snake.immortal = False
            snake.move()
            snake.draw_snake()


        sy, ey = 0, 600
        sx, ex = 0, 0
        while sx < 800:
            draw_line(sx,sy,ex,ey)
            sx += 40
            ex += 40

        sx, ex = 0, 800
        sy, ey = 0, 0
        while sy < 600:
            draw_line(sx,sy,ex,ey)
            sy += 40
            ey += 40



        wait -= 1
        wall_time -= 1





        stop = time.time()
        if speed != 6 and first_time:
            if stop - start > period:
                speed += 1
                period += period_addition
        else:
            first_time = False

        if len(snakes) == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(musics["end"])
            pygame.mixer.music.play()
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()




        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
             if run and not done:
                 done = True
             x_pos, y_pos = pygame.mouse.get_pos()
             distance = dist((x_pos, y_pos),Exit_C_pos)
             if distance <= Exit_C_R:##
                 pygame.quit()
                 sys.exit()

             if STRect.collidepoint(event.pos):
                 snakes = snakes[:snakes_amount]
                 run = True

             elif ONE_PlayerRect.collidepoint(event.pos):
                 one_rect_color = black
                 one_text_color = white
                 two_rect_color = white
                 two_text_color = black
                 three_rect_color = white
                 three_text_color = black
                 four_rect_color = white
                 four_text_color = black
                 snakes_amount = 1
             elif TWO_PlayerRect.collidepoint(event.pos):
                 one_rect_color = white
                 one_text_color = black
                 two_rect_color = black
                 two_text_color = white
                 three_rect_color = white
                 three_text_color = black
                 four_rect_color = white
                 four_text_color = black
                 snakes_amount = 2
             elif THREE_PlayerRect.collidepoint(event.pos):
                 one_rect_color = white
                 one_text_color = black
                 two_rect_color = white
                 two_text_color = black
                 three_rect_color = black
                 three_text_color = white
                 four_rect_color = white
                 four_text_color = black
                 snakes_amount = 3
             elif FOUR_PlayerRECT.collidepoint(event.pos):
                 one_rect_color = white
                 one_text_color = black
                 two_rect_color = white
                 two_text_color = black
                 three_rect_color = white
                 three_text_color = black
                 four_rect_color = black
                 four_text_color = white
                 snakes_amount = 4

