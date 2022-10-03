import wx
import wx.xrc

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"點餐不求人!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 28, 74, 90, 92, True, "微軟正黑體" ) )
		
		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"要求", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 18, 74, 90, 90, False, "微軟正黑體" ) )
		
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		ch_boxChoices = [ u"離我最近", u"評價最高", u"便宜的", u"出餐最快", u"選擇困難" ]
		self.ch_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ch_boxChoices, 0 )
		self.ch_box.SetSelection( 0 )
		self.ch_box.SetFont( wx.Font( 16, 74, 90, 90, False, "微軟正黑體" ) )
		
		gbSizer1.Add( self.ch_box, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer2.Add( gbSizer1, 0, 0, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"開始吧!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.ans = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ans.Wrap( -1 )
		self.ans.SetFont( wx.Font( 16, 74, 90, 90, False, "微軟正黑體" ) )
		
		bSizer2.Add( self.ans, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ch_box.Bind( wx.EVT_CHOICE, self.on_choice )
		self.m_button2.Bind( wx.EVT_BUTTON, self.generate )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_choice( self, event ):
		event.Skip()
	
	def generate( self, event ):
		event.Skip()
	

