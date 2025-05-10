"""This will be the main file for Implementation 1."""

from model import Model
from controller import Controller
from view import View

def main():
    SCREEN_X = 1000
    SCREEN_Y = 1000
    FPS = 30
    # SCREEN_X, SCREEN_Y, and FPS should be moved to settings.json in the future.

    model = Model(SCREEN_X, SCREEN_Y)
    view = View(SCREEN_X, SCREEN_Y)
    controller = Controller(model, view)
    controller.start(FPS)


if __name__ == "__main__":
    main()
