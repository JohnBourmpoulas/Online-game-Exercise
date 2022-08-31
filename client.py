import pygame

# Here we define the frame size and the title of the window.
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# we use 0 as number of clients for now, we will update it on later updates.
clientsNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
    
    # With this function we draw the player on the window.
    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()     # keys that had pressed to update the position of the character
        
        # The keys LEFT, RIGHT, UP, DOWN used to control the character.
        if keys[pygame.K_LEFT]:             
            self.x -= self.vel
            
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            
        if keys[pygame.K_UP]:
            self.y -= self.vel
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        
        self.rect = (self.x, self.y, self.width, self.height)   # Here we pass the changed character position each time we press the buttons we define.

def redrawWindow(win,player):
    win.fill((255,255,255)) # Color for window RGB.
    player.draw(win)        # Display player in window.
    pygame.display.update() # Update and display changes. 
    
    
def main():
    run = True                              # The game starts here.
    p = Player(50,50,100,100,(0,255,0))     # The player takes position on the frame with x,y, width,height and we give him color with RGB.
    clock = pygame.time.Clock()             
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():    # In this for loop we control if we want to stop the game while it runs.
            if event.type == pygame.QUIT:
                run = False 
                pygame.quit()
                
        p.move()                            # Here use the move() function to control the movement of the character.
        redrawWindow(win,p)                 # Here we call the functions to start display window and player.
                
main()                                      # Calling main() function to start the game.
