from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from subprocess import call
import os
APPINDICATOR_ID = 'cmstormctrl'
def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('diode.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()
def build_menu():
    menu = gtk.Menu()
    item_on = gtk.MenuItem('Turn LEDs On')
    item_on.connect('activate', ledon)
    item_off = gtk.MenuItem('Turn LEDs Off')
    item_off.connect('activate', ledoff)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_on)
    menu.append(item_off)
    menu.append(item_quit)
    menu.show_all()
    return menu
def ledon(source):
    call(["xset", "led", "3"])
def ledoff(source):
    call(["xset", "led", "off"])
def quit(source):
    gtk.main_quit()
if __name__ == "__main__":
    main()
