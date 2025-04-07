import pygame
# Class for buttons

class Buttons:
    def __init__(self, x, y, r, g, b, LP, text):                                                         # Höhe des Buttons 
        self._color = (r,g,b)                                                         # Farbe des Buttons
        self._pos = (x,y)                
        self._LP = LP                                            
        self._text = text
        self._isClicked = False
        self._hoverColor = (0,0,139)
        self._isClickedColor = (0,0,100)
        self._font = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False)
        self._rendered_text = self._font.render(self._text, True, (0, 0, 0))
        self._width = self._rendered_text.get_width()                                                           # Breite des Buttons
        self._height = 50
        self._form = pygame.Rect(x, y, self._width, self._height)                     # Erschienungsform des Buttons
        self._isSelected = False
        
    def drawButton(self, screen):
        # Building the Button 
        buttonText = self._font
        buttonText = self._rendered_text
        pygame.draw.rect(screen, self._color, self._form, width=0)
        text_in_button = buttonText.get_rect(center=self._form.center)
      

        # implementing Button logic
        mouse_pos = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()[0]
        if self._form.collidepoint(mouse_pos): # Checks whether mouse is on button or not
            pygame.draw.rect(screen, self._hoverColor, self._form, width=0)
            if mouseClick and not self._isClicked: 
                self._isClicked = True
                pygame.draw.rect(screen, self._isClickedColor, self._form, width=0)
                self.buttonClicked(self)
            self._isClicked = mouseClick
        else:
            self._isClicked = False
                 

        screen.blit(buttonText, text_in_button)

    # When a certain button is clicked, the correct method should be executed
    def buttonClicked(self, clicked_button): 
            if clicked_button == pflichtmodule:
                 global in_menu
                 in_menu = False
                 global in_pflichtmodule
                 in_pflichtmodule = True
                 menuPflichtmodule(screen)
            
                 
        # Function that executes when in pflichtmodule 
def menuPflichtmodule(screen):
    if in_pflichtmodule:
        gesammelte_lp = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
        gesammelte_lp = gesammelte_lp.render(f"Gesammelte LP in Punkten: {lp} von 180", True, (255,255,255))
        lp_prozent = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) 
        lp_prozent = lp_prozent.render(f"Gesammelte LP in Prozent: {lp / 180 * 100}% von 100%", True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(gesammelte_lp, (0,0))
        screen.blit(lp_prozent, (0,50))

        # Creating Buttons for every Button
        back = Buttons(0, 650, 255,0,0, 9, "Back to menu")
        back.drawButton(screen)
         
        



def menu(screen): 
    background = pygame.image.load("hintergrund.png")
    background = pygame.transform.scale(background, (1000,700))
    pflichtmodule.drawButton(screen)
    wahlpflicht_info.drawButton(screen)
    wahlpflicht_cyber.drawButton(screen)
    wahlpflicht_nichtFach.drawButton(screen)
    screen.blit(background,(0,0))

    


# Building the menu
pygame.font.init()
lp = 0
lp_in_prozent = 0.0
in_menu = True
in_pflichtmodule = False
pflichtmodule = Buttons(0, 150, 255,255,255, 0, "Pflichtmodule")
wahlpflicht_info = Buttons(0, 350, 255,255,255, 0, "Wahlpflicht Informatik")
wahlpflicht_cyber = Buttons(0, 250, 255,255,255, 0, "Wahlpflicht Cyber Security")
wahlpflicht_nichtFach = Buttons(0, 450, 255,255,255, 0, "Nicht fachgebundener Bereich")
running = True
pygame.init()
timer = pygame.time.Clock()
fps = 60
pygame.display.set_caption("Uni Scheduler")
screen = pygame.display.set_mode((1000, 700))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    gesammelte_lp = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
    gesammelte_lp = gesammelte_lp.render(f"Gesammelte LP in Punkten: {lp} von 180", True, (255,255,255))
    lp_prozent = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
    lp_prozent = lp_prozent.render(f"Gesammelte LP in Prozent: {lp / 180 * 100}% von 100%", True, (255,255,255))
    screen.blit(gesammelte_lp, (0,0))
    screen.blit(lp_prozent, (0,50))
    if in_menu:
        menu(screen)
    elif in_pflichtmodule:
        menuPflichtmodule(screen)
    timer.tick(fps)

    pygame.display.flip()