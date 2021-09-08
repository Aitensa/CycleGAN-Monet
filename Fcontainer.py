import Ui_Intro as Intro
import Ui_test as Test
import Ui_warn as Warn

class GuiManager():
    def __init__(self,UpdateUI):
        self.UpdateUI=UpdateUI
        self.frameDict={}

    def GetFrame(self,type):
        frame = self.frameDict.get(type)

        if frame is None:
            frame = self.Create(type)
            self.frameDict[type]=frame
        
        return frame

    def Create(self,type):
        if type == 0:
            return Intro.Intro(parent=None,id=type,UpdateUI=self.UpdateUI)
        elif type == 1:
            return Test.Test(parent=None,id=type,UpdateUI=self.UpdateUI)
        elif type ==2:
            return Warn.WARN(None,id=type,UpdateUI=self.UpdateUI)