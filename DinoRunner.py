# created by Spounka

import pygame as pg
import Scripts.Colors as Col
import Scripts.Dino as Dino
import Scripts.Cactus as Cactus
import Scripts.Vector2 as Vc2
import sys, random

pg.init()   # initialize The pygame module.

clock = pg.time.Clock()     # The Clock object

pg.display.set_caption("Dino Runner")   # The Game's Title.
screenSize = screenWidth, screenHeight = 500, 500
screen = pg.display.set_mode(screenSize)    # sets the screen's size.

GameOver = False    # Bool for checking if the game is over or not.
isPaused = False

floorHeight = 70

wm = pg.display.Info()      # Get The current info about the window
currentSize = currentHeight, currentWidth = wm.current_h, wm.current_w

dinoSize = dinoWidth,dinoHeight = 40,40     # The player's size.

startGravity = GRAVITY = 7      # The Gravity factor
startJumpForce = jumpForce = 150    # The Force used for jumping


dinoObject = Dino.Player(dinoWidth,dinoHeight,"Assets/Pictures/Dino.png",clock)     # initializing the player.
dino = dinoObject.player    # reference to the player's image.


# Player's Vector.
playerPos = Vc2.Vector2(dinoWidth, currentHeight - floorHeight - dinoHeight)

# Sources for the trees images
cactSource = ["Assets/Pictures/Cactus 1.png", "Assets/Pictures/Cactus 2.png"]
cactIndex = 0

cact = list()   # a list of all the current cactuses in the game.

cact.append(Cactus.Cactus(currentWidth, currentHeight - floorHeight - 35, 35, 35, cactSource,cactIndex))

spawnTimer = 0  # used for interval for the cactus spawning
startScore = Score = 1  # The Game's Score.

scoreFont = pg.font.Font("Assets/Fonts/BlitzkriegNF.ttf", 30)   # Loading The Font.

dinoObject.playerPos = playerPos    # Initializing the player's position
startSpeed = gameSpeed = 5      # The Current Game's Speed.

displayText = ""


# Function For Randomising time of spawning.
def Randtime():
    if gameSpeed < 15:
        randtime = random.uniform(1.4, 1.7)

    else:
        if gameSpeed < 25:
            randtime = random.uniform(1, 1.3)
        else:
            randtime = random.uniform(0.7, 1)
    return randtime


# Function To spawn random Cactus
def RandomCact():
    if gameSpeed <= 12:
        index = 0
    else:
        index = random.randint(0, len(cactSource) - 1)
    return index


rand = Randtime()


# The Game's MainLoop.
while True:

    # The Game's FPS
    clock.tick(60)

    # Getting The Cactus Index
    cactIndex = RandomCact()

    if not isPaused:
        # A loop to check for events.
        for event in pg.event.get():
            if event.type == pg.QUIT: pg.quit(); sys.exit()  # if the user presses the exit button.
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_SPACE or event.key == pg.K_UP) and not GameOver:
                    dinoObject.jump(jumpForce, GRAVITY)

                # Restart The Game if User Presses ESC
                elif (event.key == pg.K_ESCAPE) and (GameOver is True):
                    jumpForce = startJumpForce
                    GRAVITY = startGravity
                    Score = startScore
                    gameSpeed = startSpeed
                    GameOver = False
                    displayText = ""
                    cact.clear()
                elif event.key == pg.K_RETURN and not isPaused and not GameOver:
                    isPaused = True
                    displayText = "Paused."

            # Bring The player down in case of jumping then holding down button.
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN and not dinoObject.isGrounded:
                    dinoObject.velocity = 0
                    dinoObject.velocity -= GRAVITY * 20


        screen.fill(Col.Grey)   # Colors the window's background.

        currentSize = currentHeight, currentWidth = wm.current_h, wm.current_w	# Getting Window Height/Width each Frame in case of resize

        # Drawing The Ground.
        ground = pg.draw.rect(screen, Col.Black, [0, currentHeight - floorHeight, currentWidth, floorHeight])

        # Logic For Spawning Cactus and getting The Time.
        if spawnTimer <= rand and not GameOver and int(Score) > 20:

            spawnTimer += clock.get_time() / 1000

        elif spawnTimer > rand and not GameOver and len(cact) < 3:
            cact.append(Cactus.Cactus(currentWidth, currentHeight - floorHeight - 35,
                        35, 35, cactSource,cactIndex))

            spawnTimer = 0
            rand = Randtime()

        screen.blit(dino,(playerPos.x, playerPos.y))     # Draws The Player.

        # Checks if the player is touching the ground.
        if ground.colliderect(dinoObject.collider):
            dinoObject.playerPos.y = currentHeight - ground.h - dinoHeight
            dinoObject.isGrounded = True

        # Checks if the player is not grounded.
        elif not ground.colliderect(dinoObject.collider) and not GameOver:
            dinoObject.isGrounded = False
            dinoObject.velocity -= GRAVITY
            dinoObject.playerPos.y -= dinoObject.velocity / dinoObject.clock.get_time()
            dinoObject.getCollider()


        if not GameOver:
            # Increment Score in case GameOver is False.
            Score += int((gameSpeed / clock.get_time()) / 10)
            scoreText = scoreFont.render(str(Score), True, Col.Black)

            dinoObject.getCollider()

        screen.blit(scoreText, (currentWidth / 2, 0))   # Draws the Score Text on Screen.

        for c in cact:

            if int(Score) > 20 and (not GameOver):
                c.moveCact(gameSpeed * 2)

            if c.collider.colliderect(dinoObject.collider):
                GameOver = True

            c.getCollider()
            screen.blit(c.cactImg, (c.xPos, c.yPos))

        try:
            if cact[0].xPos <= -cact[0].cactImg.get_width():
                del cact[0]
        except IndexError:
            pass

        gameOverText = scoreFont.render(displayText, True, Col.Black)

        if GameOver is True:
            displayText = "Game Over"

        screen.blit(gameOverText, (currentWidth / 2 - gameOverText.get_width() / 2,
                                   currentHeight / 2 - gameOverText.get_height() / 2))

        if not GameOver: gameSpeed += 1 / (clock.get_time() * 10)
        GRAVITY += 1/(200 * clock.get_time())
        jumpForce += 1 / (200 * clock.get_time())

    if isPaused:
        for event in pg.event.get():
            if event.type == pg.QUIT: pg.quit(); sys.exit()  # if the user presses the exit button.
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    isPaused = False
                    displayText = ""
    pg.display.flip()   # The Update Function.

