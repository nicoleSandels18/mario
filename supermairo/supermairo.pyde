#Second game 

#Use timer to help with jumps
timer = 50 
xTimer = 0 

#Variables to keep track of game status
count = 0
dead = 0 
xAxis = 0 
yAxis = 515

spike = False
#For Lazers
hit = False
hitStar = False
a = 10 

#Sets up the screen 
def setup():
    
    global mario
    size(1200, 600) 
    
#To repaint background everytime 
def draw():
    background('#0000FF')
    
    backdrop = loadImage("backdrop.png") 
    image(backdrop, 0, 0)
    
    mario()
    blocksOne()
    lazers()
    star()
    
    spike = loadImage("spike.png")
    spike.resize(50, 50)
    image(spike, 225, 550)
    
def star():
    global mario, dead, xAxis, hitStar
    
    #if hitStar == True:
       # xAxis += 50
       # print("Power up")

def dead():
    global spike
    
    if spike == True:
        text("YOU DIED", 100, 100)
    else:
        print("Still alive")
    yboundary()

#Lazer obstacle
def lazers():
    global a, hit
    
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
    global xAxis, count, yAxis, xTimer, yboundry
    
    mario = loadImage("mario.png")
    mario2 = loadImage("mario2.png") 
    mario.resize(80, 80)  
    mario2.resize(80, 80) 
    
   # if restart == 1:
    if count == 0:
        image(mario, xAxis, yAxis)
    elif count == 1:
        image(mario2, xAxis, yAxis) 
        
    #Used to bring Mario down after jump
    if yAxis < yboundary:
        yAxis += 2
    if xTimer > 0:
        xTimer -= 1
    
    print(xAxis, yAxis)
    yboundary()
    
#to prevent mario from running through blocks
#Y AXIS
def yboundary():
    global xAxis, yAxis, mario, mario2, dead, spike, hit, star, hitStar
   
    #First block
    if 90 < xAxis < 200 and 450 <= yAxis <= 480:
        yAxis = 470  
   
    #Second block
    if 240 <= xAxis < 330 and 450 <= yAxis <= 516:
        yAxis = 470
 
    #Spike  
    if 200 <= xAxis < 240 and 480 <= yAxis <= 516:
        #Restarts mario
        xAxis = 0
        yAxis = 515

        #Aknowladges hit on spike
        spike = True
        print("HIT")
        dead()
       
    # #Lazers, only work when area is present with rectangle
    if 380 <= xAxis <= 450 and 0 <= yAxis <= 516 and hit == True:
        #Restarts mario
        xAxis = 0
        yAxis = 515
    lazers()
   
    #Star
    if 170 <= xAxis <= 180 and 420 <= yAxis <= 430:
        hitStar = True  
        print("power up")
    star()

#Keys used to manuveur marios charecter 
def keyPressed():
    
    global image, xAxis, count, yAxis 
    
    #Used to flip between images 
    count += 1
    if count == 2:
        count = 0
    
    #Normal movement
    if key == "d":
        xAxis += 5
    elif key == "a":
        xAxis -= 5
    elif key == "w":
        yAxis -= 20 
        #use timer to bring the jump down
    elif key == "s":
        yAxis += 10
        
    #Use info from dvd to keep within the screen 
        
    
    
    
    
    
    
