import pygame, sys
import random
#change
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

width = 1000
height = 500

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.SRCALPHA)
done = False


pygame.key.set_repeat(1, 1)

backdrop = pygame.image.load('backdrop.jpg')
fill_bg = pygame.transform.scale(backdrop, (width, height))

x = 30
y = 30
box_width = 100
box_height = 100
enemy_box = 50
boss_box = 100
                

class Hero(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("leia2.png").convert_alpha()

        
 
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x = x
        self.rect.y = y        
                

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("phasma.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (enemy_box, enemy_box))
 
        self.rect = self.image.get_rect()

    def update(self):
        moved = True
        if moved:
            up_down = random.randint(1,2)
            if up_down == 1:
                self.rect.y += 3
                if self.rect.y >=height-box_height:  self.rect.y=height-box_height
            else:
                self.rect.y -=3
                if self.rect.y <=0: self.rect.y=0
            moved = False
            pygame.time.set_timer(enemies_move, 2000)

class Darth(pygame.sprite.Sprite):
        def __init__(self):
        
            super().__init__()
            
            self.image = pygame.image.load("darth.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (boss_box, boss_box))
            
            self.rect = self.image.get_rect()

        
class Hero_shot(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([10, 4])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x += 10

class Enemy_shot(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([10, 4])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x -= 5        
        
class boss_shot(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.image.load("saber_r.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x -= 5

# This is a list of every sprite. All enemies, the player and shots as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each enemy in the game
enemy_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()

#bosses
boss_list = pygame.sprite.Group()


#Hero_location
hero_location = pygame.sprite.Group()

# --- Create the sprites

def generate_boss(Darth):
    darth = Darth()
    darth.rect.x = width-enemy_row1
    darth.rect.y = ((height/2)-boss_box)       
    enemy_list.add(darth)
    all_sprites_list.add(darth)

def generate_enemies(Enemy):
    if wave ==2 or wave ==4:
        darth = Darth()
        darth.rect.x = width-enemy_row1
        darth.rect.y = ((height/2)-boss_box)       
        enemy_list.add(darth)
        all_sprites_list.add(darth)   
        boss_list.add(darth)
    
    for i in range(int(wave)):
    
        enemy = Enemy()
     
        # Set a random location for the enemy
        enemy.rect.x = width-enemy_row2
        enemy.rect.y = random.randrange(height-100)
     
        # Add the enemy to the list of objects
        enemy_list.add(enemy)
        all_sprites_list.add(enemy)
 
# Create a  player 
player = Hero()
hero_location.add(player)
all_sprites_list.add(player)

enemy_row1 = 100
enemy_row2 = 200

#event timers
enemies_move = pygame.USEREVENT + 1
hero_reload = pygame.USEREVENT + 2
new_enemies  = pygame.USEREVENT + 3
enemies_shoot = pygame.USEREVENT + 4
boss_shoot = pygame.USEREVENT + 5

pygame.time.set_timer(enemies_shoot, 2000)
pygame.time.set_timer(hero_reload, 450)
pygame.time.set_timer(enemies_move, 2000)
pygame.time.set_timer(boss_shoot, 3000)

        
pygame.mixer.music.load('starwarstheme.mid')
pygame.mixer.music.play()    

direction = 'down'
troopery = 100

wave = 1
score = 0
health = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q or event.key == pygame.K_x):
            pygame.QUIT
            print ("Thanks for playing!")
            done = True
        elif event.type == hero_reload:
            reloaded = True
            pygame.time.set_timer(hero_reload, 0)
        elif event.type == enemies_move:
            moved = True
            pygame.time.set_timer(enemies_move, 0)

        
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: y -= 3
            if y <=0: y=0
            if pressed[pygame.K_DOWN]: y += 3
            if y >=height-box_height: y=height-box_height
            if pressed[pygame.K_LEFT]: x -= 3
            if x <=0: x=0
            if pressed[pygame.K_RIGHT]: x += 3
            if x >=200: x=200
            if pressed[pygame.K_SPACE]:
                if reloaded: 
                    shoot = Hero_shot()
                    shoot.rect.x = player.rect.x+90
                    shoot.rect.y = player.rect.y+49
                    # Add the bullet to the lists
                    all_sprites_list.add(shoot)
                    bullet_list.add(shoot) 
                    #add delay
                    reloaded = False
                    pygame.time.set_timer(hero_reload, 450)

        
        elif event.type == enemies_shoot:
            for enemy in enemy_list:
                shoote = Enemy_shot()
                shoote.rect.x = enemy.rect.x-20
                shoote.rect.y = enemy.rect.y+20
                # Add the bullet to the lists
                all_sprites_list.add(shoote)
                bullet_list.add(shoote)  
        elif event.type == boss_shoot:
            for boss in boss_list:        
                shootb = boss_shot()
                shootb.rect.x = boss.rect.x-200
                shootb.rect.y = boss.rect.y+40
                # Add the bullet to the lists
                all_sprites_list.add(shoote)
                bullet_list.add(shoote)                 
                    
    all_sprites_list.update() 
    if len(enemy_list)==0:
        generate_enemies(Enemy) 
        wave += 1

    
        
      
    for shoote in bullet_list:
        hero_hit_list = pygame.sprite.spritecollide(shoote, hero_location, True)
        
        for player in hero_hit_list:
            bullet_list.remove(shoote)
            all_sprites_list.remove(shoote)
       
        
        if shoote.rect.x < 0:
            bullet_list.remove(shoote)
            all_sprites_list.remove(shoote)         
            
                
# Calculate mechanics for each bullet
    for shoot in bullet_list:
 
        # See if it hit a enemy
        enemy_hit_list = pygame.sprite.spritecollide(shoot, enemy_list, True)
             
            
        # For each enemy hit, remove the bullet and add to the score
        for enemy in enemy_hit_list:
            bullet_list.remove(shoot)
            all_sprites_list.remove(shoot)
            score += 1
            print(score)
 
        # Remove the bullet if it flies off the screen
        if shoot.rect.x > width:
            bullet_list.remove(shoot)
            all_sprites_list.remove(shoot)

    if len(hero_location) == 0:
        print ("You scored %s.  Thanks for playing!" % score)
        pygame.QUIT
        done = True
    screen.fill(WHITE)
    screen.blit(fill_bg, (0,0))
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()
            
            