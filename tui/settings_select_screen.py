import os.path

from asciimatics.effects import Print, Cycle
from asciimatics.exceptions import NextScene, StopApplication
from asciimatics.renderers import ColourImageFile, FigletText, StaticRenderer, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout, Divider, Label, Text, PopUpDialog, DropdownList

# Const
from data_management import load, save

text_colour = Screen.COLOUR_GREEN


class SettingsSelectFrame(Frame):
    def __init__(self, screen: Screen):
        super(SettingsSelectFrame, self).__init__(screen,
                                                  screen.height,
                                                  screen.width,
                                                  can_scroll=False,
                                                  title="Select Settings",
                                                  on_load=lambda: self.set_theme("green"),
                                                  has_border=True)
        layout1 = Layout([1], fill_frame=True)
        self.add_layout(layout1)

        layout1.add_widget(Button("Help", self._helpPopup), 0)
        layout1.add_widget(DropdownList(
            [("EU4", 1),
             ("HOI4", 2), ],
            label="Select Game", name="GAME", on_change=self._onChange), 0)
        layout1.add_widget(Divider())
        layout1.add_widget(
            Text(label="Set StartPoint Horizontal", name="SPH", on_change=self._onChange, readonly=False,
                 hide_char=False), 0)
        layout1.add_widget(Divider())
        layout1.add_widget(
            Text(label="Set StartPoint Vertical", name="SPV", on_change=self._onChange, readonly=False,
                 hide_char=False), 0)
        layout1.add_widget(Divider())
        layout1.add_widget(
            Text(label="Set EndPoint Horizontal", name="EPH", on_change=self._onChange, readonly=False,
                 hide_char=False), 0)
        layout1.add_widget(Divider())
        layout1.add_widget(
            Text(label="Set EndPoint Vertical", name="EPV", on_change=self._onChange, readonly=False,
                 hide_char=False), 0)
        layout1.add_widget(Divider())
        layout1.add_widget(
            Text(label="Set Horizontal Crop size", name="CSH", on_change=self._onChange, readonly=False, hide_char=False), 0)
        layout1.add_widget(Divider())
        layout1.add_widget(
            Text(label="Set Vertical Crop size", name="CSV", on_change=self._onChange, readonly=False, hide_char=False),
            0)
        layout1.add_widget(Divider())
        layout1.add_widget(
            Text(label="Set Threads count", name="THR", on_change=self._onChange, readonly=False, hide_char=False),
            0)

        layout1.add_widget(Button("OK", self._backToMenu), 0)
        self.fix()

    def _onChange(self):
        self.save()
        data = load("data.txt")
        for key, value in self.data.items():
            if key not in data or data[key] != value:
                save("data.txt", key, value)
                break

    def _helpPopup(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Start and EndPoints - to crop specified part of video (if you want full video just set it to video resolution) \n"
                        "Horizontal crop must be divisible by difference (Between EndPoint and StartPoint) without a reminder \n"
                        "Vertical crop must be divisible by difference (Between EndPoint and StartPoint) without a reminder (if you dont want to split video on vertical set the value to the same as EndPoint Vertical) \n"
                        "Threads count - faster program execution",

                        ["Thanks"]))

    def _backToMenu(self) -> None:
        raise NextScene('MainMenu')


class SettingsSelectScene(Scene):
    def __init__(self, screen: Screen):
        effects = [SettingsSelectFrame(screen)]
        duration = -1
        clear = True
        name = "SettingsSelect"
        super(SettingsSelectScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(SettingsSelectScene, catch_interrupt=True)
