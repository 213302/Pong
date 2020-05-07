import arcade
import math
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"
class punten():
    def __init__(self,score,x,y):
        self.score=score
        self.x=x
        self.y=y
    def update(self,score1):
        self.score=score1
    def draw(self):
        arcade.draw_text(f"{self.score}",self.x,self.y,arcade.color.WHITE,50)
class peddel():
    def __init__(self,beginx,beginy,gaatomhoog,gaatdown):
        self.beginx=beginx
        self.beginy=beginy
        self.gaatomhoog=gaatomhoog
        self.gaatdown=gaatdown
    def stopup(self):
        self.gaatomhoog=False
    def stopdown(self):
        self.gaatdown=False
    def moveup(self):
        self.gaatomhoog=True
    def gadown(self):
        self.gaatdown=True
    def update(self,bally,enemy):
        if self.beginy<=25 and enemy==False:
            self.gaatdown=False
        if self.beginy>=575 and enemy==False:
            self.gaatomhoog=False
        #print(self.gaatdown, end="")
        #print(" ", end="")
        #print(self.gaatomhoog, end="")
        #print(" ", end="")
        if self.gaatdown and enemy==False:
            self.beginy-=5
        if self.gaatomhoog and enemy==False:
            self.beginy+=5
        if enemy:
            if bally>self.beginy:
                self.beginy+=2
            if bally<self.beginy:
                self.beginy-=2
    def draw(self):
        arcade.draw_rectangle_filled(self.beginx,self.beginy,10,50,arcade.color.WHITE)
class bal():
    def __init__(self, startx,starty,speedx,speedy,react):
        self.react = react 
        self.starty = starty
        self.startx = startx
        self.speedx = speedx
        self.speedy = speedy
        self.scoree=0
        self.scorep=0
    def draw(self):
        arcade.draw_circle_filled(self.startx,self.starty,5,arcade.color.WHITE)
        #arcade.draw_circle_filled(100,self.starty,5,arcade.color.WHITE)
    def updated(self,yblockplayer,yblockenemy):
        self.startx=self.startx+self.speedx
        self.starty=self.starty+self.speedy
        if self.starty>=595:
            self.speedy=self.speedy*-1
        if self.startx<=15 and yblockplayer+25>self.starty and yblockplayer-25<self.starty:
            if self.speedy>=0:
                self.speedx=(math.sqrt(((((yblockplayer+25)-self.starty)/50)*4)*((((yblockplayer+25)-self.starty)/50)*4)))
                self.speedy=(4-math.sqrt(((((yblockplayer+25)-self.starty)/50)*4)*((((yblockplayer+25)-self.starty)/50)*4)))
                self.speedx+=1
                self.speedy+=1
            if self.speedy<0:
                self.speedx=math.sqrt(((((yblockplayer-25)-self.starty)/50)*4)*((((yblockplayer-25)-self.starty)/50)*4))
                self.speedy=(4-math.sqrt(((((yblockplayer-25)-self.starty)/50)*4)*((((yblockplayer-25)-self.starty)/50)*4)))*-1
                self.speedx+=1
                self.speedy-=1
        if math.sqrt((self.startx-10)*(self.startx-10)+((yblockplayer-25)-self.starty)*((yblockplayer-25)-self.starty))<5 or math.sqrt((self.startx-10)*(self.startx-10)+((yblockplayer+25)-self.starty)*((yblockplayer+25)-self.starty))<5:
            self.speedx=self.speedx*-1
        if yblockplayer+30>=self.starty and yblockplayer-30<=self.starty and self.startx<=11:
            self.speedy=self.speedy*-1
            self.starty=self.starty+self.speedy*5
        if self.starty<=5:
            self.speedy=self.speedy*-1
        if self.startx<=0:
            self.scoree+=1
            self.startx=400
            self.starty=300
            self.speedy=3
            self.speedx=3
        
        if self.startx>=785 and yblockenemy+25>self.starty and yblockenemy-25<self.starty:
            if self.speedy>=0:
                self.speedx=(math.sqrt(((((yblockenemy+25)-self.starty)/50)*4)*((((yblockenemy+25)-self.starty)/50)*4)))*-1
                self.speedy=(4-math.sqrt(((((yblockenemy+25)-self.starty)/50)*4)*((((yblockenemy+25)-self.starty)/50)*4)))
                self.speedx-=1
                self.speedy+=1
            if self.speedy<0:
                self.speedx=math.sqrt(((((yblockenemy-25)-self.starty)/50)*4)*((((yblockenemy-25)-self.starty)/50)*4))*-1
                self.speedy=(4-math.sqrt(((((yblockenemy-25)-self.starty)/50)*4)*((((yblockenemy-25)-self.starty)/50)*4)))*-1
                self.speedx-=1
                self.speedy-=1
        if math.sqrt((self.startx+10)*(self.startx+10)+((yblockenemy-25)-self.starty)*((yblockenemy-25)-self.starty))<5 or math.sqrt((self.startx+10)*(self.startx+10)+((yblockenemy+25)-self.starty)*((yblockenemy+25)-self.starty))<5:
            self.speedx=self.speedx*-1
        if yblockenemy+30>=self.starty and yblockenemy-30<=self.starty and self.startx>=792:
            self.speedy=self.speedy*-1
            self.starty=self.starty+3*5
        if self.startx>=800:
            self.scorep+=1
            self.startx=400
            self.starty=300
            self.speedy=3
            self.speedx=3
    def rotatex(self):
        self.speedx*=-1
class MyGame(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.peddelplay = peddel(5,300,False,False)
        self.peddelenemy = peddel(795,300,False,False)
        self.bal1 = bal(400,300,3,3,True)
        self.scoree = punten(0,300,500)
        self.scorep = punten(0,500,500)

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.bal1.draw()
        self.peddelplay.draw()
        self.peddelenemy.draw()
        self.scoree.draw()
        self.scorep.draw()
        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        self.bal1.updated(self.peddelplay.beginy,self.peddelenemy.beginy)
        self.peddelplay.update(1,False)
        self.peddelenemy.update(self.bal1.starty,True)
        self.scoree.update(self.bal1.scoree)
        self.scorep.update(self.bal1.scorep)
        
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass
    def on_key_press(self, key, key_modifiers):
        if key==119:
            self.peddelplay.moveup()
            #self.peddelenemy.moveup()
        if key==115:
            self.peddelplay.gadown()
            #self.peddelenemy.gadown()
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        if key==119 or key==115:
            self.peddelplay.stopup()
            #self.peddelenemy.stopup()
            self.peddelplay.stopdown()
            #self.peddelenemy.stopdown()
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()