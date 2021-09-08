
import wx
import wx.xrc


class WARN(wx.Dialog):
	def __init__(self, parent,id,UpdateUI=None):
    
		wx.Dialog.__init__(self, parent, id, title = u"Oops!", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		self.to_test=False
		self.UpdateUI=UpdateUI
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.ERRON = wx.StaticText( self, wx.ID_ANY, u"Sorry! ! ! Something bad happened (*_*)\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ERRON.Wrap( -1 )
		bSizer3.Add( self.ERRON, 0, wx.ALL, 5 )
		
		self.Again = wx.Button( self, wx.ID_ANY, u"Try Again", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.Again, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		bSizer3.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Again.Bind( wx.EVT_BUTTON, self.ToTest )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ToTest( self, event ):
		self.UpdateUI(1)
	