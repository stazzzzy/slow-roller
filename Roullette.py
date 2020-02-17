#T. Staso
import random
from lib.graphics import *

def timer():
    slow = 10000
    for x in range(slow):
        x=x
def timer2():
    slow = 10000
    for x in range(slow):
        x=x
def roll(p,q):
    f1.move(p,q),f2.move(p,q),f3.move(p,q),f4.move(p,q),f5.move(p,q)
    r1.move(p,q),r2.move(p,q),r3.move(p,q),r4.move(p,q),r5.move(p,q)
def reset_f(p,q):
    f1.move(p,q),f2.move(p,q),f3.move(p,q),f4.move(p,q),f5.move(p,q)
def reset_r(p,q):
    r1.move(p,q),r2.move(p,q),r3.move(p,q),r4.move(p,q),r5.move(p,q)
def erase_f():
    f1.undraw()
    f2.undraw()
    f3.undraw()
    f4.undraw()
    f5.undraw()
def erase_r():
    r1.undraw()
    r2.undraw()
    r3.undraw()
    r4.undraw()
    r5.undraw()
def colorPicker():
    num = random.randrange(100)
    if num < 49:
        color = "red"
    if num >= 50:
        color = "blue"
    if num == 49:
        color = "purple"
    print("Generated block #:",num)
    return color
 
win = GraphWin("Game",655,700)
win.setBackground("#3d4a4c")
img = Image(Point(327.5,350),"lib/back.gif")
img.draw(win)

balance = 1000

money = Text(Point(327,100),balance)
money.setStyle("bold"),money.setFill("yellow")
money.setSize(30)
money.draw(win)
dollar = Text(Point(265,100),"$")
dollar.setStyle("bold"),dollar.setFill("yellow")
dollar.setSize(30)
dollar.draw(win)
betbox = Entry(Point(327.5,470),20)
betbox.draw(win)
betbox.setText("Enter amount to bet")
tri = Polygon(Point(310,175),Point(344,175),Point(327,265))
tri.setFill("black")
tri.setOutline("white")
tri.draw(win)

multiplier = "0x"
mult = Text(Point(327,350),multiplier)
mult.setStyle("bold"),mult.setFill("white")
mult.setSize(30)

t = 1
first = True
while t == 1:
    if first == True:
        f1 = Rectangle(Point(5,275),Point(130,400))
        f1.setFill(color=colorPicker())
        f1.setOutline("white")
        f1.draw(win)

        f2 = Rectangle(Point(135,275),Point(260,400))
        f2.setFill(color=colorPicker())
        f2.setOutline("white")
        f2.draw(win)

        f3 = Rectangle(Point(265,275),Point(390,400))
        f3.setFill(color=colorPicker())
        f3.setOutline("white")
        f3.draw(win)

        f4 = Rectangle(Point(395,275),Point(520,400))
        f4.setFill(color=colorPicker())
        f4.setOutline("white")
        f4.draw(win)

        f5 = Rectangle(Point(525,275),Point(650,400))
        f5.setFill(color=colorPicker())
        f5.setOutline("white")
        f5.draw(win)
        first = False
####################################################
    r1 = Rectangle(Point(0,275),Point(-125,400))
    r1.setFill(color=colorPicker())
    r1.setOutline("white")
    r1.draw(win)

    r2 = Rectangle(Point(-130,275),Point(-255,400))
    r2.setFill(color=colorPicker())
    r2.setOutline("white")
    r2.draw(win)

    r3 = Rectangle(Point(-260,275),Point(-385,400))
    r3.setFill(color=colorPicker())
    r3.setOutline("white")
    r3.draw(win)
    
    r4 = Rectangle(Point(-390,275),Point(-515,400))
    r4.setFill(color=colorPicker())
    r4.setOutline("white")
    r4.draw(win)
    
    r5 = Rectangle(Point(-520,275),Point(-645,400))
    r5.setFill(color=colorPicker())
    r5.setOutline("white")
    r5.draw(win)

    rollbox = Rectangle(Point(227.5,500),Point(427.5,590))
    rollbox.setFill("green")
    rollbox.setOutline("white")
    rollbox.draw(win)
    
    rolltext = Text(Point(327.5,545),"Press ENTER to ROLL")
    rolltext.setStyle("bold"),rolltext.setFill("white")
    rolltext.draw(win)

    clicked = True
    while clicked == True:
        bet = 0
        test = win.getKey()
        if test == "Return":
            mult.undraw()
            valid = True
            try:
                bet = int(betbox.getText())
            except:
                print("Not Valid")
                print("Got input:",betbox.getText())
                valid = False
            if bet <= balance and valid == True:
                for i in range(650):
                    timer()
                    roll(1,0)
                erase_f()
                for i in range(1300):
                    reset_f(-1,0)
                ###############################
                color2 = colorPicker()
                f1.setFill(color=colorPicker())
                f2.setFill(color=colorPicker())
                f3.setFill(color2)
                land = color2
                f4.setFill(color=colorPicker())
                f5.setFill(color=colorPicker())
                ###############################
                f1.draw(win),f2.draw(win),f3.draw(win),f4.draw(win),f5.draw(win)
                for i in range(650):
                    timer()
                    roll(1,0)
                erase_r()
                clicked = False
            
                if land == "red":
                    multiplier = "0x"
                    for i in range(bet):
                        timer2()
                        money.undraw()
                        balance -= 1
                        money = Text(Point(327,100),balance)
                        money.setStyle("bold"),money.setFill("yellow")
                        money.setSize(30)
                        money.draw(win)
                    mult = Text(Point(327,350),multiplier)
                    mult.setStyle("bold"),mult.setFill("white")
                    mult.setSize(30)
                    mult.draw(win)
                if land == "purple":
                    multiplier = "10x"
                    for i in range(bet):
                        timer2()
                        money.undraw()
                        balance += 10
                        money = Text(Point(327,100),balance)
                        money.setStyle("bold"),money.setFill("yellow")
                        money.setSize(30)
                        money.draw(win)
                    mult = Text(Point(327,350),multiplier)
                    mult.setStyle("bold"),mult.setFill("white")
                    mult.setSize(30)
                    mult.draw(win)
                if land == "blue":
                    multiplier = "2x"
                    for i in range(bet):
                        timer2()
                        money.undraw()
                        balance += 1
                        money = Text(Point(327,100),balance)
                        money.setStyle("bold"),money.setFill("yellow")
                        money.setSize(30)
                        money.draw(win)
                    mult = Text(Point(327,350),multiplier)
                    mult.setStyle("bold"),mult.setFill("white")
                    mult.setSize(30)
                    mult.draw(win)
            else:
                break
                    

            


        



