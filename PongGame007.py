import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"

# dit heb ik van de arcade site
class TextButton:
    #hier geef je variabelen mee voor de buttons, zoals de grootte en de tekst die er in moet komen.
    def __init__(self, center_x, center_y, width, height, text, font_size=18, font_face="Arial", face_color=arcade.color.LIGHT_GRAY, highlight_color=arcade.color.WHITE, shadow_color=arcade.color.GRAY, button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height


    def draw(self):
        #hier zeg je dat de buttons getekend moeten worden
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # onderkant horizontaal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2, self.center_x + self.width / 2, self.center_y - self.height / 2, color, self.button_height)

        # rechts verticaal
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2, self.center_x + self.width / 2, self.center_y + self.height / 2, color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # bovenkant horizontaal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2, self.center_x + self.width / 2, self.center_y + self.height / 2, color, self.button_height)

        # links verticaal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2, self.center_x - self.width / 2, self.center_y + self.height / 2, color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y, arcade.color.BLACK, font_size=self.font_size, width=self.width, align="center", anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True


    def on_release(self):
        self.pressed = False

#hier zeg je dat hij moet kijken of de buttons worden aan gedrukt of niet
def check_mouse_press_for_buttons(x, y, button_list):
    
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

def check_mouse_release_for_buttons(_x, _y, button_list):

    for button in button_list:
        if button.pressed:
            button.on_release()

class IncreaseButton(TextButton):
    #variabelen voor de level increase button
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 150, 50, "Increase difficulty", 12, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class DecreaseButton(TextButton):
    #variabelen voor de level decrease button
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 150, 50, "Decrease difficulty", 12, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()
     
class StartLevelButton(TextButton):
    #variabelen voor de level start button
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 150, 50, "Start Level", 12, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class InstructionButton(TextButton):
    #variabelen voor de level start button
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 150, 50, "Instructions", 12, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class GoBackButton(TextButton):
    #variabelen voor de level start button
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 150, 50, "Go Back", 12, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        #variabelen voor de buttons en de actie die de buttons moeten geven

        self.button_list = []

        increase_button = IncreaseButton(200, 300, self.difficulty_increase)
        self.button_list.append(increase_button)

        decrease_button = DecreaseButton(400, 300, self.difficulty_decrease)
        self.button_list.append(decrease_button)

        startlevel_button = StartLevelButton(600, 300, self.start_game)
        self.button_list.append(startlevel_button)

        instruction_button = InstructionButton(720, 570, self.instruction_game)
        self.button_list.append(instruction_button)

        self.difficulty = 0

    #laat menu view zien
    def on_show(self): 
        arcade.set_background_color(arcade.color.BLACK)
    
    #tekenen de buttons
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=50, anchor_x="center")
        
        for button in self.button_list:
            button.draw()
        
        output = f"Level difficulty  =  {self.difficulty}" 
        arcade.draw_text(output, SCREEN_WIDTH - 520, 200, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        pass
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
       
        check_mouse_release_for_buttons(x, y, self.button_list)

    #de acties van de buttons
    def difficulty_decrease(self):
        self.difficulty -= 1

    def difficulty_increase(self):
        self.difficulty += 1
    
    def start_game(self):
        my_game_view = MyGameView(self.difficulty)
        self.window.show_view(my_game_view)
    
    def instruction_game(self):
        instruction_view = InstructionView()
        self.window.show_view(instruction_view)

class Ball():
    def __init__(self, difficulty):
        # Hier leg je uit wat alle variabbelen zijn
        self.position_x = 100
        self.position_y = 100
        self.change_x = 4+difficulty
        self.change_y = 4+difficulty
        self.radius = 20

    def setup(self):
        pass

    def on_draw(self):
        # hier teken je objecten.
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, arcade.color.WHITE)
        

    def on_update(self, delta_time):
        # hier zeg je dat de positie van x en y steeds met 3 omhoog moet gaan
        self.position_x = self.position_x + self.change_x
        self.position_y = self.position_y + self.change_y

        # Hier zeg je dat de bal om moet draaien als hij de bovenkant en onderkant raakt.
        if self.position_y + self.radius > SCREEN_HEIGHT and self.change_y > 0:
            self.change_y = self.change_y * -1

        if self.position_y - self.radius < 0 and self.change_y < 0:
            self.change_y = self.change_y * -1

class Paddle():
    def __init__(self, x, color):
        # hier leg je uit wat de variabellen zijn van de Padlles
        self.x = x
        self.y = SCREEN_HEIGHT / 2
        self.change_y = 0
        self.width = 30
        self.height = 90
        self.color = color

    def on_draw(self):
        #hier zeg je dat hij de paddle moet tekenen, self.x geef je later mee
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def on_update(self, delta_time):
        # hier leg je uit dat je de self.y update en dan de self.change_y er bij doet
        self.y = self.y + self.change_y
   
class Player1():
    def __init__ (self):
        self.score = 0

class Player2():
    def __init__ (self):
        self.score = 0

class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        
        self.button_list2 = []

        go_back_button = GoBackButton(720, 570, self.go_back)
        self.button_list2.append(go_back_button)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150, arcade.color.WHITE, font_size=50, anchor_x="center")
        
        for button in self.button_list2:
            button.draw()
        
        output = f"If you want to pause the game press P" 
        arcade.draw_text(output, SCREEN_WIDTH - 620, 400, arcade.color.WHITE, 20)

        output = f"If you want to resume the game press ESCAPE" 
        arcade.draw_text(output, SCREEN_WIDTH - 620, 350, arcade.color.WHITE, 20)

        output = f"Team Blue uses the Arrow Up to move the paddle up  " 
        arcade.draw_text(output, SCREEN_WIDTH - 620, 300, arcade.color.WHITE, 20)
        
        output = f"and uses the Arrow down to move the paddle down " 
        arcade.draw_text(output, SCREEN_WIDTH - 620, 280, arcade.color.WHITE, 20)

        output = f"Team Red uses the W key to move the paddle up  " 
        arcade.draw_text(output, SCREEN_WIDTH - 620, 230, arcade.color.WHITE, 20)
        
        output = f"and the S key to move the paddle down   " 
        arcade.draw_text(output, SCREEN_WIDTH - 620, 210, arcade.color.WHITE, 20)

        output = f"First team that has 10 points wins   " 
        arcade.draw_text(output, SCREEN_WIDTH - 620, 160, arcade.color.WHITE, 20)

    def go_back(self):
        menu_view2 = MenuView()
        self.window.show_view(menu_view2)
  
    def on_mouse_press(self, x, y, button, key_modifiers):
        
        check_mouse_press_for_buttons(x, y, self.button_list2)

    def on_mouse_release(self, x, y, button, key_modifiers):
       
        check_mouse_release_for_buttons(x, y, self.button_list2)

class MyGameView(arcade.View):

    #hier zeg je dat je de vorige getypte dingen ook echt moet uitvoeren.
    def __init__(self, difficulty):
        # super wilt zeggen dat hij bovenliggende classes nodig heeft
        super().__init__()

        self.difficulty = difficulty
        self.ball = Ball(difficulty)
        self.paddle1 = Paddle(50, arcade.color.RED) 
        self.paddle2 = Paddle(750, arcade.color.BLUE)
        self.total_time = 0.0
        self.Player1 = Player1()
        self.Player2 = Player2()

        #geluidjes invoeren
        self.paddle_sound = arcade.load_sound('paddlepop.wav')

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.total_time = 0.0
        self.Player1.score = 0
        self.Player2.score = 0

    def on_draw(self):
        # hier leg je uit dat arcade moet gaan tekenen en renderen.
        arcade.start_render()
        self.ball.on_draw()
        self.paddle1.on_draw()
        self.paddle2.on_draw()
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        #arcade.draw_text(output, 300, 500, arcade.color.WHITE_SMOKE, 30)
        output = f" {self.Player1.score}  :  {self.Player2.score}" 
        arcade.draw_text(output, 350, 500, arcade.color.WHITE, 30)

        debug = f"cx:{self.ball.change_x} | cy:{self.ball.change_y}" 
        arcade.draw_text(debug, 0, 100, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        self.ball.on_update(delta_time)
        self.paddle1.on_update(delta_time)
        self.paddle2.on_update(delta_time)
        self.total_time += delta_time
        
        # hier zeg je dat als de ball over de rechterkant gaat dat je dan 1 punt bij het andere team moet doen
        if self.ball.position_x >= SCREEN_WIDTH:
            self.ball.position_x = 700
            self.ball.position_y = 500
            self.Player1.score = self.Player1.score + 1
            self.ball.change_x = self.ball.change_x * -1
           
           #als de score hoger is dan 3 moet de bal sneller gaan bewegen
            if self.Player1.score == 5:
                if self.ball.change_x > 0:
                    self.ball.change_x = self.ball.change_x + 1
                else:
                    self.ball.change_x = self.ball.change_x - 1
                if self.ball.change_y > 0:
                    self.ball.change_y = self.ball.change_y + 1
                else:
                    self.ball.change_y = self.ball.change_y - 1
            
            if self.Player1.score == 7:
                if self.ball.change_x > 0:
                    self.ball.change_x = self.ball.change_x + 1
                else:
                    self.ball.change_x = self.ball.change_x - 1
                if self.ball.change_y > 0:
                    self.ball.change_y = self.ball.change_y + 1
                else:
                    self.ball.change_y = self.ball.change_y - 1
            
            if self.Player1.score == 9:
                if self.ball.change_x > 0:
                    self.ball.change_x = self.ball.change_x + 1
                else:
                    self.ball.change_x = self.ball.change_x - 1
                if self.ball.change_y > 0:
                    self.ball.change_y = self.ball.change_y + 1
                else:
                    self.ball.change_y = self.ball.change_y - 1
                
        # hier zeg je dat als de ball over de linkerkant gaat dat je dan 1 punt bij het andere team moet doen
        if self.ball.position_x <= 0:
            self.ball.position_x = SCREEN_WIDTH - 100
            self.ball.position_y = 100
            self.Player2.score = self.Player2.score + 1
            self.ball.change_x = self.ball.change_x * -1
            
        #als de score hoger is dan 3 moet de bal sneller gaan bewegen
            if self.Player2.score == 5:
                if self.ball.change_x > 0:
                    self.ball.change_x = self.ball.change_x + 1
                else:
                    self.ball.change_x = self.ball.change_x - 1
                if self.ball.change_y > 0:
                    self.ball.change_y = self.ball.change_y + 1
                else:
                    self.ball.change_y = self.ball.change_y - 1
            
            if self.Player2.score == 7:
                if self.ball.change_x > 0:
                    self.ball.change_x = self.ball.change_x + 1
                else:
                    self.ball.change_x = self.ball.change_x - 1
                if self.ball.change_y > 0:
                    self.ball.change_y = self.ball.change_y + 1
                else:
                    self.ball.change_y = self.ball.change_y - 1
            
            if self.Player2.score == 9:
                if self.ball.change_x > 0:
                    self.ball.change_x = self.ball.change_x + 1
                else:
                    self.ball.change_x = self.ball.change_x - 1
                if self.ball.change_y > 0:
                    self.ball.change_y = self.ball.change_y + 1
                else:
                    self.ball.change_y = self.ball.change_y - 1

        #Hier zeg je dat de ball moet omdraaien als je de rechter paddle raakt
        if self.ball.position_x + self.ball.radius >= self.paddle2.x and self.ball.position_y <= self.paddle2.y + self.paddle2.height/2 and self.ball.position_y >= self.paddle2.y - self.paddle2.height/2:
            self.ball.change_x = self.ball.change_x * -1  
            arcade.play_sound(self.paddle_sound)
        
        #Hier zeg je dat de ball moet omdraaien als je linkerpaddle raakt
        if self.ball.position_x - self.ball.radius < self.paddle1.x and self.ball.position_y <= self.paddle1.y + self.paddle1.height/2 and self.ball.position_y >= self.paddle1.y - self.paddle1.height/2 :
            self.ball.change_x = self.ball.change_x * -1 
            arcade.play_sound(self.paddle_sound)

        #hier zeg je dat als de score van speler 1 of speler 2 10 is dat hij dan naar het Game over scherm moet gaan
        if self.Player1.score == 10:
            game_over_view1 = GameOverView1()
            self.window.show_view(game_over_view1)
        
        if self.Player2.score == 10:
            game_over_view2 = GameOverView2()
            self.window.show_view(game_over_view2)

    def on_key_press(self, symbol, key_modifiers):
        # als je de key indrukt dan gaat hij 7 pixels omhoog of 7 pixels omlaag
        if symbol == arcade.key.W:
            self.paddle1.change_y = 7
    
        if symbol == arcade.key.S:
            self.paddle1.change_y = -7
        
        if symbol == arcade.key.UP:
            self.paddle2.change_y = 7
        
        if symbol == arcade.key.DOWN:
            self.paddle2.change_y = -7
        
        #pause en resume keys. als je P indrukt dan gaat hij op pauze en als je op ESCAPE drukt dan gaat hij verder. 
        if symbol == arcade.key.P:
            self.ball.change_x = 0
            self.ball.change_y = 0
        
        if symbol == arcade.key.ESCAPE:
            self.ball.change_x = 4 + self.difficulty
            self.ball.change_y = 4 + self.difficulty

    def on_key_release(self, symbol, mod):
        #als je de key lostlaat dan stop de paddle met bewegen
        if  symbol == arcade.key.W:
            self.paddle1.change_y = 0

        if symbol == arcade.key.S:
            self.paddle1.change_y = 0

        if  symbol == arcade.key.UP:
            self.paddle2.change_y = 0

        if symbol == arcade.key.DOWN:
            self.paddle2.change_y = 0

class GameOverView2(arcade.View):
    def __init__(self):
        #hier zorg je ervoor dat hij een geluid maakt als speler 2 wint
        super().__init__()
        self.point_sound = arcade.load_sound('ohyeah.wav')

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.play_sound(self.point_sound)

    def on_draw(self):
        arcade.start_render()
       
        arcade.draw_text("Blue Team won!", 230, 400, arcade.color.WHITE, 54)

class GameOverView1(arcade.View):
    def __init__(self):
        #hier zeg je dat hij een geluidje maakt als player 1 wint
        super().__init__()
        self.point_sound = arcade.load_sound('ohyeah.wav')

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.play_sound(self.point_sound)

    def on_draw(self):
        arcade.start_render()
       
        arcade.draw_text("Red team won!", 230, 400, arcade.color.WHITE, 54)
        
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

# hij checkt hier of het proces van python het hoofdproces is.
if __name__ == "__main__":
    main()