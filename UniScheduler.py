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
                self.buttonClicked(self, screen)
            self._isClicked = mouseClick
        else:
            self._isClicked = False
        
                
        
            

                 

        screen.blit(buttonText, text_in_button)

    # When a certain button is clicked, the correct method should be executed
    def buttonClicked(self, clicked_button, screen): 
            global in_menu, in_pflichtmodule, buttons, lp, lp_in_prozent, in_wahlpflicht_cyber, in_wahlpflicht_info, in_wahlpflicht_info2
            # all if conditions for buttons shown in menu
            if in_menu:
                if clicked_button == pflichtmodule:
                    in_menu = False
                    in_pflichtmodule = True
                    menuPflichtmodule(screen)
                if clicked_button == wahlpflicht_cyber:
                    in_menu = False
                    in_wahlpflicht_cyber = True
                    menuWahlpflichtCyber(screen)
                    
                if clicked_button == wahlpflicht_info:
                    in_menu = False
                    in_wahlpflicht_info = True
                    menuWahlpflichtInfo(screen)
            #   if ...
            # all if conditions for buttons shown in pflichtmodule
            if in_pflichtmodule:
                if clicked_button == back: # back button
                    in_menu = True
                    in_pflichtmodule = False
                for button in buttons.values():
                    if clicked_button == button and not button._isSelected:
                        button._isSelected = True
                        button._color = (255,0,0)   # sums the points in percent and in integer
                        lp = lp + button._LP
                        lp_in_prozent = (lp / 180) * 100
                    elif clicked_button == button and button._isSelected:
                        button._isSelected = False
                        button._color = (255,255,255)               # subtracts the points in percent and in integer
                        lp = lp - button._LP
                        lp_in_prozent = (lp / 180) * 100
            if in_wahlpflicht_cyber:
                if clicked_button == back: # back button
                    in_menu = True
                    in_wahlpflicht_cyber = False
                for button in buttons2.values():
                    if clicked_button == button and not button._isSelected:
                        button._isSelected = True
                        button._color = (255,0,0)   # sums the points in percent and in integer
                        lp = lp + button._LP
                        lp_in_prozent = (lp / 180) * 100
                    elif clicked_button == button and button._isSelected:
                        button._isSelected = False
                        button._color = (255,255,255)               # subtracts the points in percent and in integer
                        lp = lp - button._LP
                        lp_in_prozent = (lp / 180) * 100
            if in_wahlpflicht_info:
                if clicked_button == back: # back button
                    in_menu = True
                    in_wahlpflicht_info = False
                if clicked_button == nextpage:
                    in_wahlpflicht_info2 = True
                    in_wahlpflicht_info = False
                    menuWahlpflichtInfo2(screen)
                for button in buttons3.values():
                    if clicked_button == button and not button._isSelected:
                        button._isSelected = True
                        button._color = (255,0,0)   # sums the points in percent and in integer
                        lp = lp + button._LP
                        lp_in_prozent = (lp / 180) * 100
                    elif clicked_button == button and button._isSelected:
                        button._isSelected = False
                        button._color = (255,255,255)               # subtracts the points in percent and in integer
                        lp = lp - button._LP
                        lp_in_prozent = (lp / 180) * 100
            if in_wahlpflicht_info2:
                if clicked_button == back: # back button
                    in_menu = True
                    in_wahlpflicht_info2 = False
                if clicked_button == prevpage:
                    in_wahlpflicht_info = True
                    in_wahlpflicht_info2 = False
                for button in buttons4.values():
                    if clicked_button == button and not button._isSelected:
                        button._isSelected = True
                        button._color = (255,0,0)   # sums the points in percent and in integer
                        lp = lp + button._LP
                        lp_in_prozent = (lp / 180) * 100
                    elif clicked_button == button and button._isSelected:
                        button._isSelected = False
                        button._color = (255,255,255)               # subtracts the points in percent and in integer
                        lp = lp - button._LP
                        lp_in_prozent = (lp / 180) * 100
                
                        
def menuWahlpflichtInfo2(screen):
    if in_wahlpflicht_info2:
        gesammelte_lp = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
        gesammelte_lp = gesammelte_lp.render(f"Gesammelte LP in Punkten: {lp} von 180", True, (255,255,255))
        lp_prozent = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) 
        lp_prozent = lp_prozent.render(f"Gesammelte LP in Prozent: {round(lp_in_prozent)}% von 100%", True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(gesammelte_lp, (0,0))
        screen.blit(lp_prozent, (0,50))

        # Creating Buttons for every Button
        for button in buttons4.values():
            button.drawButton(screen)
        back.drawButton(screen)
        prevpage.drawButton(screen)


def menuWahlpflichtInfo(screen):
    if in_wahlpflicht_info:
        gesammelte_lp = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
        gesammelte_lp = gesammelte_lp.render(f"Gesammelte LP in Punkten: {lp} von 180", True, (255,255,255))
        lp_prozent = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) 
        lp_prozent = lp_prozent.render(f"Gesammelte LP in Prozent: {round(lp_in_prozent)}% von 100%", True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(gesammelte_lp, (0,0))
        screen.blit(lp_prozent, (0,50))

        # Creating Buttons for every Button
        for button in buttons3.values():
            button.drawButton(screen)
        back.drawButton(screen)
        nextpage.drawButton(screen)
            
                 
        # Function that executes when in pflichtmodule 
def menuPflichtmodule(screen):
    if in_pflichtmodule:
        gesammelte_lp = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
        gesammelte_lp = gesammelte_lp.render(f"Gesammelte LP in Punkten: {lp} von 180", True, (255,255,255))
        lp_prozent = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) 
        lp_prozent = lp_prozent.render(f"Gesammelte LP in Prozent: {round(lp_in_prozent)}% von 100%", True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(gesammelte_lp, (0,0))
        screen.blit(lp_prozent, (0,50))

        # Creating Buttons for every Button
        for button in buttons.values():
            button.drawButton(screen)
        back.drawButton(screen)

# FUnction that executes when in Wahlpflicht Cyber
def menuWahlpflichtCyber(screen):
    if in_wahlpflicht_cyber:
        gesammelte_lp = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
        gesammelte_lp = gesammelte_lp.render(f"Gesammelte LP in Punkten: {lp} von 180", True, (255,255,255))
        lp_prozent = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) 
        lp_prozent = lp_prozent.render(f"Gesammelte LP in Prozent: {round(lp_in_prozent)}% von 100%", True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(gesammelte_lp, (0,0))
        screen.blit(lp_prozent, (0,50))

        for button in buttons2.values():
            button.drawButton(screen)
        back.drawButton(screen)
        
        
        
         
        



def menu(screen): 
    screen.fill((0,0,0))
    gesammelte_lp = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
    gesammelte_lp = gesammelte_lp.render(f"Gesammelte LP in Punkten: {lp} von 180", True, (255,255,255))
    lp_prozent = pygame.font.SysFont("PressStart2P-Regular.ttf", 40, bold=True, italic=False) # collected points
    lp_prozent = lp_prozent.render(f"Gesammelte LP in Prozent: {round(lp_in_prozent)}% von 100%", True, (255,255,255))
    screen.blit(gesammelte_lp, (0,0))
    screen.blit(lp_prozent, (0,50))
    background = pygame.image.load("hintergrund.png")
    background = pygame.transform.scale(background, (1000,700))
    pflichtmodule.drawButton(screen)
    wahlpflicht_info.drawButton(screen)
    wahlpflicht_cyber.drawButton(screen)
    wahlpflicht_nichtFach.drawButton(screen)
    screen.blit(background,(0,0))

    


# Building the menu
pygame.font.init()
x_space = 250
y_space = 100
start_x = 0
start_y = 100
lp = 0
lp_in_prozent = 0
in_menu = True
in_pflichtmodule = False
in_wahlpflicht_cyber = False
in_wahlpflicht_info = False
in_wahlpflicht_info2 = False
back = Buttons(0, 650, 255,0,0, 0, "Back to menu")
nextpage = Buttons(970, 650, 255, 0, 0, 0, "->")
prevpage = Buttons(900, 650, 255, 0, 0, 0, "<-")
buttons = {} # Dictionary for access on buttons pflichtmodule
buttons2 = {} # Dictionary for access on buttons wahlpflicht_cyber
buttons3 = {} # Dictionary for access on buttons wahlpflicht_info
buttons4 = {} # Dictionary for access on buttons wahlpflicht_info2
wahlpflicht_cyber_module = [("ReSi", 6), ("MCI", 6), ("Netzi", 6), ("ModKrypt", 6), ("ABA", 6), ("Forensik", 6), ("Datenanalyse", 6), ("K. Kryptographie", 6)]
for i, (name, points) in enumerate(wahlpflicht_cyber_module):
     x_pos = start_x + (i % 4) * x_space  # After appending 5 times x pos changes one line beyond
     y_pos = start_y + (i // 4) * y_space  # After appending 5 times y pos changes one line beyond

     button = Buttons(x_pos, y_pos, 255, 255, 255, points, name)
        
     buttons2[name] = button
x_space = 320
wahlpflicht_info_module1 = [("TI", 9), ("LA", 9), ("Analysis", 9), ("Softwaretech.", 6), ("Algo II", 6), ("approx Algo", 9), ("Computergraphik", 9), ("Lin. Optimierung", 9),
                           ("Diskret Mathe", 9), ("Maschinelle Gesch. I", 6), ("Rela Datenbanken", 6), ("Grundlagen KI", 9), ("Algo Geometrie", 9), ("C. Intelligence", 6), 
                           ("Maschinelle Gesch. II", 6), ("Numerik", 6), ("Intell. Sehsysteme", 6), ("Grundlagen Robotik", 6)]

# For loop for buttons to be created gets help by the list
for i, (name, points) in enumerate(wahlpflicht_info_module1):
    x_pos = start_x + (i % 3) * x_space  # After appending 5 times x pos changes one line beyond
    y_pos = start_y + (i // 3) * y_space  # After appending 5 times y pos changes one line beyond

    button = Buttons(x_pos, y_pos, 255, 255, 255, points, name)
        
    buttons3[name] = button
x_space = 340
y_space = 100
start_x = 0
start_y = 100
wahlpflicht_info_module2 = [("Sensordatenfusion", 6), ("Tutorenschulung", 6), ("Algo Grundlagen", 9), ("Graphenalforithmen", 6), ("Data Science", 6), ("Deep learning", 6),
                            ("Bildanalyse", 6), ("Machine Learning", 6), ("Software Dev", 6), ("Grundlagen KI 2", 6), ("Webtechnologien", 6)]

for i, (name, points) in enumerate(wahlpflicht_info_module2):
    x_pos = start_x + (i % 3) * x_space  # After appending 5 times x pos changes one line beyond
    y_pos = start_y + (i // 3) * y_space  # After appending 5 times y pos changes one line beyond

    button = Buttons(x_pos, y_pos, 255, 255, 255, points, name)
        
    buttons4[name] = button

x_space = 250
y_space = 100
start_x = 0
start_y = 100
pflichtmodule_module = [("LudS", 9), ("TdwA", 4), ("AlPro", 9), ("Grund. Mathe", 9), ("SysInf", 6), ("POSe", 6), ("Algo I", 9), ("SysProg", 6), ("DzI", 6), ("PG", 9), ("Praktikum", 9),
                        ("Bachelorarbeit", 12), ("Begleitseminar", 2), ("KiVS", 6), ("Stocha", 6), ("ITSi", 9), ("USaP", 9)]
# For loop for buttons to be created gets help by the list
for i, (name, points) in enumerate(pflichtmodule_module):
    x_pos = start_x + (i % 4) * x_space  # After appending 5 times x pos changes one line beyond
    y_pos = start_y + (i // 4) * y_space  # After appending 5 times y pos changes one line beyond

    button = Buttons(x_pos, y_pos, 255, 255, 255, points, name)
        
    buttons[name] = button

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
    
    if in_menu:
        menu(screen)
    elif in_pflichtmodule:
        menuPflichtmodule(screen)
    elif in_wahlpflicht_cyber:
        menuWahlpflichtCyber(screen)
    elif in_wahlpflicht_info:
        menuWahlpflichtInfo(screen)
    elif in_wahlpflicht_info2:
        menuWahlpflichtInfo2(screen)
    timer.tick(fps)

    pygame.display.flip()