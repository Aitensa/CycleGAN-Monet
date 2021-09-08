
import wx
import wx.xrc


class Intro (wx.Frame):
	
	def __init__( self, parent,id, UpdateUI=None):
		wx.Frame.__init__ ( self, parent, -1, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.to_test=False
		self.UpdateUI =UpdateUI
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.Colour(47,79,79 ) )
		#self.m_statusBar4 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		IntroMSG = wx.BoxSizer( wx.VERTICAL )
		
		self.Caption = wx.StaticText( self, wx.ID_ANY, u"Introduction:\n\n\nThis is Style Transfer App, before start, ensure you are clear with the following.\n\n1. You should choose the directory of IMGs.\n\n2. Click button SHOW to check the img you selected.\n\n3. At the Parameter unit, you should drag the slider to different point to generate different imgs.\n\n4. Finally, Click Start!\n\nEnjoy this toy*\\~^\\/^~ /*", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Caption.Wrap( -1 )
		IntroMSG.Add( self.Caption, 0, wx.ALL, 5 )
		
		self.Continue = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		IntroMSG.Add( self.Continue, 0, wx.ALL, 5 )
		
		
		self.SetSizer( IntroMSG )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Continue.Bind( wx.EVT_BUTTON, self.ToTest )
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def ToTest( self, event ):
		self.UpdateUI(1)
		self.Destroy()
