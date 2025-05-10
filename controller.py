from model import Model
from view import View
from classes import Egg, Eggnemy, WorldBorder

class Controller:

    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

    def start(self, fps: int):
        self._model.spawn_n_eggnemies(5)
        model = self._model
        self._view.start(fps, self.update, self.draw)

    def update(self):
        self.handle_egg_movement()
        self._model.handle_attacks(self.is_player_attacking())
        if self._model.get_egg.get_iframes > 0:
            self._model.get_egg.decrement_iframes()

        for key, eggnemy in self._model.eggnemies.items():
            if self._model.get_egg.curr_hp > 0 and eggnemy.curr_hp > 0:
                self.handle_eggnemy_movement(self._model.get_egg, eggnemy)

    def is_player_attacking(self):
        return self._view.L_was_pressed()

    def draw(self):
        self._view.clear_screen()

        self._view.draw_world_border(self._model.get_worldborder)

        if self._model.get_egg.curr_hp > 0:
            self._view.draw_egg(self._model.get_egg)
            self._view.draw_entity_hp(self._model.get_egg)
            self._view.debug_draw_iframes(self._model.get_egg)

            if self.is_player_attacking():
                self._view.draw_rectangular_range_indicator_attacking(self._model.get_egg)
            else:
                self._view.draw_rectangular_range_indicator(self._model.get_egg)

        for key, eggnemy in self._model.eggnemies.items():
            if eggnemy.curr_hp > 0:
                self._view.draw_eggnemy(eggnemy)
                self._view.draw_entity_hp(eggnemy)

    def handle_eggnemy_movement(self, egg: Egg, eggnemy: Eggnemy):

        if eggnemy.get_x >= egg.get_x:
            eggnemy.move_left(eggnemy.get_speed)

        elif eggnemy.get_x <= egg.get_x:
            eggnemy.move_right(eggnemy.get_speed)

        if eggnemy.get_y >= egg.get_y:
            eggnemy.move_up(eggnemy.get_speed)

        elif eggnemy.get_y <= egg.get_y:
            eggnemy.move_down(eggnemy.get_speed)

    def handle_egg_movement(self):
        """Code block that checks for WASD being pressed using the view's methods and moves the egg"""
        """It violates DRY, kind of."""
        egg: Egg = self._model.get_egg
        s = egg.get_speed
        speed: int = egg.get_speed
        border: WorldBorder = self._model.get_worldborder

        if self._view.A_was_pressed() and egg.get_x > border.get_x:
            # self._model.get_egg.move_left(s) (phase 0 movement implementation)
            border.move_right(s)

            for key, eggnemy in self._model.eggnemies.items():
                eggnemy.move_right(s)

        if self._view.S_was_pressed() and egg.get_y + egg.get_height < border.get_y + border.get_height - 5: # - 5 added so the egg is flush against the wall
            # self._model.get_egg.move_down(egg.get_speed) (phase 0 movement implementation)
            border.move_up(s)

            for key, eggnemy in self._model.eggnemies.items():
                eggnemy.move_up(s)

        if self._view.W_was_pressed() and egg.get_y > border.get_y:
            # self._model.get_egg.move_up(egg.get_speed) (phase 0 movement implementation)
            border.move_down(s)

            for key, eggnemy in self._model.eggnemies.items():
                eggnemy.move_down(s)

        if self._view.D_was_pressed() and egg.get_x + egg.get_length < border.get_x + border.get_length + 2: # + 2 added so the egg is flush against the wall
            # self._model.get_egg.move_right(egg.get_speed) (phase 0 movement implementation)
            border.move_left(s)

            for key, eggnemy in self._model.eggnemies.items():
                eggnemy.move_left(s)

