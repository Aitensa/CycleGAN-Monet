import wx
import wx.xrc


import os

import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torch.autograd import Variable
import torch
import utils

from models import Generator
from datasets import ImageDataset
import test as test


    


class Test (wx.Frame):
	def __init__( self, parent ,id,UpdateUI=None):
		wx.Frame.__init__ ( self, parent, id , title = u"Style Transfer Display", pos = wx.DefaultPosition, size = wx.Size( 750,850 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
		self.start=False
		self.ini_A=None
		self.trans_A=None
		self.run=False
		self.tag=0
		self.path='datasets/gan-getting-started/test/'
		self.UpdateUI=UpdateUI
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.SetBackgroundColour( wx.Colour(47,79,79 ) )
		
		Body = wx.BoxSizer( wx.VERTICAL )
		
		Head = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"IMG File Path" ), wx.VERTICAL )
		
		self.Path = wx.DirPickerCtrl( Head.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		Head.Add( self.Path, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		Body.Add( Head, 1, wx.EXPAND, 5 )
		
		Median = wx.GridSizer( 0, 2, 0, 0 )
		
		RealA = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RealA" ), wx.VERTICAL )
		
		self.RA = wx.BitmapButton( RealA.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"datasets/gan-getting-started/test/A//ra.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		RealA.Add( self.RA, 0, wx.ALL, 5 )
		
		self.RA_SHOW = wx.Button( RealA.GetStaticBox(), wx.ID_ANY, u"SHOW", wx.DefaultPosition, wx.DefaultSize, 0 )
		RealA.Add( self.RA_SHOW, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		Median.Add( RealA, 1, wx.EXPAND, 5 )
		
		RealB = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RealB" ), wx.VERTICAL )
		
		self.RB = wx.BitmapButton( RealB.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"datasets/gan-getting-started/test/B//rb.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		RealB.Add( self.RB, 0, wx.ALL, 5 )
		
		self.RB_SHOW = wx.Button( RealB.GetStaticBox(), wx.ID_ANY, u"SHOW", wx.DefaultPosition, wx.DefaultSize, 0 )
		RealB.Add( self.RB_SHOW, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		Median.Add( RealB, 1, wx.EXPAND, 5 )
		
		FakeB = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"FakeA" ), wx.VERTICAL )
		
		self.FB = wx.BitmapButton( FakeB.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"datasets/gan-getting-started/test/B//rb.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		FakeB.Add( self.FB, 0, wx.ALL, 5 )
		
		
		Median.Add( FakeB, 1, wx.EXPAND, 5 )
		
		FakeA = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"FakeB" ), wx.VERTICAL )
		
		self.FA = wx.BitmapButton( FakeA.GetStaticBox(), wx.ID_ANY, wx.Bitmap( u"datasets/gan-getting-started/test/A//ra.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		FakeA.Add( self.FA, 0, wx.ALL, 5 )
		
		
		Median.Add( FakeA, 1, wx.EXPAND, 5 )
		
		
		Body.Add( Median, 1, wx.EXPAND, 5 )
		
		Parameter = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Transfer Ratio" ), wx.VERTICAL )
		
		self.RATIO = wx.Slider( Parameter.GetStaticBox(), wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_LABELS )
		Parameter.Add( self.RATIO, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		Body.Add( Parameter, 1, wx.EXPAND, 5 )
		
		self.Start = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		Body.Add( self.Start, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( Body )
		self.Layout()
		#self.m_statusBar5 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Path.Bind( wx.EVT_DIRPICKER_CHANGED, self.GetPath )
		self.RA_SHOW.Bind( wx.EVT_BUTTON, self.Show_RA )
		self.RB_SHOW.Bind( wx.EVT_BUTTON, self.Show_RB )
		self.Start.Bind( wx.EVT_BUTTON, self.StartTest )
		self.RATIO.Bind(wx.EVT_BUTTON,self.ReUpdate)

	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def GetPath( self, event ):  
		self.path = self.Path.GetPath()
		if self.path is None:
    			self.UpdateUI(2)
	
	def Show_RA( self, event ):	
    		self.RA.SetBitmap(wx.BitmapFromImage(wx.Image(self.path+'\\test\A\\ra.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap()))

	def Show_RB( self, event ):
		self.RB.SetBitmap(wx.BitmapFromImage(wx.Image(self.path+'\\test\B\\rb.jpg',wx.BITMAP_TYPE_JPEG).ConvertToBitmap()))
			
	def StartTest( self, event ):
        	transfer = test.transfer(path=self.path,update=self.update)
        	transfer.run()
		

        	

	def flush_FA(self,path):
		self.FA.SetBitmap(wx.BitmapFromImage( wx.Image(path,wx.BITMAP_TYPE_PNG).ConvertToBitmap()))

	def flush_FB(self,path):
		self.FB.SetBitmap(wx.BitmapFromImage(wx.Image(path,wx.BITMAP_TYPE_PNG).ConvertToBitmap()))

	def update(self,ini_A,trans_A,path,tag):	
		self.ini_A=ini_A
		self.trans_A=trans_A
		self.tag=tag
		if not self.run:
			utils.interpolation(ini_A,trans_A,path+'/B')
			self.run=True
		self.flush_FA(path=path+'/B/s{:4d}.png'.format(self.RATIO.GetValue()))
		self.flush_FB(path=path+'/A/s{:4d}.png'.format(tag))
		


	def ReUpdate(self):
    		self.flush_FB(path='output/B/s{:4d}'.format(self.RATIO.GetValue()))
