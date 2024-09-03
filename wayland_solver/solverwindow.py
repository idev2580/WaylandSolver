import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, GObject

@Gtk.Template(resource_path="/work/idev2580dev/waylandsolver/ui/SolverWindow.ui")
class SolverWindow(Adw.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title=_("Solver"))
        return