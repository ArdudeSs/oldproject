"""This file will contain the view."""

# Should we add a range indicator for the egg, by the way?
# I think we could use circb or rectb for this.

import pyxel
from classes import Egg, Entity, WorldBorder

class View:

    def __init__(self, SCREEN_X: int, SCREEN_Y: int):
        self._SCREEN_X: int = SCREEN_X
        self._SCREEN_Y: int = SCREEN_Y

    def start(self, fps: int, updater, drawer):
        """Update and Draw are methods of the controller"""
        pyxel.init(self._SCREEN_X, self._SCREEN_Y, fps=fps)
        pyxel.run(updater, drawer)

    def draw_world_border(self, worldborder: WorldBorder):
        pyxel.rectb(worldborder.get_x, worldborder.get_y, worldborder.get_length, worldborder.get_height, 7)

    def draw_lose_message(self, egg: Egg):
        pyxel.text(egg.get_x, egg.get_y - 50, f"You lost!", 7)

    def draw_win_message(self, egg: Egg):
        pyxel.text(egg.get_x, egg.get_y - 50, f"You won!", 7)

    def debug_draw_iframes(self, egg: Egg):
        pyxel.text(egg.get_x, egg.get_y + 50, f"iframes: {egg.get_iframes}", 7)

    def draw_entity_hp(self, entity: Entity):
        pyxel.text(entity.get_x, entity.get_y + 30, f"{entity.curr_hp} / {entity.max_hp}", 7)

    def draw_egg(self, egg: Egg):
        pyxel.rect(egg.get_x, egg.get_y, egg.get_height, egg.get_length, 7)

    def clear_screen(self):
        pyxel.cls(0)

    def draw_eggnemy(self, entity: Entity):
        pyxel.rect(entity.get_x, entity.get_y, entity.get_height, entity.get_length, 6)

    def draw_circular_range_indicator(self, egg: Egg):
        pyxel.circb(
            egg.get_x+(egg.get_length // 2),
            egg.get_y+(egg.get_height // 2),
            egg.get_attack_range,
            8
            )

    def draw_rectangular_range_indicator_attacking(self, egg: Egg):
        egg_x = egg.get_x
        egg_y = egg.get_y
        egg_range = egg.get_attack_range
        egg_length = egg.get_length
        egg_height = egg.get_height

        pyxel.rectb(
            egg_x - egg_range,
            egg_y - egg_range,
            egg_length + 2*egg_range,
            egg_height + 2*egg_range,
            8
            )

    def draw_rectangular_range_indicator(self, egg: Egg):
        egg_x = egg.get_x
        egg_y = egg.get_y
        egg_range = egg.get_attack_range
        egg_length = egg.get_length
        egg_height = egg.get_height


        pyxel.rectb(
            egg_x - egg_range,
            egg_y - egg_range,
            egg_length + 2*egg_range,
            egg_height + 2*egg_range,
            10
            )

    def one_was_pressed(self):
        return pyxel.btn(pyxel.KEY_1)

    def two_was_pressed(self):
        return pyxel.btn(pyxel.KEY_2)

    def three_was_pressed(self):
        return pyxel.btn(pyxel.KEY_3)

    def A_was_pressed(self):
        return pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)

    def W_was_pressed(self):
        return pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)

    def S_was_pressed(self):
        return pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN)

    def D_was_pressed(self):
        return pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)

    def L_was_pressed(self):
        return pyxel.btn(pyxel.KEY_L)
