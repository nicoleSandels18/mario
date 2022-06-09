add_library('minim')
minim = Minim(this)

#Mario looses a life audio
deathSong = minim.loadFile("marioDeath.mp3")
#Plays when game ends
finalDeath = minim.loadFile("finalDeath.mp3") 
#Loading screen music
introSong = minim.loadFile("titleMusic.mp3") 

timer = 50
exception = 0 

#Variables to keep track of game status
# restart = 1
count = 0
mode = 1
deathCount = 0 #0 is dead

xAxis = 0
yAxis = 515

#USED to reset level completely 
spike = False 
#Trying to use for lazers 
hit = False
hitStar = False 
   
#Used to create lazers 
a = 10 
 
xTimer = 0
yBoudry = 515

#Sets up the screen 
def setup():
    global mario
    size(1200, 600) 
    
def draw():
    background('#0000FF')

    backdrop = loadImage("backdrop.png")
    image(backdrop, 0, 0)
   
    #All functions that need to be called
    loadScreen() 
    
    if mode == 0:
        mario()
        blocksOne() 
        lazers() 
        # star() 
        loose() 
        scores() 
        door() 
        goomba() 
        greenBlocks() 
    
        print(deathCount) 
        #Since not in a function, need to code out of deathscreen 
        if deathCount > 0:  
            spike = loadImage("spike.png")
            spike.resize(50, 50)
            image(spike, 225, 550)
            
            spike2 = loadImage("spike2.png")
            spike2.resize(50, 50)
            image(spike2, 1007, 550) 
            
    # print(xAxis, yAxis) 
    print(mouseX, mouseY) 
        
#######################################

def goomba():
    
    goomba = loadImage("goomba.png")
    goomba.resize(25, 25) 
    image(goomba, 100, 100) 
    
    


def greenBlocks(): 
    global xAxis, yAxis
    
    #The first green stack
    if 800 <= xAxis <= 960 and 0 <= yAxis <= 400:
        yAxis = 300 
    
    if 1060 <= xAxis <= 1198 and 0 <= yAxis <= 550:
        yAxis = 230
    
        


def loadScreen():
    global mode, deathCount, introSong
    if mode == 1: 
        intro = loadImage("introo.png")
        image(intro, 0, 0) 
        introSong.play() 
        
        if key == "p":
            introSong.pause() 
            mode = 0 
            deathCount = 3 
    
    
        

def scores():
    global deathCount
    
    if deathCount > 0 :
        
        #Keeps track of lives left for the player to see
        textSize(30) 
        begin = loadImage("lives.png") 
        image(begin, 50, 50) 
        text(deathCount, 50, 120) 
    

#Limits lives to 3 and places endscreen
def loose():
    global deathCount, mode 
    if deathCount == 0:
        finalDeath.play() 
        background(0)
        endscreen = loadImage("endscreen.png")
        image(endscreen, 0, 0) 
        textSize(40) 
        fill(0)
        text("Press space to restart", 370, 500) 
        
        #Resets the code 
        if key == " ":
            deathCount = 3
        
        if key == "i":
            #loadScreen() 
            mode = 1
            
    loadScreen() 
           
            

def door():
    global mario, xAxis, yAxis, exception, deathCount 
    
    if deathCount > 0:  

        doorClosed = loadImage("doorClosed.png")
        doorClosed.resize(100, 200)
        image(doorClosed, 1105, 139)
            
        #To open the door
        if 1123 <= xAxis <= 1182 and 161 <= yAxis <= 311:
            doorOpen = loadImage("doorOpen.png")
            doorOpen.resize(100, 200)
            image(doorOpen, 1105, 139) 
    
    #Ladder
    
    if deathCount > 0:  
        
        ladder = loadImage("ladder.png")
        ladder.resize(300, 220)
        image(ladder, 700, 400) 
        
        #Moves up the ladder
        if 799 <= xAxis <= 904 and 393 <= yAxis <= 600:
            #Allows up movement
            exception = 1
        else: 
            exception = 0 
            
    
#######################################
    
# def star():
    
#     global mario, xAxis, hitStar
    
#     star = loadImage("star.png") 
#     star.resize(40, 40) 
#     image(star, 210, 300) 
    
#     if hitStar == True:
#         xAxis += 50 
#         # hitStar = False
#         print("POWER UP") 
        

# #Lazer obstacle
def lazers():
    #NOT WORKING 
    global a, hit, deathCount
    #Blinking lazers, that if hit cause mario to 'die'
   
    if a < 0:
        a = 200  
    a -= 5
    if a >= 180:
        rect(450, 0, 10, 2000) 
        fill(255, 0, 255) 
        hit = True 
    elif a >= 160:
        rect(0, 0, 0, 0) 
        hit = False
    elif a >= 140:
        rect(450, 0, 10, 2000) 
        fill(0, 255, 0) 
        hit = True

    else:
        hit = False 
    yboundary() 
          

    
#First screen of blocks 
def blocksOne():     
    #First block
    block = loadImage("black.png") 
    block.resize(80, 80) 
    image(block, 150, 540) 
    
    #Second block
    block2 = loadImage("block.png")
    block2.resize(80, 80) 
    image(block2, 270, 540) 
    

#Function for the players charecter 
def mario():
    global xAxis, count, yAxis, xTimer, yBoudry
    
    mario = loadImage("mario.png")
    mario2 = loadImage("mario2.png") 
    mario.resize(80, 80)  
    mario2.resize(80, 80) 
    
    
    if count == 0:
        image(mario, xAxis, yAxis)
    elif count == 1:
        image(mario2, xAxis, yAxis) 
        
    #Used to bring mario down after the jump    
    if yAxis < yBoudry:
        yAxis += 7
    if xTimer > 0:
        xTimer -= 1
        
    yboundary() 
    
   
#prevents mario from running through the blocks
#X AXIS
def boundary():
    global xAxis, yAxis 
    #First block 
    if 80 < xAxis < 200 and 500 <= yAxis <= 520: 
        xAxis = 80

#Y AXIS 
def yboundary():
    global xAxis, yAxis, mario, mario2, spike, hit, star, hitStar, deathCount
    
    #First block
    if 90 < xAxis < 200 and 450 <= yAxis <= 480:
        yAxis = 470  
    
    #Second block 
    if 240 <= xAxis < 330 and 450 <= yAxis <= 516:
        yAxis = 470 
    elif 320 <= xAxis <= 340 and 450 <= yAxis <= 550:
        xAxis = 341 
        
    #Fist green block
    if 791 <= xAxis <= 830 and 515 <= yAxis <= 520:
        xAxis = 799
        if key == "w":
            
            yAxis 
  
    #Spike One
    if 200 <= xAxis < 240 and 480 <= yAxis <= 516:
        #Restarts mario 
        deathSong.play() 
        xAxis = 0 
        yAxis = 515
        deathCount -= 1 

        #Aknowladges hit on spike 
        spike = True 
        print("HIT") 
    
    #Spike Two 
        
    #When mario hits spike, creates minus one life      
    if 975 <= xAxis <= 1060 and 480 <= yAxis <= 516:
        deathSong.play() 
        xAxis = 0 
        yAxis = 515
        deathCount -= 1 
        
        
        spike = True
        print("HIT") 
        
        
    # #Lazers, only work when area is present with rectangle #######################################
    if 400 <= xAxis <= 459 and 0 <= yAxis <= 516 and hit == True:
        #Restarts mario 
        xAxis = 0 
        yAxis = 515
        deathCount -= 1 
        
    
    # #Star
    # if 170 <= xAxis <= 180 and 420 <= yAxis <= 430:
    #     hitStar = True  
    #     print("power up") 
    


#Keys used to manuveur marios charecter 
def keyPressed():
    
    global image, xAxis, count, timer, yAxis, xTimer, exception
    
    count += 1
    if count == 2:
        count = 0
    
    #Normal movement
    
    #Forward
    if key == "d":
        xAxis += 20
        boundary() #needs to call on function to prevent movement 
        yboundary() 
        
        
    #Used to jump, prevent triple jumping 
    if xTimer <= 0 and exception == 0:
        if key == "w":
            yAxis -= 65
            xTimer = 12
            boundary() 
            yboundary()
            
    elif exception == 1:
            yAxis -= 50
    door() 

    #Backwards
    if xAxis > 0:
        if key == "a":
            xAxis -= 20
            boundary() 
            


############################################## PREVIOUS CODE BELOW 
#Second game 

# #Use timer to help with jumps
# timer = 50 
# xTimer = 0 

# #Variables to keep track of game status
# count = 0
# dead = 0 
# xAxis = 0 
# yAxis = 515

# spike = False
# #For Lazers
# hit = False
# hitStar = False
# a = 10 

# #Sets up the screen 
# def setup():
    
#     global mario
#     size(800, 600) 
    
# #To repaint background everytime 
# def draw():
#     background('#0000FF')
    
#     backdrop = loadImage("backdrop.png") 
#     image(backdrop, 0, 0)
    
#     mario()
#     blocksOne()
#     lazers()
#     star()
    
#     spike = loadImage("spike.png")
#     spike.resize(50, 50)
#     image(spike, 225, 550)
    
# def star():
#     global mario, dead, xAxis, hitStar
    
#     #if hitStar == True:
#        # xAxis += 50
#        # print("Power up")

# def dead():
#     global spike
    
#     if spike == True:
#         text("YOU DIED", 100, 100)
#     else:
#         print("Still alive")
#     yboundary()

# #Lazer obstacle
# def lazers():
#     global a, hit
    
#     if a < 0:
#         a = 200
#     a -= 5
#     if a >= 180:
#         rect(450, 0, 10, 2000) 
#         fill(255, 0, 255)
#         hit = True
#     elif a >= 160:
#         rect(0, 0, 0, 0)
#         hit = False
#     elif a >= 140:
#         rect(450, 0, 10, 2000)
#         fill(0, 255, 0)
#         hit = True
#     else:
#         hit = False
        
# def blocksOne():
#     #First block
#     block = loadImage("black.png")
#     block.resize(80, 80)
#     image(block, 150, 540)
    
#     #Second block
#     block2 = loadImage("block.png")
#     block2.resize(80, 80)
#     image(block2, 270, 540)
    
        
    

# #Function for the players charecter 
# def mario():
#     global xAxis, count, yAxis, xTimer, yboundry
    
#     mario = loadImage("mario.png")
#     mario2 = loadImage("mario2.png") 
#     mario.resize(80, 80)  
#     mario2.resize(80, 80) 
    
#    # if restart == 1:
#     if count == 0:
#         image(mario, xAxis, yAxis)
#     elif count == 1:
#         image(mario2, xAxis, yAxis) 
        
#     #Used to bring Mario down after jump
#     if yAxis < yboundary:
#         yAxis += 2
#     if xTimer > 0:
#         xTimer -= 1
    
#     print(xAxis, yAxis)
#     yboundary()
    
# #to prevent mario from running through blocks
# #Y AXIS
# def yboundary():
#     global xAxis, yAxis, mario, mario2, dead, spike, hit, star, hitStar
   
#     #First block
#     if 90 < xAxis < 200 and 450 <= yAxis <= 480:
#         yAxis = 470  
   
#     #Second block
#     if 240 <= xAxis < 330 and 450 <= yAxis <= 516:
#         yAxis = 470
 
#     #Spike  
#     if 200 <= xAxis < 240 and 480 <= yAxis <= 516:
#         #Restarts mario
#         xAxis = 0
#         yAxis = 515

#         #Aknowladges hit on spike
#         spike = True
#         print("HIT")
#         dead()
       
#     # #Lazers, only work when area is present with rectangle
#     if 380 <= xAxis <= 450 and 0 <= yAxis <= 516 and hit == True:
#         #Restarts mario
#         xAxis = 0
#         yAxis = 515
#     lazers()
   
#     #Star
#     if 170 <= xAxis <= 180 and 420 <= yAxis <= 430:
#         hitStar = True  
#         print("power up")
#     star()

# #Keys used to manuveur marios charecter 
# def keyPressed():
    
#     global image, xAxis, count, yAxis 
    
#     #Used to flip between images 
#     count += 1
#     if count == 2:
#         count = 0
    
#     #Normal movement
#     if key == "d":
#         xAxis += 5
#     elif key == "a":
#         xAxis -= 5
#     elif key == "w":
#         yAxis -= 20 
#         #use timer to bring the jump down
#     elif key == "s":
#         yAxis += 10
        
        
    
    
    
    
    
    
