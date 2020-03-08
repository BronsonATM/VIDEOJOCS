import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def draw_ice():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_ice()
    draw_snow_person(on_draw.snow_person1_x, on_draw.snow_person1_y)
    draw_snow_person(on_draw.snow_person2_x, on_draw.snow_person2_y)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 5
    on_draw.snow_person1_y += 5
    on_draw.snow_person2_x -= 5
    on_draw.snow_person2_y -= 5



# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 0
on_draw.snow_person1_y = 0
on_draw.snow_person2_x = 800
on_draw.snow_person2_y = 800


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()