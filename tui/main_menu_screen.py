import os.path

from asciimatics.effects import Print, Cycle
from asciimatics.exceptions import NextScene, StopApplication
from asciimatics.renderers import ColourImageFile, FigletText, StaticRenderer, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout, Divider, Label, Text

# Const
from data_management import load

text_colour = Screen.COLOUR_GREEN


class MainMenuFrame(Frame):
    def __init__(self, screen: Screen):
        super(MainMenuFrame, self).__init__(screen,
                                            screen.height,
                                            screen.width // 5,
                                            x=(screen.width * 5 // 12),
                                            y=screen.height // 4 + 1,
                                            hover_focus=True,
                                            can_scroll=False,
                                            title="Menu",
                                            reduce_cpu=True,
                                            has_border=True,
                                            on_load=lambda: self.set_theme("green"))
        # The layouts will will be displayed in the frame
        layout1 = Layout([1])
        layout2 = Layout([1])
        layout4 = Layout([1])
        layout5 = Layout([1])
        self.add_layout(layout1)
        self.add_layout(layout2)
        self.add_layout(layout4)
        self.add_layout(layout5)
        layout1.add_widget(Divider())
        layout2.add_widget(Divider())
        layout4.add_widget(Divider())
        layout5.add_widget(Divider())
        layout1.add_widget(Button("Select File", self._selectFile), 0)
        layout2.add_widget(Button("Select Settings", self._selectSettings), 0)
        layout4.add_widget(Button("Start Processing", self._selectProcessingScreen), 0)
        layout5.add_widget(Button("Quit", self._quit), 0)
        self.fix()

    def _selectFile(self) -> None:
        raise NextScene('FileSelect')

    def _selectSettings(self) -> None:
        raise NextScene('SettingsSelect')

    def _selectProcessingScreen(self) -> None:
        raise NextScene('ProcessingScreen')

    @staticmethod
    def _quit() -> None:
        raise StopApplication("User pressed quit")


class MainMenuScene(Scene):
    def __init__(self, screen: Screen):
        effects = [Print(screen,
                         FigletText("Paradox Animated \n Background Generator", font='small'),
                         x=(screen.width - 90) // 2,
                         y=0,
                         colour=text_colour),
                   # Print(screen,
                   # SpeechBubble("Selected:\n"+str(load("data.txt"))),
                   # x=(screen.width - 100),
                   # y=15),
                   MainMenuFrame(screen)]
        duration = -1
        clear = True
        name = "MainMenu"
        super(MainMenuScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(MainMenuScene, catch_interrupt=True)
