import sys

from asciimatics.exceptions import ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from init_folders import InitData
from tui.main_menu_screen import MainMenuScene
from tui.file_select_screen import FileSelectScene
from tui.settings_select_screen import SettingsSelectScene
from tui.processing_screen import ProcessingScene


def start(screen: Screen, scene: Scene) -> None:
    scenes = [MainMenuScene(screen),  # MainMenu
              FileSelectScene(screen),  # FileSelect
              SettingsSelectScene(screen),  # SettingsSelect
              ProcessingScene(screen)]  # ProcessingScreen
    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)


if __name__ == "__main__":
    last_scene = None
    InitData()
    while True:
        try:
            print(last_scene)
            Screen.wrapper(start, catch_interrupt=True, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
