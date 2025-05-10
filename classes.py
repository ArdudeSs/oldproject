"""This file will contain the classes for Implementation 1."""

from dataclasses import dataclass




class Entity:
    # This class represents entities, which include the Egg
    # and the Eggnemies.
    def __init__(self, x: int, y: int, speed: int, max_hp: int, attack_damage: int, attack_range: int, length: int, height: int):

        self._length: int = length
        self._height: int = height
        self._x: int = x 
        self._y: int = y
        self._s: int = speed 
        """Speed is added or subtracted to an entity's position depending on which key is pressed (if 
        the entity is an egg) or depending on the egg's position if the entity is an eggnemy."""
        self._max_hp: int = max_hp
        self._curr_hp: int = max_hp
        self._attack_damage: int = attack_damage # Damage taken by enemies attacked by the entity
        self._attack_range: int = attack_range

    @property
    def get_speed(self):
        return self._s

    @property
    def get_length(self):
        return self._length

    @property
    def get_height(self):
        return self._height
    
    @property
    def get_x(self):
        return self._x

    @property
    def get_y(self):
        return self._y

    @property
    def get_hp(self):
        return self._curr_hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def curr_hp(self):
        return self._curr_hp

    @property
    def get_attack_damage(self):
        return self._attack_damage
    
    def take_damage(self, damage: int):
        if self._curr_hp - damage <= 0:
            self._curr_hp = 0
        else:
            self._curr_hp -= damage

    def move_right(self, s: int):
        self._x += s

    def move_left(self, s: int):
        self._x -= s

    def move_up(self, s: int):
        self._y -= s

    def move_down(self, s: int):
        self._y += s

class Egg(Entity):
    def __init__(self, x: int, y: int, speed: int, max_hp: int, attack_damage: int, attack_range: int, length: int, height: int):
        self._length: int = length
        self._height: int = height
        self._x: int = x 
        self._y: int = y
        self._s: int = speed 
        """Speed is added or subtracted to an entity's position depending on which key is pressed (if 
        the entity is an egg) or depending on the egg's position if the entity is an eggnemy."""
        self._max_hp: int = max_hp
        self._curr_hp: int = max_hp
        self._attack_damage: int = attack_damage # Damage taken by enemies attacked by the entity
        self._attack_range: int = attack_range
        self._iframes: int = 0 # Is increased to 15 when the egg takes any damage. The egg only takes damage when this is 0.

    @property
    def get_iframes(self):
        return self._iframes

    @property
    def get_attack_range(self):
        return self._attack_range

    @property
    def get_length(self):
        return self._length

    @property
    def get_height(self):
        return self._height
    
    @property
    def get_x(self):
        return self._x

    @property
    def get_y(self):
        return self._y
        
    def decrement_iframes(self):
        self._iframes -= 1

    def replenish_iframes(self):
        self._iframes = 15


class Eggnemy(Entity):
    pass

class Teaspoon(Entity):
    pass

class Boss(Entity):
    pass

class WorldBorder:
    def __init__(self, length: int, height: int):
        self._x = 0
        self._y = 0
        self._length = length
        self._height = height

    @property
    def get_length(self):
        return self._length

    @property
    def get_height(self):
        return self._height
    
    @property
    def get_x(self):
        return self._x

    @property
    def get_y(self):
        return self._y

    def move_right(self, s: int):
        self._x += s

    def move_left(self, s: int):
        self._x -= s

    def move_up(self, s: int):
        self._y -= s

    def move_down(self, s: int):
        self._y += s


class AttackHitbox:
    def __init__(self, egg: Egg):
        self._x = egg.get_x - egg.get_attack_range
        self._y = egg.get_y - egg.get_attack_range
        self._length = egg.get_length + 2*egg.get_attack_range
        self._height = egg.get_height + 2*egg.get_attack_range

    @property
    def get_length(self):
        return self._length

    @property
    def get_height(self):
        return self._height
    
    @property
    def get_x(self):
        return self._x

    @property
    def get_y(self):
        return self._y
