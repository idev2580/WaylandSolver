import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, GObject
from wayland_solver.mainwindow import MainWindow

class Application(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.props.resource_base_path = "/work/idev2580dev/waylandsolver"
        self.connect('activate', self.on_activate)
    
    def on_activate(self, app):
        self.main_win = MainWindow(app)
        self.main_win.present()
    
