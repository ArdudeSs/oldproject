"""This Model class is meant to contain all of the game's data, """
"""as well as other methods it might need to have. """

from classes import Entity, Egg, Eggnemy, Boss, Teaspoon, AttackHitbox, WorldBorder
from random import randint

class Model:

    def __init__(self, screen_x: int, screen_y: int):
        self.screen_x: int = screen_x
        self.screen_y: int = screen_y
        self._worldborder: WorldBorder = WorldBorder(screen_x, screen_y)
        self._egg: Egg = Egg(
            screen_x // 2,
            screen_y // 2,
            5,
            20,
            5,
            20,
            25,
            20,
            )
        self._eggnemies: dict[int, Eggnemy] = {}
        self._next_eggnemy_id = 0
        self._is_game_over: bool = False

    def add_eggnemy(self, eggnemy: Eggnemy):
        self._eggnemies.update({self._next_eggnemy_id : eggnemy})
        self._next_eggnemy_id += 1

    @property
    def get_worldborder(self):
        return self._worldborder
    
    @property
    def eggnemies(self):
        return self._eggnemies

    @property
    def get_egg(self):
        return self._egg
    
    def spawn_n_eggnemies(self, n):

        for i in range(n):
            self.add_eggnemy(Eggnemy(
                randint(0, self.screen_x),
                randint(0, self.screen_y),
                3,
                10,
                1,
                1,
                15,
                10
                ))

    def handle_attacks(self, attacking: bool):
        for key, eggnemy in self.eggnemies.items():
            if eggnemy.curr_hp > 0:
                if self.in_range(self.get_egg, eggnemy) and attacking:
                    eggnemy.take_damage(self.get_egg.get_attack_damage)

                if self.is_colliding(self.get_egg, eggnemy) and not self.get_egg.get_iframes:
                    self.get_egg.take_damage(eggnemy.get_attack_damage)
                    self.get_egg.replenish_iframes()

    def in_range(self, egg: Egg, eggnemy: Eggnemy):
        # This function determines if an eggnemy is in range of the egg.
        egg_attack_hitbox = AttackHitbox(egg)

        if (eggnemy.get_x > egg_attack_hitbox.get_x + egg_attack_hitbox.get_length) or (eggnemy.get_x + eggnemy.get_length < egg_attack_hitbox.get_x):
            return False

        if (eggnemy.get_y > egg_attack_hitbox.get_y + egg_attack_hitbox.get_height) or (eggnemy.get_y + eggnemy.get_height < egg_attack_hitbox.get_y):
            return False

        return True

    def is_colliding(self, entity1: Entity, entity2: Entity):

        if entity1.get_x + entity1.get_length < entity2.get_x or entity1.get_x > entity2.get_x + entity2.get_length:
            return False

        if entity1.get_y + entity1.get_height < entity2.get_y or entity1.get_y > entity2.get_y + entity2.get_height:
            return False

        return True
