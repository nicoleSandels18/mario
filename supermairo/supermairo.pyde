 #Need to add music minim so audio files can be attatched
add_library('minim')
minim = Minim(this)

#Mario loses a life audio
deathSong = minim.loadFile("marioDeath.mp3")
#Plays when game ends
finalDeath = minim.loadFile("finalDeath.mp3") 
#Loading screen music
introSong = minim.loadFile("titleMusic.mp3") 
#Won the lvl music
win = minim.loadFile("levelClear.mp3")
#During level music
levelMusic = minim.loadFile("levelMusic.mp3") 

#Variables to keep track of game status

#Used to allow Mario to double jump on ladders
exception = 0 
#Helps to switch between 2 different images of Mario
count = 0
#Keeps mode for game - dictates which functions should be running
mode = 1 #0 = game, 1 = loadscreen, 2 = winscreen
#Keeps track of lives left
deathCount = 0 #0 is dead
#Starts Mario at the beggining position
xAxis = 0 
yAxis = 515
#USED to reset level completely 
hitSpike = False 
#Trying to use for lazers 
hit = False
#Detects hit on star
hitStar = False    
#Used to create lazers 
a = 10 
#Used to bring Mario down after a jump 
xTimer = 0
#Keeps Mario on screen
yBoudry = 515
#Timer for first green block jump
timer2 = 0 
#Timer for extra life
timerS = 50 
#Timer for goomba
timerG = 0 
#xAxis for goomba
xGoomba = 400
#Timer for win screen
timerWin = 0

#Sets up the screen 
def setup():
    global mario
    size(1200, 600) 

def draw():
    background('#0000FF')
    global mode, xAxis, yAxis 
   
    #needs to be called
    loadScreen() 
    #Calls upon different functions depending on the mode present 
    if mode == 0:
        play() 
    if mode == 1:
        levelMusic.pause() 
        if key == "p":
            mode = 0 
    if mode == 2:
        levelMusic.pause()
        winScreen() 
        xAxis = 0
        yAxis = 515
        
#Plays entire game by use of calling on certian functions
def play():
    
    levelMusic.loop() 
    backdrop = loadImage("backdrop.png")
    image(backdrop, 0, 0)
    deathCount = 3 
    blocksOne() 
    lazers() 
    star() 
    spike()
    scores() 
    door() 
    goomba() 
    greenBlocks() 
    mario()
    loadScreen() 
    loose()
     
#Spike images
def spike():
    if deathCount > 0:  
        spike = loadImage("spike.png")
        spike.resize(50, 50)
        image(spike, 225, 550)
        
        spike2 = loadImage("spike2.png")
        spike2.resize(50, 50)
        image(spike2, 1007, 550) 
        
#Moving goomba
def goomba():
    global timerG, xGoomba, hit, deathCount, xAxis
    
    goomba = loadImage("goomba.png")
    goomba.resize(25, 25) 
    image(goomba, xGoomba, 575) 
    
    #Moves Goomba randomly across the screen
    if xGoomba == 400:
        timerG = 0 
        if timerG == 0:
            xGoomba += 20 
            timerG += 10
    elif timerG == 10:
        xGoomba += 20
    if xGoomba == 800:
        timerG += 10 
    if timerG == 20:
        xGoomba -= 20
        
   #Checks if Mario is touching Goomba
    if xGoomba - 20 <= xAxis <= xGoomba + 20 and yAxis > 490:
        hit = True 
        if hit == True: 
            deathCount -= 1
            xAxis = 0 
            
#Keeps Mario on greenblocks, checks for spikes
def greenBlocks(): 
    global xAxis, yAxis, deathCount
    
    #The first green stack, for keeping on top of stack
    if 800 <= xAxis <= 960 and 307 <= yAxis:
        yAxis = 300   
        
       #Spike One
    if 200 <= xAxis < 240 and 480 <= yAxis <= 516:
        #Restarts mario 
        deathSong.play() 
        xAxis = 0 
        yAxis = 515
        deathCount -= 1 
        #Aknowladges hit on spike 
        hitSpike = True  
        
    #Second spike 
    if 960 <= xAxis <= 979 and yAxis <= 330:
        xAxis = 979
    # #Second green block
    if 1035 <= xAxis <= 1200 and 220 < yAxis:
        yAxis = 240 

#Loading screen function
def loadScreen():
    global mode, deathCount
    if mode == 1: 
        intro = loadImage("introo.png")
        image(intro, 0, 0) 
        introSong.play() 
            
        if key == "p":
            introSong.pause() 
            mode = 0 
            deathCount = 3 
            
#Allows user to see how many lives they have remaining
def scores():
    global deathCount
    if deathCount > 0 :
        #Keeps track of lives left for the player to see
        textSize(30) 
        begin = loadImage("lives.png") 
        image(begin, 50, 50) 
        text(deathCount, 50, 120) 
        
#Produces the win screen
def winScreen():
    global xAxis, yAxis, mode, deathCount
    #Win screen
    if deathCount >= 1:
        winScreen = loadImage("winScreen.jpg")
        image(winScreen, 0, 0) 
        win.play() 
        #Changes mode depending on user input 
        if key == " ":
            deathCount = 3
            backdrop = loadImage("backdrop.png")
            image(backdrop, 0, 0)
            deathCount = 3 
            mode = 0 
            xAxis = 0
            yAxis = 515
        if key == "i":
            mode = 1

#Limits lives to 3 and places endscreen
def loose():
    global deathCount, mode 
    levelMusic.pause()
    if deathCount == 0:
        finalDeath.play() 
        background(0)
        endscreen = loadImage("endscreen.png")
        image(endscreen, 0, 0) 
        #Resets the code 
        if key == " ":
            deathCount = 3
        if key == "i":
            mode = 1
#Checks if Mario is at the door - if they have won, and helps load ladders
def door():
    global mario, xAxis, yAxis, exception, deathCount, timerWin, mode
    
    if deathCount > 0:  
        doorClosed = loadImage("doorClosed.png")
        doorClosed.resize(100, 200)
        image(doorClosed, 1120, 139)
        if timerWin > 0:
                timerWin -= 10
        
        #To open the door
        if 1120 <= xAxis <= 1182 and 161 <= yAxis <= 311:
            doorOpen = loadImage("doorOpen.png")
            doorOpen.resize(100, 200)
            image(doorOpen, 1105, 139) 
            # if timerWin == 20:
            mode = 2
            winScreen() 
        loadScreen() 
        
    #Second Ladder
    if deathCount > 0:  
        #Loads the second ladder in
        ladder = loadImage("ladder.png")
        ladder.resize(300, 220)
        image(ladder, 700, 400) 
        #Moves up the ladder
        if 799 <= xAxis <= 904 and 330 <= yAxis <= 600:
            if key == "w":
                yAxis -= 20
                
        #First Ladder
        ladder2 = loadImage("ladder2.png")
        ladder2.resize(300, 140)
        image(ladder2, 8, 290) 
        #Controls ladder movement
        if 270 <= yAxis <= 440 and 100 <= xAxis <= 120:
            exception = 1
        else:
            exception = 0 
        #Controls the ? blocks 
        if 180 <= yAxis <= 250 and 130 <= xAxis <= 230:
            yAxis = 200
        elif 180 <= yAxis <= 250 and 245 <= xAxis <= 360:
            yAxis = 200
            
#Star used to obtain bonus life
def star():
    global hitStar, deathCount, xAxis, yAxis, intro, timerS, mario
    #Places the star
    star = loadImage("star.png") 
    star.resize(40, 40) 
    image(star, 260, 130)  
    
    #Detects hit to star
    if 210 <= xAxis <= 260 and 0 <= yAxis <= 170: 
         if deathCount < 4 and hitStar == False:
            #Keeps extra life text on for a certian amount of time
            timerS -= 1
            #Text diaplays for extra life
            extraLife = loadImage("el.png")
            image(extraLife, 500, 200) 
            deathCount += 1
            if timerS < 0:
                hitStar = True 
                
#Lazer obstacle
def lazers():
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
    global deathCount, block, block2
    
    if deathCount > 0:  
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
    
#Prevents mario from running through the blocks
def boundary():
    global xAxis, yAxis 
    #First block 
    if 80 < xAxis < 200 and 500 <= yAxis <= 520: 
        xAxis = 80
        
#Another boundary function used to help detect certian hits
def yboundary():
    global xAxis, yAxis, mario, mario2, hitSpike, hit, star, deathCount
    
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
    #Spike Two 
    #When mario hits spike, creates minus one life      
    if 975 <= xAxis <= 1060 and 480 <= yAxis <= 516:
        deathSong.play() 
        xAxis = 0 
        yAxis = 515
        deathCount -= 1 
        hitSpike = True
    
    #Lazers
    if 375 <= xAxis <= 459 and 0 <= yAxis <= 700 and hit == True:
        #Restarts mario 
        xAxis = 0 
        yAxis = 515
        deathCount -= 1 
        

#Keys used to manuveur marios charecter 
def keyPressed():
    
    global image, xAxis, count, yAxis, xTimer, exception
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
            xTimer = 10
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
