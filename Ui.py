
import wx
import wx.xrc
import Fcontainer as Fc

import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torch.autograd import Variable
import torch

from models import Generator
from datasets import ImageDataset

class Ui(wx.App):
    def OnInit(self):
        self.manager = Fc.GuiManager(self.UpdateUi)
        self.frame = self.manager.GetFrame(0)
        self.frame.Show()
        return True
    
    def UpdateUi(self,type):
        self.frame.Show(False)
        self.frame=self.manager.GetFrame(type)
        self.frame.Show()

def main():
    app = Ui()
    app.MainLoop()

if __name__ == '__main__':
    main()


            

