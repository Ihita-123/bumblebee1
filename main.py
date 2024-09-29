import pgzrun
import random 

WIDTH = 600
HEIGHT= 600

bee=Actor("bee")
flower=Actor("flower")
bee.x= 200
bee.y=400 
def draw():
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()



pgzrun.go()
