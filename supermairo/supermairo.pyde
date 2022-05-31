#Second game 

#Variables to keep track of game status
restart = 1
count = 0

xAxis = 0 

#Sets up the screen 
def setup():
    
    global mario
   
    size(700, 500) 
    
    
def draw():
    background('#0000FF')
    mario()

#Function for the players charecter 
def mario():
    global xAxis, count
    
    mario = loadImage("mario.png")
    mario2 = loadImage("mario2.png") 
    mario.resize(80, 80)  
    mario2.resize(80, 80) 
    
    
   # if restart == 1:
    if count == 0:
        image(mario, xAxis, 420)
    elif count == 1:
        image(mario2, xAxis, 420) 

#Keys used to manuveur marios charecter 
def keyPressed():
    
    global image, xAxis, count
    
    count += 1
    if count == 2:
        count = 0
    
    #Normal movement
    if key == "d":
        xAxis += 10
        
    print(count)
        
    
    
    
    
