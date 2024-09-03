import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, GObject
from wayland_solver.headerbar import HeaderBar

@Gtk.Template(resource_path="/work/idev2580dev/waylandsolver/ui/MainWindow.ui")
class MainWindow(Adw.ApplicationWindow):

    #Linkage with gresource
    __gtype_name__ = "MainWindow"
    active_view = GObject.Property(type=GObject.GObject, default=None)
    
    #{varname} = Gtk.Template.Child() gets <object ~~~ id={varname}>...</object>
    _main_toolbar_view = Gtk.Template.Child()

    def __init__(self, app):
        super().__init__(application = app, title="Wayland Solver")
        self.app = app
        self.headerbar = HeaderBar(self.app)

        self._main_toolbar_view.add_top_bar(self.headerbar)

        self.is_first_use = True
        if(self.is_first_use):
            dialog = Gtk.AlertDialog(
                message="Welcome",
                detail="Welcome to Wayland Solver! For detailed manual, please go to link below.",
                buttons=["Ok", "Go to Manual"],
                default_button=0,
                cancel_button=0
            )
            dialog.choose(
                parent=self,
                callback=self._first_use_cb
            )
        
        return
        
    def _first_use_cb(self, alert_diag:Gtk.AlertDialog, task):
        manual_page:str = 'https://github.com/idev2580/WaylandSolver/tree/main'
        val = alert_diag.choose_finish(task)
        if(val == 1):
            #Redirect to github page
            print(manual_page)
            pass
        return
    
