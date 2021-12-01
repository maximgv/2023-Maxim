import pygame,random,time
pygame.init()
LivesLeft=3
a=0
#define some colours
Black= ( 0, 0, 0)
Blue =( 0, 0, 255)
Green= ( 0, 128, 0)
Olive =(128, 128, 0)
Purple =(128, 0, 128)
Red= (255, 0, 0)
White= (255, 255, 255)

#set resolution
slength=1280
sheight=720


#start up the drawing of display
screen=pygame.display.set_mode([slength,sheight])
pygame.display.set_caption("Arkanoid2")
clock=pygame.time.Clock()


#making a function for writing
def write(txt,color,size,x,y):
    font=pygame.font.Font("8-BIT WONDER.TTF",size)
    writetxt=font.render(txt,True,color)
    writerect=writetxt.get_rect()
    writerect.center=x,y
    screen.blit(writetxt,writerect)


#creating the paddle and getting it to move
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("paddle.png")
        self.image=pygame.transform.scale(self.image,[150,40])
        self.image.set_colorkey(White)
        
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vx=0
        self.vy=0
    def update(self):
       
       keys=pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
           self.vx=-7.5
       if keys[pygame.K_RIGHT]:
           self.vx=7.5
       self.rect.x+=self.vx
       if self.rect.right>=slength:
           self.rect.right=slength
       if self.rect.left<=0:
           self.rect.left=0


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


#creating the ball           
class Ball(pygame.sprite.Sprite):
    def __init__(self,p,w,c):
        super().__init__()
        self.image=pygame.image.load("ball.png")
        self.image=pygame.transform.scale(self.image,[40,40])
        self.image.set_colorkey(White)
        self.rect=self.image.get_rect()
        self.rect.x=640
        self.rect.y=600
        self.p=p
        self.w=w
        self.c=c
        self.vy=3
        self.vx=0
        self.t_collide=False
        self.b_collide=False
        self.score=0
    #what it does when hits 
    def hit_wall(self):
        hits=pygame.sprite.groupcollide(balls,self.c.walls,False,True)
        if hits:
             pygame.mixer.init()
             pygame.mixer.music.load("bounce.mp3")
             pygame.mixer.music.play(1,0.0)
             return True
        else:
            return False
    #what to do when hits paddle
    def hit_player(self):
        hits=pygame.sprite.spritecollide(self.p,balls,False)
        if hits:
             pygame.mixer.init()
             pygame.mixer.music.load("bounce.mp3")
             pygame.mixer.music.play(1,0.0)
             return True
        else:
            return False
    #score display
    def Score(self):
        write("Score - "+str(self.score),Blue,20,960,27)
    def update(self):
       if self.rect.left<=0:
           if self.t_collide:
               self.vx=random.randrange(1,3)
               self.vy=6
               self.t_collide=False
           elif self.b_collide:     
               self.vx=random.randrange(1,3)
               self.vy=-6
               self.b_collide=False
       elif self.rect.top<=0 :
           self.t_collide=True
           self.vx=random.randrange(-3,3)
           self.vy=6
       elif self.rect.right>=slength:
           if self.t_collide:
               self.vx=random.randrange(-3,-1)
               self.vy=6
               self.t_collide=False
           elif self.b_collide:     
               self.vx=random.randrange(-3,-1)
               self.vy=-6
               self.b_collide=False
       elif self.hit_player():
           self.vx=random.randrange(-3,3)
           self.vy=-6
           self.b_collide=True
       elif self.hit_wall():
           self.vx=random.randrange(-3,3)
           self.vy=6
           self.score+=1
           self.t_collide=True
        
       self.rect.x+=self.vx
       self.rect.y+=self.vy
            
class Walls1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([80,40])
        self.image.fill(Green)
        self.rect=self.image.get_rect()
        self.rect.x=x*40
        self.rect.y=y*40
class Walls2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([80,40])
        self.image.fill(Red)
        self.rect=self.image.get_rect()
        self.rect.x=x*40
        self.rect.y=y*40
class Walls3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([80,40])
        self.image.fill(Blue)
        self.rect=self.image.get_rect()
        self.rect.x=x*40
        self.rect.y=y*40
class Walls4(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([80,40])
        self.image.fill(Black)
        self.rect=self.image.get_rect()
        self.rect.x=x*40
        self.rect.y=y*40
class Walls5(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([80,40])
        self.image.fill(Purple)
        self.rect=self.image.get_rect()
        self.rect.x=x*40
        self.rect.y=y*40
class Walls6(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([80,40])
        self.image.fill(Olive)
        self.rect=self.image.get_rect()
        self.rect.x=x*40
        self.rect.y=y*40
    
def intro():
#main game 
    screen.fill(White)
    pygame.mixer.init()
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play(-1,0.0)
    write("Welcome to ",Red,35,600,50)
    icon=pygame.image.load("main.png")
    icon=pygame.transform.scale(icon,[900,500])
    screen.blit(icon,[200,75])
    wait=1
    
    while wait:
        cur=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
    
        if  250+100>cur[0]>250 and 587+65>cur[1]>587:
            pygame.draw.rect(screen,Green,[250,587,100,65]  )
            if click[0]==1:
                wait=0
        else:
            pygame.draw.rect(screen,Blue,[250,587,100,65]  )
            
        write("Start",Red,20,300,620)

        if 860+100>cur[0]>860 and 587+65>cur[1]>587:
             pygame.draw.rect(screen,Green,[860,587,100,65])
             if click[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen,Blue,[860,587,100,65])
    
        write("Exit",Red,20,905,620)
        pygame.display.flip()
def pause():
    paused=True
    screen.fill(White)
    write("Paused",Red,40,640,360)
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    paused=0
        pygame.display.flip()
class Map:
    def __init__(self,map_file):
        self.map_file=map_file
        self.map_data=[]
        self.walls=pygame.sprite.Group()
    def update(self):
        with open(self.map_file,'r+') as f:
          for line in f:
              self.map_data.append(line)
        for row ,tiles in enumerate(self.map_data):
            for col,tile in enumerate(tiles):
                    if tile=='1':
                        self.w=Walls1(col,row)
                        self.walls.add(self.w)
                        all_sprites.add(self.walls)
                    if tile=='2':
                        self.w=Walls2(col,row)
                        self.walls.add(self.w)
                        all_sprites.add(self.walls)
                    if tile=='3':
                        self.w=Walls3(col,row)
                        self.walls.add(self.w)
                        all_sprites.add(self.walls)
                    if tile=='4':
                        self.w=Walls4(col,row)
                        self.walls.add(self.w)
                        all_sprites.add(self.walls)
                    if tile=='5':
                        self.w=Walls5(col,row)
                        self.walls.add(self.w)
                        all_sprites.add(self.walls)
                    if tile=='6':
                        self.w=Walls6(col,row)
                        self.walls.add(self.w)
                        all_sprites.add(self.walls)
running=True
start=True
level=False
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                pause()
    if start :
        intro()
        start=False
        all_sprites=pygame.sprite.Group()
        balls=pygame.sprite.Group()
        walls=pygame.sprite.Group()
        p=Player(640,650)
        all_sprites.add(p)
        c=Map("level1.txt")
        c.update()
         

        b=Ball(p,c.w,c)
        balls.add(b)
        all_sprites.add(b)

    if level:
        level=False
        all_sprites=pygame.sprite.Group()
        balls=pygame.sprite.Group()
        walls=pygame.sprite.Group()
        p=Player(640,650)
        all_sprites.add(p)
        c=Map("level2.txt")
        c.update()              
        b=Ball(p,c.w,c)
        balls.add(b)
        all_sprites.add(b)
               
    all_sprites.update()
    if len(c.walls.sprites())<=0:
        level=True
        
    screen.fill(White)
    if b.rect.bottom>=sheight:
    
          pygame.mixer.music.load("gamend.mp3")
          pygame.mixer.music.play(-1,0.0)
          screen.fill(White)
          write("Thank you for playing",Red,20,640,60)
          write("Game Over",Red,60,640,640)
          icon=pygame.image.load("main.png")
          icon=pygame.transform.scale(icon,[900,500])
          screen.blit(icon,[200,75])


          p.kill()
          b.kill()
          all_sprites.remove(c.walls)
          for event in pygame.event.get():
              if event.type==pygame.QUIT:
                  pygame.quit()
                  quit()
              if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_RETURN:
                      gover=True
          
    all_sprites.draw(screen)
    b.Score()
    pygame.display.flip()
    
    
        
    
pygame.quit()
quit()
