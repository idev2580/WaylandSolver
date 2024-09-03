import sys, os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, GObject

PKGDATA_DIR = '/home/idev/Projects/WaylandSolver/builddir/data'
def set_resources():
    """Sets application ressource file."""
    resource = Gio.resource_load(
        os.path.join(PKGDATA_DIR, 'work.idev2580dev.waylandsolver.gresource'))
    Gio.Resource._register(resource)  # nopep8

set_resources()
from wayland_solver.application import Application

if __name__ == '__main__':
    app = Application(application_id="work.idev2580dev.waylandsolver")
    app.run(sys.argv)
