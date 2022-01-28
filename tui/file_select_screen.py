import os.path

import magic
from asciimatics.exceptions import NextScene, StopApplication
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Layout, Divider, Label, Text, FileBrowser, Widget, PopUpDialog

# Const

from data_management import save
text_colour = Screen.COLOUR_GREEN


class FileSelectFrame(Frame):
    def __init__(self, screen: Screen):
        super(FileSelectFrame, self).__init__(
            screen, screen.height, screen.width, has_border=False, name="My Form")
        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        self.details = Text()
        self.details.disabled = True
        self.details.custom_colour = "field"
        self._list = FileBrowser(Widget.FILL_FRAME,
                                 os.path.abspath(".."),
                                 name="mc_list",
                                 on_select=self._popup,
                                 on_change=self._details)
        layout.add_widget(Label("Paradox Animated Background Generator"))
        layout.add_widget(Divider())
        layout.add_widget(self._list)
        layout.add_widget(Divider())
        layout.add_widget(self.details)
        layout.add_widget(Label("Press Enter to select"))
        # Prepare the Frame for use.
        self.fix()

    def _popup(self):
        self._scene.add_effect(
            PopUpDialog(self._screen, "You selected: {}".format(self._list.value), ["OK"], self._raiseMainMenu))

        save("data.txt", "PATH", self._list.value)

    def _details(self):
        if self._list.value:
            if os.path.isdir(self._list.value):
                self.details.value = "Directory"
            elif os.path.isfile(self._list.value):
                self.details.value = magic.from_file(self._list.value)
        else:
            self.details.value = "--"

    def _raiseMainMenu(self, answer) -> None:
        raise NextScene('MainMenu')

    def _levelSelect(self) -> None:
        raise NextScene('levelSelect')

    @staticmethod
    def _quit() -> None:
        raise StopApplication("User pressed quit")


class FileSelectScene(Scene):
    def __init__(self, screen: Screen):
        effects = [FileSelectFrame(screen)]
        duration = -1
        clear = True
        name = "FileSelect"
        super(FileSelectScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(FileSelectScene, catch_interrupt=True)
