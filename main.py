from random import *

class Kitty:
    def __init__(cat, name):
        cat.name = name
        cat.gladness = 10
        cat.satiety = 10
        cat.health = 100
        cat.alive = True

    def to_eat(cat):
        print('Yummy..!')
        cat.gladness += 5
        cat.satiety += 10
        cat.health += 4
        
    def to_fight_with_dogs(cat):
        print('Attempt to kill them...')
        cat.gladness -= 2
        cat.satiety -= 5
        cat.health -= 10
        
    def to_sleep(cat):
        print('Slepping process...')
        cat.gladness += 3
        cat.health += 2
        
    def to_hunt(cat):
        print('Hunting process...')
        cat.gladness += 2
        cat.health += 1
        cat.satiety +=1
        
    def to_live(cat):
        print('Just a life...')
        cat.gladness -= 2
        cat.health -= 1
        cat.satiety -=2
        
    def to_live1(cat):
        print('Just a life...')
        cat.gladness -= 2
        cat.health -= 1
        cat.satiety -=2

    def be_happy(cat):
        print("I'm happy!")
        cat.gladness += 5
        cat.satiety -= 2
        
    def is_alive(cat):
        if cat.gladness <= -5:
            print("Life doesn't have any meaning...")
            cat.alive = False
            cat.statics()
        elif cat.satiety < 0:
            print('Died because of hungry')
            cat.alive = False
            cat.statics()
        elif cat.health <= 0:
            print('Died because of wounds')
            cat.alive = False
            cat.statics()
        elif cat.gladness >= 50:
            print('Died because of happiness')
            cat.alive = False
            cat.statics()
        elif cat.satiety >= 50:
            print('Dead because of obesity')
            cat.alive = False
            cat.statics()
    def statics(cat):
        print('Gladness:',cat.gladness,  'Satiety:',cat.satiety,  'Health:',cat.health, 'Is alive:', cat.alive)
        
    def live(cat, day):
        day = "Day " + str(day) + " of " + cat.name + " life"
        print(day)
        live_cube = randint(1, 8)
        
        if live_cube == 1:
            cat.to_eat()
        elif live_cube == 2:
            cat.to_sleep()
        elif live_cube == 3:
            cat.to_hunt()
        elif live_cube == 4:
            cat.be_happy()
        elif live_cube == 6:
            cat.to_fight_with_dogs()
        elif live_cube == 7:
            cat.to_live()
        elif live_cube == 8:
            cat.to_live1()
        cat.statics()
        cat.is_alive()
            
sony = Kitty('Sony')
for day in range(365):
    if sony.alive == False:
        break
    sony.live(day)



