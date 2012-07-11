import wx
import os
import ConfigParser
import win32gui

dir = os.path.abspath(os.getcwd())
cfg = ConfigParser.SafeConfigParser()
cfg.read(dir + '\dock.cfg')
ent = dict(cfg.items('main'))


class DockFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(500, 80))
        panel = wx.Panel(self, -1)
        for items in ent:
            ci = ent[items]
            hicon = win32gui.ExtractIcon(1,ci,0)
            ico = wx.NullIcon
            ico.SetHandle(hicon)
            bmp = wx.BitmapFromIcon(ico)
            #bmp.SaveFile('img/'+str(items)+'.bmp',wx.BITMAP_TYPE_BMP)
            b1 = wx.BitmapButton(panel, int(items), bmp, style=wx.NO_BORDER)
            self.Bind(wx.EVT_BUTTON, self.OnClick, b1)



        self.Centre()

    def OnClick(self, event):
        print 'bloop'


class DockMain(wx.App):
    def OnInit(self):
        frame = DockFrame(None, -1, '')
        frame.Show(True)
        return True

app = DockMain(0)
app.MainLoop()