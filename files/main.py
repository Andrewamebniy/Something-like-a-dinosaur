import pygame
import os


Path = os.path.abspath('.')+'/'


def draw_button(screen, x, y, width, height, button_image, corner_radius):
    image = pygame.transform.scale(button_image, (width, height))
    screen.blit(image, (x, y))


def is_clicked(pos, x, y, width, height):
    if x < pos[0] < x + width and y < pos[1] < y + height:
        return True
    return False


pygame.init()
screen = pygame.display.set_mode((618, 359), pygame.SCALED | pygame.FULLSCREEN)  #flags=pygame.NOFRAME
pygame.display.set_caption("тип динозаврик крч")
icon = pygame.image.load(Path + "icon.webp").convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
player_left = [
    pygame.image.load(Path + "left1.png").convert_alpha(),
    pygame.image.load(Path + "left2.png").convert_alpha(),
    pygame.image.load(Path + "left3.png").convert_alpha(),
    pygame.image.load(Path + "left4.png").convert_alpha()
]
player_right = [
    pygame.image.load(Path + "right1.png").convert_alpha(),
    pygame.image.load(Path + "right2.png").convert_alpha(),
    pygame.image.load(Path + "right3.png").convert_alpha(),
    pygame.image.load(Path + "right4.png").convert_alpha()
]
foto = pygame.image.load(Path + "background.png").convert_alpha()

ghost2 = pygame.image.load(Path + "ghost2.png").convert_alpha()
ghost1 = pygame.image.load(Path + "ghost1.png").convert_alpha()
ghost3 = pygame.image.load(Path + "bossghost.png").convert_alpha()

ghost_list = []
ghost_list2 = []
ghost_list3 = []

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 5000)

player_index = 0
player_speed = 5
player_x = 40
player_y = 250
is_jump = False
jump_len = 8
bg_x = 0
g = 0
s = 0

inscription = pygame.font.Font(Path + "RobotoMono-SemiBold.ttf", 40)
lose = inscription.render("You lose!", True, (193, 196, 199))
fire = inscription.render("FIRE", True, (196, 45, 116))
restart = inscription.render("Play again", True, (115, 132, 148))
restart_square = restart.get_rect(topleft=(180, 200))
joke = pygame.image.load(Path + "joke.png").convert_alpha()
joke2 = inscription.render("(((((((((", True, (115, 132, 148))

square = pygame.Surface((240, 90))
square.fill("Blue")

smile = pygame.image.load(Path + "smile.png").convert_alpha()
smiles = pygame.image.load(Path + "smiles.png").convert_alpha()

bullet = pygame.image.load(Path + "bullet.png").convert_alpha()
bullets = []
bullets_quantity = 3

sound = pygame.mixer.Sound(Path + "music.mp3")
sound2 = pygame.mixer.Sound(Path + "smeh.mp3")
sound3 = pygame.mixer.Sound(Path + "cric.mp3")
sound4 = pygame.mixer.Sound(Path + "ups.mp3")

BLACK = (0, 0, 0)
button_x, button_y = 405, 290
button_width, button_height = 80, 60
corner_radius = 15
button_image = pygame.image.load(Path + 'bullet.png').convert_alpha()


game_play = True
a = True

while a:
    pos = pygame.mouse.get_pos()
    screen.blit(foto, (bg_x, 0))
    screen.blit(foto, (bg_x + 618, 0))
    screen.blit(fire, (400, 315))
    draw_button(screen, button_x, button_y, button_width, button_height,  button_image, corner_radius)

    if game_play:
        player_square_rect = player_right[0].get_rect(topleft=(player_x, player_y))

        if ghost_list:
            for (i, el) in enumerate(ghost_list):
                screen.blit(ghost2, el)
                el.x -= 10

                if player_square_rect.colliderect(el):
                    sound4.play()
                    game_play = False
                    bullets_quantity = 3
                if el.x < -10:
                    ghost_list.pop(i)
        if ghost_list2:
            for (i, el) in enumerate(ghost_list2):
                screen.blit(ghost1, el)
                el.x -= 10

                if player_square_rect.colliderect(el):
                    sound4.play()
                    game_play = False
                    bullets_quantity = 3
                if el.x < -10:
                    ghost_list2.pop(i)
        if ghost_list3:
            for (i, el) in enumerate(ghost_list3):
                screen.blit(ghost3, el)
                el.x -= 10

                if player_square_rect.colliderect(el):
                    sound4.play()
                    game_play = False
                    bullets_quantity = 3
                if el.x < -10:
                    ghost_list3.pop(i)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            screen.blit(player_left[player_index], (player_x, player_y))
        else:
            screen.blit(player_right[player_index], (player_x, player_y))

        if keys[pygame.K_RIGHT] and player_x < 555:
            player_x += player_speed
        elif keys[pygame.K_d] and player_x < 555:
            player_x += player_speed
        elif keys[pygame.K_LEFT] and player_x > 5:
            player_x -= player_speed
        elif keys[pygame.K_a] and player_x > 5:
            player_x -= player_speed

        if not is_jump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
                is_jump = True
        else:
            if jump_len >= -8:
                if jump_len > 0:
                    player_y -= (jump_len ** 2) / 2
                else:
                    player_y += (jump_len ** 2) / 2
                jump_len -= 1
            else:
                is_jump = False
                jump_len = 8
        if is_jump is True and jump_len == 8:
            sound.play()

        if player_index == 3:
            player_index = 0
        else:
            player_index += 1

        bg_x -= 2
        if bg_x == -618:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4
                if el.x > 630:
                    bullets.pop(i)
                if ghost_list:
                    for (index, ghost_el) in enumerate(ghost_list):
                        if el.colliderect(ghost_el):
                            bullets.pop(i)
                            sound3.play()
                            ghost_list.pop(index)
                if ghost_list2:
                    for (index, ghost_el) in enumerate(ghost_list2):
                        if el.colliderect(ghost_el):
                            bullets.pop(i)
                            sound3.play()
                            ghost_list2.pop(index)
                if ghost_list3:
                    for (index, ghost_el) in enumerate(ghost_list3):
                        if el.colliderect(ghost_el):
                            bullets.pop(i)
                            sound3.play()
                            ghost_list3.pop(index)

    else:
        screen.fill((72, 12, 90))
        screen.blit(smile, (190, 120))
        screen.blit(smiles, (0, 0))
        screen.blit(smiles, (385, 118))
        screen.blit(joke, (0, 118))
        screen.blit(joke2, (385, 20))
        screen.blit(lose, (193, 100))
        screen.blit(square, (180, 200))
        screen.blit(restart, restart_square)
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if (restart_square.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]
                and pygame.KEYUP):
            game_play = True
            player_x = 50
            player_y = 250
            s = 0
            g = 0
            ghost_list.clear()
            ghost_list2.clear()
            ghost_list3.clear()
            bullets.clear()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list.append(ghost2.get_rect(topleft=(620, 250)))
            ghost_list2.append(ghost1.get_rect(topleft=(1000, 250)))
            g += 1
            s += 1
            if g == 3:
                ghost_list3.append(ghost3.get_rect(topleft=(820, 180)))
                g = 0
        if ((game_play and event.type == pygame.KEYUP and event.key == pygame.K_f
                or event.type == pygame.MOUSEBUTTONDOWN
                and is_clicked(pos, button_x, button_y, button_width, button_height)) and bullets_quantity > 0):
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
            bullets_quantity -= 1
            sound2.play()
        if (event.type == pygame.MOUSEBUTTONDOWN and
                not is_clicked(pos, button_x, button_y, button_width, button_height)):
            is_jump = True
            sound.play()

    if s < 5:
        clock.tick(16)
    elif s == 5:
        clock.tick(18)
    elif s == 10:
        clock.tick(20)
    elif s == 15:
        clock.tick(22)
    elif s == 20:
        clock.tick(24)
    elif s == 25:
        clock.tick(26)
    elif s == 30:
        clock.tick(28)
    elif s == 35:
        clock.tick(30)
