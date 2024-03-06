import pygame, random

pygame.init()

# display
display = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Monster Wrangler")

# set Fps , clock
fps = 60
clock = pygame.time.Clock()

font = pygame.font.Font("Abrushow.ttf", 24)


# Monster class
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, image_str, type):
        super().__init__()
        self.type = type
        self.image = pygame.image.load(image_str)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocityX = random.randint(1, 8) * random.choice([-1, 1])
        self.velocityY = random.randint(1, 8) * random.choice([-1, 1])

    def update(self):
        if self.rect.y > 540 or self.rect.y < 110:
            self.velocityY *= -1
        if self.rect.x > 1130 or self.rect.x < 5:
            self.velocityX *= -1

        self.rect.y += self.velocityY
        self.rect.x += self.velocityX


# Define Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, lives, warps):
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 8
        self.lives = lives
        self.warps = warps

    def update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.x < 1120:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.y > 115:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.y < 540:
            self.rect.y += self.velocity
        if keys[pygame.K_SPACE] and self.warps > 0 and 110 < self.rect.y < 540:
            self.warp()
            self.warps -= 1

    def warp(self):
        self.rect.center = (600, 650)


def game(round_number, lives_number, warps_number, score_number):
    colors_images = {"blue": ((11, 176, 236), "blue_monster.png"), "yellow": ((244, 167, 21), "yellow_monster.png"),
                     "green": ((83, 206, 56), "green_monster.png"), "purple": ((240, 94, 255), "purple_monster.png")}

    monster_group = pygame.sprite.Group()
    for t in colors_images:
        for k in range(round_number):
            monster = Monster(random.randint(300, 800), random.randint(200, 500), colors_images[t][1], t)
            monster_group.add(monster)

    player_group = pygame.sprite.Group()
    player = Player(600, 650,lives_number, warps_number)
    player_group.add(player)

    def choose_new_target():
        target_monster = random.choice(monster_group.sprites())
        return target_monster

    Targeted_Monster = choose_new_target()
    score = score_number
    # main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        color = colors_images[Targeted_Monster.type][0]
        imageTarget = Targeted_Monster.image
        collided_monster = pygame.sprite.spritecollideany(player, monster_group)

        if collided_monster:
            # Caught the correct monster
            if collided_monster.type == Targeted_Monster.type:
                score += 100 * round_number
                # Remove caught monster
                collided_monster.remove(monster_group)
                if not (monster_group):
                    game(round_number + 1,player.lives, player.warps, score)
                Targeted_Monster = choose_new_target()
            else:
                player.lives -= 1
                player.warp()
                if player.lives <= 0:
                    display.fill((0,0,0))
                    r = True
                    while r:
                        keys = pygame.key.get_pressed()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                r = False
                                run = False
                            if keys[pygame.K_SPACE]:
                                game(round_number=1, lives_number=5, warps_number=3, score_number=0)
                                r = False
                        display.fill((0, 0, 0))
                        GameOverText = font.render(f"Final Score {score}", True, (255, 255, 255))
                        GameOverText_rect = GameOverText.get_rect()
                        GameOverText_rect.center = (600, 350)
                        restaratText = font.render(f"Press Space to play again", True, (255, 255, 255))
                        restaratText_rect = restaratText.get_rect()
                        restaratText_rect.center = (600, 380)
                        display.blit(GameOverText, GameOverText_rect)
                        display.blit(restaratText, restaratText_rect)
                        pygame.display.update()
                        clock.tick(fps)

        # Fill the display
        display.fill((0, 0, 0))

        # define and blit Test
        scoreText = font.render(f"score {score}", True, (255, 255, 255))
        Score_rect = scoreText.get_rect()
        Score_rect.center = (65, 20)
        display.blit(scoreText, Score_rect)

        LivesText = font.render(f"Lives {player.lives}", True, (255, 255, 255))
        Lives_rect = LivesText.get_rect()
        Lives_rect.center = (65, 50)
        display.blit(LivesText, Lives_rect)

        roundText = font.render(f"Round {round_number}", True, (255, 255, 255))
        round_rect = roundText.get_rect()
        round_rect.center = (65, 80)
        display.blit(roundText, round_rect)

        warpsText = font.render(f"warps {player.warps}", True, (255, 255, 255))
        warps_rect = warpsText.get_rect()
        warps_rect.center = (1135, 50)
        display.blit(warpsText, warps_rect)

        catch_text = font.render("Current Catch", True, (255, 255, 255))
        catch_rect = catch_text.get_rect()
        catch_rect.center = (600, 20)
        display.blit(catch_text, catch_rect)

        player_group.update()
        player_group.draw(display)

        monster_group.update()
        monster_group.draw(display)

        pygame.draw.rect(display, color, pygame.Rect(5, 110, 1190, 500), 5)
        pygame.draw.rect(display, color, pygame.Rect(577, 35, 65, 65), 2)
        imageTarget_rect = imageTarget.get_rect()
        imageTarget_rect.center = (610, 67)
        display.blit(imageTarget, imageTarget_rect)
        # Update the display and tick the clock
        pygame.display.update()
        clock.tick(fps)


running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_SPACE]:
            game(round_number=1, lives_number=5, warps_number=3, score_number=0)
            running = False
    display.fill((0, 0, 0))
    TitleText = font.render("Monster wrangler", True, (255, 255, 255))
    TitleText_rect = TitleText.get_rect()
    TitleText_rect.center = (600, 350)
    staratText = font.render(f"Press Space to play", True, (255, 255, 255))
    staratText_rect = staratText.get_rect()
    staratText_rect.center = (600, 380)
    display.blit(TitleText, TitleText_rect)
    display.blit(staratText, staratText_rect)
    pygame.display.update()
    clock.tick(fps)
# End the game
pygame.quit()
