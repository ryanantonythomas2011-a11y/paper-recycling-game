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
def create_items(items_to_create):
    new=[]
    for i in items_to_create:
        item=Actor(i)
        new.append(item)
    return new
def create_extra_items(number_of_extra_items):
    items_to_create=["paper"]
    for i in range (number_of_extra_items):
        extra=random.choice(items)
        items_to_create.append(extra)
    return items_to_create
def layout_items(items_layout):
    gaps=len(items_layout)+1
    gaps_size=WIDTH/gaps
    random.shuffle(items_layout)
    for i,j in enumerate(items_layout):
        new_position=(i+1)*gaps_size
        j.x=new_position
def animate_items(items_to_animate):
    global Animations
    for i in items_to_animate:
        duration=Start_speed-Current_Level
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,y=HEIGHT,on_finished=handle_gameover)
        Animations.append(animation)
def stop_animation(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()
def handle_gameover():
    global Game_Over
    Game_Over=True                   
def handle_gamecomplete():
    global Current_Level,Current_Items,Game_complete,Animations
    stop_animation(Animations)
    if Current_Level==Final_Level:
        Game_complete=True
    else:
        Current_Level+=1
        Current_Items=[]
        Animations=[]
def on_mouse_down(pos):
    global Current_Items , Current_Level
    for i in Current_Items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handle_gamecomplete()
            else:
                handle_gameover()
def make_items(num):
    items_to_create = create_extra_items(num)
    new=create_items(items_to_create)
    layout_items(new)
    animate_items(new)
    return new
def update():
    global Current_Items
    if len(Current_Items)==0:
        Current_Items=make_items(Current_Level)

pgzrun.go()


 
