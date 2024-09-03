import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, GObject
from wayland_solver.window import MainWindow

class Application(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register()
        menu = Gio.Menu()
        about_section = Gio.Menu()
        quit_section = Gio.Menu()
        about_section.append(label="Show Logs", detailed_action=None)
        about_section.append(label="Manual", detailed_action=None)
        about_section.append(label="About", detailed_action=None)
        quit_section.append(label="Quit", detailed_action=None)
        menu.append_section("About", about_section)
        menu.append_section("Quit", quit_section)
        self.set_menubar(menu)
        self.connect('activate', self.on_activate)
    
    def on_activate(self, app):
        self.main_win = MainWindow(application=app, show_menubar=True)
        self.main_win.present()
    
