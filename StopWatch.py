# StopWatch

# template for "Stopwatch: The Game"

import simplegui

# define global variables
win=0
loss=0
seconds=0
tenseconds=0
minutes=0
points= str(win) +"/"+ str(loss)

mtime= str(minutes) + ":"+str(tenseconds) + str(seconds)+".0"

# define helper function format that converts time
# Points
def format(t):
    global loss
    global win
    global points
    
    t=str(t)
    
    if (t=="0.0" or t=="1.0" or t=="2.0" or t=="3.0" or 
        t=="4.0" or t=="5.0" or t=="6.0" or t=="7.0" or 
        t=="8.0" or t=="9.0"):
            win +=1
    loss+=1
    points= str(win) + "/" + str(loss)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    time.start()
    
def stop():
    global seconds
    
    time.stop()
    
    t=seconds
    format(t)
    
    
def reset():
    global seconds
    global tenseconds
    global minutes
    global mtime
    global win
    global loss
    global points
    
    seconds=0
    tenseconds=0
    minutes=0
    win= 0
    loss=0
    mtime=(str(minutes)+ ":" + str(tenseconds) + 
        str(seconds) + ".0")
    points= str(win) + "/" + str(loss)
    time.stop()
    
# define event handler for timer with 0.1 sec interval
def time():
    global seconds
    global tenseconds
    global minutes
    global mtime
    
    seconds= seconds+0.1
    if seconds==10:
        tenseconds=1
        seconds=0
    elif tenseconds==6:
        minutes=minutes+1
        tenseconds=0
    
    mtime=str(minutes)+":"+str(tenseconds)+str(seconds)

# define draw handler
def draw(canvas):
    canvas.draw_text(mtime,[40,110] , 50, "Red")
    canvas.draw_text(points,[130,40] ,25, "Green")
  
# create frame
f= simplegui.create_frame("Stop watch",200,200)
time=simplegui.create_timer(100, time)
f.add_button("Start",start,100)
f.add_button("Stop",stop,100)
f.add_button("Reset",reset,100)
f.set_draw_handler(draw)

# start frame
f.start()
