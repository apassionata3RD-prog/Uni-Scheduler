import pygame
import time

gesammelteLP = 0

class modules:
    def __init__(self, name, x, y, width, height, r, g, b, LP, textName, size, bold, italic, r2, g2, b2, text, antialias, pos_X, pos_Y):
        # Attribute für das Rechteck
        self._name = name
        self._rect = pygame.Rect(x, y, width, height)
        self._color = (r, g, b)
        self._LP = LP
        self._posRect = (x,y)
        self._color = (r2, g2, b2)
        self._text = text
        self._antialias = antialias
        self._pos = (pos_X, pos_Y)
        self._font = pygame.font.SysFont(textName, size, bold, italic)
        self._isVisible = True
        self._clickHolding = False
      
        #Funktionen für die Module/Rechtecke
    def getName(self):
        return self._name
    def getSize(self):
        return self._rect
    def getColor(self):
        return self._color
    def getPoints(self):
        return self._points
    def getTextName(self):
        return self._text
    def getColorText(self):
        return self._color
    def getText(self):
        return self._text
    def getAntialias(self):
        return self._antialias
    def getPos(self):
        return self._pos
    

    def createFont(self, screen):
        text = self._font.render(self._text, self._antialias, self._color)
        screen.blit(text, (self._pos))

    def addPoints(self):
        global gesammelteLP
        gesammelteLP = gesammelteLP + self._LP
        print("Points given")

    def subtractPoints(self):
        global gesammelteLP
        gesammelteLP = gesammelteLP - self._LP

    def drawRect(self, screen):
        clicked = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        # Wenn auf ein Button geklickt wird führe Aktivität aus
        if clicked and self._isVisible == True and self._rect.collidepoint(mouse_pos) and self._clickHolding == False:
            self._clickHolding = True
            self._font = pygame.font.SysFont("arial", 25, bold=True, italic=False)
            self._isVisible = False
            modules.addPoints(self)
        
            # Wenn Button nicht mehr verfügbar, werde Grau und unclickable
        if not self._isVisible:
            pygame.draw.rect(screen, (196, 196, 196), self._rect, border_radius=20)
            if clicked and self._rect.collidepoint(mouse_pos) and self._clickHolding == False:
                self._clickHolding = True
                self._isVisible = True
                modules.subtractPoints(self)
        
        # Wenn Maus über Button verändere Farbe für schöner
        if self._rect.collidepoint(mouse_pos) and self._isVisible:
            pygame.draw.rect(screen, (36, 81, 171), self._rect, border_radius=20)

            # Male Rechteck
        elif self._isVisible:
            pygame.draw.rect(screen, (50, 112, 234), self._rect, border_radius=20)
        text = self._font.render(self._text, self._antialias, self._color)
        text_rect = text.get_rect()
        text_rect.center = self._rect.center
        screen.blit(text, (text_rect))

        # Direkt auf false setzen wenn Maus nicht mehr geklickt
        if not clicked:
            self._clickHolding = False

    


def setStartingWindow():
    pygame.init()
    pygame.font.init()
    punkteStand = pygame.font.SysFont("arial", 30, bold=True, italic=False)
    screen = pygame.display.set_mode((1000, 500))
    Alpro = modules("AlPro", 100, 100, 150, 50, 50, 112, 234, 9, "arial", 30, True, False, 0,0,0, "AlPro", True, 100, 20)
    ItSicherheit = modules("It-Sicherheit", 260, 100, 150, 50, 112, 234, 9, 9, "arial", 25, True, False, 0,0,0, "IT-Sicherheit", True, 500, 20)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        points = punkteStand.render(f"Aktuell gesammelte LP: {gesammelteLP}", True, (255,255,255))
        screen.fill((0, 0, 0))
        Alpro.drawRect(screen)
        ItSicherheit.drawRect(screen)
        screen.blit(points, (500, 400))



        pygame.display.flip()
setStartingWindow()

