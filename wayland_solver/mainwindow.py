import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, GObject

@Gtk.Template(resource_path="/work/idev2580dev/waylandsolver/ui/MainWindow.ui")
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title('Wayland Solver')
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
            self.open(manual_page)

            pass
        return
    
