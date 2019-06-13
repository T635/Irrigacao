from threading import Thread
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import os
import sys
import time
import RPi.GPIO as gpio        
gpio.setmode(gpio.BOARD)
gpio.setup(18, gpio.IN)
os.system('python Envio_desligar.py')
class MyWindow(Gtk.Window):
        def __init__(self):
                Gtk.Window.__init__(self, title="")
                grid = Gtk.Grid()
                self.add(grid)
                color_grid = Gdk.color_parse('grey')
                rgba_grid = Gdk.RGBA.from_color(color_grid)
                grid.override_background_color(0, rgba_grid)
                #------------------------#
                label = Gtk.Label()
                label.set_markup("<big><b>              Controle irrigacao 1.0</b></big>")
                grid.add(label)
                color_label = Gdk.color_parse('crimson')
                rgba_label = Gdk.RGBA.from_color(color_label)
                label.override_color(0, rgba_label)
                #------------------------#
                switch1 = Gtk.Switch()
                switch1.connect("notify::active", self.Manual)
                switch1.set_active(False)
                grid.attach(switch1, 1, 2 ,1 ,1)
                #------------------------#
                label2 = Gtk.Label()  
                label2.set_text("Manual:                                      ")
                grid.attach_next_to(label2, switch1, Gtk.PositionType.LEFT, 1,1)
                label2.override_color(0, rgba_label)
                #------------------------#
                switch2 = Gtk.Switch()
                switch2.connect("notify::active", self.Automatico)
                switch2.set_active(False)
                grid.attach(switch2, 1, 3, 1, 1)
                #------------------------#
                label3 = Gtk.Label() 
                label3.set_text("Automatico:                               ")
                grid.attach_next_to(label3, switch2, Gtk.PositionType.LEFT, 1, 1)
                label3.override_color(0, rgba_label)
        def Manual(self, switch, gparam):
                if switch.get_active():
                        os.system('python Envio_ligar.py')
                elif (switch.get_active() == False):
                        os.system('python Envio_desligar.py')
        def Automatico(self, switch, gparam):
                        if (switch.get_active() == True):
                                while True:
                                        a = gpio.input(18)
                                if (a == 1):
                                        os.system('python Envio_ligar.py')
                                if (a == 0):
                                        os.system('python Envio_desligar.py')
        
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
os.system('python Envio_desligar.py')
win.show_all()
Gtk.main()
