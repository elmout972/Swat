#!/usr/bin/python

import pygtk
pygtk.require('2.0')
import gtk
import appindicator
import os

class SWAppIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator("Swat", "icon", appindicator.CATEGORY_APPLICATION_STATUS
                                          , os.path.dirname(os.path.realpath(__file__)))
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")
        # self.ind.set_icon("favicon.ico", "TOTO")


        # Create a menu
        self.menu = gtk.Menu()
        
        item = gtk.MenuItem("Open SWat")
        item.connect("activate", self.openSWApp)
        item.show()
        self.menu.append(item)

        check = gtk.CheckMenuItem("Check Menu Item")
        check.show()
        self.menu.append(check)

        radio = gtk.RadioMenuItem(None, "Radio Menu Item")
        radio.show()
        self.menu.append(radio)
        separator = gtk.SeparatorMenuItem()
        separator.show()
        self.menu.append(separator)

        image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        image.connect("activate", self.quit)
        image.show()
        self.menu.append(image)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)
        self.window = SWAppWindow();
        print(self.ind.get_icon_theme_path())

    def openSWApp(self, widget, data=None):
        print("OpenSWapp")
        self.window.show_all()
        
    def quit(self, widget, data=None):
        gtk.main_quit()


class SWAppWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.set_title("Swat")
        self.set_position(gtk.WIN_POS_CENTER)
        # self.set_icon_from_file("./icon.png")
        self.set_size_request(250, 200)
        self.set_border_width(10)

        # Add root VBox
        self.rootVBox = gtk.VBox(False, 0)
        self.add(self.rootVBox)
        self.rootVBox.show()

        self.createSWMenuBar()

        self.connect("delete_event", self.delete_event)    
        self.connect("destroy", self.destroy)
        self.button = gtk.Button("Hello World")
        self.button.connect("clicked", self.hello, None)
        self.button.connect("clicked", self.delete_event, None)
    
        # This packs the button into the window (a GTK container).
        self.rootVBox.pack_start(self.button, False, False, 2)

        self.button.show()


    def createSWMenuBar(self):
        # Menu bar
        menuBar = gtk.MenuBar()

        # File menu
        fileMenu = gtk.MenuItem("File")
        menu = gtk.Menu()
        menuBar.append(fileMenu)
        fileMenu.set_submenu(menu)
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", self.delete_event, None)
        menu.append(exit)

        # Options menu
        optionMenu = gtk.MenuItem("Options")
        menuBar.append(optionMenu)
        menu = gtk.Menu()
        optionMenu.set_submenu(menu)

        self.rootVBox.pack_start(menuBar, False, False, 2)


    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        self.hide()
        return True
        
    def destroy(self, widget, data=None):
        print "destroy signal occurred"


    def hello(self, widget, data=None):
        print "Hello World"    


def main():
    gtk.main()
    return 0


if __name__ == "__main__":
    indicator = SWAppIndicator()
    main()
