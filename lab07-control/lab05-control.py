""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
def suelo():
    """Dibuja el suelo"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)
class emoji:
    def __init__(self, position_x, position_y, change_x, change_y, radio, color_Fondo, color_Ojos):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radio = radio
        self.color_Fondo = color_Fondo
        self.color_Ojos = color_Ojos
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radio, self.color_Fondo)
        arcade.draw_circle_filled(self.position_x - 4, self.position_y + 5, self.radio/3.33, self.color_Ojos)
        arcade.draw_circle_filled(self.position_x + 4, self.position_y + 5, self.radio/3.33, self.color_Ojos)

    def update(self):
        # Mueve el emoji
        self.position_y += self.change_y
        self.position_x += self.change_x

        # Detecta cuando llega el emoji al borde
        if self.position_x < self.radio:
            self.position_x = self.radio

        if self.position_x > SCREEN_WIDTH - self.radio:
            self.position_x = SCREEN_WIDTH - self.radio

        if self.position_y < self.radio:
            self.position_y = self.radio

        if self.position_y > SCREEN_HEIGHT - self.radio:
            self.position_y = SCREEN_HEIGHT - self.radio


class MyGame(arcade.Window):
    """ Our Custom Window Class"""


    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        #Esconde el puntero
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AUBURN)

        self.emoji = emoji(300, 300, 0, 0, 10, arcade.color.YELLOW_GREEN, arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.emoji.draw()
        suelo()

    def update(self, delta_time):
        self.emoji.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.emoji.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.emoji.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.emoji.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.emoji.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.emoji.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.emoji.change_y = 0




def main():
    window = MyGame()
    arcade.run()


main()