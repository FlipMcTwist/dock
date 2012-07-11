import os
import pygtk, gtk
import ConfigParser
import win32gui

dir = os.path.abspath(os.getcwd())
cfg = ConfigParser.SafeConfigParser()
cfg.read(dir + '\dock.cfg')
ent = dict(cfg.items('main'))



class dock:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(2)
        self.box = gtk.HBox(False, 0)
        self.window.add(self.box)



        for items in ent:
            ci = ent[items]
            hicon = win32gui.ExtractIcon(1,ci,0)
            dc = win32ui.CreateDCFromHandle(hicon)
            print dc
            self.ebox = gtk.EventBox()
            self.button = gtk.Button(ci)
            self.button.connect("clicked", self.bloop, ci)
            self.box.pack_start(self.ebox, True, True, 0)
            self.ebox.add(self.button)
            self.button.show()
            self.ebox.show()

        self.box.show()
        self.window.show()

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def bloop(self, widget, data):
        print data


    def main(self):
        gtk.main()


if __name__ == "__main__":
    dock = dock()
    dock.main()