import os.path

from helpers import getFramesCount, getPath

_path = getPath()


def GenerateCode(Data):
    Game = int(Data["GAME"])  ##EU4 - 1 ; HOI4 - 2 ; ///
    if Game == 1:
        GenerateEu4(Data)
    elif Game == 2:
        print("ss")


def GenerateEu4(Data):
    FramesCount = getFramesCount()

    path = _path + "\\FinalResult\\"
    MoveX = int(Data["CSH"])
    MoveY = int(Data["CSV"])
    CurrentMoveX = int(Data["SPH"])
    CurrentMoveY = int(Data["SPV"])
    MaxMoveX = int(Data["EPH"])
    MaxMoveY = int(Data["EPV"])
    front = open(path + "AndThisTo(Interface-Frontend-gui).txt", "w")
    back = open(path + "AndThisTo(Interface-Alert-gfx).txt", "a")
    while CurrentMoveX < MaxMoveX:  # H
        while CurrentMoveY < MaxMoveY:  # Y
            front.write(""" 
            guiButtonType = {{
                name ="frontend_bg_tile_{0}_{1}"
                spriteType = "GFX_frontend_bg_tile_{0}_{1}"
                position = {{ x= {2} y = {3} }}
                Orientation = "UPPER_LEFT"}}\n
            """.format(str(round(CurrentMoveX / MoveX)), str(round(CurrentMoveY / MoveY)), CurrentMoveX, CurrentMoveY))

            back.write(""" 
            frameAnimatedSpriteType = {{
            	name = "GFX_frontend_bg_tile_{0}_{1}"
            	texturefile = "gfx\\animated_textures\\frontend_background\\spritesheet-{0}-{1}.dds"
            	noOfFrames = {2}
            	animation_rate_fps = 24
            	looping = yes
            	play_on_show = yes
            	pause_on_loop = 0.0
            	alwaystransparent = yes}}\n
            """.format(str(round(CurrentMoveX / MoveX)), str(round(CurrentMoveY / MoveY)), str(FramesCount)))
            CurrentMoveY = CurrentMoveY + MoveY
        CurrentMoveY = 0  # We want only to place in 0 on y
        CurrentMoveX = CurrentMoveX + MoveX
    front.close()
    back.close()
