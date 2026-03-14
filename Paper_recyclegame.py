import pgzrun
import random
WIDTH=800
HEIGHT=500
items=["battery","bag","bottle","chips"]
Final_Level=6
Current_Level=1
Game_Over=False
Game_complete=False
Animations=[]
Current_Items=[]
Start_speed=10
def draw():
    global Current_Items, Current_Level, Game_complete, Game_Over
    screen.clear()
    screen.blit("recycling background",(0,0))
    if Game_Over:
        screen.draw.text("Game Over you lost",center=(500,300),color="red",fontsize=50)
    elif Game_complete:
        screen.draw.text("Well Done you won",center=(500,300),color="green",fontsize=50)
    else:
        for i in Current_Items:
            i.draw()
pgzrun.go()            

