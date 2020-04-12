import arcade
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
def suelo():
    """Dibuja el suelo"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)
def cabeza(x,y):
    """Dibuja la cabeza"""
    arcade.draw_circle_filled(300+x, 200+y, 10, arcade.color.YELLOW)
    arcade.draw_circle_filled(296+x, 205+y, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(304+x, 205+y, 3, arcade.color.BLACK)
def on_draw(delta_time):
    arcade.start_render()
    suelo()
    cabeza(on_draw.coordenada_x, on_draw.coordenada_y)
    cabeza(-20, -20)
    on_draw.coordenada_x +=1
    on_draw.coordenada_y +=2
on_draw.coordenada_x=0
on_draw.coordenada_y=0
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)




    arcade.schedule(on_draw,1/60)
    arcade.run()

main()
