from asciimatics.exceptions import NextScene
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Button, Frame, Layout, Divider, PopUpDialog

# Const
from data_management import load
from functions.code_generation import GenerateCode
from functions.dds_converter import ConvertSprites
from functions.ffmpeg_spliter import SplitVideo
from functions.sprite_merger import MergeSprites

text_colour = Screen.COLOUR_GREEN


class ProcessingFrame(Frame):
    def __init__(self, screen: Screen):
        super(ProcessingFrame, self).__init__(screen,
                                              screen.height,
                                              screen.width,
                                              hover_focus=True,
                                              can_scroll=False,
                                              title="Processing",
                                              reduce_cpu=True,
                                              has_border=True,
                                              on_load=lambda: self.set_theme("green"))
        layout1 = Layout([1, 1, 1])
        self.add_layout(layout1)
        layout1.add_widget(Divider(), 0)
        layout1.add_widget(Divider(), 1)
        layout1.add_widget(Divider(), 2)
        layout1.add_widget(Button("Auto-Processing", self._autoProcessing), 0)
        layout1.add_widget(Button("Split Video", self._splitVideoProcessing), 1)
        layout1.add_widget(Button("Merge Sprites", self._spriteMergeProcessing), 1)
        layout1.add_widget(Button("Convert Spritesheet", self._convertSpritesheetProcessing), 1)
        layout1.add_widget(Button("Generate Mod Files", self._generateModFilesProcessing), 1)
        layout1.add_widget(Button("Back to Main Menu", self._selectMainMenu), 2)
        self.fix()

    def _autoProcessing(self):
        Data = load("data.txt")
        SplitVideo(Data)
        MergeSprites(Data)
        ConvertSprites(Data)
        GenerateCode(Data)
        self._successPopUp()

    def _splitVideoProcessing(self):
        Data = load("data.txt")
        SplitVideo(Data)
        self._successPopUp()

    def _spriteMergeProcessing(self):
        Data = load("data.txt")
        MergeSprites(Data)
        self._successPopUp()

    def _convertSpritesheetProcessing(self):
        Data = load("data.txt")
        ConvertSprites(Data)
        self._successPopUp()

    def _generateModFilesProcessing(self):
        Data = load("data.txt")
        GenerateCode(Data)
        self._successPopUp()

    def _successPopUp(self):
        self._scene.add_effect(
            PopUpDialog(self._screen, "The task was completed successfully", ["OK"]))
        raise NextScene('ProcessingScreen')

    def _selectMainMenu(self) -> None:
        raise NextScene('MainMenu')


class ProcessingScene(Scene):
    def __init__(self, screen: Screen):
        effects = [ProcessingFrame(screen)]
        duration = -1
        clear = True
        name = "ProcessingScreen"
        super(ProcessingScene, self).__init__(
            effects,
            duration,
            clear,
            name
        )


if __name__ == "__main__":
    Screen.wrapper(ProcessingScene, catch_interrupt=True)
