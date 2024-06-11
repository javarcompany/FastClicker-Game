import pygame
import time
from random import randint

pygame.init()
'''Creating the program winedow'''
main_window = pygame.display.set_mode((500,500))
background = (200, 255, 255)
main_window.fill(background)

clock = pygame.time.Clock()

class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = None):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def setColor(self, new_color):
        self.fill_color = new_color  #Change the rectangle color variable

    def drawRectangle(self):   # Fill Rectangle with Color
        pygame.draw.rect(main_window, self.fill_color, self.rectangle)

    def setOutline(self, frame_color, thickness): #Changes the outline Color
        pygame.draw.rect(main_window, frame_color, self.rectangle, thickness)

    def collidePoint(self, x, y):
        return self.rectangle.collidepoint(x, y)
    

class Label(Area):
    def setText(self, text, font_size =12, textColor = (0, 0, 0)):  #Sets the Text
        self.text = pygame.font.SysFont("Verdana", font_size).render(text, True, textColor)

    def drawRect_Label(self,  shift_x = 0, shift_y = 0): #Draws the text area
        self.drawRectangle()
        main_window.blit(self.text, (self.rectangle.x + shift_x,  self.rectangle.y + shift_y ))

points = 0
number_of_cards = 4
cards = []
x_position = 70
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
DARK_BLUE = (0, 0, 100)
startTime = time.time()
currentTime = startTime

for card in range(number_of_cards):
    new_card = Label(x = x_position, y = 170, width = 70, height = 100, color = YELLOW)
    new_card.setOutline(BLUE, 10)
    new_card.setText("CLICK", 26)
    cards.append(new_card)
    x_position += 100

wait = 0

# GAME INTERFACE
time_text = Label(0, 0, 50, 50, background)
time_text.setText("Time: ", 40, DARK_BLUE)
time_text.drawRect_Label(20, 20)

timer = Label(50, 55, 50, 40, background)
timer.setText('0', 40, DARK_BLUE)
timer.drawRect_Label(0, 0)

score_text = Label(380, 0, 50, 50, background)
score_text.setText("Score: ", 45, DARK_BLUE)
score_text.drawRect_Label(20, 20)

score = Label(430, 55, 50, 40, background)
score.setText('0', 40, DARK_BLUE)
score.drawRect_Label(0, 0)

while True:
    if wait == 0:
        #TRansfer the Label
        wait = 20 
        click = randint(1, number_of_cards)
        for position_card in range(number_of_cards):
            cards[position_card].setColor(YELLOW)
            if (position_card + 1) == click:
                cards[position_card].drawRect_Label(10, 40)
            else:
                cards[position_card].drawRectangle()        
    else:
        wait -= 1

    #Handling Click Events on the Cards
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(number_of_cards):
                if cards[i].collidePoint(x, y):
                    if i + 1 == click:
                        cards[i].setColor(GREEN)
                        points += 1
                    else:
                        cards[i].setColor(RED)
                        points -= 1

                    cards[i].drawRectangle()
                    score.setText(str(points), 40, DARK_BLUE)
                    score.drawRect_Label(0, 0)
    
    #winning & LOSING
    newTime = time.time()

    #Time is Up Condition
    if newTime - startTime >= 11:
        win = Label(0, 0, 500, 500, RED)
        win.setText("Time is Up!!!", 60, DARK_BLUE)
        win.drawRect_Label(110, 180)
        break

    if int(newTime) - int(currentTime) == 1:
        timer.setText(str(int(newTime) - int(startTime)), 40, DARK_BLUE)
        timer.drawRect_Label(0, 0)
        currentTime = newTime

    if points >= 2:
        win  = Label(0, 0, 500, 500, GREEN)
        win.setText("YOU WIN !!!!!", 60, DARK_BLUE)
        win.drawRect_Label(140, 180)
        break

    pygame.display.update()
    clock.tick(40)

pygame.display.update()