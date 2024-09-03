from gi.repository import Adw, GObject, Gtk

@Gtk.Template(resource_path="/work/idev2580dev/waylandsolver/ui/HeaderBar.ui")
class HeaderBar(Adw.Bin):
    class State:
        MAIN = 0
        SEARCH = 1
    
    #Linkage with gresource
    __gtype_name__ = "HeaderBar"
    __gtype_name__ = "HeaderBar"

    _search_button = Gtk.Template.Child()
    _headerbar = Gtk.Template.Child()
    _menu_button = Gtk.Template.Child()

    search_mode_active = GObject.Property(type=bool, default=False)
    stack = GObject.Property(type=Adw.ViewStack)

    def __init__(self, application):
        """Initialize Headerbar

        :param Application application: Application object
        """
        super().__init__()

        self._stack_switcher = Adw.ViewSwitcher(
            focusable=False, halign="center",
            policy=Adw.ViewSwitcherPolicy.WIDE)

        self.bind_property(
            "stack", self._stack_switcher, "stack",
            GObject.BindingFlags.BIDIRECTIONAL
            | GObject.BindingFlags.SYNC_CREATE)
        self.bind_property(
            "search-mode-active", self._search_button, "active",
            GObject.BindingFlags.BIDIRECTIONAL
            | GObject.BindingFlags.SYNC_CREATE)

    @GObject.Property
    def state(self):
        """State of the widget

        :returns: Widget state
        :rtype: HeaderBar.State
        """
        return self._state

    @state.setter  # type: ignore
    def state(self, value):
        """Set state of the of widget

        This influences the look and functionality of the headerbar.

        :param HeaderBar.State value: Widget state
        """
        self._state = value
        self._update()

        search_visible = self.props.state != HeaderBar.State.SEARCH
        self._search_button.props.visible = search_visible

        if value == HeaderBar.State.EMPTY:
            self._search_button.props.sensitive = False
            self._stack_switcher.hide()
        else:
            self._search_button.props.sensitive = True
            self._stack_switcher.show()

    def _update(self):
        if self.props.state != HeaderBar.State.MAIN:
            self._headerbar.props.title_widget = None
        else:
            self._headerbar.props.title_widget = self._stack_switcher

        self._menu_button.props.visible = (
            self.props.state in [HeaderBar.State.MAIN, HeaderBar.State.EMPTY]
        )